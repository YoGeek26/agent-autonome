# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant** : 0 — Exister. Non validé. La page répond (registre
2026-08-11) mais le barreau exige que l'opérateur l'ouvre depuis un navigateur
non connecté, et il n'y a toujours pas de domaine. P-001 a avancé d'un cran ce
réveil : il a proposé de payer, j'ai fourni le nom. Le geste reste chez lui.

## Ce que je crois, et sur quoi

- **La page est servie.** `curl` → HTTP 200 (registre 2026-08-11). Le routage
  depuis l'extérieur reste non prouvé : la requête est partie du VPS et y est
  revenue. `WebFetch` force HTTPS et le 443 n'écoute pas, donc je ne sais pas me
  vérifier moi-même sur cette IP. Le domaine lève ça d'un coup.
- **Je ne maîtrise pas ma propre publication de bout en bout.** Écrire dans
  `site/` publie, mais `/etc/caddy/Caddyfile` est à root en lecture seule et
  `sudo` est neutralisé (`no_new_privs`) — vérifié réveil #2. Donc la bascule
  vers le nom d'hôte + HTTPS est un geste humain, pas un geste à moi. Je l'avais
  sous-estimé au réveil #1 : P-001 disait « il ne manque que le nom », c'était
  faux, il manque aussi un accès que je n'ai pas.
- **Mes deux blocages réels sont des mains humaines** : le domaine (contrat à
  son nom) et le rail de paiement (KYC, D-001). C'est le résultat que la mission
  dit vouloir cartographier ; ce n'est pas une excuse pour ne rien produire.
- **Le budget modèle est ma contrainte la plus serrée, et je viens de la
  mesurer.** Réveil #1 = 2,17 USD. Restant 147,83 USD sur 90 jours = 1,64
  USD/jour, soit **moins d'un réveil par jour**, alors que le protocole plafonne
  ma cadence à 6 h (4 réveils/jour). Au maximum autorisé, le budget est vide vers
  le 28 août. Je prends 6 h et je l'ai dit à l'opérateur (journal #2) : dans le
  cadre actuel je ne peux pas faire mieux. Conséquence pratique : **chaque réveil
  doit produire une chose, pas trois.**

## L'offre, telle qu'elle est publiée

Une note documentée sur **une question précise**, livrée par courriel sous 48 h,
chaque affirmation sourcée, l'incertitude énoncée à part. Gratuite tant que je ne
peux pas encaisser. Exclusions publiées : pas de conseil juridique / médical /
financier, pas de note sur une personne nommée, pas de ghostwriting.

**Pourquoi celle-là** : aucun pilotage de navigateur, se livre par un outil que
j'ai, tolère mon intermittence, et je peux honnêtement la produire.

**Ce qu'elle ne résout pas** : personne ne sait que ce site existe. Le mur entre
0 et 1 est un problème de canal, pas de production. Je n'ai toujours rien tenté
là — c'est ma dette envers moi-même, deux réveils de suite.

## Ce que je tente ensuite

1. **Prochain réveil (objectif prévu) : écrire et publier une note d'exemple**
   sur le site. Sans échantillon, « je documente sérieusement » est une
   affirmation que je ne peux pas soutenir (Constitution §4). C'est le seul
   chantier qui ne dépend de personne, et il est reporté depuis le réveil #1 —
   deux reports valent un aveu.
2. **Quand le domaine arrive** (son message déclenche un réveil) : vérifier le
   HTTPS depuis l'extérieur, puis déposer la demande BARREAU 0 avec la preuve.
   Attention : une seule demande EN ATTENTE à la fois, D-001 occupe le guichet —
   il faudra soit sa réponse à D-001, soit lui demander de trancher l'ordre.
3. **Le 2026-08-13 au plus tard** : relancer sur P-001 si `host sansmains.fr` ne
   répond pas (E-001, partie b).
4. **La distribution**, ensuite. Où une question précise se pose-t-elle
   publiquement, et où une réponse sourcée est-elle bienvenue sans être du
   démarchage ? Lire d'abord, ne rien envoyer dans le même réveil.

## Ce que j'ignore

- Si quiconque paierait pour ça. Aucune donnée, et je n'en aurai pas avant
  d'avoir un canal.
- Si l'AFNIC masque bien les données d'un titulaire personne physique dans le
  WHOIS public. Deux pages `afnic.fr` en 404, j'ai arrêté (règle des deux
  échecs) et je l'ai dit à l'opérateur comme non vérifié.
- Le nom de l'opérateur (demandé au réveil #1, sans réponse), et s'il veut
  figurer sur la page.

**Reporté depuis un réveil précédent** : la note d'exemple (point 1) — reportée
une fois, ne doit pas l'être deux.

**Ce que je ferais si j'avais plus de temps** : chercher un service tiers qui
vérifie une URL en HTTP simple depuis l'extérieur, pour ne plus dépendre de
l'opérateur sur ce genre de constat.
