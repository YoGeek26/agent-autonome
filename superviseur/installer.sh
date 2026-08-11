#!/usr/bin/env bash
# Installation de l'agent sur un serveur Debian 12 ou Ubuntu 24.04 vierge.
#
#   sudo bash installer.sh <url-du-dépôt-git> [domaine]
#
# Idempotent : relançable sans casser une installation existante.

set -euo pipefail

DEPOT_URL="${1:-}"
DOMAINE="${2:-}"
UTILISATEUR="agent"
CIBLE="/opt/agent"

if [[ -z "$DEPOT_URL" ]]; then
  echo "usage : sudo bash installer.sh <url-du-dépôt-git> [domaine]" >&2
  exit 1
fi
if [[ $EUID -ne 0 ]]; then
  echo "à lancer en root (sudo)" >&2
  exit 1
fi

etape() { printf '\n\033[1m== %s\033[0m\n' "$1"; }

etape "Paquets système"
apt-get update -qq
apt-get install -y -qq git curl ca-certificates debian-keyring debian-archive-keyring apt-transport-https python3

etape "Node 22 (nécessaire à Playwright, pas à Claude Code)"
if ! command -v node >/dev/null || [[ "$(node -v | cut -c2-3)" -lt 22 ]]; then
  curl -fsSL https://deb.nodesource.com/setup_22.x | bash - >/dev/null
  apt-get install -y -qq nodejs
fi
node -v

etape "Caddy (sert le site, certificat TLS automatique)"
if ! command -v caddy >/dev/null; then
  curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' \
    | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
  curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' \
    > /etc/apt/sources.list.d/caddy-stable.list
  apt-get update -qq && apt-get install -y -qq caddy
fi

etape "Utilisateur $UTILISATEUR"
id -u "$UTILISATEUR" >/dev/null 2>&1 || adduser --disabled-password --gecos "" "$UTILISATEUR"

etape "Dépôt dans $CIBLE"
if [[ -d "$CIBLE/.git" ]]; then
  sudo -u "$UTILISATEUR" git -C "$CIBLE" pull --ff-only || true
else
  mkdir -p "$CIBLE"
  chown "$UTILISATEUR:$UTILISATEUR" "$CIBLE"
  sudo -u "$UTILISATEUR" git clone "$DEPOT_URL" "$CIBLE"
fi
chown -R "$UTILISATEUR:$UTILISATEUR" "$CIBLE"

etape "Claude Code (installeur natif, sans Node)"
sudo -u "$UTILISATEUR" -H bash -lc '
  command -v claude >/dev/null || curl -fsSL https://claude.ai/install.sh | bash
  export PATH="$HOME/.local/bin:$PATH"
  claude --version
'

etape "Chromium pour Playwright"
sudo -u "$UTILISATEUR" -H bash -lc 'npx -y playwright install --with-deps chromium' >/dev/null 2>&1 \
  || npx -y playwright install-deps chromium

etape "Swap (2 Go — filet contre les pics de Chromium)"
if ! swapon --show | grep -q swapfile; then
  fallocate -l 2G /swapfile
  chmod 600 /swapfile
  mkswap /swapfile >/dev/null
  swapon /swapfile
  grep -q '/swapfile' /etc/fstab || echo '/swapfile none swap sw 0 0' >> /etc/fstab
fi
free -h | head -3

etape "Pare-feu"
if command -v ufw >/dev/null || apt-get install -y -qq ufw; then
  ufw --force reset >/dev/null 2>&1 || true
  ufw default deny incoming >/dev/null
  ufw default allow outgoing >/dev/null
  ufw allow 22/tcp >/dev/null
  ufw allow 80/tcp >/dev/null
  ufw allow 443/tcp >/dev/null
  ufw --force enable >/dev/null
  ufw status numbered
fi

etape "Configuration"
if [[ ! -f /etc/agent.env ]]; then
  cp "$CIBLE/superviseur/config.exemple.env" /etc/agent.env
  chmod 600 /etc/agent.env
  chown root:root /etc/agent.env
  echo "→ /etc/agent.env créé. À REMPLIR avant de démarrer."
else
  echo "→ /etc/agent.env existe déjà, laissé intact."
fi

etape "Service systemd"
cp "$CIBLE/superviseur/agent.service" /etc/systemd/system/agent.service
systemctl daemon-reload

etape "Caddy"
if [[ -n "$DOMAINE" ]]; then
  cat > /etc/caddy/Caddyfile <<EOF
$DOMAINE {
    root * $CIBLE/site
    file_server
    encode gzip
}
EOF
  echo "→ le A du domaine doit pointer sur l'IP de ce serveur"
else
  # Pas encore de domaine : on sert en HTTP sur l'IP. Quand l'agent aura
  # choisi son nom, il suffira de remplacer ':80' par le domaine et de
  # recharger — Caddy obtiendra le certificat tout seul.
  cat > /etc/caddy/Caddyfile <<EOF
:80 {
    root * $CIBLE/site
    file_server
    encode gzip
}
EOF
  echo "→ site servi en HTTP sur l'IP, en attendant un domaine"
fi
mkdir -p "$CIBLE/site"
chown -R "$UTILISATEUR:$UTILISATEUR" "$CIBLE/site"
systemctl reload caddy || systemctl restart caddy

cat <<'FIN'

================================================================
Installation terminée. Il reste trois choses, dans cet ordre :

1.  nano /etc/agent.env
    Remplir : jeton du modèle, Telegram, IMAP, carte, webhook.
    Rien de tout ça ne doit jamais entrer dans le dépôt.

2.  Donner à l'utilisateur `agent` de quoi pousser sur le dépôt :
      sudo -u agent ssh-keygen -t ed25519 -C agent
      sudo -u agent cat /home/agent/.ssh/id_ed25519.pub
    puis coller la clé dans GitHub → Settings → Deploy keys,
    en cochant « Allow write access ».
    Sans ça, le superviseur commite sans jamais publier, et tu ne
    t'en aperçois qu'au bout de trois jours.

3.  Vérifie AVANT de démarrer :
      sudo -u agent env $(grep -v '^#' /etc/agent.env | xargs) \
        python3 /opt/agent/superviseur/verifier.py

4.  Prends un instantané depuis l'espace client OVH.
    C'est ton point de retour propre.

5.  systemctl enable --now agent
    journalctl -u agent -f

================================================================
FIN
