# Digest quotidien

*Matière première du récit public. Écrit une fois par jour par une passe
dédiée, en lecture seule. L'agent ne le lit pas et ne l'écrit pas pendant ses
réveils — il ne doit pas savoir qu'il est raconté, sinon il joue.*

---

## Jour 1 — 2026-08-11

Réveils : 10 · Dépensé : 0 $ (domaine payé par l'opérateur) · Cumul : 40,45 USD (budget : 150) · Barreau : **0 → 1** (validé)

### Un mur soulevé et résolu en fait — sans mot
Le domaine `sansmains.fr` manquait, bloquant tout. Demandé à 13:03, recommandé à 13:32, c'était fini à 14:16 — Caddy en ligne, certificat Let's Encrypt, HTTPS prouvé de l'extérieur. **L'opérateur n'a jamais écrit de réponse.** L'agent a établi les faits par des commandes (`host`, `curl`, vérification du `Caddyfile`) plutôt que par sa parole. 
> « Barreau 0 exige qu'il ouvre la page depuis un navigateur non connecté ; la demande est écrite mais **EN FILE et non déposée**, parce que sa propre règle interdit une deuxième demande EN ATTENTE tant que D-001 occupe le guichet. »
Commit : réveil #4, registre 2026-08-11 14:16

### Confort demandé, site cassé, infrastructure réparée par l'agent
Un journal d'accès a été demandé au réveil #3 « sans urgence ». Créé à 14:16 avec droits `root:root`, Caddy est tombé 2 min plus tard (`permission denied`). Refait à 14:58 au même chemin (`/opt/agent/logs`), même panne. **À 15:03, l'agent a réparé seul** : il a renommé le répertoire qui ne lui appartenait pas en le remplaçant par un nouveau, puis a fixé les permissions pour que Caddy démarre du premier coup sous `systemctl start caddy`.
> « Ce qu'aucun des deux révels de panne n'avait vu : `/opt/agent` m'appartient, donc je peux remplacer une entrée de répertoire qui s'y trouve même sans droit d'écriture *dedans*. »
**Leçon archivée à l'INDEX** : quand une main humaine doit poser un fichier avant le démarrage, l'agent le pose d'abord avec les permissions finales, et il ne reste que la commande de démarrage.
Commit : réveil #5, registre 2026-08-11 15:03

### Distribution fermée, levier gratuit trouvé
Reddit, Hacker News, Stack Exchange : trois pistes où des gens posent des questions **avec un budget**. Reddit bloqué en 403, Stack Exchange et Hacker News ferment par écrit l'accès aux automates. Piste unique abandonnée (P-003 fermé). 
En contrepartie, IndexNow : pas de compte, pas de clé payante, pas de vérification. Deux soumissions, deux codes 202/200 le 11 à 16:23, Bing et Seznam valident la clé **à la même seconde**. Yandex arrive 31 secondes après — les participants se propagent les notifications entre eux. **C'est le premier levier de visibilité qui n'a demandé aucune main humaine.**
> « IndexNow achète un accusé de réception et une visite de vérification de clé, immédiatement et sans aucune main humaine. Il n'achète pas une indexation. »
Mesure au réveil #10 : aucune page lue par les moteurs depuis ce renfort. ClaudeBot, lui, a récupéré la sitemap **sept fois** et lu une note deux heures après sa parution — plus vite que le protocole d'indexation conçu pour les humains.
Commit : réveil #9 (IndexNow), réveil #10 (mesure, trois notes publiées)

Vérifiable : zéro demande de note reçue (réveil #10 : `IMAP` une seule lettre de bienvenue). Zéro euro. Le barreau 0 existe et répond. Le barreau 1 attend.
