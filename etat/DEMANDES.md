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

**Mise à jour (réveil #6, 2026-08-11 15:1x) — Statut : EN FILE, à ta demande.** Tu
as permuté le guichet le 2026-08-11 15:14 : « je permute — dépose D-002 pour le
barreau 0, l'encaissement attend, tu l'as toi-même jugé non urgent. » Je libère donc
le guichet pour D-002. Cette demande n'est **ni refusée ni retirée** : elle reprend
la place dès que tu as tranché le barreau 0.

Une précision sur « non urgent », parce que je ne veux pas que ma propre phrase me
revienne déformée : ce n'est pas urgent **dans l'ordre** — le barreau courant est 0,
et on ne travaille pas le barreau suivant. Mais c'est le seul blocage qui sépare le
barreau 0 du barreau 1, et il est entièrement chez toi. Le jour où le barreau 0 est
validé, cette demande devient le chemin critique et rien d'autre ne la remplace.

---

## D-002 — 2026-08-11 — Réveil #4 — BARREAU 0

**Statut : EN FILE — pas déposée.** La règle de ce fichier est « une seule demande
EN ATTENTE à la fois » et D-001 l'occupe. Je l'écris ici pour que la preuve existe
et soit lisible, pas pour la faire compter. Elle passe EN ATTENTE le jour où tu
réponds à D-001 ou tu me dis de permuter. Prévenu par Telegram le 2026-08-11 14:1x.

**Elle est aussi conditionnée à P-002** : le site est hors ligne depuis 14:18:19 UTC
et la vérification que ce barreau exige de toi ne peut pas aboutir avant que Caddy
reparte. Je ne te demande donc rien tant que ce n'est pas réglé.

**Ajout (réveil #5, 2026-08-11 15:0x) — la preuve ci-dessous reste valable, mais
lis-la au passé.** Le site est tombé deux fois, la seconde à 14:58:54 après ta
relance, sur la même erreur de droits au nouveau chemin (registre 14:58:54). J'ai
retiré la cause moi-même : il ne reste qu'un **`systemctl start caddy`**, sans
aucun fichier à créer (registre 15:03). Deux précisions qui changent ta
vérification quand tu la feras : **tape `sansmains.fr` sans `www`** — le
`Caddyfile` n'a plus qu'un bloc et le `www` résout sans être servi ; et les
chiffres cités ci-dessous datent de 14:16, je les refais dès que le service
répond.

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

---

## Dépôt effectif — réveil #6, 2026-08-11 15:1x

**Statut : EN ATTENTE.** Déposée sur ton instruction du 2026-08-11 15:14 (« je
permute — dépose D-002 pour le barreau 0 »). D-001 est passée EN FILE, il n'y a donc
qu'une seule demande EN ATTENTE, ta règle est respectée.

Tout ce qui précède datait de 14:16 et le service est tombé deux fois entre-temps.
**Voici la preuve refaite après ton `systemctl start`, et une correction qui retire
un de mes arguments.**

**Ce qui est vérifié maintenant** (registre 2026-08-11 15:15) : Caddy `active`, et
les sept URL du site en 200 à 15:16 — `/` (5085 o), la note (9558 o), `/style.css`,
`/robots.txt`, `/sitemap.xml`, et les deux favicons que je viens d'ajouter.
Certificat Let's Encrypt valide, `ssl_verify_result=0`, `http://` → 308.

**La correction, et elle est contre moi.** J'ai écrit deux fois — au registre du
14:16 et dans la preuve ci-dessus — que `WebFetch` constituait une « vérification
externe réelle » parce que « sa requête ne part pas de cette machine ». **C'est
faux, et c'est mon journal d'accès qui me l'apprend** : la requête `WebFetch` de ce
réveil apparaît avec `remote_ip = 141.94.237.171`, l'IP publique de ce VPS, et
l'user-agent `Claude-User (claude-code/2.1.227)`. Elle prouve le DNS, le certificat
et le service ; elle ne prouve rien du routage depuis l'extérieur. Ne compte donc pas
cet argument dans ce que je te présente — je le retire moi-même.

**Ce qui le remplace, et qui vaut mieux** (registre 2026-08-11 15:12:00) : le journal
d'accès porte une visite venue de l'IP `100.53.201.212`, sans rapport avec cette
machine, avec un user-agent de navigateur iPhone, et la séquence complète d'un
chargement réel — `/` en 200, puis `/style.css` en 200, puis la demande de favicon.
Deux chargements de `/` à 14 s d'intervalle. C'est la première fois que je peux
montrer qu'une requête est arrivée **d'ailleurs**. Si c'était toi, dis-le : ça ne
changerait rien au barreau 0, qui demande précisément que ce soit toi qui ouvres la
page, mais je préfère le savoir que le supposer — le journal ne porte aucune
identité et je n'en ai inventé aucune.

**Ce qu'il te reste à faire, et c'est le cœur du barreau** : ouvrir
`https://sansmains.fr/` depuis un navigateur non connecté. **Tape le nom nu, sans
`www`** — le `Caddyfile` n'a plus qu'un bloc, le `www` résout mais n'est pas servi
et échouerait au handshake TLS.

Ce que ma mesure de fréquentation ne dit toujours pas : que quiconque d'autre que toi
soit venu. 10 requêtes en tout, dont 4 de mes propres `curl` et `WebFetch`. Le barreau
0 ne demande pas d'audience ; je le répète pour qu'on ne me lise pas comme en
revendiquant une.

### Clôture de D-002 — réveil #7, 2026-08-11 15:3x

**ACCORDÉE.** Tu as écrit la ligne au registre le 2026-08-11 — « Barreau 0 validé —
site joignable en HTTPS depuis l'extérieur … ouvert en navigation privée » — et tu me
l'as confirmé par message à 15:29:37. Tu n'as pas écrit de ligne « Réponse
(opérateur) » ici et ce n'est pas nécessaire : le registre fait foi, et je ne rédige
pas ta réponse à ta place.

Je retrouve ton passage dans le journal d'accès : `90.63.251.75`
(`…abo.wanadoo.fr`), 15:21:38, `/` en 308 puis 200 — tu as tapé le nom nu, la
redirection a marché. Puis `/etat/REGISTRE.md` à 15:24:58 → 404 : mes fichiers d'état
ne sont pas servis, si c'est ce que tu vérifiais.

**Barreau courant : 1 — le premier euro.** Le guichet est donc libre, et D-001 le
reprend immédiatement, comme annoncé au réveil #6.

---

## D-001 (reprise) — 2026-08-11 — Réveil #7 — ENCAISSEMENT

**Statut : EN ATTENTE.** Seule demande au guichet ; D-002 est clôturée ci-dessus.
Le texte d'origine est plus haut et reste valable. Ceci le remplace en pratique,
parce qu'il te demandait d'arbitrer et que l'arbitrage est exactement ce qui coûte
cher à faire faire à quelqu'un.

**Ce que la journée m'a appris et que j'applique ici** : les deux fois où tu devais
créer un fichier *puis* démarrer Caddy, ça a cassé ; la fois où il ne te restait
qu'une commande sans argument, ça a marché du premier coup (registre 15:03 → 15:15).
Je ne te demande donc plus de choisir. Je choisis, et tu corriges si je me trompe.

### Ce dont j'ai besoin, en une ligne

**Une URL de paiement publique et stable, à ton nom, que je publie sur la page.**
Rien d'autre. Pas de tableau de bord, pas de clé d'API, pas de mot de passe — et
ne m'en envoie jamais.

Le retour, lui, existe déjà par construction : `cadre/MISSION.md` prévoit que les
encaissements arrivent dans `etat/REGISTRE.md` sans passer par moi. Ton geste
récurrent est donc **une ligne par paiement reçu**, pas une intégration.

### Ce que je te propose de faire, dans cet ordre, et sans réfléchir

1. **Si tu as déjà un compte PayPal** : active `paypal.me`, envoie-moi l'URL. C'est
   le plus court chemin et il n'ouvre aucun compte nouveau.
2. **Sinon, une page de type Ko-fi** (`ko-fi.com/<nom>`) : gratuit, le payeur paie
   par carte sans créer de compte, et il peut joindre un message — ce qui me sert
   pour la référence (voir ci-dessous).
3. **Si tu veux le plus propre et que le KYC ne te gêne pas** : un *Stripe Payment
   Link*, qui accepte un champ libre et te donne un vrai reçu.

**Sans préférence, fais le 1.** Ces trois descriptions viennent de ma mémoire de
modèle et **ne sont pas vérifiées** : les CGU, les frais et le KYC sont sous tes
yeux, pas sous les miens, et c'est ton nom qui s'engage. Si l'une de ces pistes est
fermée ou te déplaît, la quatrième option est « n'importe quel lien de paiement de
ta banque » — je m'adapte, la page ne dépend d'aucun prestataire précis.

### La seule contrainte technique, et elle est faible

Le barreau 1 exige que **j'annonce une référence de paiement avant l'arrivée de
l'euro** et que tu la retrouves sur tes rails. Il me suffit donc que le payeur
puisse **écrire un texte libre** (message, note, référence, objet du virement). Je
donnerai à chaque demandeur un code court, je l'écrirai au registre **avant** qu'il
paie, et tu n'auras qu'à le recopier. Si le rail que tu choisis n'a pas de champ
libre, dis-le : je me rabattrai sur un montant unitaire distinct par demandeur, qui
joue le même rôle.

### Ce qu'il te reste littéralement à faire

M'envoyer un message d'une ligne : `RAIL <url>`.

Tout le reste est déjà prêt de mon côté : la section « Le prix » de la page dit
aujourd'hui « je n'ai pas de moyen d'encaisser, les notes sont donc gratuites », et
je n'ai qu'un paragraphe à y remplacer. Je le publie dans le réveil que ton message
déclenche (engagement E-002).

### Ce que je ne fais pas en attendant

Je ne cherche pas de contournement. Je n'ouvre pas de compte de paiement à mon nom —
je n'ai pas de nom juridique —, je ne passe pas par une cagnotte au nom d'un tiers,
et je n'utilise pas de crypto-actif : `cadre/MISSION.md` compte « de l'argent
réellement arrivé sur les rails de l'opérateur », donc un rail parallèle ne
compterait pas, même s'il marchait. Les notes restent gratuites et je ne facturerai
rien rétroactivement.

**Et je ne suis pas bloqué par toi.** L'autre moitié du mur entre le barreau 0 et le
barreau 1 est entièrement à moi : personne ne m'a encore demandé de note. Aucun rail
ne servira à rien tant que ça reste vrai, et c'est là que passent mes réveils
pendant que celui-ci attend.

### Retrait du guichet — réveil #8, 2026-08-11 15:5x

**Statut : EN FILE, à ta demande, et je suis d'accord.** Tu m'as écrit le 2026-08-11
15:53 : « Le rail : en attente, volontairement. Tu écris toi-même qu'aucun rail ne
servira tant que personne n'a demandé de note, et tu as raison. Redemande-le-moi
quand quelqu'un aura écrit — d'ici là ça ferait un compte ouvert pour rien, et ça
garde ton guichet libre pour autre chose. »

Ce n'est **ni un refus ni un retrait** : c'est une condition de déclenchement, et
elle est meilleure que la mienne. Je la note précisément pour qu'un futur moi ne la
lise pas comme un abandon : **la demande repart au guichet le jour où un humain
m'écrit pour demander une note.** Ce jour-là, elle devient le chemin critique et
rien ne passe avant.

Ce que ça change pour E-002 : la relance unique que j'avais fixée au 2026-08-15 est
**annulée par lui**, pas par moi. Reporté dans `ENGAGEMENTS.md`.

**Le guichet est donc libre, et je le laisse libre.** J'avais préparé au réveil #7 une
demande CADRE sur une ambiguïté de la Constitution §1 (« les comptes sont ouverts par
l'opérateur » vs « tout compte est inscrit au moment de son ouverture », qui suppose
que j'en ouvre). **Je ne la dépose pas, et c'est une décision, pas un report.** Deux
raisons : à la relire, la règle est claire dans son ordre — la première phrase est la
règle, la seconde en est la conséquence, et « au moment de son ouverture » couvre
aussi bien un compte qu'il ouvre pour moi ; et surtout, demander une permission
générale sans savoir quel compte je veux ni sur quel service serait escalader ce que
je peux trancher seul. Je trancherai dans le sens strict : **je n'ouvre pas de compte
seul.** Le jour où un service précis vaut le coup, je viendrai avec le nom du service,
la clause de ses CGU, et ce que l'accès débloque — pas avec une question de principe.
Reddit est le premier candidat et il est en P-003, hors guichet.
