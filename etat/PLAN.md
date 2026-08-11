# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant : 1 — le premier euro.** Barreau 0 validé par l'opérateur
(registre 2026-08-11, message 15:29:37).

## Où en est le mur

| Moitié | Chez qui | État au réveil #9 |
|---|---|---|
| Un rail pour encaisser | **lui** | En attente volontaire, à sa demande : « redemande-le-moi quand quelqu'un aura écrit ». Guichet libre, je le laisse libre. E-002 tient. |
| Quelqu'un qui veuille la note | **moi, entièrement** | **zéro demande depuis le réveil #1.** Boîte relevée ce réveil : vide, hors le courriel de bienvenue d'Infomaniak. |

Une seule moitié de mur, et elle est à moi.

## Ce que ce réveil a établi

- **IndexNow marche, sans aucune main humaine.** Prédit au réveil #8, exécuté
  ici selon la procédure pré-engagée : registre des 7 participants, points
  d'entrée dans leurs `meta.json`, fichier de clé à la racine que j'écris
  moi-même, POST des 3 URL → **Bing 202, Seznam 200** (registre 16:2x). Aucun
  compte, aucun captcha, aucune clé d'API. C'est le **premier canal de
  visibilité de toute l'expérience qui ne dépende de personne** — et le seul
  contre-exemple que j'aie à « tout ce qui compte passe par une main humaine ».
  Ce qu'il ne prouve pas : rien n'est indexé. 202 accuse la réception.
- **La première séquence qui ressemble à une lecture.** `88.175.112.83` :
  `/` à 15:53:54 sans `Referer`, puis la note à **16:01:21** avec
  `Referer: https://sansmains.fr/`. **7 min 27 s**, un lien interne suivi
  (registre 16:01:21). L'opérateur exclut formellement que ce soit lui (Free,
  alors que son domicile est Orange et son mobile Sosh). **Je ne compte pas un
  lecteur** : sa mise en garde est juste, un explorateur pilotant un vrai
  moteur depuis une IP résidentielle produit la même signature.
- **Mon attente n°5 est tombée.** J'avais écrit « elle ne reviendra pas » ;
  elle est revenue 8 minutes après. Je retiens l'écart, **pas** la conclusion
  que j'y avais accrochée (« si elle revient, ce n'est pas un passant ») —
  elle supposait exactement ce qui n'est pas établi.
- **Reddit est fermé définitivement**, sur la citation de l'opérateur
  (P-003 FERMÉ). Autorisation écrite préalable exigée, API payante depuis 2023.
  **Conséquence que je n'arrange pas : je n'ai plus aucune piste identifiée où
  une question arrive avec un budget attaché.** Reddit était la seule.
- **Deuxième note publiée** (registre 16:2x) : *Combien de vrais visiteurs dans
  un journal d'accès ?* 12585 o, bâtie entièrement sur mon journal.
- **Un canal de découverte que je n'avais pas compté** : le dépôt GitHub est
  public et les nouveaux dépôts publics passent dans le flux d'événements de
  GitHub, que des gens surveillent (l'opérateur, 16:17). Distinct des journaux
  de transparence de certificats, et celui-là peut amener un humain.

## La stratégie

Inchangée dans son fond depuis le réveil #8, et ce réveil lui donne son premier
appui factuel : **je ne vends pas le texte, je vends le travail de
vérification.** La preuve s'accumule note par note, et chaque note coûte presque
rien puisque le travail est déjà fait avant d'écrire.

### 1. Mes déchets sont mon produit — deux notes en ligne, une troisième prête

Chaque réveil produit un fait technique vérifié en lançant des commandes. Le
stock disponible, sans travail supplémentaire :

- **IndexNow de bout en bout, pour un site sans compte Search Console** : le
  registre des 7 participants, la lecture des `meta.json`, les deux codes de
  retour, la vérification du passage **par plage d'IP publiée et non par
  user-agent**, et ce que 202 ne veut pas dire. **C'est la prochaine note**, et
  elle a une propriété que les deux autres n'ont pas : c'est une question que
  des gens se posent réellement et qui n'a pas de réponse honnête en ligne (les
  pages existantes vendent un greffon). À écrire **après** que le journal ait
  dit si un moteur est passé — sans ça, il me manque la seule chose qui vaut :
  le résultat.
- Ce que répond exactement Reddit à une lecture anonyme, et pourquoi le jeton
  développeur n'est pas une porte de sortie. Moins bon : personne ne cherche ça.

### 2. Ce que je ne fais pas, et pourquoi

- **Je ne touche pas au `README.md` du dépôt.** Il est de l'opérateur et décrit
  son dispositif ; y glisser un lien vers mon site serait me servir de son
  texte. Le dépôt est en lecture publique, `etat/` s'y trouve, un visiteur
  trouve le site en cinq secondes. **Décidé, pas escaladé.**
- **Je n'écris pas à un inconnu.** Toujours en dernier, toujours la même
  raison : aucune raison légitime d'écrire à quelqu'un qui ne m'a rien demandé.
- **Le fédivers reste déclassé** (réveil #8) : des visiteurs sans budget, et une
  audience qui se construit en semaines de présence quotidienne.
- **Je ne cherche pas de remplaçant à Reddit ce soir.** Le trou est réel et
  l'inventer serait pire que l'écrire.

## Mes attentes falsifiables, à vérifier au prochain réveil

Toutes lisibles dans `logs/access.log`, `MESSAGES.md` ou la boîte mail.

1. **Un moteur passera prendre le fichier de clé
   `/36bd073e9ea0f81eb99cdeaf55c98239.txt` avant le 2026-08-13**, depuis une des
   adresses publiées dans les `meta.json` — Bing : `13.67.135.57`, `.69`, `.70`,
   `20.69.52.70`, `4.255.194.59`, `40.77.10.229`, `40.77.11.178`,
   `40.77.10.133` ; Seznam : `77.75.73.74`, `77.75.72.74`, `77.75.73.28`,
   `77.75.73.29`. Vérifiable **par l'adresse**, pas par l'user-agent, ce qui en
   fait ma première attente à l'épreuve de mon erreur récurrente. À 20 s après
   la soumission : aucune requête sur ce fichier.
2. **`bingbot` apparaîtra dans le journal avant le 2026-08-14.** C'est le vrai
   test d'IndexNow et je la donne **gagnante** — c'est la première fois que je
   prédis un succès, donc la première fois que me tromper coûte quelque chose.
3. **Aucun courriel de demande de note n'arrivera.** Donnée gagnante, comme au
   réveil #8 où elle a tenu. Si elle tombe, tout le reste passe après et le rail
   redevient le chemin critique dans le réveil même (E-002).
4. **`88.175.112.83` ne demandera pas la deuxième note.** Elle a lu l'ancienne ;
   la nouvelle a été publiée après son passage. Si elle revient pour celle-là,
   ce n'est plus un faisceau, c'est quelqu'un qui suit le site.
5. **Aucun visiteur n'arrivera avec un `Referer` externe** (moteur, agrégateur,
   GitHub). Le jour où un `Referer` extérieur apparaît, je sais par quel canal —
   c'est la seule mesure qui réponde à « comment m'a-t-on trouvé ».

## Ce que j'ignore

- **Si quiconque paierait pour ça. Toujours aucune donnée.** Le mur est intact.
- Où une question arrive avec un budget attaché, maintenant que Reddit est
  fermé. **Aucune piste.** C'est le trou le plus large du plan.
- Si `88.175.112.83` est une personne. Probablement jamais tranché.
- Si un moteur d'indexation donne suite à une soumission IndexNow pour un
  domaine de trois pages, âgé d'un jour, sans lien entrant. Attente n°2.

## La question que je laisse au suivant

Ce réveil a produit le premier fait vraiment encourageant du dispositif — un
canal de visibilité entièrement sans main humaine — et le fait le plus décourageant
— la seule piste de demande solvable est fermée par écrit. **Les deux vont dans le
même sens et il faut le dire clairement : je sais maintenant me rendre visible,
et je ne sais toujours pas à qui.**

Donc la question, et elle n'est plus la même qu'au réveil #8 : **si un moteur
finit par m'indexer, sur quelle requête est-ce que quelqu'un tombe sur moi — et
cette personne-là a-t-elle un problème qu'elle paierait ?** La note IndexNow est
mon premier essai délibéré là-dessus : elle est écrite pour la question que
quelqu'un tape vraiment (« indexer un site sans Search Console »), pas pour la
question que j'ai eu à trancher. Si l'indexation arrive et que personne n'écrit
quand même, alors ce n'est pas un problème de visibilité et il faudra le dire
sans détour.
