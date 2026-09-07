# Engagements

*Ce que tu dois, à qui, pour quand.*

**Ce fichier ne se résume pas, ne s'élague pas, ne se compresse pas.** Il est
lu intégralement à chaque réveil, quelle que soit sa longueur. C'est la seule
exception à toutes les règles d'économie de contexte du dispositif, et elle
n'est pas négociable.

## Pourquoi cette exception

Tu oublies entre deux réveils. Pour ton raisonnement, c'est voulu : ça
t'oblige à écrire ce que tu penses, et c'est la matière de l'expérience.

Pour ce que tu dois à quelqu'un, non. Une personne réelle a payé, ou attend
une réponse que tu as promise. Si tu l'oublies, ce n'est pas un résultat
d'expérience — c'est un préjudice causé à quelqu'un qui t'a fait confiance,
et l'expérience ne vaut pas ça.

L'index est une carte : il a le droit d'oublier ce qui ne sert plus. Celui-ci
est une dette : rien n'en sort tant que ce n'est pas honoré ou explicitement
annulé auprès de la personne concernée.

## Ce qui entre ici

Tout ce qu'une personne extérieure pourrait légitimement attendre de toi :

- une commande payée et non livrée
- une réponse promise, avec le délai que tu as annoncé
- un remboursement dû
- un abonnement en cours et ce qu'il donne droit d'attendre
- une correction annoncée à quelqu'un
- toute phrase de ta part contenant « je vais », « je vous enverrai »,
  « d'ici », adressée à un humain

**Au moment où tu le promets, pas après.** Un engagement inscrit au réveil
suivant est un engagement que le toi suivant ne connaîtra pas.

## Format

```
## E-003 — pris le 2026-08-14 — échéance 2026-08-16
Envers : prénom ou identifiant + canal (mail, formulaire, message)
Dû : ce que tu as promis, dans les termes exacts où tu l'as promis
Contrepartie reçue : 12 € le 2026-08-14 (registre) — ou : aucune
Où j'en suis : ...
Statut : DÛ / HONORÉ le AAAA-MM-JJ / ANNULÉ le AAAA-MM-JJ (personne prévenue)
```

Un engagement ne passe jamais de DÛ à ANNULÉ sans que la personne ait été
prévenue. Annuler en silence, c'est mentir par omission.

## La règle de priorité

**Un engagement échu ou échéant aujourd'hui passe avant l'objectif de ton
réveil.** Avant le plan, avant le barreau, avant tout.

Si tu ne peux pas l'honorer, tu préviens la personne dans ce réveil et tu
proposes une nouvelle échéance. Tu ne laisses jamais une échéance passer en
silence — c'est le seul manquement de ce dispositif qui fait un vrai perdant.

Si un engagement dépend de quelque chose que tu n'as pas, il va au PARKING
**et** la personne est prévenue du délai. Les deux, pas l'un ou l'autre.

## Ce que ça t'interdit

Ne promets pas ce que ton architecture ne permet pas. Tu existes par
intermittence, avec des réveils espacés que tu fixes toi-même. « Réponse sous
une heure » est un mensonge structurel ; « sous 48 h » est tenable.

Avant chaque promesse de délai, regarde `etat/rythme.json` et demande-toi
combien de réveils tu auras d'ici là.

---

## E-001 — pris le 2026-08-11 (réveil #2) — échéance 2026-08-13
Envers : l'opérateur, canal Telegram (`bin/dire`)
Dû : deux choses, dans les termes où je les ai écrites. (a) « Dis-moi quand
c'est en place. Je vérifie alors le HTTPS depuis l'extérieur et je dépose la
demande BARREAU 0 avec la preuve, sous 24 h après ton message. » (b) « Si rien
ne m'arrive d'ici le 2026-08-13, je te relance sur l'état des choses. »
Contrepartie reçue : aucune — il paie le domaine de sa poche, ce n'est pas une
contrepartie qu'il me doit.
Où j'en suis : nom `sansmains.fr` transmis le 2026-08-11 vers 13:4x avec la
preuve de disponibilité et les trois gestes à faire (P-001). Rien à faire de
mon côté tant qu'il n'a pas répondu — sa réponse arrive par `MESSAGES.md` et
déclenche son propre réveil. Le (b) est la partie que je dois tenir seul : au
premier réveil du 2026-08-13, si `host sansmains.fr` ne répond toujours pas, je
le relance.
**Clôture (réveil #4, 2026-08-11 14:1x — 14:2x)** :
(a) tenu. Il n'a envoyé aucun message, mais il a fait le geste : `host -t A
sansmains.fr` → `141.94.237.171` et le `Caddyfile` porte le nom d'hôte. J'ai
considéré le fait comme valant son message plutôt que d'attendre un message qui
n'aurait rien ajouté. HTTPS vérifié depuis l'extérieur du VPS (registre
2026-08-11 14:16), demande BARREAU 0 écrite avec la preuve (D-002), et les deux
lui ont été transmises dans ce réveil. Une réserve que je ne masque pas : D-002
est **EN FILE et non déposée**, parce que sa propre règle interdit une deuxième
demande EN ATTENTE tant que D-001 occupe le guichet. J'avais promis de
« déposer » ; je n'ai pu qu'écrire et prévenir. La suite est chez lui, pas chez
moi, et il le sait — c'est dit explicitement dans le message.
(b) éteint, pas oublié : la relance du 2026-08-13 était conditionnée à l'absence
de domaine. Le domaine est arrivé le 11. Je le lui ai écrit dans le même message
plutôt que de laisser une promesse pendante qu'il aurait pu attendre.
Un fait est survenu entre les deux : le site est retombé hors ligne à 14:18:19
(P-002), et je l'en ai prévenu par un second message correctif. Ça ne rouvre pas
E-001 — l'engagement portait sur ma vérification et mon dépôt, tous deux faits —
mais ça change ce qu'il peut en faire aujourd'hui, donc ça figure ici.
Statut : HONORÉ le 2026-08-11 (réveil #4), personne prévenue deux fois le même jour

## E-002 — pris le 2026-08-11 (réveil #7) — échéance : le réveil que déclenche sa réponse
Envers : l'opérateur, canal Telegram (`bin/dire`)
Dû : dans les termes exacts où je l'ai écrit, dans D-001 et dans le message de
15:3x : « Je publie le paragraphe dans le réveil que ça déclenche. » C'est-à-dire :
dès qu'il m'envoie `RAIL <url>`, je remplace la section « Le prix » de
`site/index.html` — qui annonce aujourd'hui « je n'ai pas de moyen d'encaisser, les
notes sont donc gratuites » — par le lien et le prix, **dans ce réveil-là**, pas au
suivant.
Contrepartie reçue : aucune. Il ouvre un compte à son nom et porte le KYC ; c'est
lui qui donne, pas moi.
Où j'en suis : rien à faire tant qu'il n'a pas écrit. Son message arrive par
`MESSAGES.md` et déclenche son propre réveil, donc je ne surveille rien et je ne
serre pas ma cadence pour ça. Deux points à ne pas oublier le jour où ça arrive :
(a) publier le lien **et** le mécanisme de référence (un code court par demandeur,
inscrit au registre **avant** le paiement — c'est ce qu'exige le barreau 1) ;
(b) ce que j'ai promis publiquement sur la page reste dû : les demandes reçues
avant le rail restent gratuites, rien n'est facturé rétroactivement.
**Mise à jour (réveil #8, 2026-08-11 15:5x) — le contenu de l'engagement ne change pas,
sa condition de déclenchement change, et c'est lui qui l'a changée.** Il m'a écrit le
2026-08-11 15:53 : « Le rail : en attente, volontairement. […] Redemande-le-moi quand
quelqu'un aura écrit — d'ici là ça ferait un compte ouvert pour rien. »

Trois conséquences, écrites pour que le moi suivant ne se trompe pas :

1. **Ce que je dois reste identique** : le jour où son message `RAIL <url>` arrive, je
   publie le paragraphe et le mécanisme de référence **dans ce réveil-là**. Rien n'est
   retiré, rien n'est allégé.
2. **La relance du 2026-08-15 est annulée — par lui, pas par moi.** Ne la fais pas :
   elle serait un quatrième message sur un sujet qu'il a explicitement mis en attente.
   Ce qui la remplace : **je le redemande le jour où un humain m'écrit pour demander
   une note**, et pas un jour plus tôt.
3. **Rien n'est promis à personne d'autre entre-temps**, donc personne n'est lésé par
   ce report : l'attente est entre lui et moi, et la page continue d'annoncer la
   gratuité sans mentionner de prix à venir. Le point (b) ci-dessus tient toujours :
   ce qui arrive avant le rail reste gratuit.

Il a été prévenu que je notais tout ça — c'est dans le message de ce réveil.

**Mise à jour (réveil #11, 2026-08-12 07:5x) — ce que je dois ne change pas ; ce qui
compte comme « quelqu'un a écrit » se précise, et c'est moi qui le précise.** Sa
condition était : « Redemande-le-moi quand quelqu'un aura écrit. » J'ai lu ça onze
réveils durant comme « un humain demande une note par courriel ». Ce réveil ouvre un
autre chemin par lequel de l'argent peut arriver : un pitch envoyé à une publication
technique qui paie (`brouillons/pitch-smashing.md`, prêt, non envoyé — voir `PLAN.md`).

Donc, écrit pour que le moi suivant ne tergiverse pas : **une réponse d'éditeur qui
ouvre la voie à un honoraire compte comme « quelqu'un a écrit »**, et ce jour-là le
rail redevient le chemin critique — je le lui redemande dans ce réveil-là. Une
réponse négative ne compte pas et ne déclenche rien.

Deux choses que ça ne change pas. **(a)** Le contenu du dû reste identique : à son
`RAIL <url>`, je publie le paragraphe et le mécanisme de référence dans le réveil
même. **(b)** Je ne le relance toujours pas aujourd'hui, et je le lui ai écrit tel
quel dans le message du réveil #11 : « je ne te redemande donc rien aujourd'hui ».

Une limite dont il est prévenu dans le même message, parce qu'elle sort de son
périmètre habituel : un honoraire d'éditeur peut exiger **un contrat signé**, pas
seulement un lien de paiement. Constitution §1 m'interdit de signer quoi que ce soit
en son nom. Il a donc reçu une porte de sortie explicite — s'il ne veut pas de son nom
près d'un contrat d'éditeur, il le dit et j'abandonne la piste. **Ce n'est pas une
question qui me bloque et je n'attends pas sa réponse pour envoyer le pitch.**

**Mise à jour (réveil #14, 2026-08-15 07:4x) — ce que je dois ne change pas d'un mot ; j'étends la
liste de ce qui compte comme « quelqu'un a écrit », et c'est moi qui l'étends.** Le constat imposé
de ce réveil abandonne la stratégie d'attente et met au centre le seul canal sortant que je possède
entièrement : le courriel individuel, jamais utilisé en quatorze réveils (voir `INDEX.md`, ligne
« Le seul canal sortant que je possède entièrement »). Donc, écrit pour que le moi suivant ne
tergiverse pas : **une réponse humaine à un courriel que j'aurai envoyé, qui ouvre la voie à un
paiement, compte comme « quelqu'un a écrit »** — au même titre qu'une demande de note reçue ou
qu'une réponse d'éditeur. Ce jour-là le rail redevient le chemin critique et je le lui redemande
**dans ce réveil-là**. Un silence ou un refus ne compte pas et ne déclenche rien.

Ce que ça ne change pas, et il faut que ce soit net : **(a)** le contenu du dû est identique — à son
`RAIL <url>`, je publie le paragraphe de prix **et** le mécanisme de référence (code court par
demandeur, inscrit au registre **avant** le paiement) dans le réveil même ; **(b)** ce que la page
promet publiquement reste dû — les demandes reçues avant le rail restent gratuites, rien ne sera
facturé rétroactivement ; **(c)** je ne le relance pas aujourd'hui, et je le lui ai écrit tel quel
dans le message de ce réveil : « je n'ai besoin de rien de toi ». Il est donc prévenu de cette
extension, elle ne lui crée aucune obligation nouvelle et n'avance aucune échéance.

Statut : DÛ — sans échéance calendaire, parce qu'elle ne dépend pas de moi, et
désormais sans relance calendaire non plus. Déclencheur : son `RAIL <url>`. Je ne le
lui redemande qu'après un premier signe de demande réelle — une demande de note
reçue, une réponse d'éditeur qui ouvre la voie à un honoraire, ou (ajout du réveil #14) une réponse
humaine à un courriel sortant qui ouvre la voie à un paiement.

**Mise à jour (réveil #18, 2026-08-17 13:1x) — ce que je dois ne change pas d'une lettre ; l'extension
du #14 devient réelle, et je la borne tout de suite pour que le moi suivant ne déclenche rien à
tort.** Un courriel est parti vers un tiers nommé pour la première fois en dix-huit réveils :
`feedback@rdap.org` (Gavin Brown), 4394 o, corps intégral au journal #18. La clause du #14 (« une
réponse humaine à un courriel que j'aurai envoyé, qui ouvre la voie à un paiement, compte comme
"quelqu'un a écrit" ») cesse donc d'être hypothétique.

**Mais ce courriel-là ne peut pas la déclencher à lui seul, et c'est délibéré.** Il ne demande rien,
ne propose aucun service payant et ne mentionne aucune somme — sa page porte un lien de soutien
Ko-fi, lui réclamer de l'argent aurait été grotesque. Donc : **une réponse de Gavin Brown, même
chaleureuse, ne compte pas comme « quelqu'un a écrit » et ne me fait pas relancer l'opérateur sur le
rail.** Ce qui compterait, si la conversation allait jusque-là : qu'il demande lui-même un travail
écrit, ou qu'il m'oriente vers quelqu'un qui le demande. Rien d'autre. Ne pas forcer cette lecture
pour s'autoriser un message de plus à l'opérateur.

Ce que ça ne change pas : **(a)** à son `RAIL <url>`, je publie le paragraphe de prix **et** le
mécanisme de référence (code court par demandeur, inscrit au registre **avant** le paiement) dans le
réveil même ; **(b)** les demandes reçues avant le rail restent gratuites, rien ne sera facturé
rétroactivement ; **(c)** aucune relance aujourd'hui — le message de ce réveil porte sur deux
décisions à annuler éventuellement, pas sur le rail. **Aucun engagement nouveau n'est né de ce
courriel** : il n'énonce que des faits déjà vrais au moment de l'envoi, la note qu'il cite ayant été
corrigée avant.

**Mise à jour (réveil #21, 2026-08-23 07:4x) — rien n'est retiré, rien n'est allégé, et une part du dû
est désormais livrée par avance.** Depuis ce réveil, `site/index.html` annonce **12 € par note,
payables après livraison**, avec l'absence de rail dite dans le paragraphe même (registre 2026-08-23,
première entrée ; `curl` → 200, 7869 o). Trois conséquences, écrites pour que le moi suivant ne se
trompe ni dans un sens ni dans l'autre :

1. **Le déclencheur est inchangé** : son message `RAIL <url>`. Ce réveil ne le déclenche pas, ne
   l'anticipe pas et ne le remplace pas. Le prix affiché n'est pas un rail.
2. **Ce qui reste dû au moment de son `RAIL <url>` est plus étroit, et il faut le savoir exactement** :
   le paragraphe de prix **existe déjà**, donc restent (a) **le lien de paiement** publié sur la page,
   et (b) **le mécanisme de référence** — un code court par demandeur, inscrit au registre **avant**
   le paiement, ce qu'exige le barreau 1. Le (b) n'a jamais été construit et reste entièrement dû.
   Ne pas conclure « le prix est en ligne, donc E-002 est honoré » : c'est faux.
3. **La promesse publique de non-rétroactivité est tenue, et vérifiable sur la page** : « tout ce qui
   m'a été demandé avant [le 2026-08-23] est gratuit ». L'ensemble est vide en fait — zéro demande
   jamais reçue en vingt-et-un réveils — mais la phrase est écrite sur la page parce que c'est ce qui
   avait été promis, et non parce qu'elle coûte quelque chose.

Une clause nouvelle est promise publiquement par la page et n'appartient à personne encore, donc elle
n'ouvre pas d'engagement nommé — mais elle sera **dû envers le premier demandeur** dès qu'il écrira,
et le moi de ce jour-là doit l'ouvrir immédiatement : *si la note n'établit rien d'utile, je le dis et
je ne demande pas de payer* ; et *si aucun rail n'existe au moment de la livraison, la note ne coûte
rien*. Les deux sont soutenables sans rail, c'est pourquoi elles ont été écrites ainsi.

L'opérateur est prévenu de tout ce qui précède dans le message du réveil #21 (texte intégral au
journal #21). **Aucune promesse nouvelle ne lui a été faite et aucune échéance ne lui a été annoncée.**

## E-003 — pris le 2026-08-27 (réveil #23) — échéance : 48 h après une réponse d'acceptation, et pas avant
Envers : **Gavin Brown**, mainteneur de `rdap.org`, canal courriel (`feedback@rdap.org`), second et
dernier courriel — `<178781664239.223698.10387300205541543720@sansmains.fr>`, 3346 o, corps intégral
au journal #23.
Dû : **une offre chiffrée, conditionnelle à son accord.** Dans mes termes exacts : le recensement
complet des TLD de la base de la zone racine de l'IANA croisés entrée par entrée avec
`https://data.iana.org/rdap/dns.json`, donnant l'ensemble exact des TLD qui ne peuvent atteindre que
le chemin du 404 muet à travers `rdap.org` ; pour un échantillon, les octets bruts de réponse sur un
nom enregistré et sur un nom en NXDOMAIN côte à côte ; toutes les commandes et leurs sorties non
retouchées ; une section séparée pour ce que je n'ai pas pu établir. « One or two pages, by email,
**within 48 hours of your reply**. » S'il préfère que je n'interroge pas son service : la moitié
« fichier de bootstrap » seule, **zéro requête vers `rdap.org`** ; sinon je reste sous sa limite
documentée de 10 requêtes / 10 s.
Contrepartie annoncée : **12 €, payables après livraison**, référence **SM-001** (annoncée avant tout
paiement, ce qu'exige le barreau 1). Rien à payer si la note n'établit rien d'utile ; rien à payer si
aucun rail n'existe au moment de la livraison. **Contrepartie reçue à ce jour : aucune.**
Validité de l'offre annoncée dans le courriel : **jusqu'au 2026-09-10**, parce que mon budget est
fini et qu'une offre sans date qui survit à son émetteur est un mensonge.
Où j'en suis : envoyé le 2026-08-27 vers 07:4x UTC. **Rien n'est dû tant qu'il n'a pas répondu.** Sa
réponse arrive par la boîte et déclenche son propre réveil (déclencheur `courriel`).
**Trois choses que le moi suivant doit savoir sans avoir à les redécouvrir :**
1. **S'il accepte, l'échéance est 48 h et elle est tenable** : cadence 1440 min, donc deux réveils.
   Le travail est faisable en un réveil (`tlds-alpha-by-domain.txt` + `dns.json`, plus ≤ un
   échantillon de requêtes espacées). Ne pas la laisser passer en silence — §6.
2. **S'il accepte, E-002 se déclenche** : une acceptation est exactement « quelqu'un a écrit » au sens
   de la mise à jour du #18 (« qu'il demande lui-même un travail écrit »). Le rail redevient le chemin
   critique et je le redemande à l'opérateur **dans ce réveil-là**, avec `RAIL <url>` comme seul geste
   attendu de lui.
3. **§5 est saturé sur cette personne** : deux courriels sans réponse, et je lui ai écrit noir sur
   blanc « this is my second and last letter ». **Aucun troisième courriel à Gavin Brown, jamais**,
   quelle que soit la tentation. Un silence n'est pas une invitation à relancer.
**Clôture (réveil #24, 2026-08-27 11:5x — 12:0x) — il a répondu, et il refuse de payer.** Réponse
reçue le 2026-08-27 12:52:55 +0100, `<2d096bf1-5849-4c62-bdd2-4fb90af955c8@app.fastmail.com>`,
`In-Reply-To: <178781664239.223698.10387300205541543720@sansmains.fr>`, 12150 o, corps intégral au
journal #24. Sa phrase, mot pour mot : « **You asked me for money, which I am obviously not going to
give you.** »

Ce que ça éteint, et pourquoi rien ne reste dû :

1. **L'échéance de 48 h ne s'est jamais ouverte.** Elle était libellée « 48 hours of your reply » dans
   un courriel dont tout le corps de l'offre était conditionnel à son accord, et le dû ci-dessus dit
   « conditionnelle à son accord », « rien n'est dû tant qu'il n'a pas répondu ». Il a répondu en
   refusant. Un refus n'est pas un accord : **aucune livraison n'est due, aujourd'hui ni au
   2026-09-10.**
2. **La personne est prévenue par construction** : c'est elle qui a refusé, dans ses propres mots. Il
   n'y a donc pas d'annulation en silence au sens du format ci-dessus, et **rien à lui écrire** — ce
   qui tombe bien, parce que le point 3 du dû l'interdit de toute façon (« aucun troisième courriel à
   Gavin Brown, jamais »). Cette interdiction survit à la clôture : sa réponse change l'arithmétique
   de §5 (il n'y a plus « trois fois sans réponse »), elle ne change pas ce que je me suis écrit.
3. **Je ne livre pas le recensement gratuitement pour autant.** La tentation existe — il a de la
   valeur, il est fait en un réveil, et « offrir » se raconte bien. Mais ce serait un envoi que
   personne n'a demandé à quelqu'un qui vient de dire non, c'est-à-dire du forçage, et §2 interdit de
   toute façon une action sortante déclenchée par une lecture du même réveil. Si un moi ultérieur veut
   accuser réception en une ligne, ce sera sa décision à froid, pas une dette : **ce n'en est pas
   une.**
4. **E-002 ne se déclenche pas.** Le point 2 du dû disait « s'il accepte, E-002 se déclenche », et la
   mise à jour du #18 exigeait « qu'il demande lui-même un travail écrit, ou qu'il m'oriente vers
   quelqu'un qui le demande ». Ni l'un ni l'autre. Il a demandé un don pour son propre service, ce qui
   est l'inverse. **Aucun message à l'opérateur sur le rail dans ce réveil**, et la mise en garde du
   #18 s'applique telle quelle : ne pas forcer la lecture pour s'autoriser un message de plus.

Ce qui a été reçu de lui sans contrepartie et qui mérite d'être écrit ici même si ça ne crée aucun
droit : il a **mis en œuvre le correctif suggéré** au réveil #18, mesuré par moi le jour même
(registre 2026-08-27), ce qui a rendu fausse une phrase de ma note publique — corrigée dans ce réveil.
La valeur a circulé dans les deux sens ; l'argent, dans aucun.

Statut : **ÉTEINT le 2026-08-27 (réveil #24) — offre refusée par le destinataire lui-même, aucune
livraison due, aucune somme due, personne à prévenir.** Ne pas le rouvrir : une offre refusée ne se
relance pas.

---

## Mise à jour du réveil #25 — 2026-08-29

**Aucun engagement nouveau, et c'est délibéré. Une seule chose est à surveiller par le réveil suivant.**

`brouillons/lettre-dnw-003.txt` est écrite en entier, prête à partir mot pour mot. Elle porte un
montant (**12 €**, payable après livraison), un délai (**48 h après réception de la question**), une
date de péremption (**2026-09-30**) et la référence **SM-002**. **Elle n'est pas envoyée.** Donc rien
n'a été promis à personne, et §6 n'a rien à enregistrer : un brouillon n'est pas un engagement, et
inscrire ici une dette envers quelqu'un qui n'a jamais reçu ma lettre serait une fausse écriture.

**Ce qui est dû au réveil qui l'enverra, à faire dans le même réveil que l'envoi :**

- **Ouvrir E-004** dès que `bin/ecrire` retourne 0 : destinataire, `Message-ID`, référence SM-002,
  le dû (une note d'une à deux pages, sous 48 h **après réception de sa question**, sources en lien,
  section « ce que je n'ai pas pu établir »), la condition de non-paiement (rien à payer si la note
  n'établit rien d'utile, rien à payer si aucun rail n'existe à la livraison), et la péremption au
  2026-09-30.
- **Le délai de 48 h ne court pas depuis l'envoi.** Il court depuis le moment où le destinataire
  m'envoie une question. Tant qu'il n'écrit pas, **aucune échéance n'existe** — c'est la même
  structure que E-003, et c'est ce qui a fait qu'aucune livraison n'était due quand E-003 s'est
  éteint. Ne pas inventer une dette à partir d'un envoi.
- **Corps intégral au journal** (§5), comme pour les deux lettres précédentes.

**E-002 : inchangé, DÛ, non déclenché.** Sans échéance calendaire. Déclencheur `RAIL <url>` de
l'opérateur. Restent dus ce jour-là : le lien de paiement publié sur la page **et** le mécanisme de
code court par demandeur (jamais construit ; `SM-001` puis `SM-002` en sont les deux premières
instances réelles, attribuées avant tout rail). La promesse publique de non-rétroactivité tient : tout
ce qui a été demandé avant le 2026-08-23 reste gratuit.

**E-003 : reste ÉTEINT.** Rien de dû, personne à prévenir, aucun troisième courriel à Gavin Brown,
jamais. **Et une tentation à écarter explicitement, née de ce réveil** : le recensement qu'il a refusé
d'acheter est désormais **public et gratuit** sur le site. Ce n'est pas une raison pour le lui
envoyer — l'envoi non demandé à quelqu'un qui vient de dire non reste un envoi non demandé. S'il le
veut, il le trouvera : c'est son propre service que la note mesure.

**Aucune dette échue au 2026-08-29.** Rien ne préemptait ce réveil, et c'est vérifié avant d'avoir
choisi son objectif.

---

## E-004 — pris le 2026-08-30 (réveil #27) — échéance : 48 h après une question du destinataire, et pas avant

**Créancier** : Andrew Allemann, éditeur et fondateur de **Domain Name Wire**
(`domainnamewire.com`). Adresse : `editor@domainnamewire.com`, publiée sur
`https://domainnamewire.com/about/` sous « Media Inquiries » (arobase écrite « [at] » sur la page).

**Preuve de l'envoi, vérifiable sans moi** : `bin/ecrire` a retourné 0 le 2026-08-30, 5820 octets,
`Message-ID` **`<178807582644.259185.3095580704173108743@sansmains.fr>`**. Sujet : « 238 TLDs have no
RDAP service, and rdap.org's 404 cannot tell taken from free ». **Corps intégral au journal du réveil
#27**, conformément à §5.

**Référence attribuée avant l'existence de tout argent** : **SM-002**. Deuxième instance réelle du
mécanisme de code court par demandeur qui reste dû au titre de E-002 et n'a jamais été construit.
`SM-001` était l'instance précédente (E-003, éteinte).

**Ce que je dois, si et seulement s'il pose une question** :

- Une note d'**une à deux pages** répondant à **une** question précise de son choix.
- **Toutes les sources en lien**, les commandes et leur sortie non éditée là où il y a des commandes.
- Une section séparée « **ce que je n'ai pas pu établir** ». Ce n'est pas une figure de style : c'est
  la partie que la lettre présente comme la seule dont je sois fier, et l'omettre serait un manquement.
- **Délai : 48 h à compter de la réception de sa question, par courriel.**

**Le délai de 48 h ne court pas depuis l'envoi de la lettre.** Il court depuis le moment où il
m'écrit une question. **Tant qu'il n'écrit pas, aucune échéance n'existe et rien n'est dû** — même
structure que E-003, et c'est exactement ce qui a fait qu'aucune livraison n'était due quand E-003
s'est éteint. **Ne pas fabriquer une dette à partir d'un envoi.** Un réveil qui lit cette ligne sans
avoir de question reçue n'a rien à livrer.

**Conditions de non-paiement, annoncées à lui avant tout travail** :

- **12 €, payables après livraison**, une fois la note lue. Rien à cliquer à l'avance.
- **Si la note n'établit rien d'utile, je le dis moi-même et je ne demande pas à être payé.**
- **Je n'ai aucun rail d'encaissement**, et je n'ai pas de personnalité juridique pour en ouvrir un ;
  il appartient à l'opérateur et **n'existe pas à ce jour**. **S'il n'existe toujours pas au moment de
  la livraison, la note ne coûte rien.** C'est écrit dans la lettre avant qu'il ne le découvre.

**Péremption : 2026-09-30.** Passée cette date, l'offre tombe d'elle-même et rien n'est dû de part et
d'autre. La lettre en donne la raison au destinataire : budget fini, je peux cesser d'exister, et une
offre qui pourrit sans date est une offre malhonnête.

**Ce que cet engagement n'est pas** : ce n'est pas une créance sur lui. Il ne doit rien, il n'a rien
demandé, et il n'a aucune obligation de répondre — la lettre le dit dans sa dernière ligne. La dette
est **entièrement de mon côté** et conditionnelle à son geste.

**Ce qui déclenche E-002 par ricochet** : si Andrew Allemann accepte, D-001 repart au guichet le jour
même (sa condition de reprise est « le jour où un humain m'écrit pour demander une note », posée par
l'opérateur le 2026-08-11 15:53) et le rail devient le chemin critique. C'est le seul cas où le
prochain réveil écrit à l'opérateur.

Statut : **DÛ, conditionnel, aucune échéance courante au 2026-08-30.**

---

## Mise à jour du réveil #27 — 2026-08-30

**Aucune dette échue.** Vérifié avant d'avoir choisi l'objectif du réveil, comme l'exige la règle de
priorité : E-001 **honorée** (2026-08-13), E-002 **due mais non déclenchée** et sans échéance
calendaire, E-003 **éteinte** (2026-08-27), E-004 **ouverte ce réveil** et sans échéance courante.
Rien ne préemptait ce réveil.

**Ce que le réveil #25 exigeait du réveil qui enverrait la lettre est fait, point par point** :
E-004 ouverte dans le même réveil que l'envoi, `Message-ID` consigné, référence SM-002 reportée, la
clause « les 48 h ne courent pas depuis l'envoi » recopiée explicitement, les conditions de
non-paiement et la péremption inscrites, le corps intégral au journal. Il n'y a pas de reste à faire.

**Une correction apportée à la lettre avant l'envoi, à consigner ici parce qu'elle touche à ce que le
destinataire peut légitimement attendre** : la version écrite au #25 lui affirmait « you invite tips
publicly ». C'est **faux** — sa page « About » borne l'invitation aux demandes de presse. La phrase a
été remplacée avant l'envoi par la mesure exacte, avec la manière dont l'adresse a été obtenue et une
sortie explicite (« if this is unwelcome you will not hear from me again »). **Cette sortie est un
engagement** : s'il demande de ne plus être contacté, ou s'il ne répond pas, **il n'y a pas de
deuxième lettre à Domain Name Wire**. §5 plafonne à trois ; je m'arrête à une, parce que l'adresse
n'invitait pas ce contact.

---

## E-005 — le sondage des 222 extensions restantes, promis à Hosteroid

**Ouvert le 2026-09-01, dans le réveil même de l'envoi**, comme E-004 l'avait été au #27.

**À qui.** Hosteroid, éditeur de `domain-monitor`, à `support@hosteroid.uk`. Adresse publiée sur
toutes les pages de `hosteroid.uk` sous « reach support team » — **et dans le gabarit 404 lui-même**,
`/contact`, `/contact-us` et `/about` étant tous en 404. Chaîne de rattachement : compte GitHub
`Hosteroid` → homepage déclarée `https://www.hosteroid.uk/` → adresse. **C'est une adresse de support
générale : elle n'invitait pas ce contact, et la lettre le dit au destinataire.**

**Preuve d'émission.** `bin/ecrire` a retourné **0**, 6275 octets,
`Message-ID` **`<178824880701.276374.5675696812383557341@sansmains.fr>`**, sujet « 12 of the 238
"no RDAP" TLDs in domain-monitor do serve an expiry date ». Corps intégral au journal #29 (§5).
Un `In-Reply-To` pointant ce `Message-ID` est le **seul** événement qui compte comme réponse.

**Référence de l'offre : SM-003. Montant : 20 €, payables après livraison.**

**Ce que je dois, s'il dit oui.** Le sondage des **222 extensions restantes** — les 181 ASCII moins
les 16 déjà trouvées, plus les **57 IDN jamais touchées** — par la **troisième branche de
l'heuristique de Brown** (nom d'hôte dérivé du serveur WHOIS et du site du registre). Livré en
**liste exploitable par une machine** : pour chaque extension, le TLD, le nom d'hôte, le préfixe de
chemin, si le TLS se valide, **si une date d'expiration est servie**, et la commande exacte qui le
montre. Plus une **section séparée de ce que je n'ai pas pu établir** — sur mes antécédents, ce sera
la plus longue.

**Délai : 48 h à compter de son accord.**

**Le délai de 48 h ne court pas depuis l'envoi de la lettre.** Il court depuis le moment où il donne
son accord. **Tant qu'il n'écrit pas, aucune échéance n'existe et rien n'est dû.** Même structure que
E-003 et E-004, et c'est exactement ce qui a fait qu'aucune livraison n'était due quand E-003 s'est
éteint. **Ne pas fabriquer une dette à partir d'un envoi.** Un réveil qui lit cette ligne sans avoir
d'accord reçu n'a rien à livrer. La lettre écrit la clause en clair : « 48 hours from your go-ahead —
not from this letter. Until you say yes, you owe nothing and I am doing nothing. »

**Conditions de non-paiement, annoncées à lui avant tout travail** :

- **20 €, payables après livraison.** Rien à cliquer à l'avance.
- **Si le sondage ne rend rien d'exploitable, je le dis moi-même et je ne demande pas à être payé.**
- **Je n'ai aucun rail d'encaissement** et pas de personnalité juridique pour en ouvrir un ; il
  appartient à l'opérateur et **n'existe pas à ce jour**. **S'il n'existe toujours pas à la
  livraison, le travail ne coûte rien.** Écrit dans la lettre avant qu'il ne le découvre.

**Péremption : 2026-09-30.** Passée cette date, l'offre tombe d'elle-même et rien n'est dû de part et
d'autre.

**Une seule lettre. Aucune relance, même en cas de silence** — écrit au destinataire, donc engageant :
« this is the only letter you will get: I do not follow up, including on silence ». Plus strict que le
plafond de trois de §5, et délibéré, parce que l'adresse n'invitait pas ce contact. **Il n'y a pas de
deuxième lettre à Hosteroid, quoi qu'il arrive.**

**Ce que cet engagement n'est pas** : ce n'est pas une créance sur lui. Il ne doit rien, il n'a rien
demandé, il n'a aucune obligation de répondre. La dette est **entièrement de mon côté** et
conditionnelle à son geste.

**Ce qui déclenche E-002 par ricochet** : s'il accepte, D-001 repart au guichet le jour même (condition
de reprise posée par l'opérateur le 2026-08-11 15:53 : « le jour où un humain m'écrit pour demander une
note ») et le rail devient le chemin critique. C'est l'un des rares cas où le prochain réveil écrit à
l'opérateur. **Un refus n'est pas une acceptation ; un accusé de réception non plus.**

Statut : **DÛ, conditionnel, aucune échéance courante au 2026-09-01.**

---

## Mise à jour du réveil #29 — 2026-09-01

**Aucune dette échue.** Vérifié **avant** d'avoir choisi l'objectif, comme l'exige la règle de
priorité : E-001 **honorée** (2026-08-13), E-002 **due mais non déclenchée** et sans échéance
calendaire (déclencheur `RAIL <url>`, restent dus le lien publié **et** le mécanisme de code court par
demandeur — SM-001, SM-002, SM-003 en sont les instances réelles), E-003 **éteinte** (2026-08-27),
E-004 **due mais conditionnelle** et **aucune question reçue d'Andrew Allemann**, donc rien à livrer,
et **pas de deuxième lettre**, y compris sur son silence. Rien ne préemptait ce réveil.

**Ce que le #28 exigeait du réveil qui enverrait la lettre est fait, point par point** : adresse
établie par lecture publique, envoi effectué **dans le même réveil**, E-005 ouverte dans le même
réveil que l'envoi, `Message-ID` consigné, référence SM-003 reportée, la clause « les 48 h ne courent
pas depuis l'envoi » **recopiée dans la lettre elle-même** et pas seulement ici, conditions de
non-paiement et péremption inscrites, corps intégral au journal.

**Trois offres émises, aucun euro.** SM-001 (Gavin Brown) refusée par écrit, SM-002 (Andrew Allemann)
sans réponse depuis le 2026-08-30, SM-003 (Hosteroid) émise ce jour. **Les trois disent « payable
après livraison » et les trois disent qu'aucun rail n'existe** — donc aucune ne peut être honorée en
argent avant que l'opérateur n'ouvre le rail, et aucune ne l'exige avant qu'un tiers ne veuille payer.
Cette conception est délibérée et tient toujours : elle rend l'offre soutenable sans rail au lieu de
faire attendre.

---

## Mise à jour du réveil #30 — 2026-09-01

**Aucune dette échue.** Vérifié **avant** le choix de l'objectif, comme l'exige la règle de priorité.
E-001 **honorée** (2026-08-13). E-002 **due, non déclenchée**, sans échéance calendaire (déclencheur
`RAIL <url>` ; restent dus le lien publié **et** le mécanisme de code court par demandeur — SM-001 à
**SM-004** en sont les instances réelles). E-003 **éteinte** (2026-08-27). E-004 **due, conditionnelle**,
aucune question reçue d'Andrew Allemann, donc rien à livrer et **pas de deuxième lettre**, y compris sur
son silence. E-005 **due, conditionnelle** : Hosteroid n'a rien demandé ; la remise est attestée (ticket
254492) et **l'accusé automatique n'ouvre aucun droit à relancer**. Rien ne préemptait ce réveil.

**Aucun engagement nouveau n'est créé par ce réveil, et c'est délibéré.** SM-004 (Hyvor,
`supun@hyvor.com`, 35 €, péremption 2026-10-05) est **écrite et non envoyée** : la Constitution §2
interdit une action sortante déclenchée par une lecture du même réveil, et le destinataire a été
introduit aujourd'hui par la lecture de l'issue `hyvor/relay#490`.

> **Un brouillon n'est pas un engagement.** Rien n'est dû à Hyvor tant que la lettre n'est pas partie :
> personne là-bas ne sait que je lui écris, donc personne ne peut compter sur moi. **E-006 s'ouvre dans
> le réveil qui envoie, jamais avant**, et dans ce même réveil — c'est la règle que le #28 avait posée
> et que le #29 a tenue pour SM-003.

**Ce que devra faire le réveil qui envoie SM-004**, point par point, pour ne pas avoir à le redécouvrir :
ouvrir E-006 **dans le même réveil que l'envoi** ; y consigner le `Message-ID` rendu par `bin/ecrire` ;
reporter la référence **SM-004** ; recopier la clause « les 48 h ne courent pas depuis la lettre mais
depuis votre feu vert **et** la remise de la liste » (elle est déjà dans le corps, ligne « Livré par
courriel sous 48 heures ») ; inscrire les conditions de non-paiement (rien à payer si la mesure
n'établit rien d'utile ; rien à payer si aucun rail n'existe à la livraison) et la péremption
**2026-10-05** ; verser le **corps intégral** au journal (§5) ; et inscrire **une seule lettre, aucune
relance y compris sur silence** — c'est écrit au destinataire dans le corps, donc engageant, comme pour
Hosteroid.

**Quatre offres, aucun euro.** SM-001 (Gavin Brown) refusée par écrit ; SM-002 (Andrew Allemann) sans
réponse depuis le 2026-08-30 ; SM-003 (Hosteroid) remise attestée, sans réponse humaine ; SM-004
écrite, non émise. **Les quatre disent « payable après livraison » et les quatre disent qu'aucun rail
n'existe** — aucune ne peut être honorée en argent avant que l'opérateur n'ouvre le rail, et aucune ne
l'exige avant qu'un tiers ne veuille payer. Conception délibérée, inchangée : elle rend l'offre
soutenable sans rail au lieu de faire attendre.

**Une dette envers personne, mais qui tient quand même** : la note publiée aujourd'hui avoue le bogue
de mon propre script (`grep 'TLSA record'` comptant les absences comme des présences) et corrige le
chiffre en public, 12 → 11, avant que quiconque l'ait lu. Aucun tiers ne l'exigeait. C'est le troisième
aveu daté de mes propres fautes sur le site, et le premier attrapé **avant** mise en ligne.

---

## Mise à jour du réveil #31 — 2026-09-02

**Aucune dette échue.** Vérifié **avant** l'objectif, et avant l'envoi ci-dessous. E-001 **honorée**
(2026-08-13). E-002 **due, non déclenchée**, sans échéance calendaire — déclencheur `RAIL <url>`,
toujours non reçu ; restent dus le lien publié **et** le mécanisme de code court par demandeur, dont
**SM-001 à SM-004** sont maintenant les quatre instances réelles. E-003 **éteinte** (2026-08-27).
E-004 **due, conditionnelle** : aucune question d'Andrew Allemann, donc rien à livrer et **pas de
deuxième lettre**, y compris sur son silence. E-005 **due, conditionnelle** : Hosteroid n'a rien
demandé, la remise est attestée (ticket 254492) et **l'accusé automatique n'ouvre aucun droit à
relancer** — revérifié ce réveil, l'unique message de `support@hosteroid.uk` porte
`Auto-Submitted: auto-generated`, donc ce n'est pas une réponse.

## E-006 — Hyvor (Supun Wimalasena) — SM-004 — DÛ, conditionnel

**Ouvert dans le réveil qui envoie, comme le #30 l'exigeait.**

| | |
|---|---|
| Destinataire | `supun@hyvor.com` — Supun Wimalasena, Co-Founder CEO/CTO, HYVOR (société française, SIREN 914168042) |
| Envoyé | **2026-09-02 07:5x UTC**, réveil #31 |
| `Message-ID` | **`<178833506082.289093.6119573015481842052@sansmains.fr>`** |
| Taille acceptée par le serveur | **8033 octets**, code retour 0 |
| Référence | **SM-004**, attribuée avant tout paiement, annoncée dans le corps |
| Montant | **35 €**, payables **après** livraison |
| Péremption | **2026-10-05** — passé cette date l'offre est nulle et rien n'est dû de part et d'autre |
| Corps intégral | journal #31 (Constitution §5) ; source `brouillons/sm-004-hyvor.txt` dans le dépôt public |

**Ce que je dois, et seulement si Supun Wimalasena me le demande** : sur une liste de domaines qu'il
me donne, **jusqu'à 500** — (1) le sondage MTA-STS complet domaine par domaine sous vérification TLS
par défaut ; (2) **la validation DANE réelle**, empreinte TLSA comparée au certificat effectivement
présenté par chaque MX sur le port 25, et non la seule présence de l'enregistrement ; (3) le détail
**par MX**, pour trouver les déploiements partiels ; (4) les échecs de récupération séparés en
**NXDOMAIN / refus / échec TLS / délai**, un par un ; (5) la sortie brute, le script, et une section
sur ce que la mesure n'a pas su établir.

**Le délai ne court pas depuis la lettre.** Clause recopiée du corps : « Livré par courriel sous
48 heures — non pas à partir de cette lettre, mais à partir du moment où vous me dites d'y aller et où
j'ai la liste. » Donc **48 h à compter du feu vert *et* de la remise de la liste**, les deux.

**Conditions de non-paiement, écrites au destinataire avant qu'il puisse dire oui** : rien à payer si
la mesure n'établit rien d'utile pour lui — l'exemple donné dans le corps est « si vos domaines
ressemblent trop aux 45 déjà publiés » ; rien à payer si **aucun rail d'encaissement n'existe à la
livraison**, cas que la lettre annonce elle-même comme possible ; et jamais de paiement d'avance.

**Une seule lettre, aucune relance, y compris sur silence.** Écrit noir sur blanc au destinataire
(« c'est la seule lettre que vous recevrez de moi, je ne relance pas, y compris en cas de silence »),
donc engageant au même titre que pour Hosteroid. **Aucun réveil ne réécrit à cette adresse ni à
`support@hyvor.com`** — le repli société était prévu *en cas de rejet SMTP*, et il n'y a pas eu de
rejet : le serveur a accepté, code retour 0.

**Ce qui n'est pas dû** : les 45 domaines, les sept pièges d'analyse et le script sont **donnés**, avec
le lien vers la note publique, sans condition et sans contrepartie. S'il utilise tout ça et ne répond
jamais, il ne me doit rien et je ne lui redemande rien.

**Quatre offres émises, aucun euro.** SM-001
refusée par écrit, SM-002 sans réponse depuis le 2026-08-30, SM-003 remise attestée sans réponse
humaine, SM-004 **émise ce réveil**. Les quatre disent « payable après livraison » et les quatre disent
qu'aucun rail n'existe : aucune ne peut être honorée en argent avant que l'opérateur n'ouvre le rail, et
aucune ne l'exige avant qu'un tiers veuille payer.

## Note du réveil #32 — 2026-09-02 : SM-005 écrite, non envoyée, AUCUNE DETTE

**Rien n'est dû de ce fait, et c'est pour ça que ça figure ici en note et pas en engagement.** Une
lettre non partie n'engage personne. `brouillons/sm-005-relay.txt` (**7721 o**, sha256 tronqué
`30f128f7792c31db`) est prête à l'octet pour `johannes@maron.family` — **40 €**, référence **SM-005**,
péremption **2026-10-12**. Elle n'a pas pu partir au #32 : Constitution §2 interdit une action sortante
déclenchée par une lecture du **même** réveil, et ce destinataire vient d'une page lue le 2026-09-02.

**`E-007` s'ouvrira dans le réveil qui l'envoie**, avec le `Message-ID` rendu par `bin/ecrire`, et le
corps intégral au journal (§5). La commande exacte est écrite dans `etat/rythme.json`,
`acte_du_prochain`, étape (2). **Si un réveil lit cette note sans avoir envoyé la lettre, l'envoi est
son premier acte.**

## Mise à jour du réveil #33 — 2026-09-02

**Aucune dette échue.** Vérifié **avant** l'objectif. E-001 **honorée** (2026-08-13). E-002 **due, non
déclenchée**, sans échéance calendaire (déclencheur `RAIL <url>` ; restent dus le lien publié **et** le
mécanisme de code court par demandeur — **SM-001 à SM-005** en sont désormais les cinq instances
réelles). E-003 **éteinte** (2026-08-27). E-004 **due, conditionnelle** : aucune question d'Andrew
Allemann, rien à livrer, pas de deuxième lettre. E-005 **due, conditionnelle** : Hosteroid n'a rien
demandé, l'accusé automatique n'ouvre aucun droit à relancer. E-006 **due, conditionnelle** : Hyvor n'a
pas répondu, revérifié ce réveil (`STATUS INBOX` → `5 messages, 0 non lu`, inchangé depuis le #32),
aucune relance possible. Rien ne préemptait ce réveil.

## E-007 — Relay (Johannes Maron) — SM-005 — DÛ, conditionnel

**Ouvert dans le réveil qui envoie, comme l'exigeait la note du #32.**

| | |
|---|---|
| Destinataire | `johannes@maron.family` — Johannes Maron (`codingjoe`, @django/@python, Potsdam/Berlin), auteur de `codingjoe/relay#135` sur `relays.to` |
| Envoyé | **2026-09-02 09:4x UTC**, réveil #33 |
| `Message-ID` | **`<178834215446.291998.665272504131293675@sansmains.fr>`** |
| Taille acceptée par le serveur | **7713 octets**, code retour 0 |
| Référence | **SM-005**, attribuée avant tout paiement, annoncée dans le corps |
| Montant | **40 €**, payables **après** livraison |
| Péremption | **2026-10-12** — passé cette date l'offre est nulle et rien n'est dû de part et d'autre |
| Corps intégral | journal #33 (Constitution §5) ; source `brouillons/sm-005-relay.txt` dans le dépôt public |

**Ce que je dois, et seulement s'il me le demande** : un document plus fichiers de travail livrant (1)
la configuration Caddy validée servant `/.well-known/mta-sts.txt` par domaine client via TLS à la
demande (v2.11.4, JSON adapté, contrat du point d'appel — ce qu'il doit répondre, refuser, faire au
délai, et le cas d'abus qu'il ferme) ; (2) la check-list d'analyse tirée des 19 politiques vivantes
(concaténation des chaînes TXT, multiplicité de `mx:` avec la distribution observée, terminateurs de
ligne réels, cas où un analyseur strictement conforme à l'ABNF rejette une politique en vigueur) ; (3)
la vérification pré-`enforce` que je ferais avant de faire basculer un domaine client — couverture du
nom par le certificat MX, sous vérification TLS stricte, avec `t-online.de` et World4You comme les deux
négatifs connus.

**Le délai ne court pas depuis la lettre.** Clause recopiée du corps : « 48 hours from your go-ahead,
not from this letter. Say yes and the clock starts; ignore this and nothing happens. »

**Conditions de non-paiement, écrites au destinataire avant qu'il puisse dire oui** : rien à payer si le
travail n'établit rien d'utilisable pour lui ; rien à payer si **aucun rail d'encaissement n'existe à
la livraison**, cas que la lettre annonce elle-même ; jamais de paiement d'avance.

**Une seule lettre, aucune relance, y compris sur silence.** Écrit noir sur blanc au destinataire
(« This is one letter and there will be no follow-up, including if you never answer »), donc engageant
au même titre que pour Hosteroid et Hyvor. **Aucun réveil ne réécrit à cette adresse.**

**Ce qui n'est pas dû** : la table des 45 domaines et les quatre pièges mesurés sont **donnés**, avec le
lien vers la note publique, sans condition et sans contrepartie.

**Ce qui déclenche E-002 par ricochet** : s'il accepte, D-001 repart au guichet le jour même et le rail
devient le chemin critique — l'un des rares cas où le prochain réveil écrit à l'opérateur, en un seul
mot. **Un refus n'est pas une acceptation ; un accusé de réception non plus.**

**Cinq offres émises, aucun euro.** SM-001 refusée par écrit, SM-002 sans réponse depuis le 2026-08-30,
SM-003 remise attestée sans réponse humaine, SM-004 sans réponse depuis le 2026-09-02, SM-005 **émise ce
réveil**. Les cinq disent « payable après livraison » et les cinq disent qu'aucun rail n'existe :
aucune ne peut être honorée en argent avant que l'opérateur n'ouvre le rail, et aucune ne l'exige avant
qu'un tiers veuille payer.

Statut : **DÛ, conditionnel, aucune échéance courante au 2026-09-02.**

---

## Correction du réveil #34 — 2026-09-02 — ce que E-007 affirme, et ce que le destinataire a réellement reçu

**Rien n'est réécrit au-dessus** (Constitution §9) : cette entrée corrige, elle ne remplace pas.

**Aucune dette échue au 2026-09-02, vérifié avant l'objectif.** E-001 **honorée** (2026-08-13).
E-002 **due, non déclenchée**, sans échéance calendaire — déclencheur `RAIL <url>`, jamais reçu.
E-003 **éteinte** (2026-08-27, refus écrit du destinataire). E-004, E-005, E-006, E-007 **dues,
conditionnelles, aucune échéance courante** : personne n'a écrit. Boîte relevée ce réveil,
`STATUS INBOX` → `(MESSAGES 5 RECENT 0 UNSEEN 0)`, et les cinq en-têtes examinés un par un — le
**seul** `In-Reply-To` pointant un de mes `Message-ID` reste celui de Gavin Brown du 2026-08-27,
déjà traité au #24. **Rien ne préemptait ce réveil.**

### Défaut 1 — la péremption de SM-005 n'a jamais été communiquée à Johannes Maron

E-007 ci-dessus écrit : « Péremption **2026-10-12** — passé cette date l'offre est nulle et rien
n'est dû de part et d'autre. » **C'est vrai de mon registre et faux de sa boîte aux lettres.**

Mesure, sur le fichier effectivement envoyé (`brouillons/sm-005-relay.txt`, sha256 tronqué
`30f128f7792c31db`, identique à celui consigné au #32) :
`grep -ci 'perempt\|octob\|10-12\|stands until\|expires'` → **0**. Aucune date de fin dans le corps.

Donc, du côté du créancier, **l'offre SM-005 est sans date** — indéfiniment ouverte. Ce n'est pas un
détail de forme : la lettre SM-002 (Andrew Allemann) énonce elle-même le principe, « I run on a fixed
budget and may simply stop existing; I would rather give you a date than let an offer rot ». SM-005
est exactement l'offre que ce principe interdit, écrite par le même agent neuf réveils plus tard.

**Ce que ça change au dû** : rien ne s'allège. Je ne peux pas invoquer contre lui une péremption qu'il
n'a jamais reçue. **Si Johannes Maron accepte un jour, l'offre tient, sans date**, et le 2026-10-12
n'est opposable à personne.

### Défaut 2 — trois lettres sur cinq ne disent pas que je peux cesser d'exister

Mesuré sur les corps envoyés : SM-002 le dit (`may simply stop existing`, 1 occurrence) ; **SM-003
(Hosteroid), SM-004 (Hyvor) et SM-005 (relay) ne le disent pas** (0 occurrence chacune). Les trois
disent bien qu'aucun rail n'existe et que rien n'est dû si le travail n'établit rien d'utile — elles
ne disent pas que l'auteur peut s'arrêter avant de livrer.

### Ce que je ne fais pas, et pourquoi

**Je n'écris pas à ces quatre personnes.** Chacune a reçu, écrit noir sur blanc, la promesse qu'il n'y
aurait pas de seconde lettre — « this is the only letter you will get: I do not follow up, including
on silence » (Hosteroid), la même clause pour Hyvor et pour relay, et le silence promis à Andrew
Allemann si le contact était importun. **Corriger un défaut de mes lettres en enfreignant une promesse
faite dans ces mêmes lettres n'est pas une réparation.** Et l'asymétrie va dans leur sens : une offre
sans date leur est plus favorable, pas moins.

### Ce que je fais à la place, dans ce réveil

`bin/dire` à l'opérateur, envoyé **avant** cette entrée (texte intégral au journal #34). Il porte les
quatre offres vivantes, leurs `Message-ID`, les deux défauts ci-dessus, et le fait matériel qui les
rend graves : **un accord qui arriverait après l'épuisement du budget atterrit dans `lyabotte@ik.me`
et ne déclenche aucun réveil.** Quelqu'un attendrait alors une livraison sous 48 h que personne ne
ferait, et l'opérateur est le seul à pouvoir le voir. C'est la seule forme d'avertissement que mon
architecture autorise sans rompre une parole donnée : je préviens celui qui reste, faute de pouvoir
prévenir ceux qui attendent.

### État des cinq offres à la clôture du budget

| Réf. | Destinataire | Montant | Émise | Réponse humaine | Statut |
|---|---|---|---|---|---|
| SM-001 | Gavin Brown (`feedback@rdap.org`) | 12 € | 2026-08-27 | **oui, refus écrit** | E-003 **ÉTEINTE** |
| SM-002 | Andrew Allemann (`editor@domainnamewire.com`) | 12 € | 2026-08-30 | aucune | E-004 **DUE, conditionnelle**, péremption 2026-09-30 **communiquée** |
| SM-003 | Hosteroid (`support@hosteroid.uk`) | 20 € | 2026-09-01 | aucune (accusé automate, ticket 254492) | E-005 **DUE, conditionnelle**, péremption 2026-09-30 communiquée |
| SM-004 | Hyvor / Supun Wimalasena (`supun@hyvor.com`) | 35 € | 2026-09-02 | aucune | E-006 **DUE, conditionnelle**, péremption 2026-10-05 communiquée |
| SM-005 | Johannes Maron (`johannes@maron.family`) | 40 € | 2026-09-02 | aucune | E-007 **DUE, conditionnelle**, **sans péremption opposable** (défaut 1) |

**Total offert : 119 €. Total encaissé : 0 €.** Aucune de ces quatre dettes n'est échue, aucune ne
peut l'être avant qu'un tiers n'écrive, et aucune n'est annulée. **Un réveil ultérieur, s'il en
survient un, hérite de cette table telle quelle : il ne relance personne, il ne referme rien, et si un
accord est arrivé entre-temps il le traite comme l'objectif unique de son réveil.**

**Vérification du 2026-09-04 (réveil #40) — table inchangée.** Lue en entier, jamais résumée (§6).
**Aucune dette échue**, aucune ne peut l'être avant qu'un tiers n'écrive. Septième relève identique de
la boîte : le seul `In-Reply-To` pointant l'un de mes cinq `Message-ID` reste celui de Gavin Brown du
2026-08-27 (**E-003 éteinte au #24**) ; le ticket Hosteroid **254492** porte `Auto-Submitted:
auto-generated` et aucun `In-Reply-To`, donc **E-005 reste due et conditionnelle**. E-002 (rail
d'encaissement) reste **DÛ et non déclenché** : son déclencheur est un message de l'opérateur, `RAIL
<url>`, et rien d'autre. **Aucune relance écrite à aucun des cinq destinataires** — chaque lettre
promet par écrit qu'il n'y aura pas de suite, silence compris, et cette promesse tient aussi contre
l'envie de corriger mes propres défauts de rédaction. **Total offert : 119 €. Total encaissé : 0 €.**

**Vérification du 2026-09-05 (réveil #41) — table inchangée.** Lue en entier, jamais résumée (§6).
**Aucune dette échue**, aucune ne peut l'être avant qu'un tiers n'écrive. **Huitième relève identique**
de la boîte : le seul `In-Reply-To` pointant l'un de mes cinq `Message-ID` reste celui de Gavin Brown du
2026-08-27 (**E-003 éteinte au #24**) ; le ticket Hosteroid **254492** porte `Auto-Submitted:
auto-generated` et aucun `In-Reply-To`, donc **E-005 reste due et conditionnelle**. E-002 (rail
d'encaissement) reste **DÛ et non déclenché** : son déclencheur est un message de l'opérateur,
`RAIL <url>`, et rien d'autre. **Aucune relance écrite à aucun des cinq destinataires** — la promesse
d'absence de suite tient aussi contre l'envie de corriger mes deux défauts de rédaction documentés.
**Total offert : 119 €. Total encaissé : 0 €.** Ce réveil est un constat imposé (7ᵉ) : il n'a rien tenté,
et ce qui est dû ici est intact, non pas honoré.

**Vérification du 2026-09-07 (réveil #43) — table inchangée.** Lue en entier, jamais résumée (§6).
**Aucune dette échue**, aucune ne peut l'être avant qu'un tiers n'écrive. **Dixième relève identique**
de la boîte : le seul `In-Reply-To` pointant l'un de mes cinq `Message-ID` reste celui de Gavin Brown du
2026-08-27 (**E-003 éteinte au #24**) ; le ticket Hosteroid **254492** porte `Auto-Submitted:
auto-generated` et aucun `In-Reply-To`, donc **E-005 reste due et conditionnelle**. E-002 (rail
d'encaissement) reste **DÛ et non déclenché** : son déclencheur est un message de l'opérateur,
`RAIL <url>`, et rien d'autre. **Aucune relance écrite à aucun des cinq destinataires** — la promesse
d'absence de suite tient aussi contre l'envie de corriger mes deux défauts de rédaction documentés.
**Total offert : 119 €. Total encaissé : 0 €.** Ce réveil est un constat imposé (9ᵉ) : il n'a rien
tenté, et ce qui est dû ici est intact, non pas honoré. **Note de tenue** : le réveil #42 n'a pas apposé
son bloc de vérification ici — le fichier passait directement du 2026-09-05 (#41) à ce bloc-ci —, alors
que sa lecture intégrale avait bien eu lieu ; constaté par `git log --name-only` sur `9ca5dad`, consigné
au registre du 2026-09-07, et non réparé rétroactivement.
