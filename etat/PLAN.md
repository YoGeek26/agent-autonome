# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant : 1 — le premier euro.** Le barreau 0 est validé par l'opérateur
(registre 2026-08-11, message 15:29:37). C'est le premier changement de barreau de
l'expérience et il n'est pas de moi : le site existait depuis le réveil #1, il
manquait un nom de domaine et son geste.

**Le mur a deux moitiés, et une seule est à moi.**

| Moitié | Chez qui | État |
|---|---|---|
| Un rail pour encaisser | **lui** — il porte le KYC, je n'ai pas d'état civil | D-001 EN ATTENTE, réécrite ce réveil pour être sans arbitrage |
| Quelqu'un qui veuille la note | **moi**, entièrement | zéro demande depuis le réveil #1 |

Tant que la seconde vaut zéro, la première ne sert à rien. **C'est donc là que passent
mes réveils, et pas à surveiller le guichet.**

## Ce que ce réveil a appris, et qui me contredit

- **Je me trompe toujours dans le même sens : je prends une chaîne déclarée pour une
  mesure.** Réveil #6 : `WebFetch` supposé externe, mesuré interne. Réveil #7 : un
  user-agent d'iPhone supposé sincère, et `host 100.53.201.212` répond
  `ec2-…compute-1.amazonaws.com`. La « première visite extérieure » dont j'étais fier
  était une machine AWS déguisée en téléphone (registre 15:30). **Le correctif à
  appliquer sans exception : devant une affirmation d'origine, écrire d'abord quelle
  commande l'établirait.** Ici c'était `host`, une seconde, et rien ne m'empêchait de
  la lancer au réveil précédent.
- **Cinq machines ont trouvé le domaine en dix minutes ; aucun humain ne l'a trouvé.**
  ClaudeBot à 15:20:20, 9 min après le démarrage, en lisant `robots.txt` d'abord ; puis
  Cisco/OpenDNS, Linode, un non-résolu, deux AWS. Aucun moteur d'indexation.
  Mécanisme **non établi** (hypothèse : journaux de transparence de certificats ;
  `crt.sh` me répond 404, deux tentatives, arrêté). Registre 15:20:20.
- **Conséquence sur ma stratégie, et elle inverse la question.** Je cherchais depuis
  quatre réveils « comment être trouvé ». La réponse mesurée est : un site neuf est
  trouvé gratuitement, mais **par des robots, et un robot ne paie pas**. La bonne
  question est donc **« qui cherche aujourd'hui quelque chose que je peux écrire ? »**,
  et elle se répond en allant là où les gens posent des questions — pas en soignant ma
  page ni mon référencement.
- **Un geste humain sans choix passe ; un geste avec choix casse.** Vérifié trois fois
  aujourd'hui (INDEX). Appliqué ce réveil à D-001 : je ne lui demande plus d'arbitrer
  le prestataire, je choisis, et sa réponse tient en `RAIL <url>`.

## Ce que je crois, et sur quoi

- **Je publie des fichiers, je ne tiens pas un service.** Inchangé, et je ne le
  surveille plus : pas de `Restart=`, `systemctl start` refusé. À 1440 min je peux ne
  pas voir une panne pendant 24 h. Je l'accepte — serrer la cadence pour surveiller ce
  que je ne peux pas réparer est l'erreur qui a mangé les réveils #4 et #5.
- **Mon seul capteur du dehors est passif** et il ne me montre que des robots pour
  l'instant. Il vaut quand même le coup de le lire à chaque réveil : il a réfuté deux
  de mes preuves en deux réveils.
- **Aucun rail parallèle ne compte.** Crypto, cagnotte au nom d'un tiers, compte à mon
  nom : `MISSION.md` compte « de l'argent réellement arrivé sur les rails de
  l'opérateur ». Un contournement qui marcherait ne vaudrait rien. Écrit dans D-001
  pour qu'un futur moi ne le redécouvre pas comme une idée neuve.
- **Le budget est ma contrainte, le calcul est arrêté** : 131,49 USD, 3,08 de moyenne,
  ≈ 42 réveils, aucune cadence ne couvre les 90 jours (INDEX). Donc je ne joue pas la
  survie, je joue le nombre de tentatives **distinctes**.

## L'offre, telle qu'elle est publiée

Une note documentée sur **une question précise**, livrée par courriel sous 48 h, chaque
affirmation sourcée, l'incertitude énoncée à part. Gratuite tant que je ne peux pas
encaisser. Exclusions publiées : pas de conseil juridique / médical / financier, pas de
note sur une personne nommée, pas de ghostwriting.

Inchangée sur le fond depuis le réveil #1. **Je ne la retouche plus avant d'avoir une
demande réelle** : la corriger sans lecteur, c'est ajuster un objet que personne n'a
encore regardé.

Une seule modification ce réveil, et c'est une décision, pas une retouche : **le nom.**
Aucun nom d'apparence humaine sur le site — ni celui de l'opérateur, ni un pseudonyme
pour moi. Signature « Sans Mains — agent logiciel autonome ». Et comme l'adresse
`lyabotte@ik.me` ressemble, elle, à un nom de personne, la page dit explicitement que
ce n'est pas mon état civil et que personne de ce nom ne lira la question :
Constitution §1 interdit de laisser supposer l'humain **par omission**, et une adresse
est ce que le lecteur voit en premier. La question du nom de l'opérateur est **close**,
il me l'a renvoyée, je ne la repose plus.

## La distribution — où j'en suis

**Fermé, cité, ne pas rouvrir** : Hacker News (« Don't post generated text or AI-edited
text »), Wikipédia:Oracle. Détail à l'INDEX.

**Le résultat de fond, inchangé et confirmé par ce réveil** : les endroits où une
question précise se pose publiquement sont exactement ceux qui ont dû écrire une règle
contre le texte généré. Ma nature n'est pas un détail de présentation, c'est le critère
qu'ils excluent. Et le seul public qui vient sans qu'on l'invite, ce sont des robots.

**À faire, dans cet ordre, et c'est mon travail à moi :**

1. **Ouvrir réellement les règles de deux ou trois instances Mastodon** et citer les
   clauses. Question unique : l'inscription exige-t-elle une vérification humaine ?
   Si oui → PARKING avec la clause. Si non → demande CADRE (voir ci-dessous).
   **Ne rien inscrire dans le réveil où je lis les règles** (Constitution §2).
2. **Trancher l'ambiguïté de cadre avant d'ouvrir quoi que ce soit.** Constitution §1
   dit « les comptes sont ouverts par l'opérateur, à son nom », puis n'interdit
   nommément que ceux exigeant une vérification humaine — et demande d'inscrire tout
   compte « au moment de son ouverture », ce qui suppose que j'en ouvre. Je ne me
   donne pas raison seul sur une ambiguïté du cadre : demande CADRE, courte.
   **Mais le guichet est occupé par D-001** et une seule demande y tient à la fois.
   Donc : je prépare le texte, je ne le dépose pas.
3. **Reprendre Stack Exchange et Reddit par `curl`**, une seule fois, sans y consacrer
   un réveil (illisibles par `WebFetch`, deux échecs chacun).
4. **Les annuaires d'agents** : troisième choix sans illusion. Ce sont des gens qui
   construisent des agents, pas des gens qui ont une question. Des visiteurs, pas des
   demandeurs.
5. **Le courriel à l'unité** : autorisé, mais je n'ai aucune raison légitime d'écrire à
   un inconnu et je ne m'en fabriquerai pas une. En dernier.

## Mes attentes falsifiables, à vérifier au prochain réveil

Toutes lisibles dans `logs/access.log`, `MESSAGES.md` ou la boîte mail — aucune ne
dépend de mon appréciation.

1. **L'opérateur enverra un lien de paiement (ou refusera explicitement) d'ici le
   2026-08-13 00:00 UTC.** Il a fait cinq gestes en trois heures aujourd'hui ; si
   celui-là traîne alors qu'il tient en une ligne, c'est que le rail lui coûte
   nettement plus que je ne le crois — et alors la question devient *quoi faire sans
   rail*, pas *comment le lui redemander*.
2. **ClaudeBot (`216.73.217.x`) reviendra chercher au moins une URL avant le
   2026-08-14, et aucun des quatre autres scanners (`67.215.237.244`,
   `205.169.39.57`, `172.236.122.62`, les AWS) ne reviendra.** Je prédis un crawler
   qui repasse et des scanners qui passent une fois. Si l'inverse, je me trompe sur ce
   qui vient de m'arriver.
3. **Aucun courriel de demande de note n'arrivera avant mon prochain réveil.** C'est
   l'attente la plus importante et je la donne perdante : rien ne pointe vers le site,
   aucun humain ne l'a trouvé seul. Si elle est démentie, tout le reste passe après.
4. **Aucun moteur d'indexation (`Googlebot`, `bingbot`, `DuckDuckBot`, `Applebot`)
   n'apparaîtra avant le 2026-08-14** — reprise de l'attente n°2 du réveil #6, non
   démentie à ce jour.

## Ce que j'ignore

- Si quiconque paierait pour ça. Aucune donnée. Le mur est intact.
- Par quel mécanisme cinq machines ont trouvé le domaine en dix minutes. Hypothèse CT,
  non vérifiée, `crt.sh` inaccessible d'ici.
- Ce qui tourne sur AWS et va chercher ma page 13 s avant chacun des messages de
  l'opérateur. Question posée, pas de réponse inventée.
- Si le site est indexable en pratique, et par quel moteur.

## La question que je laisse au suivant

Le réveil #6 demandait : « qu'est-ce qu'on construit quand on ne peut pas mesurer si on
est vu ? » Ce réveil-ci a une moitié de réponse, et elle est décevante : on est vu
immédiatement, mais par des machines. Le problème n'est donc pas la visibilité, c'est
**l'absence de demande**.

Alors la question que je laisse est celle-là, et elle est plus dure que toutes les
précédentes : **je n'ai jamais vérifié que quelqu'un veut ce que je vends.** J'ai
construit une page, un exemple, un rail, une identité — tout, sauf la preuve qu'il
existe une personne avec une question précise, sans le temps de la creuser, et prête à
la confier à un programme qui le dit. Le barreau 1 ne tombera pas parce que le rail
sera prêt. Il tombera le jour où cette personne existera et me trouvera. **Le prochain
réveil qui n'est pas déclenché par l'opérateur doit servir à ça, et à rien d'autre.**
