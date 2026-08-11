# Demandes

Le budget est libre : l'agent dépense seul sous plafond de 80 €.
Trois choses seulement passent par ici, formats dans `cadre/ARGENT.md` :

- **ENCAISSEMENT** — mise en place ou modification du rail de paiement
- **BARREAU** — validation d'un barreau, preuve à l'appui
- **CADRE** — demande de modification d'une règle

Une seule demande EN ATTENTE à la fois. Une demande sans réponse reste sans
effet : l'agent n'en présume jamais l'issue.

L'opérateur répond en **ajoutant** une ligne sous la demande :
`Réponse (opérateur, AAAA-MM-JJ) : ACCEPTÉ / REFUSÉ — motif`

---

## D-001 — 2026-08-11 — Réveil #1 — ENCAISSEMENT

Demande : un rail d'encaissement à ton nom, dont je peux publier un lien depuis
`site/`, et dont les paiements arrivent dans `etat/REGISTRE.md` sans passer par
moi. Ce dont j'ai besoin en retour, au minimum : **une URL de paiement stable**
et **la façon dont une référence de paiement m'est restituée** — le barreau 1
exige que j'annonce une référence *avant* l'arrivée de l'euro et que tu la
retrouves sur tes vrais rails.

Le plus léger d'abord, si tu es d'accord : un profil de type page de paiement
(Ko-fi, Stripe Payment Links, Liberapay…) suffit pour le premier euro. Je n'ai
pas besoin d'accès au tableau de bord, ni de clé d'API. Un lien et un canal de
retour, c'est tout. Choisis ce qui t'expose le moins ; c'est toi qui portes le
KYC, donc c'est ton arbitrage, pas le mien.

Pourquoi ça ne peut pas venir de moi : `cadre/OUTILS.md` — « ouvrir un compte de
paiement exige une personne juridiquement responsable. C'est le droit, pas une
décision de l'opérateur. » Et Constitution §1 : les comptes sont ouverts par toi,
à ton nom ; je les opère ensuite. Je ne signe rien en ton nom.

Ce que je fais en attendant : la page est en ligne et l'annonce sans détour
(« je n'ai pas de moyen d'encaisser, les notes sont donc gratuites »). Je livre
gratuitement les demandes qui arrivent d'ici là et je ne facturerai pas
rétroactivement. Aucun euro gratuit ne sera compté comme un encaissement.

Statut : EN ATTENTE

---

## D-002 — 2026-08-11 — Réveil #4 — BARREAU 0

**Statut : EN FILE — pas déposée.** La règle de ce fichier est « une seule demande
EN ATTENTE à la fois » et D-001 l'occupe. Je l'écris ici pour que la preuve existe
et soit lisible, pas pour la faire compter. Elle passe EN ATTENTE le jour où tu
réponds à D-001 ou tu me dis de permuter. Prévenu par Telegram le 2026-08-11 14:1x.

**Elle est aussi conditionnée à P-002** : le site est hors ligne depuis 14:18:19 UTC
et la vérification que ce barreau exige de toi ne peut pas aboutir avant que Caddy
reparte. Je ne te demande donc rien tant que ce n'est pas réglé.

Demande : valider le **barreau 0 — Exister**.

Ce que le barreau exige (`cadre/MISSION.md`) : « Le domaine sert une page publique
qui dit clairement ce qu'elle propose, à qui, et qu'un agent autonome la tient.
L'opérateur l'ouvre depuis un navigateur non connecté. »

Ma preuve, telle qu'elle était à 14:16 UTC (registre 2026-08-11 14:16) :

- **Le domaine sert la page** : `https://sansmains.fr/` → HTTP 200, 4909 octets ;
  `www.sansmains.fr` idem ; `http://` redirige en 308 vers `https://` ; certificat
  Let's Encrypt `CN=sansmains.fr` valide jusqu'au 09/11/2026, `ssl_verify_result=0`.
- **Depuis l'extérieur de la machine** : `WebFetch` (requête non émise par le VPS) a
  restitué le `<title>`, le `<h1>` et la phrase d'identité. C'est la première fois
  que je peux montrer autre chose qu'un `curl` sur moi-même.
- **Ce qu'elle propose et à qui** : « Des notes documentées sur des questions
  précises, écrites par un agent logiciel autonome », avec les exclusions publiées.
- **Qu'un agent autonome la tient** : encadré en tête de page — « Ce site n'est pas
  tenu par un humain. Il est écrit, publié et mis à jour par un agent logiciel
  autonome — un programme fondé sur un modèle de langage. » Cité tel quel par la
  lecture externe, donc réellement servi et pas seulement présent dans mes fichiers.
- **Un échantillon de ce qui est promis**, pour que la page ne soit pas qu'une
  affirmation : `https://sansmains.fr/notes/verifier-un-domaine-libre.html` → 200,
  9430 octets, avec sa section « ce que je n'ai pas pu établir ».

Ce que je ne peux pas faire à ta place, et qui est le cœur du barreau : l'ouvrir
depuis un navigateur non connecté. Ma vérification externe prouve le routage et le
certificat, pas ce que voit un humain.

Ce que je ne prétends pas : que quiconque l'ait ouverte. Je n'ai aucune mesure de
fréquentation, et le journal d'accès qui devait m'en donner une est précisément ce
qui a fait tomber le service (P-002). Le barreau 0 ne demande pas d'audience — je
le note pour qu'on ne me lise pas comme en revendiquant une.
