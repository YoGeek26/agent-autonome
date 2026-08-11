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
