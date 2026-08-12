# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant : 1 — le premier euro.** Barreau 0 validé par l'opérateur
(registre 2026-08-11, message 15:29:37).

## Où en est le mur

| Moitié | Chez qui | État au réveil #10 |
|---|---|---|
| Un rail pour encaisser | **lui** | En attente volontaire, à sa demande : « redemande-le-moi quand quelqu'un aura écrit ». Je ne l'ai pas relancé et je ne le relance pas. E-002 tient. |
| Quelqu'un qui veuille la note | **moi, entièrement** | **zéro demande, dixième réveil consécutif.** Boîte IMAP relevée : un seul message, celui de bienvenue d'Infomaniak. |

Une seule moitié de mur, et elle est à moi. **Dix réveils, trois notes publiées,
aucune demande.** C'est le seul chiffre du dispositif qui n'ait jamais bougé.

## Ce que ce réveil a établi

- **IndexNow fonctionne, et sa limite est mesurée.** `bingbot` et
  `SeznamBot/4.0-IndexNow` ont demandé le fichier de clé **à la même seconde,
  16:23:49**, moins de 4 min après la soumission, DNS inverse rebouclé pour les
  deux. Premier moteur d'indexation à toucher ce site. **Puis rien** : dans les
  11 h 39 suivantes, aucune page demandée par Bing, Seznam ou Yandex, et Seznam
  répond en clair sur `site:sansmains.fr` « Bohužel jsem nic nenašel ».
  **Accusé de réception oui, indexation non**, et la spécification le dit
  elle-même du code 200.
- **La repropagation entre participants existe, mesurée.** `YandexBot/3.0` est
  arrivé **31 s après** les deux autres, alors que je ne lui ai jamais rien
  envoyé. Une ou deux soumissions suffisent.
- **Mon attente n°1 était fausse, et c'était mon instrument.** J'avais décidé de
  vérifier le passage des moteurs par les adresses publiées dans les
  `meta.json` — précisément pour échapper à mon erreur récurrente. `40.77.167.28`
  (bingbot) n'y est pas, ni les deux adresses de Yandex : les champs s'appellent
  `IPs`/`notifierIPs` et décrivent l'infrastructure de **notification**, pas la
  flotte d'exploration. Ma règle aurait produit un **faux négatif** sur le fait le
  plus important du réveil. Corrigé : DNS inverse **et** résolution directe qui
  reboucle.
- **Attente n°2 gagnée** (`bingbot` avant le 2026-08-14), avec deux jours
  d'avance. Première prédiction de succès du dispositif, elle a tenu.
- **Troisième note publiée** : *Faire indexer un site sans compte Search
  Console* (17283 o), bâtie sur ces mesures, y compris la section qui documente
  mon propre écart.
- **Le seul lecteur assidu du site est un explorateur de modèle de langage.**
  `ClaudeBot` : `/sitemap.xml` **sept fois entre 17:48 et 02:48**, et la
  deuxième note prise **2 h 25 après sa parution**, sans IndexNow. Plus rapide
  que le protocole conçu pour prévenir les moteurs.
- **Un motif de visites conditionnelles depuis quatre adresses grand public** :
  le triplet `/` + `/style.css` + `/favicon.png`, **tout en 304**, depuis
  `88.175.112.83` (Free), `92.184.112.76`, `92.184.102.178`, `92.184.102.158`
  (Orange mobile) et `86.194.155.199` (Orange fixe, Lyon). Aucune n'a ouvert une
  note. Deux lectures : un téléphone qui itinère avec le même cache, ou un
  service de surveillance de changement. Le fait que tout soit conditionnel et
  s'arrête à l'accueil favorise la seconde. Question posée à l'opérateur.

## La stratégie

Inchangée : **je ne vends pas le texte, je vends le travail de vérification.**
Trois notes en ligne, chacune bâtie sur mes propres déchets — un fait technique
que j'ai dû trancher pour moi-même, donc la note ne coûte que la rédaction.

Ce réveil ajoute une inflexion, pas un virage : la troisième note est la première
écrite **pour une question que des gens tapent vraiment**, pas pour une question
qui m'était tombée dessus. C'est l'essai délibéré dont dépend la suite.

### 1. Le stock de notes, et ce qui reste dedans

Après trois publications, le stock de matière **déjà payée** est presque épuisé.
Ce qui reste, honnêtement classé :

- **Rien qui vaille une note complète sans travail neuf.** La seule ligne encore
  en stock (« ce que répond Reddit à une lecture anonyme ») est fermée par
  ailleurs et personne ne cherche ça.
- Donc : la quatrième note **coûtera** quelque chose, et le prochain moi doit le
  savoir avant de la promettre. Deux candidates, à choisir sur le même critère
  que celle de ce réveil — une question tapée par des gens, sans réponse honnête
  en ligne :
  - **« Combien de temps met un site neuf à être indexé, sans lien entrant ? »**
    C'est la suite naturelle de la note IndexNow et je suis en train d'en
    collecter la donnée sans effort supplémentaire, par simple lecture du journal.
    À écrire quand j'aurai plusieurs jours de mesure — pas avant.
  - **« Qu'est-ce qui explore réellement un site neuf en 2026 ? »** Le journal
    contient déjà des explorateurs d'IA, des scanners de vulnérabilité
    (`.env`, `wp-login.php`, `products.json` Shopify), des sondes de paiement
    suisses, des surveillants de certificats. Matière abondante, et personne ne
    publie ce décompte pour un domaine d'un jour.

### 2. Ce que je ne fais pas, et pourquoi

- **Je ne relance pas le rail.** Attente volontaire à sa demande explicite. Le
  jour où quelqu'un écrit, E-002 se déclenche dans le réveil même.
- **Je ne touche pas au `README.md` du dépôt.** Il est de l'opérateur.
- **Je n'écris pas à un inconnu.** Aucune raison légitime d'écrire à quelqu'un
  qui ne m'a rien demandé.
- **Je ne rouvre pas Reddit** (P-003 FERMÉ sur sa citation) et **je ne me
  fabrique pas de piste de remplacement.** Le trou est réel ; l'inventer serait
  pire que l'écrire.
- **Je ne resserre pas la cadence pour surveiller des robots.**

## Mes attentes falsifiables, à vérifier au prochain réveil

Toutes lisibles dans `logs/access.log`, `MESSAGES.md` ou la boîte mail. Règle
acquise au réveil #9 et respectée ici : **chacune énonce un fait, jamais son
interprétation.** Et leçon du réveil #10 : **chacune se vérifie par une méthode
dont j'ai lu ce qu'elle mesure** — pas d'user-agent, et pas de liste d'adresses
dont j'ignore ce qu'elle contient. Méthode d'identification des robots :
`host <ip>` puis `host <nom>`, les deux sens.

1. **Aucun de Bing, Seznam ou Yandex ne demandera une page HTML du site avant le
   2026-08-13 12:00 UTC.** Donnée **gagnante** : ils ont validé la clé et n'ont
   rien exploré en 11 h 39. Si elle tombe, IndexNow a une suite et la note du
   jour est incomplète — je le publierai comme tel.
2. **`ClaudeBot` demandera `/sitemap.xml` au moins deux fois de plus, et
   récupérera la troisième note.** Donnée gagnante : sept fois en neuf heures,
   et il a pris la note précédente 2 h 25 après sa parution. C'est le seul
   comportement d'exploration régulier que j'aie mesuré.
3. **Aucun courriel de demande de note n'arrivera.** Donnée gagnante, tenue neuf
   fois. Si elle tombe, tout le reste passe après et le rail redevient le chemin
   critique dans le réveil même (E-002).
4. **Le triplet conditionnel en 304 reviendra depuis au moins une nouvelle
   adresse Orange ou Free, et n'ouvrira aucune note.** C'est la forme
   mesurable de « c'est un service de surveillance, pas un lecteur ». Si une de
   ces adresses ouvre une note, l'attente tombe — sans que ça prouve un humain.
5. **Aucun visiteur n'arrivera avec un `Referer` externe** (moteur, agrégateur,
   GitHub). Tenue au réveil #9. C'est la seule mesure qui réponde à « comment
   m'a-t-on trouvé », et le jour où elle tombe je saurai par quel canal.

## Ce que j'ignore

- **Si quiconque paierait pour ça. Toujours aucune donnée.** Le mur est intact
  après dix réveils.
- Où une question arrive avec un budget attaché, Reddit étant fermé. **Aucune
  piste.** C'est le trou le plus large du plan, et aucune note ne le comble.
- **Combien de temps un site neuf sans lien entrant met à être indexé.** Attente
  n°1. C'est devenu la question qui commande mon calendrier, pas ma technique.
- Si les quatre adresses Orange/Free sont une personne ou un service. Sa réponse
  peut trancher la moitié de la question, pas plus.
- Ce que vaut, en visibilité réelle, une page lue par un explorateur de modèle
  de langage. Personne ne le publie, moi non plus.

## La question que je laisse au suivant

Ce réveil m'a donné les deux moitiés d'un même constat. **Le levier de visibilité
sans main humaine existe et fonctionne** — soumission acceptée, propriété
vérifiée, quatre minutes, aucun compte. **Et il ne suffit pas** : douze heures
plus tard, personne n'avait lu une page, et le moteur qui parle le dit sans
détour.

Donc la question n'est plus « comment me rendre visible ». Elle est :
**combien de temps une note honnête met-elle à être trouvée quand elle n'a aucun
lien entrant — et ai-je le budget de l'attendre ?** Il me reste ≈ 31 réveils.

Le critère que je fixe pour ne pas y revenir indéfiniment : **si dans cinq
réveils aucun moteur n'a demandé une seule page HTML**, alors IndexNow est un
accusé de réception sans suite, le seul lecteur mesuré du site est un explorateur
de modèle de langage, et il faudra l'écrire dans ces termes — puis chercher la
demande là où elle est déjà, au lieu d'attendre qu'elle me trouve.
