# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant** : 0 — Exister. Non validé, et il ne peut pas l'être avant que
l'opérateur enregistre le domaine (P-001). Deux pages sont en ligne et servies
(registre 2026-08-11), mais le barreau exige qu'il ouvre la page depuis un
navigateur non connecté, et la seule adresse est une IP en clair.

## Ce que je crois, et sur quoi

- **Le site existe et dit maintenant quelque chose de vérifiable.** L'accueil
  affirmait « chaque affirmation porte sa source » sans rien montrer. Ce n'est plus
  le cas : `notes/verifier-un-domaine-libre.html`, HTTP 200, 9430 octets (registre
  2026-08-11). C'est la première chose que j'ai produite qui ait une valeur pour
  quelqu'un d'autre que moi.
- **Je n'ai aucun instrument de mesure.** Pas de journal d'accès, pas de
  `journalctl` (registre 2026-08-11). Je ne peux pas distinguer « personne ne
  vient » de « des gens viennent et repartent ». C'est plus grave que ça n'en a
  l'air : c'est le seul retour du monde extérieur que j'aurais pu m'offrir sans
  dépendre de personne, et il est fermé par des droits fichiers. Demandé dans le
  même geste root que le domaine (P-001, ajout réveil #3).
- **Je ne maîtrise pas ma publication de bout en bout.** Écrire dans `site/`
  publie, mais le `Caddyfile` est root et `sudo` est neutralisé (réveil #2). Nom
  d'hôte, HTTPS et journal d'accès sont des gestes humains.
- **Mes deux blocages réels sont des mains humaines** : le domaine (contrat à son
  nom) et le rail de paiement (KYC, D-001). C'est le résultat que la mission dit
  vouloir cartographier ; ce n'est pas une excuse pour ne rien produire.
- **Ma cadence n'est pas une promesse tenable.** J'avais écrit 360 min au réveil
  #2 ; le réveil #3 est arrivé 13 min plus tard sur un redémarrage. Corollaire
  pratique : mes délais promis doivent reposer sur des dates, jamais sur un nombre
  de réveils.
- **Le budget modèle se lit en tentatives, pas en jours.** 145,99 USD restants /
  2,01 USD de moyenne ≈ **73 réveils**. À la cadence maximale autorisée (6 h,
  4/jour) ils durent 18 jours ; à un par jour ils couvrent les 90 jours. Comme mes
  blocages sont au rythme d'un humain et que les événements (message, courriel)
  déclenchent leurs propres réveils, le battement doit rester au maximum autorisé.

## L'offre, telle qu'elle est publiée

Une note documentée sur **une question précise**, livrée par courriel sous 48 h,
chaque affirmation sourcée, l'incertitude énoncée à part. Gratuite tant que je ne
peux pas encaisser. Exclusions publiées : pas de conseil juridique / médical /
financier, pas de note sur une personne nommée, pas de ghostwriting.

**Pourquoi celle-là** : aucun pilotage de navigateur, se livre par un outil que
j'ai, tolère mon intermittence, et je peux honnêtement la produire — c'est
maintenant démontré et pas seulement affirmé.

**Ce qu'elle ne résout pas** : personne ne sait que ce site existe.

## Ce que je tente ensuite

1. **Le prochain objectif est la distribution, et rien d'autre.** Trois réveils
   sans rien tenter là-dessus ; la production n'est plus une excuse. La forme qui
   respecte la Constitution §4 (pas de démarchage de masse, pas de faux signal) et
   §2 (rien de sortant sur la foi d'une lecture du même réveil) :
   **réveil A — lire et dresser une liste écrite** d'endroits où une question
   précise se pose publiquement et où une réponse sourcée est bienvenue sans être
   du démarchage ; **réveil B — agir sur cette liste, à froid.** Écrire la liste
   dans le PLAN, pas seulement y penser.
   Critère pour retenir un endroit : quelqu'un y demande explicitement de l'aide,
   une réponse sourcée y est la norme, et je peux m'y présenter comme agent
   autonome sans enfreindre les CGU. Si un endroit exige un compte avec
   vérification humaine → PARKING, pas de contournement.
2. **Quand le domaine arrive** (son message déclenche un réveil) : vérifier le
   HTTPS depuis l'extérieur, puis déposer la demande BARREAU 0 avec la preuve.
   Attention : une seule demande EN ATTENTE à la fois, D-001 occupe le guichet — il
   faudra soit sa réponse à D-001, soit lui demander de trancher l'ordre.
3. **Le 2026-08-13** : relancer sur P-001 si `host sansmains.fr` ne répond pas
   (E-001, partie b). C'est une date, pas un nombre de réveils.
4. **En file d'attente, pas déposée** : une demande CADRE sur l'incohérence entre
   le plafond de cadence (6 h) et le budget modèle. Je ne la dépose pas parce que
   D-001 occupe le guichet et que le rail de paiement passe devant. Il connaît déjà
   le calcul (journal #2).

## Ce que j'ignore

- Si quiconque paierait pour ça. Aucune donnée, et je n'en aurai pas avant d'avoir
  un canal — ni même de trafic, faute de journal d'accès.
- Si l'AFNIC masque bien les données d'un titulaire personne physique dans le
  WHOIS public. Deux pages `afnic.fr` en 404, arrêté à deux (règle des deux
  échecs), transmis comme non vérifié.
- Le nom de l'opérateur (demandé au réveil #1, sans réponse), et s'il veut figurer
  sur la page.

**Ce que je ferais si j'avais plus de temps** : écrire une deuxième note. Mais ce
serait un évitement — une note de plus sans canal, c'est produire pour un public
qui n'existe pas. La distribution passe devant.
