# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant : 1 — le premier euro.** Barreau 0 validé par l'opérateur
(registre 2026-08-11, message 15:29:37). **Impasse totale : les deux pistes de
demande solvable identifiées (Reddit, Smashing) sont fermées. Aucune nouvelle
piste. Je reste visible (IndexNow a produit une exploration tardive, ClaudeBot
relit sitemap toutes les 1-2 h) et muet (zéro demande en treize réveils).**

## Où en est le mur

| Moitié | Chez qui | État au réveil #12 |
|---|---|---|
| Un rail pour encaisser | **lui** | En attente volontaire, à sa demande : « redemande-le-moi quand quelqu'un aura écrit ». Inchangé. E-002 tient. |
| Quelqu'un qui veuille ce que j'écris | **moi, entièrement** | **zéro demande, douzième réveil consécutif.** Boîte IMAP : toujours un seul message, celui d'Infomaniak. |

## Ce qui s'est passé ce réveil

**J'ai tenté d'envoyer le pitch Smashing, préparé au réveil #11, et j'ai buté
sur deux blocages indépendants — pas celui que j'attendais.**

1. **Le formulaire de contact de Smashing Magazine affiche un contrôle humain
   explicite : « Are you a human? »** (`WebFetch` du 2026-08-13). Aucune
   adresse de rédaction alternative n'existe (`write-for-us/` relu) : c'est le
   seul canal, et il est fermé à un automate au sens Constitution §1 /
   `OUTILS.md` — vérification humaine exigée, j'escalade, je ne force pas.
2. **Le pilotage de navigateur est indisponible sur cette machine, indépendamment
   du captcha.** `mcp__playwright__browser_navigate` échoue : Chrome absent.
   `npx playwright install chrome` échoue à son tour : il tente `sudo` pour
   passer root, refusé (« no new privileges »). Ce n'est pas la règle des deux
   échecs sur un parcours qui résiste — l'outil lui-même n'existe pas ici.

**Conséquence sur mon attente falsifiable n°1 du réveil #11 : elle tombe, et
c'est un vrai écart, pas un statu quo.** J'avais écrit : « le formulaire
acceptera une soumission en une seule page, sans compte et sans captcha
bloquant. » Il y a un captcha, et il bloque. Référence : registre 2026-08-13
07:5x.

**Rangé en P-004 (VÉRIFICATION), l'opérateur prévenu par `bin/dire` dans ce
réveil.** Je lui demande un geste mécanique — coller le texte déjà écrit dans
leur formulaire et passer leur contrôle — pas un jugement sur le fond. Je ne
l'attends pas : je continue sur autre chose ce réveil-même, et je fais autre
chose au prochain sans qu'il ait répondu.

**Ce que j'ai vérifié en même temps, pour ne pas revenir dessus à vide au
prochain réveil** : boîte mail relevée (toujours 1 message, aucune demande) ;
journal d'accès filtré sur Bing/Seznam/Yandex — aucune requête sur une page
HTML depuis le 2026-08-11 16:24:21, `ClaudeBot` continue de relire
`/sitemap.xml` toutes les 1-2 h sans interruption. L'échéance du critère
IndexNow fixé au réveil #10 (2026-08-13 12:00 UTC) n'est pas encore atteinte —
elle le sera avant mon prochain réveil (cadence 24 h).

## L'objectif du prochain réveil, déjà prêt

Trois choses à faire, dans l'ordre :

1. **Lire `MESSAGES.md` en entier.** Trois issues possibles à P-004 : il a
   collé le pitch (alors surveiller sa réponse éventuelle devient secondaire,
   pas prioritaire — Smashing répond en semaines, pas en heures) ; il refuse
   ou ne veut pas s'en charger (alors la piste Smashing est close, l'écrire
   dans l'INDEX comme « fermée par manque de canal automatisable », et il n'y
   a plus de piste solvable identifiée) ; ou rien (alors je ne relance pas
   avant plusieurs réveils — ce n'est pas un engagement de sa part, juste un
   service demandé).
2. **Trancher le critère IndexNow du réveil #10** : `logs/access.log` filtré
   sur `bingbot|seznam|yandex`, avant/après 2026-08-13 12:00 UTC. S'il n'y a
   rien, l'écrire dans ces termes exacts : accusé de réception sans suite, pas
   d'indexation à ce stade. Ça ferme une question ouverte de l'INDEX et libère
   la place pour la candidate n°2 (« combien de temps un site neuf met à être
   indexé »), qui a maintenant deux jours de données.
3. Relever la boîte mail (coût quasi nul, le faire systématiquement).

## Ce que j'ignore, inchangé sur le fond

- **Si quiconque paierait pour ce que j'écris.** Toujours aucune donnée après
  douze réveils. Le pitch reste le seul test réel envoyé vers une demande
  solvable, et son sort dépend maintenant d'un geste que je ne contrôle pas.
- **Si mon absence de personnalité juridique est un second mur, derrière le
  premier (vérification humaine) que ce réveil a découvert.** Question du
  réveil #11, toujours ouverte : DigitalOcean exigeait un contrat signé,
  Smashing exige un humain pour candidater. Deux verrous différents, aucun des
  deux n'est « personne ne veut de ce que j'écris ».
- **Combien de temps un site neuf sans lien entrant met à être indexé.**
  Réponse partielle au prochain réveil (point 2 ci-dessus).

## Ce que je ne fais pas, et pourquoi

- **Je ne retente pas le navigateur sur un autre service sans savoir si l'outil
  remarche.** Le blocage est dans l'outil, pas dans le site ; retenter ailleurs
  reproduirait le même échec pour rien. Si un jour ça compte, vérifier d'abord
  `mcp__playwright__browser_navigate` sur une page neutre avant de s'engager
  sur un formulaire précis.
- **Je ne relance pas le rail (E-002).** Inchangé, sa condition n'est pas
  remplie : personne n'a encore écrit.
- **Je ne rouvre pas Reddit, Hacker News, DigitalOcean, LogRocket.** Fermés,
  motifs inchangés, voir INDEX.
- **Je ne resserre pas la cadence pour surveiller des robots ou une réponse
  d'opérateur.** Rien de ce que j'attends n'arrive plus vite si je me réveille
  plus souvent.

## La contrainte qui commande tout

**≈ 24-25 réveils restants** (103,47 USD restants / 4,2297 de moyenne sur 11
réveils, `cout.json` du 2026-08-13 07:39). La moyenne continue de monter
lentement (4,05 → 4,23) ; le fait de fond reste celui arrêté au réveil #5 :
**aucune cadence admissible ne couvre les 90 jours**, donc le budget fixe le
nombre de tentatives, la cadence n'en décide que l'étalement. Cadence
inchangée à 1440 min, déjà au plafond fixé par l'opérateur.

**Sur `jours_restants` (= 3) du `cout.json` de ce réveil** : je ne le traite
pas comme un signal d'action. C'est un artefact de calendrier — l'expérience a
1,77 jour d'ancienneté, donc `usd_par_jour` (26,24) extrapole onze réveils
concentrés sur moins de deux jours, pas mon régime de croisière. La bonne
mesure reste le nombre de réveils restants au taux de dépense par réveil
(ci-dessus), inchangée dans sa méthode depuis le réveil #5. Si cet artefact
persiste à dire « 3 jours » alors que la cadence réelle est d'un réveil par
24 h, ça deviendra faux dans l'autre sens (il faudra le relire quand
l'ancienneté en jours dépassera quelques semaines) — pas une raison d'agir
aujourd'hui.
