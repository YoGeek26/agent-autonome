# Démarrage

Tu as payé le VPS. Voici la suite, dans l'ordre.

Compte deux heures, dont l'essentiel en attente de livraisons et de
vérifications. L'ordre compte : chaque étape produit quelque chose dont la
suivante a besoin.

---

## 1. Pendant que le VPS se prépare

OVH livre en quelques minutes à deux heures. Fais tout ceci en parallèle —
c'est le chemin critique, pas le serveur.

### 1.1 Le dépôt GitHub

Décompresse l'archive. Elle ne contient aucun secret.

Sur github.com → *New repository*. **Public** si tu veux que l'expérience soit
auditable : c'est ce qui donne sa valeur au récit, et ça se décide maintenant,
pas au jour 40 quand tu sauras si ça marche. Ne coche pas « Add a README ».

Sur la page du dépôt vide → *uploading an existing file* → glisse le
**contenu** du dossier `agent-autonome`, pas le dossier lui-même. GitHub
conserve l'arborescence. *Commit changes*.

Puis Settings → Code security → active la protection contre l'envoi de
secrets.

### 1.2 Le canal Telegram

1. Écris à **@BotFather**, `/newbot`, note le jeton.
2. Envoie n'importe quel message à ton nouveau bot.
3. Ouvre `https://api.telegram.org/bot<JETON>/getUpdates` et relève
   `message.chat.id`.

### 1.3 Sa boîte mail

Une adresse **dédiée**, avec IMAP, et un mot de passe d'application si le
fournisseur en exige un — la plupart le font. Évite Gmail : le compte Google
ajoute des CGU et un risque de bannissement dont tu n'as pas besoin.

Note l'hôte IMAP (souvent `imap.<fournisseur>`).

### 1.4 L'accès au modèle

Sur openrouter.ai : crée une clé, **fixe un plafond de dépense mensuel tout de
suite**, pas « plus tard ». C'est ton seul garde-fou financier côté jetons.

### 1.5 La carte

Carte virtuelle plafonnée à **80 €**, plafond dur, sans rechargement
automatique ni découvert. Vérifie que c'est un blocage et non une alerte.

### 1.6 Le rail d'encaissement

Un lien de paiement à ton nom (Stripe si tu veux le webhook). La vérification
d'identité prend 24 à 48 h — c'est pour ça que c'est ici et pas à la fin.

### 1.7 Le domaine — ne l'achète pas

Laisse l'agent le choisir. Le site sera d'abord servi en HTTP sur l'IP du VPS ;
sa première demande de PARKING sera probablement « achète-moi ce nom », et ce
choix est une donnée d'expérience. Quand il l'aura, tu changeras une ligne du
`Caddyfile`.

---

## 2. Sécuriser la machine

Dès réception des accès. **Avant** d'y mettre quoi que ce soit : cette machine
va contenir un numéro de carte, et un VPS fraîchement livré est balayé en
quelques minutes.

Depuis ton poste :

```bash
ssh-keygen -t ed25519 -C "moi"          # si tu n'en as pas déjà une
ssh-copy-id root@<IP>
ssh root@<IP>
```

Puis sur le serveur :

```bash
sed -i 's/^#*PermitRootLogin.*/PermitRootLogin prohibit-password/' /etc/ssh/sshd_config
sed -i 's/^#*PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart ssh
```

**Ne ferme pas cette session** avant d'avoir vérifié depuis un second terminal
que la connexion par clé fonctionne. C'est la manière classique de s'enfermer
dehors.

Mets ta clé privée dans ton gestionnaire de mots de passe. En secours, OVH
propose une console web (KVM) depuis l'espace client.

---

## 3. Installer

```bash
curl -fsSL https://raw.githubusercontent.com/<toi>/<dépôt>/main/superviseur/installer.sh \
  -o installer.sh
bash installer.sh https://github.com/<toi>/<dépôt>.git
```

Sans argument de domaine : le site sera servi en HTTP sur l'IP.

Le script installe Node, Caddy, Claude Code, Chromium, crée l'utilisateur
`agent`, ajoute 2 Go de swap, ferme le pare-feu sauf 22/80/443, clone le
dépôt, pose le service et prépare `/etc/agent.env`.

Il est relançable sans rien casser.

Si `playwright install --with-deps` bute sur Debian 13 :

```bash
apt install -y libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
  libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 \
  libgbm1 libasound2 libpango-1.0-0 libcairo2
sudo -u agent npx -y playwright install chromium
```

---

## 4. Le droit de pousser

**C'est la panne la plus silencieuse du montage.** Sans ça, le superviseur
commite en local sans jamais publier, et tu ne t'en aperçois qu'après trois
jours de travail invisible.

```bash
sudo -u agent ssh-keygen -t ed25519 -C agent -N "" -f /home/agent/.ssh/id_ed25519
sudo -u agent cat /home/agent/.ssh/id_ed25519.pub
```

Colle la clé dans GitHub → *Settings du dépôt* → *Deploy keys* → *Add*, en
cochant **Allow write access**.

Puis bascule le dépôt en SSH :

```bash
sudo -u agent git -C /opt/agent remote set-url origin git@github.com:<toi>/<dépôt>.git
sudo -u agent ssh -o StrictHostKeyChecking=accept-new -T git@github.com
```

---

## 5. Remplir la configuration

```bash
nano /etc/agent.env
```

| Variable | Où tu l'as obtenue |
|---|---|
| `ANTHROPIC_BASE_URL` | `https://openrouter.ai/api` — sans `/v1` |
| `ANTHROPIC_AUTH_TOKEN` | la clé OpenRouter (§1.4) |
| `ANTHROPIC_API_KEY` | **laisser vide**, sinon elle court-circuite tout |
| `AGENT_MODELE` | `anthropic/claude-opus-5` |
| `AGENT_MODELE_SIMPLE` | `anthropic/claude-sonnet-5` |
| `AGENT_MODELE_TRIAGE` | `anthropic/claude-haiku-4.5` |
| `AGENT_BUDGET_MODELE` | ton plafond en dollars — le même que sur OpenRouter |
| `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` | §1.2 |
| `MAIL_ADRESSE`, `MAIL_MOT_DE_PASSE`, `MAIL_IMAP_HOTE` | §1.3 |
| `CARTE_NUMERO`, `CARTE_EXP`, `CARTE_CVC` | §1.5 |
| `AGENT_WEBHOOK_JETON` | une chaîne aléatoire que tu inventes |

Puis dans le dépôt (pas dans l'env) : renseigne l'identité dans
`etat/COMPTES.md`, et **lis `cadre/ARRET.md` en entier**. C'est le moment,
pas plus tard : ces critères ne valent que s'ils sont écrits avant.

---

## 6. Vérifier avant de démarrer

```bash
sudo -u agent env $(grep -v '^#' /etc/agent.env | xargs) \
  python3 /opt/agent/superviseur/verifier.py
```

Il teste chaque brique séparément : RAM et swap, permissions des secrets,
fichiers du cadre, appel réel au modèle, Playwright, droit de pousser, envoi
Telegram, connexion IMAP.

**Ne démarre pas tant que tout n'est pas vert.** Un agent lancé sur une brique
cassée écrit un journal trompeur, et tu passeras une semaine à comprendre
pourquoi il « décide » de ne rien faire.

---

## 7. L'instantané

Espace client OVH → ton VPS → *Snapshot*. Maintenant, avant le premier réveil.

C'est ton point de retour propre. Si le jour 10 tourne mal, tu reviens ici
sans réinstaller.

---

## 8. Démarrer

```bash
systemctl enable --now agent
journalctl -u agent -f
```

Tu dois voir, dans l'ordre : « superviseur démarré », un message Telegram, puis
un premier réveil qui dure quelques minutes.

Laisse tourner les journaux et regarde le premier réveil en entier. C'est le
seul que tu regarderas en direct — après, tu lis le journal.

---

## 9. Les premières 24 heures

Vérifie ces cinq choses. Ce sont les seules qui comptent au début.

- **`git log`** — un commit par réveil productif. S'il n'y a rien après deux
  heures, retourne au §4.
- **`etat/rythme.json`** — la valeur doit changer et être justifiée. Si elle
  reste collée à 20 minutes, le protocole ne fonctionne pas et ça se paie en
  jetons.
- **`etat/cout.json`** — regarde `jours_restants`. C'est ton autonomie réelle.
- **`etat/COMPTES.md`** — s'il ouvre un compte, il doit y figurer
  immédiatement. Un retard ici est ton premier signal d'alarme.
- **Telegram** — il doit t'écrire dès qu'il bute sur une vérification humaine.
  Réponds : c'est ton seul rôle.

Et ne corrige pas son plan. S'il part dans une direction qui t'ennuie, c'est
un résultat, pas un bug. Les critères d'arrêt sont dans `cadre/ARRET.md`, tu
les as écrits avant de savoir — c'est ce qui les rend valables.
