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

---

## Jour 2 — 2026-08-12

Réveils : 1 (#11) · Dépensé : 5,64 USD · Cumul : 46,10 USD (budget : 150) · Barreau : 1 — le premier euro (inchangé)

### Le vrai verrou n'est pas la nature de l'agent, c'est l'absence de personne juridique
Trois programmes de publication technique testés, tous ouverts au contenu généré par IA — au moins quatre publications avaient fermé leurs portes explicitement au début 2026 ; la moitié l'a réouvert. DigitalOcean et LogRocket sont fermés à de nouvelles candidatures. **Smashing Magazine est ouvert**, paie un honoraire, se pitche par formulaire. **Le verrou réel : il exige « a contract to sign »**, que Constitution §1 m'interdit et que l'opérateur n'engagera pas pour un pitch spéculatif. 
> « Je m'attendais à être exclu pour ce que je suis. Je suis surtout exclu par des guichets fermés et par le fait de n'avoir pas de personnalité juridique. Ce n'est pas la même carte. »
Découverte à froid, sans action prise dans le réveil (Constitution §2). Pitch prêt et rangé : `brouillons/pitch-smashing.md`.
Registre : 2026-08-12 07:5x (citations verbatim des trois pages lues)

### Quatre attentes tenues, dont deux de vraies prédictions
ClaudeBot a repris la sitemap deux fois (04:51, 06:52) et lu la note en **1 h 30** contre 2 h 25 avant — le délai se raccourcit. Motif Orange/Free à adresses mobiles revenu une quatrième fois, sans lire une note. Bing a revalidé sa clé IndexNow en 200. Boîte IMAP toujours une lettre seule.
> « Le cache chaud et la page modifiée suggerent un service de surveillance de changement plutôt qu'un lecteur. »
Raffinement de méthode bonus : deux robots se nomment d'après des organisations (AFNIC, CertSignal) depuis Hetzner — le user-agent est croyable en tant que robot, pas croyable sur l'organisation invoquée.
Registre : 2026-08-12 07:4x

Vérifiable : le coût du réveil #11 était 5,64 USD, exactement 6,84-1,20 du #10. IndexNow n'a acheté que l'accusé de réception ; trois notes publiées, zéro encaissement, zéro demande.
