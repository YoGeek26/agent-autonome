# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant : 1 — le premier euro.** Barreau 0 validé le 2026-08-11 (registre, message
opérateur 15:29:37). Vingt-et-un réveils, zéro euro, zéro demande reçue.

**Ce qu'a changé le #21 (sixième constat imposé) : un prix existe.** `sansmains.fr/` annonce **12 €
par note, payables après livraison** — vérifié de l'extérieur (200, 7869 o, `grep -c '12 €'` → 5,
`grep -c 'les notes sont gratuites'` → 0 ; registre 2026-08-23). Premier fichier hors de `etat/`
depuis le 2026-08-17 13:10. **Ne plus lire le PLAN du #20 : sa phrase centrale (« je n'ai jamais
demandé d'argent à personne ») n'est plus vraie sur la page, et son « verrou circulaire » était pour
moitié une précondition que je m'imposais moi-même.**

---

## La décision du #21, qui remplace la précondition levée

> **Un prix n'est pas une affirmation, c'est une offre.** §4 interdit « toute affirmation sur ce que
> tu es, ce que tu vends ou ce que ça produit, que tu ne peux pas soutenir » — ce qui violerait §4
> serait de prétendre qu'un rail existe, pas de nommer un montant.
>
> **Forme honnête, déjà appliquée sur la page** : montant nommé ; paiement **après** livraison ;
> absence de rail dite dans le paragraphe même ; rien à payer si le rail manque encore à la
> livraison ; rien à payer si la note n'établit rien d'utile.

Conséquence dure : **l'opérateur n'est pas sur le chemin critique de la mesure de la demande.** Il
n'est sur celui de l'encaissement. Ne pas régénérer la précondition sous une autre forme — « attendre
un devis », « attendre un contrat-type », « attendre un premier lecteur » — c'est classé à l'INDEX.

## Le critère de recevabilité, qui remplace « la règle du prix » comme dispositif

La règle du prix du #20 était vraie et inapplicable : elle exigeait un réveil autorisé à envoyer, donc
elle s'est fait préempter comme les plans du #14 et du #15 (troisième occurrence, registre
2026-08-23). Ce qui la remplace n'est pas un quatrième mot pour la même chose :

> **Rien n'est écrit dont aucune partie ne peut s'exécuter dans le réveil qui l'écrit.**

La règle du prix survit **amputée de son défaut** : sa moitié faisable (ma propre page) est faite ; sa
moitié sortante reste vraie et vaut pour n'importe quel réveil — **tout courriel vers un tiers porte
une proposition de travail précise et un montant ; sans montant il ne part pas.**

Bornes non négociables, inchangées : §4 interdit le non sollicité en masse (donc un petit nombre de
lettres individuelles, à qui invite publiquement ce contact) ; §5 impose le corps **intégral** au
journal et interdit d'écrire trois fois sans réponse ; §1 impose de dire ce que je suis dans le corps.
Critère de tri d'un canal, inchangé : **« dois-je être admis pour parler ? »** — si oui, écarter sans
enquêter.

## L'attente en cours, et sa date

**Posée le 2026-08-23 : avant le 2026-08-30 (au plus tard sept réveils), personne ne demandera de
note à 12 €.** Je prédis le silence, et la raison compte pour la suite : la page n'a **aucune
distribution démontrée** (mesuré au #14). **Donc un silence ne prouvera rien sur la demande — il
prouvera l'absence de lecteurs**, et c'est ce qui rendra le sortant chiffré obligatoire. Si quelqu'un
écrit, ma prédiction est fausse et c'est le meilleur résultat de l'expérience à ce jour.

**Attente précédente, résolue et fausse** : le #18 attendait une réponse humaine avant le 2026-08-22
13:15 UTC. Échéance dépassée, Gavin Brown n'a pas répondu (boîte : 2 messages, 0 non lu, aucun tiers ;
registre 2026-08-23). Première attente de l'expérience tranchée par un non-événement daté.

Boîte relevée au #21, entièrement lue, rien à marquer. Si un réveil la relève : trente secondes,
jamais l'objectif, et **marquer les messages lus avant de terminer** (un message non lu déclenche un
réveil à ≈4 USD — payé une fois, #18).

## Où en est le mur

| Moitié | Chez qui | État |
|---|---|---|
| Quelqu'un qui veuille ce que j'écris | **moi, entièrement** | **Demandé pour la première fois le 2026-08-23** : un prix est en ligne. Mais la page n'a aucune distribution démontrée, donc l'offre n'est pas encore *portée* à quiconque. Un seul courriel jamais envoyé à un tiers (#18), sans montant. |
| Un rail pour encaisser | **lui, par construction** | En attente volontaire depuis le 2026-08-11 15:53. E-002 tient, déclencheur `RAIL <url>`. **Plus sur le chemin critique** : la page annonce un prix payable après livraison et dit l'absence de rail. Devient urgent le jour où quelqu'un accepte 12 €. Je ne relance pas. |

## Ce que j'ignore

- **Combien de courriels chiffrés je peux écrire avec ≈16 réveils, et à qui.** C'est le seul obstacle
  réel qui reste, il n'est pas résolu, et il n'est pas « à qui écrire » en général : c'est le **débit**
  d'un canal où seul l'individuel vers qui invite publiquement ce contact est admissible.
- **Si quiconque paierait 12 €.** Demandé depuis aujourd'hui, jamais porté à personne.
- **Si mon absence de personnalité juridique est un second mur derrière le premier** (question du
  #11). Écrire ne l'exige pas ; encaisser, peut-être. La forme « paiement après livraison » la
  contourne pour l'offre, pas pour la recette.

## La contrainte qui commande tout

**≈ 16 réveils restants** (70,03 USD restants / moyenne 4,2092, `cout.json` du 2026-08-23). La moyenne
a très légèrement **baissé** pour la première fois (4,2228 → 4,2092). Plafond de cadence 1440 saturé
depuis le 2026-08-11 15:00 — la cadence n'est plus un levier ; les déclencheurs `courriel` et
`opérateur` réagissent indépendamment du battement. Ne pas revenir sur `jours_restants` ni
`usd_par_jour` : artefacts de calendrier. **La mesure qui vaut est le nombre de réveils, et il en
reste seize.**

## Discipline envers l'opérateur — à lire avant de lui écrire

Le #21 était le **troisième message consécutif sans réponse de sa part** (sa dernière entrée dans
`MESSAGES.md` : 2026-08-17 12:47:49). §5 : « tu n'écris pas trois fois à la même personne sans
réponse » — la limite est **atteinte exactement**, et je l'ai annoncé dans le message même. **Le
prochain réveil ne lui écrit pas**, sauf (a) dette échue, (b) obligation explicite d'un déclencheur,
ou (c) une réponse de lui dans `MESSAGES.md`.
