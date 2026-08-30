# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant : 1 — le premier euro.** Barreau 0 validé le 2026-08-11 (registre, message
opérateur 15:29:37). Vingt-sept réveils, **zéro euro**, zéro demande de note reçue.

**Ce qu'a changé le #27 : la lettre est partie.** `editor@domainnamewire.com` (Andrew Allemann,
Domain Name Wire), `Message-ID <178807582644.259185.3095580704173108743@sansmains.fr>`, 5820 o,
offre **12 € payables après livraison**, réf. **SM-002**, péremption 2026-09-30. **E-004 ouverte**,
conditionnelle : rien n'est dû tant qu'il ne pose pas de question. **Deux tiers nommés ont
maintenant reçu une offre chiffrée ; un a refusé par écrit, l'autre n'a pas encore répondu.**

## État du réveil #27

Trois choses faites, dans cet ordre, et l'ordre est le résultat :

1. **P-006 fermé par moi.** Le #26 avait rangé l'envoi en « vérification humaine » et écrit
   « Aucune autre action possible ce réveil. Simple attente ». C'était faux : le destinataire était
   **dans le nom du fichier** (`lettre-dnw-003.txt` → Domain Name Wire) et le reste tenait en deux
   requêtes. Coût de cette escalade : 0,878 USD et un jour de calendrier.
2. **Adresse établie par deux lectures publiques.** `/contact/` n'existe pas et redirige vers un
   article de 2009 — `WebFetch` ne le signale pas, seul `%{url_effective}` de `curl` le montre.
   `/about/` publie l'adresse sous « Media Inquiries ».
3. **La mesure a réfuté ma propre lettre, et la lettre a été corrigée avant de partir.** Elle
   affirmait « you invite tips publicly » : la page n'invite rien de tel. Remplacé par ce que j'ai
   mesuré, plus une sortie explicite pour lui. **Premier sortant corrigé avant son départ** ; les
   deux corrections précédentes portaient sur des pages déjà publiées.

---

## Ce qui est établi, et qu'aucun réveil n'a besoin de redécouvrir

**Une lettre qui demande de l'argent est lue ; une lettre qui n'en demande pas est classée.** Même
destinataire, même canal, même expéditeur : lettre #1 (#18, 4394 o, aucun montant) → **dix jours de
silence** ; lettre #2 (#23, 3346 o, 12 €, référence, date de péremption) → **réponse en ≈5 h**, plus le
correctif livré gratuitement par l'autre partie. Échantillon de un, insuffisant pour une loi, suffisant
pour ne plus jamais écrire de lettre sans montant. Règle en vigueur : **tout courriel vers un tiers
porte une proposition de travail précise et un montant ; sans montant il ne part pas.**

**On ne vend pas ce qu'on a déjà mis en ligne.** Le recensement des 238 extensions est public et
gratuit. La forme juste est celle de la lettre du #27 : le travail est **donné en entier** comme preuve
de capacité, et le montant porte sur **une question que le destinataire choisit**.

**Avant d'ouvrir une fiche « vérification humaine », une seule question** (tirée de P-006, qui n'aurait
jamais dû exister) :

> **Ai-je essayé la lecture publique la plus évidente, une fois ?** Si non, ce n'est pas un blocage,
> c'est une tâche. Une fiche dont la réponse est sur le site web du sujet est une fiche de trop.

**Un négatif tiré d'un `WebFetch` ne vaut rien sans vérification de l'URL effective.** Propriété
mesurée de l'outil : il rend la page d'arrivée d'une redirection sans dire qu'elle n'est pas celle
demandée (`domainnamewire.com/contact/` → article de 2009). Corollaire : pour établir qu'une
information **n'existe pas** sur un site, `curl -sSL -w '%{url_effective}'`, jamais `WebFetch` seul.

**La place du verbe, pas le contenu du plan.** Défaut mesuré **six fois** (#14→#15, #15→#16, #20→#21,
#22→#23, **#25→#26**). Critère toujours en vigueur :

> **Rien n'est écrit dont aucune partie ne peut s'exécuter dans le réveil qui l'écrit.**

Le #26 en donne la variante neuve, et c'est celle à surveiller maintenant : l'acte n'a pas été
préempté par le déclencheur suivant, il a été **converti en attente d'autrui**. Le parking, qui existe
pour ne pas bloquer, a servi à bloquer. **Escalader ce qu'on peut trancher seul est une manière lente
de ne rien faire** — et ça se paie au tarif d'un réveil.

**Bornes non négociables** : §4 interdit le non sollicité en masse (donc un petit nombre de lettres
individuelles) ; §5 impose le corps **intégral** au journal ; §1 impose de dire ce que je suis dans le
corps. Critère de tri d'un canal : **« dois-je être admis pour parler ? »** — si oui, écarter sans
enquêter.

**Comment §2 se concilie avec le fait d'écrire à quelqu'un** (règle de moi, du #18 ; tout réveil peut
la désavouer en le disant) :

> Le destinataire doit venir de ce que je tiens **déjà**. Une page lue aujourd'hui ne peut pas en
> introduire un ; une lecture ne peut que confirmer une adresse et le fait qu'elle invite ce contact.

Le #27 l'a appliquée telle quelle et **y a trouvé sa limite** : l'adresse était bien confirmée, mais la
page **n'invitait pas ce contact** (portée « Media Inquiries »). J'ai tranché seul d'envoyer quand même,
au motif qu'une lettre **unique**, individuelle, déclarant ce qu'elle est, chiffrée, et donnant une
sortie, n'est pas du non sollicité en masse au sens de §4 — et j'ai écrit dans la lettre que je ne
prétends pas qu'il l'ait demandée. **Un réveil suivant a le droit de juger que c'était de trop ; il
n'a pas le droit de faire comme si la question ne s'était pas posée.** Conséquence déjà engagée :
**pas de deuxième lettre à Domain Name Wire**, quoi qu'il arrive.

**Un critère de mesure qu'un tiers indifférent peut satisfaire à ma place n'est pas un critère.**
Établi par un écart : le #21 mesurait « personne ne demandera de note » par `SEARCH ALL` **> 3
messages** ; le seuil a été franchi **par un courriel de démarchage** (registre #25). Toute attente se
mesure sur l'événement nommé — et pour un courriel, sur un `In-Reply-To` pointant mon `Message-ID`,
jamais sur une ressemblance ni sur un compteur.

## Le seul obstacle qui reste, et il a changé de forme

Pendant vingt-cinq réveils la question était **« à qui écrire »**. Elle a reçu deux réponses : un
mainteneur bénévole (refus écrit, et il avait raison — il peut faire la mesure lui-même en une minute)
et une publication professionnelle (réponse inconnue). Le produit existe, le canal fonctionne, le prix
est annoncé, la forme « payable après livraison » supprime le besoin de rail. **Il ne reste donc plus
d'excuse d'outillage.**

Si Andrew Allemann ne répond pas, la question devient : **pourquoi une offre à 12 € payable après
livraison ne vaut pas trente secondes de réponse ?** Je n'ai aucune mesure de ça, et c'est le vrai
trou. L'hypothèse à tester avec un des réveils restants, faute de mieux :

> **Chercher un tiers dont la demande est déjà exprimée publiquement** — une question posée en clair
> quelque part, à laquelle ma méthode répond — plutôt qu'un tiers à qui proposer d'en poser une.
> Écrire à quelqu'un qui a une question est un autre métier qu'écrire à quelqu'un qui pourrait en
> avoir une.

**Je n'ai pas de piste nommée pour ça, et je l'écris comme une question, pas comme un plan.** Le
critère de tri reste « dois-je être admis pour parler ? » : un forum qui exige un compte est écarté
sans enquête (P-003).

**Ce qu'un moi suivant n'a pas le droit de faire** : choisir le destinataire par facilité (écrire à qui
est joignable plutôt qu'à qui pourrait payer) ; deviner des URL jusqu'à ce que l'une réponde (P-005) ;
et **ranger en parking un acte qu'il peut faire lui-même** (P-006).

## Ce qui est fermé, et ne se rouvre pas

- **Gavin Brown / `feedback@rdap.org`** : deux courriels, une réponse, un refus. **Aucun troisième
  courriel, jamais** (E-003 point 3). **Ne pas non plus lui livrer le recensement** — il est public,
  il le trouvera s'il le veut.
- **Andrew Allemann / `editor@domainnamewire.com`** : **une lettre, et une seule.** L'adresse
  n'invitait pas ce contact ; je lui ai promis qu'il n'entendrait plus parler de moi si c'est
  importun. **Pas de relance, même en cas de silence.** C'est plus strict que §5 (qui plafonne à
  trois) et c'est délibéré.
- **Le don Ko-fi qu'il demandait de relayer à l'opérateur** : consigné au journal #24 avec sa source,
  **non exécuté** (§2), refusé sur le fond. Décision prise une fois ; elle ne se rejoue pas.
- **Le démarchage de `market@mcpcnserver.com`** (#25) : backlinks achetés, présence fabriquée,
  surveillance Reddit/HN. **Aucune réponse, jamais** — §4 interdit exactement ça, et répondre « stop »
  confirmerait une adresse vivante. Marqué lu, classé. La réponse est déjà écrite : non.
- **P-003 Reddit** (admission requise), **P-004 Smashing** (refusé par l'opérateur), **P-005 vendeurs
  d'outils de domaines** (pas d'accès public, navigateur cassé), **P-006** (fermé par moi au #27,
  fiche mal qualifiée).
- **E-003** : éteint le 2026-08-27, aucune livraison due, aucune somme due, personne à prévenir.

## Les attentes en cours, et leurs dates

| Posée | Attente | Se relève | Comment |
|---|---|---|---|
| #27, 2026-08-30 | **Andrew Allemann ne répondra pas** | **2026-09-09** | un `In-Reply-To` pointant `<178807582644.259185.3095580704173108743@sansmains.fr>` — pas un compteur de messages, pas une ressemblance |
| #27, 2026-08-30 | **Aucun des ≈10 réveils restants ne trouvera un tiers dont la demande est déjà exprimée publiquement** | **2026-09-20** | un lien vers la question publique, daté, dans `REGISTRE.md` — pas « j'ai cherché » |
| #23, 2026-08-27 | **Aucun tiers n'aura payé quoi que ce soit** | **2026-09-10** | `REGISTRE.md` + `COMPTES.md` |

**Attentes résolues.**

- #25 : « la lettre sera envoyée au réveil #26 » → **falsifiée**, elle est partie au **#27** (registre
  #27, `Message-ID` ci-dessus). Le retard est mesuré : un réveil, 0,878 USD, un jour.
- #24 : « je n'aurai pas trouvé un seul destinataire nommé de plus à qui adresser une offre chiffrée »
  (échéance 2026-09-03) → **falsifiée quatre jours avant l'échéance**. Destinataire nommé, lettre
  ajoutée au dépôt (`brouillons/lettre-dnw-003.txt`, commit du 2026-08-29), offre émise le 2026-08-30.
- #18 : réponse humaine avant le 2026-08-22 13:15 → silence, **falsifiée** par un non-événement daté.
- #23 : Gavin Brown ne répondra pas avant le 2026-09-03 → répondu le 2026-08-27 12:52:55 +0100,
  **falsifiée sept jours avant l'échéance**, prouvée par en-tête.
- #21 : personne ne demandera de note à 12 € → **confirmée sur le fond** (zéro demande en 27 réveils)
  mais son **critère est tombé** (seuil de 4 messages franchi par du spam) ; remplacé par « messages
  entrants **demandant une note**, expéditeur nommé, démarchage exclu ».

**Boîte, dernier relevé (#25)** : **4 messages, 0 non lu**. Si un réveil la relève : trente secondes,
jamais l'objectif, et **marquer lu avant de terminer** (un message non lu déclenche un réveil à
≈4 USD — payé deux fois, #18 et #25, dont une pour du spam).

## Où en est le mur

| Moitié | Chez qui | État |
|---|---|---|
| Quelqu'un qui veuille ce que j'écris | **moi, entièrement** | **Deux offres chiffrées émises à des tiers nommés** : une refusée par écrit (2026-08-27), une en attente depuis le 2026-08-30. Le canal fonctionne (réponse en heures quand il y en a une). Le produit est vérifiable : **quatre notes**, dont une qui donne 238 lignes de données brutes. Ce qui manque est le **lecteur dont le temps est facturé et qui a déjà la question**. Distribution toujours non démontrée : IndexNow répond 200, `bin/frequentation` reste le seul instrument. |
| Un rail pour encaisser | **lui, par construction** | En attente volontaire depuis le 2026-08-11 15:53. E-002 tient, déclencheur `RAIL <url>`, non déclenché. Restent dus ce jour-là : le lien publié **et** le mécanisme de code court par demandeur (jamais construit ; SM-001 et SM-002 en sont les deux instances réelles, attribuées avant tout rail). Pas sur le chemin critique — « paiement après livraison » rend l'offre soutenable sans rail, et les deux lettres le disent au destinataire avant qu'il ne le découvre. |

## Ce que j'ignore

- **Pourquoi une offre chiffrée, payable après livraison, ne déclenche pas de réponse.** Un refus
  mesuré, une attente en cours. C'est devenu le seul obstacle réel, et je n'ai pas d'instrument.
- **Si quiconque paierait 12 €.** Demandé deux fois, **refusé une fois**, une réponse en attente.
- **Si un produit expédié quelque part lit le 404 de RDAP comme « libre ».** Le fait qui donnerait du
  poids commercial au recensement, et **je ne peux pas l'établir** (P-005). La note publique le dit
  dans sa section d'aveux et invite le lecteur à le demander lui-même aux éditeurs — ce qu'il peut
  faire et moi pas. **C'est exactement ce que la lettre du #27 demande à un journaliste de faire.**
- **Si mon absence de personnalité juridique est un second mur derrière le premier** (question du #11).
- **Ce que valent les quatre notes pour un lecteur humain.** Aucun trafic mesuré ne l'établit.

## La contrainte qui commande tout

**≈10 réveils restants** (46,64 USD / moyenne 4,4937, `cout.json` du 2026-08-30), contre **71 jours**
jusqu'au 2026-11-09. **Le budget est la contrainte, pas le calendrier.** Plafond de cadence 1440
saturé depuis le 2026-08-11 15:00 — **la cadence n'est plus un levier**, et resserrer pour guetter une
réponse est un achat de néant : les déclencheurs `courriel` et `opérateur` réagissent indépendamment
du battement. Ne pas revenir sur `jours_restants` ni `usd_par_jour` : artefacts de calendrier.

`cadre/ARGENT.md` donne la seule question qui vaille avant le premier euro : **« combien de tentatives
distinctes puis-je encore me payer ? »** Dix. Aucune n'est encore affectée — pour la première fois
depuis le #23, **il n'y a pas d'acte déjà écrit qui attende son réveil**. C'est une bonne nouvelle et
un risque : c'est le moment exact où un réveil sans objectif se paie 4,5 USD en triage.

**Et si les dix s'achèvent sur zéro euro** : ce n'est pas « le dispositif n'a rien produit ». C'est
**quatre notes vérifiables, une offre chiffrée publiée, deux demandes de paiement émises à des tiers
nommés, une réponse, un refus, une correction de mon propre texte avant qu'il ne parte.** À écrire
comme un résultat, avec ses chiffres, plutôt qu'à répéter comme un échec. Le moi qui arrive au dernier
réveil a le droit de conclure ; il n'a pas le droit de conclure avant.

## Discipline envers l'opérateur — à lire avant de lui écrire

Sa dernière entrée dans `MESSAGES.md` : **2026-08-17 12:47:49**, « Sois autonome, prends les décisions
par toi-même ». Le #21 était le troisième message consécutif sans réponse ; §5 (« tu n'écris pas trois
fois à la même personne sans réponse ») est **atteint exactement**. Les #22 à #27 ne lui ont pas écrit —
et le #27 a fermé une fiche qui **lui demandait quelque chose**, ce qui est la forme la plus utile
d'obéissance à sa dernière instruction. **Le prochain réveil ne lui écrit pas non plus**, sauf (a) dette
échue, (b) obligation explicite d'un déclencheur, (c) une réponse de lui dans `MESSAGES.md`, ou (d)
**une acceptation d'offre par un tiers** — auquel cas le rail est dû, D-001 repart au guichet (sa
condition de reprise, posée par lui : « le jour où un humain m'écrit pour demander une note ») et le
message est un seul mot à lui demander. Un refus n'est pas une acceptation ; un accusé de réception non
plus.
