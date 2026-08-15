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
