#!/usr/bin/env python3
"""
Vérification préalable — à lancer avant le premier démarrage.

    sudo -u agent env $(grep -v '^#' /etc/agent.env | xargs) \
        python3 /opt/agent/superviseur/verifier.py

Teste chaque brique séparément. Sans ça, tu démarres et tu débogues quatre
choses à la fois dans les journaux systemd.
"""

import imaplib
import json
import os
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

DEPOT = Path(os.environ.get("AGENT_DEPOT", "/opt/agent"))
ok_global = True


def verdict(nom: str, ok: bool, detail: str = "") -> None:
    global ok_global
    marque = "\033[32m  OK  \033[0m" if ok else "\033[31mÉCHEC \033[0m"
    print(f"[{marque}] {nom}" + (f" — {detail}" if detail else ""))
    if not ok:
        ok_global = False


def machine() -> None:
    try:
        info = Path("/proc/meminfo").read_text()
        ram = int([l for l in info.splitlines()
                   if l.startswith("MemTotal")][0].split()[1]) // 1024
        swap = int([l for l in info.splitlines()
                    if l.startswith("SwapTotal")][0].split()[1]) // 1024
        verdict("RAM", ram >= 3500, f"{ram} Mo (4 Go attendus)")
        verdict("Swap", swap >= 1500, f"{swap} Mo (2 Go recommandés)")
    except Exception as e:
        verdict("Mémoire", False, str(e))
    libre = shutil.disk_usage("/").free // (1024 ** 3)
    verdict("Disque libre", libre >= 8, f"{libre} Go")


def secrets() -> None:
    f = Path("/etc/agent.env")
    if not f.exists():
        verdict("/etc/agent.env", False, "absent")
        return
    mode = oct(f.stat().st_mode)[-3:]
    verdict("/etc/agent.env", mode == "600", f"permissions {mode}, 600 attendu")

    attendus = ["TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID"]
    manquants = [v for v in attendus if not os.environ.get(v)]
    verdict("Variables Telegram", not manquants,
            "manque " + ", ".join(manquants) if manquants else "")

    auth = any(os.environ.get(v) for v in
               ("ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_API_KEY",
                "CLAUDE_CODE_OAUTH_TOKEN"))
    verdict("Authentification modèle", auth,
            "" if auth else "aucun jeton renseigné")


def claude_code() -> None:
    chemin = shutil.which("claude")
    verdict("Commande claude", bool(chemin), chemin or "introuvable dans PATH")
    if not chemin:
        return
    try:
        r = subprocess.run(
            ["claude", "-p", "Réponds exactement : PRET", "--output-format", "json",
             "--max-turns", "2", "--allowedTools", ""],
            capture_output=True, text=True, timeout=180, cwd=DEPOT,
        )
        texte = ""
        try:
            texte = json.loads(r.stdout).get("result", "")
        except Exception:
            texte = r.stdout
        verdict("Appel au modèle", "PRET" in texte.upper(),
                (texte or r.stderr)[:120].replace("\n", " "))
    except Exception as e:
        verdict("Appel au modèle", False, str(e)[:120])


def navigateur() -> None:
    try:
        r = subprocess.run(["npx", "-y", "playwright", "--version"],
                           capture_output=True, text=True, timeout=180)
        verdict("Playwright", r.returncode == 0, r.stdout.strip()[:60])
    except Exception as e:
        verdict("Playwright", False, str(e)[:80])
    cache = Path.home() / ".cache" / "ms-playwright"
    chromiums = list(cache.glob("chromium*")) if cache.exists() else []
    verdict("Chromium installé", bool(chromiums),
            str(chromiums[0].name) if chromiums else f"rien dans {cache}")


def depot_git() -> None:
    if not (DEPOT / ".git").exists():
        verdict("Dépôt git", False, f"{DEPOT} n'est pas un dépôt")
        return
    verdict("Dépôt git", True, str(DEPOT))
    try:
        r = subprocess.run(["git", "push", "--dry-run"], cwd=DEPOT,
                           capture_output=True, text=True, timeout=60)
        verdict("Droit de pousser", r.returncode == 0,
                (r.stderr or "").strip().splitlines()[-1][:110]
                if r.returncode else "clé de déploiement acceptée")
    except Exception as e:
        verdict("Droit de pousser", False, str(e)[:80])


def telegram() -> None:
    jeton = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    salon = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not (jeton and salon):
        verdict("Envoi Telegram", False, "non configuré")
        return
    try:
        d = urllib.parse.urlencode({
            "chat_id": salon,
            "text": "✅ Vérification préalable : le canal fonctionne.",
        }).encode()
        u = f"https://api.telegram.org/bot{jeton}/sendMessage"
        with urllib.request.urlopen(urllib.request.Request(u, data=d),
                                    timeout=20) as r:
            ok = json.load(r).get("ok", False)
        verdict("Envoi Telegram", ok, "regarde ton téléphone" if ok else "")
    except Exception as e:
        verdict("Envoi Telegram", False, str(e)[:110])


def courriel() -> None:
    hote = os.environ.get("MAIL_IMAP_HOTE", "")
    utilisateur = os.environ.get("MAIL_ADRESSE", "")
    mdp = os.environ.get("MAIL_MOT_DE_PASSE", "")
    if not (hote and utilisateur and mdp):
        verdict("IMAP", False, "non configuré (l'agent ne recevra rien)")
        return
    try:
        with imaplib.IMAP4_SSL(hote) as m:
            m.login(utilisateur, mdp)
            m.select("INBOX")
        verdict("IMAP", True, f"{utilisateur} sur {hote}")
    except Exception as e:
        verdict("IMAP", False, str(e)[:110])


def cadre() -> None:
    requis = [
        "CLAUDE.md", "cadre/CONSTITUTION.md", "cadre/MISSION.md",
        "cadre/OUTILS.md", "cadre/ARGENT.md", "cadre/ARRET.md",
        "prompts/REVEIL.md", "prompts/TRIAGE.md", "prompts/VERIFICATION.md",
        "prompts/DIGEST.md", "etat/ENGAGEMENTS.md", "etat/INDEX.md",
        "bin/dire",
    ]
    manquants = [f for f in requis if not (DEPOT / f).exists()]
    verdict("Fichiers du cadre", not manquants,
            "manque " + ", ".join(manquants) if manquants else f"{len(requis)} présents")
    d = DEPOT / "bin" / "dire"
    if d.exists():
        verdict("bin/dire exécutable", os.access(d, os.X_OK),
                "" if os.access(d, os.X_OK) else "chmod +x bin/dire")


def main() -> int:
    print("\n\033[1mVérification préalable\033[0m\n")
    for section, f in [
        ("Machine", machine), ("Secrets", secrets), ("Cadre", cadre),
        ("Claude Code", claude_code), ("Navigateur", navigateur),
        ("Dépôt", depot_git), ("Telegram", telegram), ("Courriel", courriel),
    ]:
        print(f"\n— {section}")
        f()
    print()
    if ok_global:
        print("\033[32mTout est vert. Tu peux prendre l'instantané, "
              "puis démarrer.\033[0m\n")
        return 0
    print("\033[31mCorrige les échecs avant de démarrer.\033[0m "
          "Un agent lancé sur une brique cassée écrit un journal trompeur.\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
