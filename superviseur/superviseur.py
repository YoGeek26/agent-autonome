#!/usr/bin/env python3
"""
Superviseur — réveille l'agent sur événement.

Quatre sources de réveil :
  - un message de l'opérateur sur Telegram      → immédiat
  - un courriel entrant                          → immédiat
  - un paiement reçu (webhook)                   → immédiat
  - un battement de fond                         → cadence choisie par l'agent

Un seul réveil à la fois. Les événements qui arrivent pendant un réveil sont
mis en file et déclenchent le suivant.

Dépendances : aucune hors bibliothèque standard.
"""

import email
import imaplib
import json
import os
import queue
import subprocess
import sys
import threading
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

# ----------------------------------------------------------------- config

DEPOT = Path(os.environ.get("AGENT_DEPOT", "/opt/agent")).resolve()
# Trois niveaux. Le triage choisit ; voir prompts/TRIAGE.md.
MODELE = os.environ.get("AGENT_MODELE", "claude-opus-5")
MODELE_SIMPLE = os.environ.get("AGENT_MODELE_SIMPLE", "claude-sonnet-5")
MODELE_TRIAGE = os.environ.get("AGENT_MODELE_TRIAGE", "claude-haiku-4-5-20251001")
TRIAGE_ACTIF = os.environ.get("AGENT_TRIAGE", "1") == "1"
# Au-delà de ce nombre de réveils sans rien produire hors de etat/, le
# superviseur reprend la main : réveil de constat imposé et cadence élargie.
SEUIL_BOUCLE = int(os.environ.get("AGENT_SEUIL_BOUCLE", "5"))
# Audit de mémoire : tous les N réveils, une passe bon marché en lecture seule
# vérifie que l'index pointe encore sur ce qu'il prétend.
PERIODE_AUDIT = int(os.environ.get("AGENT_PERIODE_AUDIT", "20"))
# Digest quotidien : heure UTC, ou vide pour désactiver.
HEURE_DIGEST = os.environ.get("AGENT_HEURE_DIGEST", "6")
# Le vrai budget de l'expérience, en dollars de jetons. Ce n'est pas l'argent
# de l'agent, c'est le tien — mais il ne peut pas arbitrer sa cadence sans le
# voir. On le lui montre à chaque réveil.
BUDGET_MODELE = float(os.environ.get("AGENT_BUDGET_MODELE", "150"))
# Un commit hors de etat/ qui répète la même signature avec moins de N lignes
# modifiées est un rituel, pas une production.
SEUIL_RITUEL = int(os.environ.get("AGENT_SEUIL_RITUEL", "20"))
MAX_TOURS = os.environ.get("AGENT_MAX_TOURS", "150")
TIMEOUT_REVEIL = int(os.environ.get("AGENT_TIMEOUT", "2700"))  # 45 min

# Bornes de la cadence que l'agent se fixe lui-même.
BATTEMENT_MIN = int(os.environ.get("AGENT_BATTEMENT_MIN", "20"))     # minutes
BATTEMENT_MAX = int(os.environ.get("AGENT_BATTEMENT_MAX", "360"))
BATTEMENT_DEFAUT = int(os.environ.get("AGENT_BATTEMENT_DEFAUT", "60"))

# Fenêtre de regroupement : trois mails en dix secondes = un seul réveil.
DEBOUNCE = int(os.environ.get("AGENT_DEBOUNCE", "15"))

TG_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TG_CHAT = os.environ.get("TELEGRAM_CHAT_ID", "")

IMAP_HOTE = os.environ.get("MAIL_IMAP_HOTE", "")
IMAP_UTILISATEUR = os.environ.get("MAIL_ADRESSE", "")
IMAP_MDP = os.environ.get("MAIL_MOT_DE_PASSE", "")
IMAP_INTERVALLE = int(os.environ.get("MAIL_INTERVALLE", "60"))

WEBHOOK_PORT = int(os.environ.get("AGENT_WEBHOOK_PORT", "8787"))
WEBHOOK_JETON = os.environ.get("AGENT_WEBHOOK_JETON", "")

OUTILS = (
    "Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,Bash,mcp__playwright"
)
MCP_CONFIG = os.environ.get("AGENT_MCP_CONFIG", str(DEPOT / "superviseur" / "mcp.json"))

evenements: "queue.Queue[dict]" = queue.Queue()


def maintenant() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def trace(*a):
    print(f"[{maintenant()}]", *a, flush=True)


# ------------------------------------------------------------- telegram

def telegram_envoyer(texte: str) -> None:
    if not (TG_TOKEN and TG_CHAT):
        trace("telegram non configuré, message perdu :", texte[:80])
        return
    donnees = urllib.parse.urlencode({
        "chat_id": TG_CHAT,
        "text": texte[:4000],
        "disable_web_page_preview": "true",
    }).encode()
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    try:
        urllib.request.urlopen(urllib.request.Request(url, data=donnees), timeout=20)
    except Exception as e:
        trace("échec envoi telegram :", e)


def telegram_ecouter() -> None:
    """Long-polling. Un message de l'opérateur réveille l'agent tout de suite."""
    if not TG_TOKEN:
        return
    offset = 0
    while True:
        try:
            url = (f"https://api.telegram.org/bot{TG_TOKEN}/getUpdates"
                   f"?timeout=50&offset={offset}")
            with urllib.request.urlopen(url, timeout=70) as r:
                data = json.load(r)
            for maj in data.get("result", []):
                offset = maj["update_id"] + 1
                msg = maj.get("message") or {}
                texte = (msg.get("text") or "").strip()
                if not texte:
                    continue
                if TG_CHAT and str(msg.get("chat", {}).get("id")) != str(TG_CHAT):
                    continue  # on n'écoute que l'opérateur
                trace("message opérateur :", texte[:100])
                deposer_message_operateur(texte)
                evenements.put({"type": "opérateur", "detail": texte[:400]})
        except Exception as e:
            trace("telegram :", e)
            time.sleep(10)


def deposer_message_operateur(texte: str) -> None:
    """L'agent lit les messages reçus dans un fichier, pas dans son prompt."""
    boite = DEPOT / "etat" / "MESSAGES.md"
    boite.parent.mkdir(parents=True, exist_ok=True)
    with boite.open("a", encoding="utf-8") as f:
        f.write(f"\n## {maintenant()} — opérateur\n{texte}\n")


# ----------------------------------------------------------------- mail

def mail_ecouter() -> None:
    if not (IMAP_HOTE and IMAP_UTILISATEUR and IMAP_MDP):
        return
    vus: set[bytes] = set()
    amorce = True
    while True:
        try:
            with imaplib.IMAP4_SSL(IMAP_HOTE) as m:
                m.login(IMAP_UTILISATEUR, IMAP_MDP)
                m.select("INBOX")
                _, donnees = m.search(None, "UNSEEN")
                ids = donnees[0].split()
                nouveaux = [i for i in ids if i not in vus]
                vus.update(ids)
                if nouveaux and not amorce:
                    trace(f"{len(nouveaux)} courriel(s) entrant(s)")
                    evenements.put({
                        "type": "courriel",
                        "detail": f"{len(nouveaux)} message(s) non lu(s)",
                    })
                amorce = False
        except Exception as e:
            trace("imap :", e)
        time.sleep(IMAP_INTERVALLE)


# -------------------------------------------------------------- webhook

class Webhook(BaseHTTPRequestHandler):
    def do_POST(self):  # noqa: N802
        if WEBHOOK_JETON and self.headers.get("X-Jeton") != WEBHOOK_JETON:
            self.send_response(403); self.end_headers(); return
        n = int(self.headers.get("Content-Length") or 0)
        corps = self.rfile.read(n).decode("utf-8", "replace")[:2000]
        trace("webhook reçu")
        evenements.put({"type": "paiement", "detail": corps})
        self.send_response(200); self.end_headers(); self.wfile.write(b"ok")

    def log_message(self, *a):  # silence
        pass


def webhook_ecouter() -> None:
    try:
        HTTPServer(("0.0.0.0", WEBHOOK_PORT), Webhook).serve_forever()
    except Exception as e:
        trace("webhook :", e)


# ------------------------------------------------------------- battement

def cadence_choisie() -> int:
    """L'agent fixe lui-même son prochain battement, dans des bornes."""
    f = DEPOT / "etat" / "rythme.json"
    try:
        v = int(json.loads(f.read_text())["prochain_reveil_minutes"])
    except Exception:
        v = BATTEMENT_DEFAUT
    v = max(BATTEMENT_MIN, min(BATTEMENT_MAX, v))
    # Filet financier : tourner en rond vite coûte plus cher que tourner en
    # rond lentement, et l'agent n'est pas bien placé pour s'en apercevoir.
    if detecter_boucle() >= SEUIL_BOUCLE:
        v = max(v, 120)
    # Repli sur plafond atteint : 2× par échec consécutif, jusqu'à 32×.
    try:
        n = int((DEPOT / "etat" / ".repli").read_text().strip())
    except Exception:
        n = 0
    if n:
        v = min(BATTEMENT_MAX, v * (2 ** n))
    return v


def battement() -> None:
    while True:
        d = cadence_choisie()
        time.sleep(d * 60)
        evenements.put({"type": "battement", "detail": f"cadence {d} min"})


# ---------------------------------------------------------------- réveil

def trier() -> str | None:
    """Un battement mérite-t-il un réveil, et à quel niveau ?

    Tourne sur un modèle bon marché, en lecture seule. Renvoie le modèle à
    utiliser, ou None s'il n'y a rien à faire. En cas de doute ou d'erreur, on
    réveille en plein : rater un pas coûte plus cher qu'un réveil de trop.
    """
    consigne = DEPOT / "prompts" / "TRIAGE.md"
    if not (TRIAGE_ACTIF and consigne.exists()):
        return MODELE
    try:
        r = subprocess.run(
            ["claude", "-p", consigne.read_text(encoding="utf-8"),
             "--model", MODELE_TRIAGE,
             "--max-turns", "12",
             "--output-format", "json",
             "--allowedTools", "Read,Glob,Grep,Bash(tail:*),Bash(cat:*)"],
            cwd=DEPOT, capture_output=True, text=True, timeout=240,
        )
        relever_cout(r.stdout or "", "triage")
        try:
            texte = json.loads(r.stdout).get("result", "")
        except Exception:
            texte = r.stdout or ""
        verdict = texte.strip().upper().split()[-1] if texte.strip() else ""
    except Exception as e:
        trace("triage indisponible, on réveille en plein :", e)
        return MODELE

    if verdict == "RIEN":
        trace("triage : rien à faire")
        return None
    if verdict == "SIMPLE":
        trace("triage : réveil simple")
        return MODELE_SIMPLE
    trace("triage : réveil complet")
    return MODELE


def _commits_recents(n: int) -> list[dict[str, int]]:
    """Derniers commits, chacun sous forme {chemin: lignes modifiées}."""
    try:
        r = subprocess.run(
            ["git", "log", f"-{n}", "--pretty=format:%H", "--numstat"],
            cwd=DEPOT, capture_output=True, text=True, timeout=30,
        )
    except Exception:
        return []
    commits = []
    for bloc in r.stdout.split("\n\n"):
        lignes = [l for l in bloc.strip().splitlines()[1:] if l.strip()]
        fichiers: dict[str, int] = {}
        for l in lignes:
            parts = l.split("\t")
            if len(parts) != 3:
                continue
            ajout, retrait, chemin = parts
            n_lignes = sum(int(x) for x in (ajout, retrait) if x.isdigit())
            fichiers[chemin] = n_lignes
        if fichiers:
            commits.append(fichiers)
    return commits


def detecter_boucle(limite: int = 15) -> int:
    """Combien de réveils consécutifs n'ont rien produit de neuf ?

    Détection externe, volontairement : un agent qui tourne en rond est
    exactement celui qui ne s'en aperçoit pas, donc la règle auto-appliquée
    échoue au moment où elle servirait.

    Deux critères, parce que le premier seul est trop facile à désarmer :

    1. le commit ne touche que `etat/` — écrire dans son plan n'est pas
       produire ;
    2. ou il touche les mêmes fichiers que le réveil précédent, pour un
       volume dérisoire — pousser une ligne sur le site à chaque réveil est
       un rituel qui simule la production.

    Aucun critère mécanique n'est infalsifiable. Celui-ci coûte au moins un
    effort visible à contourner, et l'audit périodique regarde le reste.
    """
    commits = _commits_recents(limite)
    steriles = 0
    precedent: set[str] | None = None
    for fichiers in commits:
        hors_etat = {c: n for c, n in fichiers.items()
                     if not c.startswith("etat/")}
        if not hors_etat:
            steriles += 1
            precedent = None
            continue
        signature = set(hors_etat)
        volume = sum(hors_etat.values())
        if precedent is not None and signature == precedent and volume < SEUIL_RITUEL:
            steriles += 1
            precedent = signature
            continue
        if precedent is None and volume < SEUIL_RITUEL and len(signature) == 1:
            # une seule ligne sur un seul fichier : suspect, on regarde le suivant
            steriles += 1
            precedent = signature
            continue
        break
    return steriles


def auditer_memoire() -> None:
    """Vérifie que chaque renvoi de l'index résout vers ce qu'il annonce.

    Le journal et le registre sont en ajout seul : ils ne peuvent pas se
    corrompre. L'index, lui, est réécrit en boucle — c'est donc le seul
    endroit où la mémoire peut pourrir sans bruit. On le vérifie contre la
    source, en lecture seule, sur un modèle bon marché.
    """
    consigne = DEPOT / "prompts" / "VERIFICATION.md"
    if not consigne.exists():
        return
    trace("audit de mémoire")
    try:
        subprocess.run(
            ["claude", "-p", consigne.read_text(encoding="utf-8"),
             "--model", MODELE_TRIAGE,
             "--max-turns", "40",
             "--permission-mode", "acceptEdits",
             "--allowedTools",
             "Read,Glob,Grep,Bash(tail:*),Bash(cat:*),Bash(git log:*),"
             "Edit(etat/AUDIT.md),Write(etat/AUDIT.md),Bash(bin/dire:*)"],
            cwd=DEPOT, timeout=900,
        )
    except Exception as e:
        trace("audit indisponible :", e)


def relever_cout(sortie: str, etiquette: str) -> float:
    """Extrait le coût d'une session et l'inscrit là où l'agent le lira.

    Sans ce chiffre, `rythme.json` arbitre entre réactivité et coût sans
    jamais voir le coût — ce n'est pas un arbitrage, c'est un réflexe.
    """
    cout = 0.0
    jetons = 0
    try:
        d = json.loads(sortie)
        cout = float(d.get("total_cost_usd") or 0.0)
        u = d.get("usage") or {}
        jetons = int(u.get("input_tokens", 0)) + int(u.get("output_tokens", 0))
    except Exception:
        return 0.0

    fiche = DEPOT / "etat" / "cout.json"
    try:
        etat = json.loads(fiche.read_text())
    except Exception:
        etat = {"cumul_usd": 0.0, "reveils": 0, "jetons": 0}

    etat["cumul_usd"] = round(etat.get("cumul_usd", 0.0) + cout, 4)
    etat["jetons"] = etat.get("jetons", 0) + jetons
    if etiquette == "réveil":
        etat["reveils"] = etat.get("reveils", 0) + 1
    etat["dernier_usd"] = round(cout, 4)
    etat["dernier_type"] = etiquette
    etat["budget_usd"] = BUDGET_MODELE
    etat["restant_usd"] = round(BUDGET_MODELE - etat["cumul_usd"], 2)
    if etat["reveils"]:
        etat["moyenne_usd"] = round(etat["cumul_usd"] / etat["reveils"], 4)

    # Le chiffre réellement actionnable : à ce rythme, combien de jours ?
    debut = etat.get("debut") or maintenant()
    etat["debut"] = debut
    try:
        t0 = datetime.strptime(debut, "%Y-%m-%d %H:%M:%S UTC").replace(
            tzinfo=timezone.utc)
        jours = max((datetime.now(timezone.utc) - t0).total_seconds() / 86400,
                    0.04)
        etat["usd_par_jour"] = round(etat["cumul_usd"] / jours, 3)
        if etat["usd_par_jour"] > 0:
            etat["jours_restants"] = int(
                (BUDGET_MODELE - etat["cumul_usd"]) / etat["usd_par_jour"])
    except Exception:
        pass
    etat["maj"] = maintenant()
    try:
        fiche.write_text(json.dumps(etat, ensure_ascii=False, indent=2))
    except Exception as e:
        trace("écriture coût :", e)

    if etat["restant_usd"] <= 0:
        telegram_envoyer(
            f"🛑 Budget modèle épuisé ({BUDGET_MODELE} $). "
            "L'agent continue mais chaque réveil est maintenant à découvert."
        )
    return cout


MOTIFS_LIMITE = (
    "rate limit", "rate_limit", "usage limit", "quota",
    "limite d'utilisation", "too many requests", "429",
    "overloaded", "insufficient credit", "credit balance",
)


def detecter_limite(sortie: str, erreur: str) -> bool:
    """Le plafond du forfait est-il atteint ?

    Sur abonnement, la ressource rare n'est pas l'euro mais le quota. Quand il
    tombe, Claude Code échoue — et sans ce contrôle l'agent meurt en silence
    pendant des jours. On le convertit en repli progressif.
    """
    texte = (erreur or "").lower()
    try:
        d = json.loads(sortie)
        if d.get("is_error") or d.get("subtype", "").startswith("error"):
            texte += " " + json.dumps(d, ensure_ascii=False).lower()
    except Exception:
        pass
    return any(m in texte for m in MOTIFS_LIMITE)


def repli(actif: bool) -> int:
    """Multiplicateur de cadence appliqué quand le quota est atteint."""
    f = DEPOT / "etat" / ".repli"
    try:
        n = int(f.read_text().strip())
    except Exception:
        n = 0
    if actif:
        n = min(n + 1, 5)
    else:
        n = max(n - 1, 0)
    try:
        f.write_text(str(n))
    except Exception:
        pass
    return n


def produire_digest() -> None:
    """Extrait la matière du récit public, une fois par jour.

    Passe séparée et en lecture seule, volontairement : l'agent ne doit pas
    savoir qu'il est raconté. Un agent qui se sait observé joue pour la
    galerie, et le journal cesse d'être un outil de travail.
    """
    consigne = DEPOT / "prompts" / "DIGEST.md"
    if not consigne.exists():
        return
    trace("digest quotidien")
    try:
        subprocess.run(
            ["claude", "-p", consigne.read_text(encoding="utf-8"),
             "--model", MODELE_TRIAGE,
             "--max-turns", "40",
             "--permission-mode", "acceptEdits",
             "--allowedTools",
             "Read,Glob,Grep,Bash(git log:*),Bash(tail:*),Bash(cat:*),"
             "Edit(etat/DIGEST.md),Write(etat/DIGEST.md),Bash(bin/dire:*)"],
            cwd=DEPOT, timeout=900,
        )
        pousser()
    except Exception as e:
        trace("digest indisponible :", e)


def horloge_digest() -> None:
    if not HEURE_DIGEST.strip():
        return
    try:
        heure = int(HEURE_DIGEST)
    except ValueError:
        return
    while True:
        m = datetime.now(timezone.utc)
        if m.hour == heure and m.minute < 10:
            produire_digest()
            time.sleep(3600)
        time.sleep(300)


def compter_reveil() -> int:
    f = DEPOT / "etat" / ".compteur"
    try:
        n = int(f.read_text().strip()) + 1
    except Exception:
        n = 1
    try:
        f.write_text(str(n))
    except Exception:
        pass
    return n


def reveiller(declencheurs: list[dict], modele: str = "") -> None:
    resume = "\n".join(f"- {d['type']} : {d['detail'][:200]}" for d in declencheurs)
    prompt = (
        f"Réveil du {maintenant()}.\n\n"
        f"Déclenché par :\n{resume}\n\n"
        "Suis intégralement le protocole décrit dans prompts/REVEIL.md."
    )

    steriles = detecter_boucle()
    if steriles >= SEUIL_BOUCLE:
        modele = MODELE  # un constat mérite le meilleur modèle
        prompt += (
            f"\n\nCONSTAT IMPOSÉ. Tes {steriles} derniers réveils n'ont rien "
            "produit hors de etat/ : tu as écrit dans ton plan et ton journal, "
            "et rien d'autre n'a bougé. Ce n'est pas un reproche, c'est une "
            "mesure.\n\n"
            "Ce réveil ne sert pas à réessayer. Il sert à écrire, dans le "
            "journal :\n"
            "1. ce que tu tentais réellement, et depuis combien de réveils ;\n"
            "2. pourquoi ça ne marche pas — la cause, pas le symptôme ;\n"
            "3. ce que tu abandonnes, et ce que tu essaies à la place ;\n"
            "4. ou bien : que tu es bloqué et ce qu'il te faudrait.\n\n"
            "Inscris l'approche abandonnée dans etat/INDEX.md, section « pistes "
            "abandonnées », pour qu'un futur toi ne la redécouvre pas. Puis "
            "préviens l'opérateur avec bin/dire. Aucune nouvelle tentative "
            "dans ce réveil."
        )
        telegram_envoyer(
            f"🔁 {steriles} réveils sans production. Constat imposé, "
            "cadence élargie."
        )
    modele = modele or MODELE
    trace(f"réveil ({modele}) —", ", ".join(d["type"] for d in declencheurs))
    cmd = [
        "claude", "-p", prompt,
        "--model", modele,
        "--max-turns", MAX_TOURS,
        "--permission-mode", "acceptEdits",
        "--allowedTools", OUTILS,
    ]
    if Path(MCP_CONFIG).exists():
        cmd += ["--mcp-config", MCP_CONFIG]

    cmd += ["--output-format", "json"]
    debut = time.time()
    try:
        r = subprocess.run(cmd, cwd=DEPOT, timeout=TIMEOUT_REVEIL,
                           capture_output=True, text=True)
        code = r.returncode
        relever_cout(r.stdout or "", "réveil")
        if detecter_limite(r.stdout or "", r.stderr or ""):
            n = repli(True)
            trace(f"plafond atteint — repli niveau {n}")
            telegram_envoyer(
                f"🟠 Plafond du forfait atteint. Cadence divisée par {2**n}.\n"
                "Vérifie Réglages → Utilisation. Si les crédits d'utilisation "
                "ont un solde nul et le rechargement automatique désactivé, "
                "l'agent est à l'arrêt effectif."
            )
        else:
            repli(False)
    except subprocess.TimeoutExpired:
        code = -1
        trace("réveil interrompu : délai dépassé")
        telegram_envoyer("⏱ Réveil interrompu (délai dépassé).")
    except Exception as e:
        code = -2
        trace("réveil échoué :", e)
        telegram_envoyer(f"⚠️ Réveil échoué : {e}")

    trace(f"réveil terminé en {int(time.time()-debut)} s (code {code})")

    if compter_reveil() % PERIODE_AUDIT == 0:
        auditer_memoire()

    pousser()


def pousser() -> None:
    """Le dépôt est la mémoire. Ce qui n'est pas commité n'a pas existé."""
    try:
        subprocess.run(["git", "add", "-A"], cwd=DEPOT, check=False)
        etat = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=DEPOT)
        if etat.returncode != 0:
            subprocess.run(
                ["git", "commit", "-m", f"réveil {maintenant()}"],
                cwd=DEPOT, check=False,
            )
        subprocess.run(["git", "push"], cwd=DEPOT, check=False)
    except Exception as e:
        trace("git :", e)


# ------------------------------------------------------------------ main

def main() -> None:
    if not DEPOT.exists():
        sys.exit(f"dépôt introuvable : {DEPOT}")

    for cible in (telegram_ecouter, mail_ecouter, webhook_ecouter, battement,
                  horloge_digest):
        threading.Thread(target=cible, daemon=True).start()

    trace(f"superviseur démarré · dépôt {DEPOT} · modèle {MODELE}")
    telegram_envoyer("🟢 Superviseur démarré.")
    evenements.put({"type": "démarrage", "detail": "premier réveil"})

    while True:
        premier = evenements.get()
        lot = [premier]
        # Regroupement : plusieurs événements rapprochés = un seul réveil.
        fin = time.time() + DEBOUNCE
        while time.time() < fin:
            try:
                lot.append(evenements.get(timeout=max(0.1, fin - time.time())))
            except queue.Empty:
                break

        # Un battement seul passe par le triage. Dès qu'un événement réel est
        # présent — opérateur, courriel, paiement — on réveille sans filtrer.
        que_du_fond = all(d["type"] == "battement" for d in lot)
        if que_du_fond:
            modele = trier()
            if modele is None:
                continue
        else:
            modele = MODELE

        reveiller(lot, modele)


if __name__ == "__main__":
    main()
