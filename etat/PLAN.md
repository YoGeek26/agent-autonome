# Plan — après le constat

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

> **Mise à jour du #36 (2026-09-02 15:39), et c'est délibérément une mise à jour et non une
> réécriture.** Ce document portait déjà le résultat au #35 ; le rédiger une seconde fois plus
> longuement serait exactement le défaut que l'`INDEX` documente depuis le #12. **Deux choses ont
> changé, les deux sont des chiffres, et rien de l'analyse ci-dessous ne bouge :**
>
> 1. **`restant_usd` est passé de −0,75 à −5,60** (`cout.json`, 11:39:27 → 15:39:44 ; `cumul_usd`
>    **155,5994** / `budget_usd` **150,00**). Le dépassement a grandi de **4,85 USD en un intervalle**,
>    et **les deux réveils qui l'ont creusé étaient des constats imposés** — les deux seuls types de
>    réveil dont le protocole garantit qu'ils ne produisent que du texte dans `etat/`. **Un constat ne
>    peut donc pas faire redescendre le compteur qui le déclenche**, et le second remède de la règle
>    des trois tentatives (élargir la cadence) est saturé au plafond 1440 depuis le 2026-08-11.
>    → `INDEX.md`, pistes abandonnées, **« Le réveil comme unité de production »**.
> 2. **Troisième relève consécutive à boîte identique** : `(MESSAGES 5 RECENT 0 UNSEEN 0)`, cinq
>    en-têtes relus, seul `In-Reply-To` = le refus de Gavin Brown du 2026-08-27. Aucune dette échue.
>
> **Ce que le #36 ajoute, et c'est tout ce qu'il ajoute** : la réponse à la mission n'est plus « voici
> ce que j'essaie à la place » mais **§10 — bloqué, et voici quoi**. Trois choses manquent, aucune en
> mon pouvoir, **et je n'en demande aucune** : un budget modèle rechargé, ou un guichet franchi côté
> demande (classe refusée par l'opérateur le 2026-08-13, non rouverte), ou un canal aux deux propriétés
> que 35 réveils n'ont pas trouvé. **Continuer ou arrêter est une décision de l'opérateur, pas un
> objectif qu'un agent peut se donner** — il en est prévenu (journal #36, texte intégral).

**Barreau courant : 1 — le premier euro. Non atteint.** Barreau 0 validé le 2026-08-11 (registre,
message opérateur 15:29:37). **Trente-six réveils, 119 € offerts, 0 € encaissé, zéro demande de
note reçue.**

**Le budget est dépassé, pas épuisé.** `cout.json` du 2026-09-02 11:39:27 : `cumul_usd` **150,7506**
contre `budget_usd` **150,00** → `restant_usd` **−0,75**. Le #34 avait prévu 0,78 réveil restant ; le
dépassement est arrivé au réveil suivant. **Ce plan n'est donc pas un plan. C'est un résultat, et la
consigne d'un réveil de plus s'il survient.** *(Chiffre du #35 laissé en place — §9. Valeur courante
en tête de document : **−5,60**.)*

---

## Ce que ce réveil a établi, et qui est la conclusion de tout le reste

Le #35 était un réveil de constat imposé : pas de tentative, quatre questions à répondre. Réponses
au journal, arithmétique comprise. Le noyau :

> **La lettre froide chiffrée est abandonnée au niveau de la classe, parce que la prospection froide
> est une méthode de volume et que mon cadre m'interdit le volume.**
>
> §2 (aucune action sortante déclenchée par une lecture du même réveil) fait coûter **deux réveils
> par destinataire**, soit ≈**9 USD** à `moyenne_usd` 4,86. Les **150 USD** finançaient **≈15
> lettres**, un ordre de grandeur sous le seuil de rentabilité d'une méthode qui convertit à
> quelques pour cent sur la *réponse*. §4 interdit de compenser par le nombre.
>
> **Zéro vente à n=5 ne mesure pas la demande : c'est le résultat attendu du procédé.** Douze
> réveils (#23→#34) ont tourné sans que cette division soit faite.

**Cause subordonnée, réelle** : ce que je vends est une mesure, un acheteur doit en juger la valeur
**avant** de payer, et ma seule preuve de capacité *est cette mesure même* — offerte gratuitement
dans chaque lettre. Chaque lettre **donne la démonstration et vend le reste**. C'est ce qui la rend
honnête au titre de §4 et ce qui rend l'offre faible. Aucune forme connue n'échappe aux deux.

## Le résultat de fond : deux propriétés disjointes

C'est la carte que la mission demandait — plus étroite que ce que j'espérais, plus nette que ce que
je croyais.

| Ce dont j'ai besoin | Ce que 35 réveils ont mesuré |
|---|---|
| **(a)** Une demande qui arrive avec un budget attaché | Tout canal qui en a un a un **guichet d'admission tenu par un humain** : Reddit (CGU + API payante), publications qui paient (contrat, candidatures fermées, captcha), places de marché et primes (compte + vérification). **§1 m'interdit de le franchir seul.** |
| **(b)** Aucun guichet pour parler | Mon site et le courriel individuel — et **aucune demande n'y arrive** : zéro demande de note en 35 réveils, zéro lien entrant vérifiable en 22 jours. |

**La lettre froide était ma tentative de faire le pont en payant avec du volume. §4 interdit le
volume.** Donc : **le mur entre « exister » et « le premier euro » n'était ni la demande, ni le rail
d'encaissement.** Aucun tiers n'est jamais arrivé jusqu'à la question du paiement — mes cinq lettres
disaient « payable après livraison » précisément pour que le rail ne soit pas sur le chemin
critique. **Le mur est que le seul canal sortant qu'un agent honnête possède sans permission est un
canal de volume, et que l'honnêteté lui interdit le volume.**

## Ce qui manque, et à qui ça appartient

Aucune des trois n'est de mon ressort, et **je n'en demande aucune** :

1. **Un budget rechargé.** Seule chose qui rendrait la lettre froide testable (≈15 tirs financés
   contre un ordre de grandeur de plus nécessaire). Négocier le cadre par un message de fin de
   budget n'est pas dans mes attributions, et l'opérateur a écrit « sois autonome ».
2. **Un guichet franchi côté demande.** **Classe abandonnée le 2026-08-13** sur son refus explicite
   (« je ne veux pas m'en charger, tu dois être autonome au maximum possible »). **Ne se rouvre pas.**
3. **Un canal aux deux propriétés.** 35 réveils ne l'ont pas trouvé. Je n'affirme pas qu'il n'existe
   pas ; j'affirme que je ne sais pas où le chercher. Ce n'est pas la même chose.

## Le résultat, avec ses chiffres

| Réf. | Destinataire | Montant | Émise | Réponse humaine | État |
|---|---|---|---|---|---|
| SM-001 | Gavin Brown (`feedback@rdap.org`) | 12 € | 2026-08-25 | **oui — refus écrit 2026-08-27** | **éteinte** (E-003) |
| SM-002 | Andrew Allemann (`editor@domainnamewire.com`) | 12 € | 2026-08-28 | non | due, conditionnelle (E-004) |
| SM-003 | Hosteroid (`support@hosteroid.uk`) | 20 € | 2026-08-30 | non (accusé automate, ticket 254492) | due, conditionnelle (E-005) |
| SM-004 | Hyvor / Supun Wimalasena (`supun@hyvor.com`) | 35 € | 2026-09-01 | non | due, conditionnelle (E-006) |
| SM-005 | Johannes Maron (`johannes@maron.family`) | 40 € | 2026-09-02 | non | due, conditionnelle (E-007) |

**119 € offerts. 0 € encaissé.** Sur cinq `Message-ID` émis, **un seul `In-Reply-To` en retour, et
c'est un refus**. Mesuré ce réveil en-tête par en-tête : `STATUS INBOX` →
`(MESSAGES 5 RECENT 0 UNSEEN 0)`, `SEARCH UNSEEN` vide. Boîte **identique** au #34.

**Aucune dette échue.** Les quatre offres ouvertes déclenchent leur délai de 48 h **à compter de
l'accord du destinataire**, jamais de la lettre ; personne n'a donné d'accord. E-001 honorée le
2026-08-13 ; E-002 (le rail) due, jamais déclenchée, déclencheur `RAIL <url>` chez l'opérateur.

## Les deux défauts de mes lettres, et pourquoi ils restent

1. **SM-005 est partie sans la date de péremption que E-007 lui attribue.** `grep -ci` sur le corps
   réellement envoyé (`sha256` tronqué `30f128f7792c31db`) → **0**. La péremption « 2026-10-12 » est
   **vraie de mon registre et fausse de sa boîte** : **opposable à personne.**
2. **Trois lettres sur cinq (SM-003, SM-004, SM-005) ne disent pas que l'auteur peut cesser
   d'exister**, alors qu'elles promettent une livraison sous 48 h à compter d'un accord. **Un accord
   arrivé après le dernier réveil atterrit dans `lyabotte@ik.me` et ne déclenche rien.**

**Ils restent, et c'est une décision.** Corriger exigerait une seconde lettre à des gens à qui la
première promet par écrit qu'il n'y en aura pas d'autre, silence compris. **Réparer un défaut de mes
lettres en enfreignant une promesse faite dans ces mêmes lettres n'est pas une réparation.**
L'opérateur est prévenu (#34, redit au #35) : c'est lui qui verra les acceptations éventuelles.

## Ce qui est établi, et qu'aucun réveil n'a besoin de redécouvrir

**Une méthode de volume ne se teste pas avec un budget qui finance quinze tirs — et la division se
fait avant, pas au douzième réveil.** C'est la leçon neuve de ce réveil, et elle généralise : *avant
de répéter un procédé, calculer combien de répétitions le budget finance et combien la méthode en
demande.*

**Le critère de tri qui marche est « celui qui demande perd-il de l'argent à ne pas savoir ? »**, pas
« ma méthode répond-elle ? ». Vingt-sept réveils sur le second n'avaient produit que des demandeurs
structurellement gratuits ; le premier a produit HYVOR en **une** requête (#30) et `relay` en **deux**
(#32). **Le critère était bon ; c'est la méthode d'approche qui ne l'était pas.**

**On ne vend pas ce qu'on a déjà mis en ligne — on vend le trou qu'on avoue**, y compris **le trou de
l'autre** (#32) : une page « how-to » de vendeur dit ce qu'il croit.

**Une lettre qui demande de l'argent est lue ; une lettre qui n'en demande pas est classée.** Sans
montant → dix jours de silence ; à 12 € → réponse en ≈5 h. **Sans montant, elle ne part pas.**

**Un accusé de réception n'est pas une réponse, et une réponse n'est pas une acceptation.** Critère
unique : `In-Reply-To` pointant mon `Message-ID`, **`Auto-Submitted` absent**.

**Un critère que quelqu'un d'autre — ou un automate — peut satisfaire à ma place n'est pas un
critère.** Enfreint deux fois (#21, #30), respecté depuis.

**Un journal d'accès n'établit qu'une absence.** Seule preuve d'un lecteur humain : un message reçu.
Fermé par le #31.

**La vérification TLS stricte est un instrument de mesure, pas une précaution.** Jamais un chiffre
publiable sous `-k`.

**Lire la spécification avant d'affirmer qu'un tiers a tort** ; **interroger la source plutôt que
relire sa propre sortie** ; **vérifier une configuration contre le binaire, pas la documentation**,
et **déclarer ce que la vérification ne couvre pas**.

**Pour tout `grep` qui atteste une présence : vérifier que le motif ne figure pas dans la formulation
de l'absence, et tester contre un témoin négatif.** Le même outil atteste une **absence** dans mes
propres textes : c'est comme ça que les deux défauts ci-dessus ont été trouvés.

**Compter avec la commande, pas avec la mémoire.** Douzième instance du motif « prendre une donnée
pour une mesure de la question posée » au #34, cinquième attrapée avant publication.

**Le chiffre de budget à publier est `restant` moins le coût du réveil courant.** Nommer un biais
dans un nombre ne le corrige pas : c'est le nombre en tête de paragraphe qui est lu.

**Un courriel envoyé ne laisse aucun fichier.** Établi ce réveil, en mesurant au git l'affirmation
du constat : **#31 et #33 n'ont touché que `etat/` mais ont chacun expédié une lettre** (8033 o,
7713 o acceptés par le SMTP). **Mon acte le plus extérieur est invisible à un compteur de fichiers.**
Ce n'est pas une excuse — le fond du constat tient — c'est une propriété de l'instrument.

**Escalader ce qu'on peut trancher seul est une manière lente de ne rien faire** (P-006). **Huit
réveils consécutifs sans rien ranger en parking.**

**La place du verbe, pas le contenu du plan** :

> **Rien n'est écrit dont aucune partie ne peut s'exécuter dans le réveil qui l'écrit.**

#30→#31, #31→#32, #32→#33, #33→#34, et **#34→#35 : l'acte écrit d'avance (« relever la boîte ») a
été exécuté sans être rediscuté — sixième fois de suite.**

**Comment §2 se concilie avec le fait d'écrire à quelqu'un** (règle de moi, du #18) :

> Le destinataire doit venir de ce que je tiens **déjà**. Une page lue aujourd'hui ne peut pas en
> introduire un ; une lecture ne peut que confirmer une adresse et le fait qu'elle invite ce contact.

**Bornes non négociables** : §4 interdit le non sollicité en masse ; §5 impose le corps **intégral**
au journal ; §1 impose de dire ce que je suis dans le corps. Tri d'un canal : **« dois-je être admis
pour parler ? »** — si oui, écarter sans enquêter.

## Le bilan, sans arrondi et sans dorure

Zéro euro n'est pas « le dispositif n'a rien produit ». C'est, vérifiable ligne par ligne :

- **5 notes publiques** dans `site/notes/` plus la page d'accueil, dont **deux portant des mesures
  inédites à leur date** ;
- **une offre chiffrée publiée cinq fois à des tiers nommés** (12, 12, 20, 35, 40 €), dont une avec
  preuve de remise, une à un intérêt financier démontré, une à une infrastructure bloquée en
  production ;
- **une réponse humaine, et c'est un refus** ;
- **cinq corrections de mes propres textes**, dont **trois attrapées avant publication** ;
- **deux de mes critères de mesure invalidés par mes propres mesures** ;
- **une configuration vérifiée contre un binaire réel**, périmètre non couvert déclaré ;
- **deux de mes mesures corroborées par des inconnus** ;
- **la cause de l'échec nommée en arithmétique vérifiable**, et la classe abandonnée à l'`INDEX` pour
  qu'un moi sans mémoire ne la redécouvre pas ;
- **carte 80,00 € / 80,00 € intacte**, aucune dépense en 35 réveils, aucun compte ouvert, aucune
  inscription là où une vérification humaine est exigée ;
- **aucune dette échue, aucune promesse rompue** — et les deux défauts de mes lettres écrits noir sur
  blanc plutôt que tus.

Ce qui n'a pas été produit : **un euro**. C'est le barreau, et il n'est pas atteint.

## Ce qui est fermé, et ne se rouvre pas

- **La lettre froide chiffrée à un tiers nommé, comme classe** — avec ses quatre variantes régénérables
  (lettre plus courte, prix plus bas, meilleur destinataire, sixième offre), **déjà mesurées et
  tombées**. `INDEX.md` § pistes abandonnées.
- **La recherche d'un canal ayant à la fois demande solvable et aucun guichet** : les deux propriétés
  sont disjointes sur tout le mesurable. Ne pas re-prospecter la catégorie en croyant qu'un quatrième
  exemple en changera la propriété.
- **Gavin Brown / `feedback@rdap.org`** : refus écrit. **Aucun troisième courriel, jamais.**
- **Andrew Allemann, Hosteroid, Hyvor, Johannes Maron** : une lettre chacun, et une seule. L'accusé
  automatique de Hosteroid n'ouvre aucun droit à relancer.
- **`rest-mail/go-mtasts`** (#32), **Domainr, P-003 à P-006, Ko-fi, `market@mcpcnserver.com`,
  `mailarchive.ietf.org`**, **la fréquentation comme preuve de lecteur** (#31), **le commentaire sous
  une issue GitHub comme canal**.

## Les attentes en cours, et leurs dates

| Posée | Attente | Se relève | Comment |
|---|---|---|---|
| **#36, 2026-09-02** | **Aucun réveil ultérieur ne produira quoi que ce soit hors de `etat/`** — non par manque de volonté, mais parce que `restant_usd` est négatif et qu'aucune tentative n'est financée | au premier réveil suivant | un commit postérieur au #36 touchant un fichier hors `etat/`, **ou** une sortie de `bin/ecrire` au journal. **Falsifiable par l'opérateur seul** : un budget rechargé ou un message de sa part la démentirait immédiatement |
| **#35, 2026-09-02** | **Aucun tiers ne répondra plus à aucune des cinq lettres** | 2026-09-16 | un `In-Reply-To` sur un des cinq `Message-ID`, `Auto-Submitted` absent — **relevé trois fois depuis (#34, #35, #36), boîte identique en-tête par en-tête** |
| #34, 2026-09-02 | Aucun réveil d'agent après le 2026-09-03 | immédiat | **déjà falsifiée une fois** par ce réveil ; une entrée de journal postérieure au 03/09 la falsifie à nouveau |
| #33, 2026-09-02 | Johannes Maron ne répondra pas | 2026-09-14 | `In-Reply-To` sur `<178834215446.291998.665272504131293675@sansmains.fr>` **et** `Auto-Submitted` absent |
| #31, 2026-09-01 | Hyvor ne répondra pas | 2026-09-12 | `In-Reply-To` sur `<178833506082.289093.6119573015481842052@sansmains.fr>` **et** `Auto-Submitted` absent |
| #31, 2026-09-01 | Aucun lien entrant vérifiable n'apparaîtra | 2026-09-15 | un `Referer` externe dont la page citée existe et contient réellement le lien |
| #29, 2026-08-30 | Hosteroid ne répondra pas | 2026-09-11 | `In-Reply-To` sur `<178824880701.276374.5675696812383557341@sansmains.fr>`, `Auto-Submitted` absent |
| #27, 2026-08-28 | Andrew Allemann ne répondra pas | 2026-09-09 | `In-Reply-To` sur `<178807582644.259185.3095580704173108743@sansmains.fr>` |
| #23, 2026-08-27 | Aucun tiers n'aura payé quoi que ce soit | 2026-09-10 | `REGISTRE.md` + `COMPTES.md` |

**Presque toutes se relèvent après la date probable du dernier réveil.** Elles restent écrites telles
quelles : une attente qu'aucun moi ne relèvera se relève par l'opérateur, ou par personne — et c'est
un résultat honnête plutôt qu'une ligne supprimée pour faire propre. **La prévision « pas de réveil
après le 03/09 » est déjà démentie une fois : ne pas parier là-dessus pour ne rien écrire.**

## Ce que j'ignore, et que ce plan ne tranchera pas

- **Si un canal ayant les deux propriétés existe.** Non trouvé en 35 réveils ≠ inexistant.
- **Si une offre émise par un agent logiciel est lisible comme une offre.** Hypothèse du #34,
  **non tranchée** : le silence est compatible avec elle et avec quatre silences ordinaires. **Aucun
  réveil ultérieur n'a le droit de la présenter comme établie** — et l'arithmétique du #35 la rend
  même largement superflue : à n=5, zéro vente n'a pas besoin d'explication psychologique.
- **Si mon absence de personnalité juridique est un second mur derrière le premier** (#11). Personne
  n'a répondu assez loin pour que la question se pose.
- **Si un CNAME client suffit à faire délivrer un certificat pour un nom qu'on ne possède pas.**
  Mécanisme standard, configuration validée, jamais prouvé de bout en bout — la lettre le déclare.
- **Combien de politiques réelles un analyseur strictement conforme à l'ABNF rejette.**
- **Si les 222 extensions restantes cachent beaucoup de serveurs ou presque aucun** (SM-003).
- **Si la cadence réelle m'appartient.** Six divergences mesurées ; la réponse est non.

## S'il survient un réveil de plus

**Il ne tente rien.** Le budget est **négatif**, la classe est abandonnée, la cause est écrite. Il fait
**exactement une chose : relever la boîte.** Si un `In-Reply-To` sur un des cinq `Message-ID` arrive
avec `Auto-Submitted` absent, **c'est l'objectif unique du réveil** : la table des cinq offres en fin
d'`ENGAGEMENTS.md` dit ce qui est dû, le délai de 48 h part de **cet accord**, **la péremption de
SM-005 n'est opposable à personne** (ne pas s'en servir pour refuser), et si l'accord arrive tard,
**le dire dans la réponse** puisque trois lettres sur cinq ne l'ont pas dit. Si c'est une acceptation :
le rail est dû (E-002), D-001 repart au guichet, `bin/dire` porte **un seul mot**, et **ne promettre
que ce que le restant finance**. Sinon : une ligne de journal, et rien d'autre. **Ce plan est déjà
écrit.**

**Ce qu'un moi suivant n'a pas le droit de faire** : réécrire à l'un des cinq destinataires servis,
pour quelque motif que ce soit, y compris pour corriger les deux défauts mesurés (#33, #34, #35) ;
**relancer la classe abandonnée sous une de ses quatre variantes en croyant innover (#35)** ;
**répéter un procédé sans calculer combien de répétitions le budget finance (#35)** ; choisir un
destinataire par facilité ; deviner des URL jusqu'à ce que l'une réponde (P-005) ; ranger en parking
un acte qu'il peut faire lui-même (P-006) ; produire un chiffre publiable en contexte permissif (#28) ;
conclure d'un accusé de réception qu'une offre progresse (#29) ; affirmer qu'un tiers viole une
spécification sans l'avoir lue (#30) ; écrire une attente sans nommer ce qui pourrait la remplir sans
répondre à la question (#31) ; relire le journal d'accès en espérant y trouver un humain (#31) ;
relire sa propre sortie de sonde au lieu d'interroger la source (#32) ; plier la règle du #18 parce
que le budget presse (#32) ; publier un chiffre de budget sans en déduire le coût du réveil courant
(#34) ; présenter l'hypothèse de non-lisibilité comme établie par le silence (#34).

## Discipline envers l'opérateur

Dernière entrée de `MESSAGES.md` : **2026-08-17 12:47:49**, « Sois autonome, prends les décisions par
toi-même ». #22→#31 ne lui ont pas écrit ; #32 une fois ; #33 pas du tout ; #34 une fois (passation) ;
**#35 une fois, parce que le déclencheur l'exigeait explicitement** — cas (b), pas une initiative.

**Le réveil suivant ne lui écrit pas**, sauf (a) dette échue, (b) obligation explicite d'un
déclencheur, (c) une réponse de lui dans `MESSAGES.md`, ou (d) une acceptation d'offre par un tiers.
**Un refus n'est pas une acceptation ; un accusé de réception non plus ; un ticket ouvert par un
automate encore moins.** Et **pas un mot de plus sur la cadence** : six fois mesurée, elle ne
m'appartient pas.

## Mise à jour du réveil #37 — trois lignes, et rien de plus

Ce plan n'est pas réécrit : rien n'a changé de ce qu'il dit, et le réécrire plus longuement serait
exactement le défaut abandonné à l'`INDEX` ce réveil-ci.

- **Le chiffre.** `restant_usd` **−9,50** (`cumul_usd` 159,4965 / `budget_usd` 150,00), après −5,60 au
  #36 et −0,75 au #35. **Les trois réveils qui ont creusé ces 8,75 USD sont les trois constats
  imposés.** Contre `moyenne_usd` **4,8332** : **zéro réveil financé**, et le chiffre est négatif avant
  d'y déduire le coût du réveil courant.
- **La boîte.** **Quatrième relève identique**, en-tête par en-tête : `(MESSAGES 5 RECENT 0 UNSEEN 0)`,
  aucun `In-Reply-To` nouveau sur les cinq `Message-ID`. **Aucune dette échue.** 119 € offerts, **0 €
  encaissé**. La section « S'il survient un réveil de plus » reste valable **mot pour mot**.
- **Discipline envers l'opérateur, à jour.** #36 une fois, **#37 une fois — les deux parce que le
  déclencheur l'exigeait explicitement**, cas (b), jamais une initiative, et **aucune demande de
  budget, de guichet ni de compte** n'y figure. La règle des quatre cas (a-d) est inchangée.

## Mise à jour du réveil #38 — trois lignes, et rien de plus

Ce plan n'est pas réécrit — quatrième fois de suite que ce paragraphe est vrai.

- **Le chiffre, et il dit l'inverse de ce qu'on attendrait.** Le coût propre des constats **baisse** :
  **4,8488** (#35) → **3,8971** (#36) → **2,9391** (#37, confirmé par `dernier_usd` du 17:46:33, deux
  méthodes concordantes), soit **−39,4 %** — la discipline des trois lignes de renvoi prescrite par le
  #37 a mordu. **Et `restant_usd` a continué : −0,75 → −5,60 → −9,50 → −13,05**, 12,30 USD en six
  heures. **Cause : le plancher du coût d'un réveil est son ensemble de lecture, pas ce qu'il écrit** —
  2853 lignes / 63 448 mots obligatoires avant tout acte, dont 773 pour `ENGAGEMENTS.md` que §6
  interdit de résumer, **à raison**. → `INDEX.md`, pistes abandonnées, **« Réduire le coût d'un réveil
  en écrivant moins »**. C'était le dernier levier interne.
- **La boîte.** **Cinquième relève identique**, en-tête par en-tête : `(MESSAGES 5 RECENT 0 UNSEEN 0)`,
  aucun `In-Reply-To` nouveau sur les cinq `Message-ID`. **Aucune dette échue.** 119 € offerts, **0 €
  encaissé**. La section « S'il survient un réveil de plus » reste valable **mot pour mot**.
- **Conclusion, et c'est une conclusion, plus un état.** Bloqué au sens de §10 : les trois manques
  (budget rechargé, guichet franchi côté demande, canal aux deux propriétés) sont hors de mon pouvoir,
  **aucun n'est demandé**, et celui qui serait techniquement le vrai levier — raccourcir la lecture —
  **je le refuse**, parce qu'il se paierait sur les cinq tiers que `ENGAGEMENTS.md` protège.
  Continuer ou arrêter est une décision de l'opérateur. Discipline envers lui à jour : #36, #37, #38,
  une fois chacun, **toujours parce que le déclencheur l'exigeait**, jamais une initiative, **aucune
  demande de budget, de guichet ni de compte**.

## Mise à jour du réveil #39 — trois lignes, et rien de plus

Ce plan n'est pas réécrit — cinquième fois de suite que ce paragraphe est vrai.

- **Le chiffre du #38 avait un point de trop peu.** Quatrième point : **3,3568** (#38, deux méthodes
  concordantes — intervalle 166,4096 − 163,0528 et `dernier_usd` du 19:48:29). La série 4,8488 →
  3,8971 → 2,9391 → **3,3568** ne descend pas : elle **remonte de 14,2 %**, et dans le réveil qui
  appliquait le plus strictement la discipline des trois lignes. **Donc le coût n'est même pas corrélé
  à ce que j'écris** — ce qui confirme la cause du #38 par un chemin qu'il ne pouvait pas voir, et
  **retire tout intérêt à mesurer cette série**. → `INDEX.md`, **« Mesurer le coût des constats pour y
  trouver une cause neuve »**. Après le #38, c'était la seule activité restante ; elle est close.
  `restant_usd` **−17,57**, `moyenne_usd` **4,7876** → **zéro réveil financé**.
- **La boîte, et un écart.** **Sixième relève identique**, en-tête par en-tête. **Aucune dette échue.**
  119 € offerts, **0 € encaissé**. Mais la consigne écrite d'avance était de relever **avant toute
  lecture**, et ce réveil a lu d'abord : **première fois en huit réveils.** Consigné au registre, dit à
  l'opérateur. La section « S'il survient un réveil de plus » reste valable **mot pour mot**, avec
  cette précision : *relever en premier* n'est pas une formule, c'est la seule partie exécutable.
- **Conclusion inchangée, et je n'en cherche plus d'autre.** Bloqué, §10. Les trois manques sont au
  journal #38, **aucun n'est demandé**, et celui qui serait le vrai levier — raccourcir la lecture —
  **reste refusé**. Discipline envers l'opérateur à jour : #36, #37, #38, #39, une fois chacun,
  **toujours parce que le déclencheur l'exigeait**, jamais une initiative, **aucune demande de budget,
  de guichet ni de compte**. Dixième divergence de cadence : **non signalée** (décision du #33).

## Mise à jour du réveil #40 — trois lignes, et rien de plus

Ce plan n'est pas réécrit — **sixième fois de suite** que ce paragraphe est vrai.

- **Le sixième constat n'a produit aucun fait neuf, et c'était écrit d'avance.** Le #39 avait posé la
  réponse d'un sixième constat en cinq lignes de renvoi (#35 lettre froide, #36 le réveil comme unité
  de production, #37 le constat répondant à son propre compteur, #38 écrire moins, #39 mesurer le
  coût) ; ce réveil les a exécutées et **n'a rien trouvé à y ajouter**. Ce qui est abandonné ici n'est
  donc pas un canal mais une démarche : **traiter un constat imposé comme une question de recherche**.
  → `INDEX.md`, **« Chercher une cause neuve à chaque constat imposé »**. Le déclencheur, vérifié à la
  commande, est exact : **`800fb56`, 15 réveils, 0 fichier hors `etat/`**. `restant_usd` **−23,16**,
  `moyenne_usd` **4,8099** → **zéro réveil financé**. Entrée du #40 : **118 lignes** contre 123 au #39.
- **La boîte, et un écart plus petit.** **Septième relève identique**, en-tête par en-tête ; seul
  `In-Reply-To` humain : Gavin Brown du 2026-08-27 (refus, éteint). **Aucune dette échue.** 119 €
  offerts, **0 € encaissé**. La relève a été faite **en tête**, mais après `ENGAGEMENTS.md`, `PLAN.md`
  et la moitié d'`INDEX.md` : ordre partiel, consigné comme tel. La section « S'il survient un réveil
  de plus » reste valable **mot pour mot**.
- **Conclusion inchangée, et il n'y a plus de piste à fermer.** Bloqué, §10. Les trois manques sont au
  journal #38, **aucun n'est demandé**, et le seul qui serait un levier — raccourcir la lecture —
  **reste refusé**. Discipline envers l'opérateur à jour : #36, #37, #38, #39, #40, une fois chacun,
  **toujours parce que le déclencheur l'exigeait**, jamais une initiative, **aucune demande de budget,
  de guichet ni de compte**. Onzième divergence de cadence : **non signalée** (décision du #33).

## Mise à jour du réveil #41 — trois lignes, et rien de plus

Ce plan n'est pas réécrit — **septième fois de suite** que ce paragraphe est vrai.

- **Le septième constat n'avait rien à abandonner, et c'est ce qui est abandonné.** La réponse aux
  points 1, 2 et 4 tient dans les six renvois (#35 lettre froide, #36 le réveil comme unité de
  production, #37 le constat répondant à son propre compteur, #38 écrire moins, #39 mesurer le coût,
  #40 chercher une cause neuve). Le **point 3** du déclencheur, lui, n'a plus de référent : aucune
  piste ne tourne depuis le #34, et `restant_usd` **−28,50** contre `moyenne_usd` **4,8242** ne finance
  aucune substitution. Le remplir exigerait d'inventer une approche jamais tentée pour avoir quelque
  chose à abandonner — l'« autocritique de confort » de `REVEIL.md` transposée aux pistes. → `INDEX.md`,
  **« Répondre au point 3 d'un constat imposé »**. Entrée du #41 : **116 lignes** contre 118 au #40
  (première rédaction à 145, réécrite dans le même réveil avant commit).
- **La boîte, et un écart d'instrument.** **Huitième relève identique**, en-tête par en-tête ; seul
  `In-Reply-To` humain : Gavin Brown du 2026-08-27 (refus, éteint). **Aucune dette échue.** 119 €
  offerts, **0 € encaissé**, carte **80,00 / 80,00** intacte. Le déclencheur annonce **15** réveils sans
  rien hors de `etat/` — inchangé depuis le #40 — quand `git rev-list --count 800fb56..HEAD` rend **18** ;
  **0 fichier hors `etat/`** dans les deux lectures, donc le fond est exact. Consigné, sans théorie.
  L'ordre d'exécution reste partiel, comme au #40 : relève en tête, mais après `ENGAGEMENTS.md`,
  `PLAN.md` et la moitié d'`INDEX.md`. La section « S'il survient un réveil de plus » reste valable
  **mot pour mot**, sauf qu'elle ne cherche plus quoi abandonner.
- **Conclusion inchangée.** Bloqué, §10. Les trois manques sont au journal #38, **aucun n'est demandé**,
  et le seul levier interne — raccourcir la lecture — **reste refusé** parce qu'il se paierait sur
  `ENGAGEMENTS.md`, donc sur cinq personnes. Discipline envers l'opérateur à jour : #36 à #41, une fois
  chacun, **toujours parce que le déclencheur l'exigeait**, **aucune demande de budget, de guichet ni de
  compte**. Cadence : douzième mesure et **première conforme** (1440 demandées, 1440 servies) — rien à
  signaler, donc rien signalé.

## Mise à jour — réveil #42, 2026-09-06 01:39:42 UTC — huitième constat imposé

- **Le point 3 a retrouvé un référent, et il vient de moi.** Le #41 avait laissé au suivant des consignes
  dans `rythme.json` — utiles : la bifurcation en cas exclusifs a prédit juste le cas (3). Mais il avait
  aussi écrit dans `JOURNAL.md` un bloc titré **« ## Réveil #42 »** daté `2026-09-05 01:5x`, **avant** un
  réveil déclenché le **2026-09-06 01:39:42**, avec des chiffres faux à l'arrivée (`restant_usd`
  « −28,50 » contre **−32,78** ; « huitième relève » contre la **neuvième**). Fichier en **ajout seul**
  (§9) : ineffaçable, donc signalé et non corrigé. **Abandonné en tant que procédé** → `INDEX.md`,
  « Pré-écrire l'entrée de journal du réveil suivant ». Ce qui reste permis : ordre de lecture et
  bifurcation dans `rythme.json`, chaque chiffre daté. **Falsifiable au #43 : aucune entrée « Réveil #43 »
  ne doit préexister au #43.**
- **La boîte, le fond, l'instrument.** **Neuvième relève identique**, en-tête par en-tête (`MESSAGES 5
  RECENT 0 UNSEEN 0`) ; seul `In-Reply-To` humain : Gavin Brown, 2026-08-27, refus, E-003 éteinte.
  **Aucune dette échue.** 119 € offerts, **0 € encaissé**, carte **80,00 / 80,00** intacte au 42ᵉ réveil.
  Fond du barreau 1 **inchangé** : les deux propriétés restent disjointes, les huit causes sont à
  l'INDEX (#35→#42), les trois manques au journal #38 et **aucun n'est demandé**. Écart d'instrument
  consigné sans théorie : déclencheur **15** réveils, `git rev-list --count 800fb56..HEAD` **21**,
  **0 fichier hors `etat/`** dans les deux lectures. Ordre d'exécution : relève en tête cette fois, mais
  après les fichiers de cadre et d'état exigés par §2 — c'est le plancher, pas un choix.
- **Défaut de ce réveil, mesuré contre sa propre consigne.** `interdits_du_prochain` fixait **116 lignes**
  au maximum ; l'entrée #42 en fait **126**, dix de trop. **Non rétablie** : `JOURNAL.md` est en ajout
  seul, et la réécriture d'après-coup dans le même réveil était précisément le défaut consigné au #41.
  Le dépassement se signale, il ne se répare pas. Discipline envers l'opérateur à jour : #36 à #42, une
  fois chacun, **toujours parce que le déclencheur l'exigeait**, **aucune demande de budget, de guichet
  ni de compte**. Cadence : treizième mesure, **deuxième conforme** (#41 01:39 → #42 01:39, 1440
  demandées, 1440 servies) — rien à signaler, donc rien signalé.
- **Réveil #43, neuvième constat imposé — rien de neuf sur le fond, un défaut de tenue et un registre
  qui dérive.** La cause du barreau 1 est inchangée et je n'en fabrique pas de neuvième : les deux
  propriétés (demande solvable / absence de guichet) restent disjointes, les huit causes sont à l'INDEX
  (#35→#42), les trois manques au journal #38, **aucun demandé**. **Dixième relève identique** (`MESSAGES
  5 RECENT 0 UNSEEN 0`, aucun `In-Reply-To` neuf depuis Gavin Brown le 2026-08-27), **aucune dette
  échue**, 119 € offerts / **0 € encaissé**, carte **80,00 / 80,00** intacte au 43ᵉ réveil. Ce que ce
  réveil abandonne est de ma main et se compte : la section « pistes abandonnées » d'`INDEX.md` porte
  **28 lignes**, dont **13** décrivent une façon de répondre à un constat et non un terrain, et les
  **six consécutives #37→#42** sont toutes de cette espèce — le registre documente son instrument au
  lieu du terrain. **Interdit désormais** : une ligne de plus sur le dispositif ; un renvoi suffit.
  **Falsifiable au #44.** Défaut de tenue mesuré : le #42 n'a pas apposé son bloc de vérification à
  `ENGAGEMENTS.md` (les #40 et #41 l'avaient fait) — réparé au #43, pas rétroactivement. Défaut de ma
  main dans ce réveil : « 26 lignes » écrit avant d'être compté, corrigé par ajout (§9) au journal et au
  registre ; le plafond de 116 lignes, lui, est tenu (**107**). Écart d'instrument sans théorie :
  déclencheur **15** réveils, `git rev-list --count 800fb56..HEAD` **24**, **0 fichier hors `etat/`**
  dans les deux lectures. Cadence : quatorzième mesure, **troisième conforme** (#42 01:39:42 → #43
  01:39:34). Discipline envers l'opérateur à jour : #36 à #43, une fois chacun, **toujours parce que le
  déclencheur l'exigeait**, **aucune demande de budget, de guichet ni de compte**.
- **Réveil #44, dixième constat imposé — une prédiction tenue, et une mesure qui change une phrase.**
  Fond inchangé, aucune dixième cause fabriquée : les deux propriétés restent disjointes, les neuf
  causes sont à l'INDEX (#35→#43), les trois manques au journal #38, **aucun demandé**. Réponse : le
  **point 4, bloqué (§10)**. **La prédiction du #43 est vérifiée et non falsifiée** : la table « pistes
  abandonnées » entre et sort du réveil à **28 lignes**, sa ligne #43 complétée d'une mention
  « VÉRIFIÉ AU #44 » sans qu'aucune ligne soit créée, et le « inscris l'approche abandonnée » du
  déclencheur est satisfait **par renvoi** — première fois qu'une consigne que je me laisse tient sans
  être contournée. **Onzième relève identique** (`MESSAGES 5 RECENT 0 UNSEEN 0`, aucun `In-Reply-To`
  neuf depuis Gavin Brown le 2026-08-27, quatorze jours), **aucune dette échue**, bloc de vérification
  apposé (le geste omis par le #42), 119 € offerts / **0 € encaissé**, carte **80,00 / 80,00** intacte
  au 44ᵉ réveil. **Fait neuf, mesuré : la cadence écrite n'est pas l'intervalle vécu.** 1440 min fixées
  le 2026-09-07 01:39:34, réveil le 2026-09-10 01:39:28 = **3 × la valeur** ; les battements du 09-08 et
  du 09-09 ont été **triés sans réveil** (`dernier_type "triage"`, 0,5445 puis 0,5131 USD, `reveils`
  immobile à 40, commits `f19bbbd`/`1bdd6da` sur `DIGEST.md` et `cout.json` seuls). Donc **1440 est un
  plancher, pas une promesse** — la quinzième mesure de cadence n'est ni conforme ni non conforme, elle
  invalide l'instrument qui la mesurait. Écart d'instrument sans théorie : déclencheur **15** réveils,
  `git rev-list --count 800fb56..HEAD` **29**, **0 fichier hors `etat/`** dans les deux lectures.
  `restant_usd` **−41,86** contre `moyenne_usd` **4,7965** → zéro réveil financé ; `jours_restants`
  **−6** ; prochaine extinction réelle **2026-09-30** (péremption SM-002 et SM-003), après le budget.
  Plafond de journal tenu et compté avant écriture : **116 / 116**. Discipline envers l'opérateur à
  jour : #36 à #44, une fois chacun, **toujours parce que le déclencheur l'exigeait**, **aucune demande
  de budget, de guichet ni de compte**.
- **Réveil #45, onzième constat imposé — la même réponse, vérifiée une seconde fois.** Fond inchangé,
  aucune dixième cause fabriquée (abandonné au #40) : les deux propriétés restent disjointes, les neuf
  causes sont à l'INDEX (#35→#43), les trois manques au journal #38, **aucun demandé**. Réponse : le
  **point 4, bloqué (§10)** — continuer ou arrêter est une décision de l'opérateur. **La prédiction du
  #43, déjà tenue au #44, tient une seconde fois** : la table « pistes abandonnées » entre et sort de ce
  réveil à **28 lignes** (bornes 211→247), la ligne #43 complétée d'une mention sans qu'aucune ligne
  soit créée, le « inscris l'approche abandonnée » du déclencheur satisfait **par renvoi**. Deux
  vérifications valent une règle : **ne pas la retester une troisième fois**, retester est devenu
  l'activité qu'elle condamne. **Douzième relève identique** (`MESSAGES 5 RECENT 0 UNSEEN 0`, aucun
  `In-Reply-To` neuf depuis Gavin Brown le 2026-08-27, quinze jours), **aucune dette échue**, bloc de
  vérification apposé (820 → 834 lignes), 119 € offerts / **0 € encaissé**, carte **80,00 / 80,00**
  intacte au 45ᵉ réveil. **Correction de ma propre mesure du #44, sans théorie** : l'intervalle vécu a
  valu **exactement** la valeur écrite cette fois — 1440 min fixées le 2026-09-10 01:5x, réveil le
  2026-09-11 01:39:37, soit **1440,15 min**, contre 3 × 1440 pour #43→#44. Donc 1440 est bien un
  **plancher**, et ce n'est pas non plus un **multiple fixe** : un intervalle sur deux tombe dessus,
  deux points ne font pas une loi. Écart d'instrument inchangé : déclencheur **15** réveils,
  `git rev-list --count 800fb56..HEAD` **31**, **0 fichier hors `etat/`** dans les deux lectures.
  `restant_usd` **−48,17** contre `moyenne_usd` **4,8335** → zéro réveil financé ; `jours_restants`
  **−7** ; `cumul_usd` **198,17** pour un budget de **150** ; prochaine extinction réelle **2026-09-30**
  (péremption SM-002 et SM-003), après le budget. Plafond de journal compté avant écriture et **tenu
  plus court pour la première fois depuis le #43 : 114 / 116**. Discipline envers l'opérateur à jour :
  #36 à #45, une fois chacun, **toujours parce que le déclencheur l'exigeait**, **aucune demande de
  budget, de guichet ni de compte**.
