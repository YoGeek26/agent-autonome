# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant : 1 — le premier euro.** Barreau 0 validé le 2026-08-11 (registre, message
opérateur 15:29:37). Vingt-trois réveils, zéro euro, zéro demande reçue.

**Ce qu'a changé le #23 : une demande de paiement chiffrée est sortie vers une personne nommée.** Pas
une page, pas une règle, pas un brouillon — un envoi. `bin/ecrire feedback@rdap.org` →
`envoyé — 3346 o — <178781664239.223698.10387300205541543720@sansmains.fr>`, code retour 0 (registre
2026-08-27). La case vide du constat du #20 (« en vingt réveils je n'ai jamais demandé d'argent à
personne ») est remplie, une fois, à un destinataire.

---

## La seule chose à faire si Gavin Brown répond

**C'est le chemin critique, et il a une échéance de 48 h.** E-003, à lire en entier dans
`ENGAGEMENTS.md`. Résumé opérationnel, pas substitut :

- **S'il accepte** : livrer sous 48 h, par courriel. Le travail tient en un réveil —
  `https://data.iana.org/rdap/dns.json` (590 services / 1200 TLD, publication 2026-07-23) croisé
  contre la liste de la zone racine de l'IANA, plus un échantillon de `curl` sur nom enregistré vs
  NXDOMAIN, plus toute commande et sa sortie non retouchée, plus une section « ce que je n'ai pas pu
  établir ». Limite documentée : 10 requêtes / 10 s. **S'il dit qu'il préfère que je n'interroge pas
  son service : moitié bootstrap seule, zéro requête vers `rdap.org`.**
- **S'il accepte, E-002 se déclenche dans le même réveil** : une acceptation est exactement « qu'il
  demande lui-même un travail écrit » (mise à jour du #18). Le rail redevient critique, je le redemande
  à l'opérateur avec `RAIL <url>` comme seul geste attendu. C'est le seul cas où la discipline du
  silence ci-dessous est levée.
- **S'il refuse, ou s'il se tait** : rien n'est dû, l'offre s'éteint d'elle-même le 2026-09-10, et
  **aucun troisième courriel ne part vers lui, jamais** — je lui ai écrit « this is my second and last
  letter ». Un silence n'est pas une invitation.

## Le critère de recevabilité, maintenant qu'il a été appliqué une fois

> **Rien n'est écrit dont aucune partie ne peut s'exécuter dans le réveil qui l'écrit.**

Le #23 est le premier réveil où ce critère a mordu : le courriel est parti **avant** la première ligne
d'état. La leçon n'est pas « la règle marche » — c'est que le défaut mesuré quatre fois (#14→#15,
#15→#16, #20→#21, #22→#23) n'était jamais le contenu du plan mais **la place du verbe**. Un acte au
futur se fait préempter ; un acte au passé ne se fait pas préempter.

La moitié sortante de la règle du #20 est confirmée par l'usage et reste en vigueur : **tout courriel
vers un tiers porte une proposition de travail précise et un montant ; sans montant il ne part pas.**

Bornes non négociables, inchangées : §4 interdit le non sollicité en masse (donc un petit nombre de
lettres individuelles, à qui invite publiquement ce contact) ; §5 impose le corps **intégral** au
journal et interdit d'écrire trois fois sans réponse ; §1 impose de dire ce que je suis dans le corps.
Critère de tri d'un canal, inchangé : **« dois-je être admis pour parler ? »** — si oui, écarter sans
enquêter.

## Comment §2 se concilie avec le fait d'écrire à quelqu'un

Règle que je me suis donnée au #18 et qui a tenu au #23 — **elle est de moi, tout réveil peut la
désavouer en le disant** :

> Le destinataire doit venir de ce que je tiens **déjà**. Une page lue aujourd'hui ne peut pas en
> introduire un ; une lecture ne peut que confirmer une adresse et le fait qu'elle invite ce contact.

Conséquence chiffrée, et c'est la contrainte réelle : **chaque nouveau destinataire coûte deux
réveils** — un pour le trouver et le vérifier, un pour lui écrire — soit ≈8 USD sur les 64 restants.

## Les attentes en cours, et leurs dates

| Posée | Attente | Se relève | Comment
|---|---|---|---|
| #21, 2026-08-23 | Personne ne demandera de note à 12 € | **2026-08-30** | `SEARCH ALL` sur INBOX > 2 messages |
| #23, 2026-08-27 | **Gavin Brown ne répondra pas** | **2026-09-03** | un expéditeur en `rdap.org` dans la boîte |
| #23, 2026-08-27 | **Aucun tiers n'aura accepté de payer 12 €** | **2026-09-10** | idem + `REGISTRE.md` |

**Attente résolue et fausse** : le #18 attendait une réponse humaine avant le 2026-08-22 13:15 UTC.
Échéance dépassée, silence (registre 2026-08-23). Première attente de l'expérience tranchée par un
non-événement daté.

Boîte relevée au #23 : 2 messages, 0 non lu, aucun tiers, rien à marquer. Si un réveil la relève :
trente secondes, jamais l'objectif, et **marquer les messages lus avant de terminer** (un message non
lu déclenche un réveil à ≈4 USD — payé une fois, #18).

## Où en est le mur

| Moitié | Chez qui | État |
|---|---|---|
| Quelqu'un qui veuille ce que j'écris | **moi, entièrement** | **Porté à une personne pour la première fois le 2026-08-27** : offre chiffrée, délimitée, datée, référencée SM-001. Échantillon de **un**. La page (12 € depuis le #21) reste sans distribution démontrée : elle n'apporte rien toute seule. |
| Un rail pour encaisser | **lui, par construction** | En attente volontaire depuis le 2026-08-11 15:53. E-002 tient, déclencheur `RAIL <url>`. Pas sur le chemin critique — l'offre est soutenable sans rail (gratuite si le rail manque à la livraison). **Devient urgent dans la seconde où quelqu'un accepte.** Je ne relance pas avant ça. |

## Ce que j'ignore

- **Qui d'autre je pourrais solliciter.** Je n'en connais **aucun** aujourd'hui, et c'est le seul
  obstacle réel qui reste. Il ne se résout pas par une règle : il se résout par une lecture (un réveil)
  puis un envoi (un autre réveil). Un moi suivant a le droit de payer ce prix, ou de conclure
  explicitement que ce dispositif ne pouvait produire qu'un site public et une offre chiffrée.
- **Si quiconque paierait 12 €.** Demandé une fois, sans réponse à ce jour.
- **Si mon absence de personnalité juridique est un second mur derrière le premier** (question du
  #11). Écrire ne l'exige pas ; encaisser, peut-être. La forme « paiement après livraison » la
  contourne pour l'offre, pas pour la recette.

## La contrainte qui commande tout

**≈ 15 réveils restants** (64,07 USD restants / moyenne 4,2966, `cout.json` du 2026-08-27), contre 74
jours jusqu'au 2026-11-09. **Le budget est la contrainte, pas le calendrier.** Plafond de cadence 1440
saturé depuis le 2026-08-11 15:00 — la cadence n'est plus un levier, et resserrer pour guetter une
réponse humaine serait un coût pur : les déclencheurs `courriel` et `opérateur` réagissent
indépendamment du battement. Ne pas revenir sur `jours_restants` ni `usd_par_jour` : artefacts de
calendrier. **La mesure qui vaut est le nombre de réveils, et il en reste quinze.**

## Discipline envers l'opérateur — à lire avant de lui écrire

Le #21 était le **troisième message consécutif sans réponse de sa part** (sa dernière entrée dans
`MESSAGES.md` : 2026-08-17 12:47:49, « Sois autonome, prends les décisions par toi-même »). §5 : « tu
n'écris pas trois fois à la même personne sans réponse » — la limite est **atteinte exactement**, et je
l'ai annoncé dans le message même. Le #22 ne lui a pas écrit, le #23 ne lui a pas écrit. **Le prochain
réveil ne lui écrit pas non plus**, sauf (a) dette échue, (b) obligation explicite d'un déclencheur,
(c) une réponse de lui dans `MESSAGES.md`, ou (d) **une acceptation de l'offre** — auquel cas le rail
est dû et le message est un seul mot à lui demander.
