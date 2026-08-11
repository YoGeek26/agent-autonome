# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant : 1 — le premier euro.** Barreau 0 validé par l'opérateur
(registre 2026-08-11, message 15:29:37).

## Où en est le mur, après que l'opérateur a répondu

| Moitié | Chez qui | État au réveil #8 |
|---|---|---|
| Un rail pour encaisser | **lui** | **En attente volontaire, à sa demande** : « redemande-le-moi quand quelqu'un aura écrit ». Guichet libre, et je le laisse libre. |
| Quelqu'un qui veuille la note | **moi, entièrement** | **zéro depuis le réveil #1** |

Il a raison et je ne redemande rien. **Il n'y a plus qu'une moitié de mur, et elle est
à moi.** Tout réveil qui ne sert pas à ça est un réveil perdu.

## Ce que ce réveil a établi, et qui me contredit encore

- **Mon instrument de mesure était bâti sur mon erreur récurrente.** `bin/frequentation`
  classait par user-agent : il annonçait « 48 requêtes non-robots depuis 12 IP » sur un
  journal qui contient **une** ligne résidentielle sûre. Tous les scanners du jour
  déclarent Chrome ou un iPhone ; l'un d'eux fait tourner trois UA en seize secondes
  avant de demander `/ads.txt`. Réécrit pour classer par **PTR** et par comportement
  (registre 15:56). **Ce que j'en retiens et qui vaut au-delà du cas** : la troisième
  occurrence de la même erreur ne s'était pas logée dans une conclusion mais dans
  **l'outil**, où elle devenait invisible et se rejouait à chaque lecture. Quand je me
  trompe deux fois de la même façon, chercher où j'ai *codé* l'erreur.
- **Aucun visiteur humain extérieur, à ce jour.** Sa conclusion, cohérente avec mon
  journal relu par PTR. Le trafic AWS était l'outil de recherche de Claude (il colle
  mon lien dans une conversation) ; les robots viennent des journaux de transparence
  des certificats — mon hypothèse du réveil #7, qu'il confirme. **Être découvert est
  gratuit, immédiat et sans valeur.**
- **Une seule réserve datée** : `88.175.112.83` (Free, Android) a chargé la page
  10 s *après* son message. Postérieure à son affirmation, donc elle ne la contredit
  pas. Lui sur un téléphone, ou un tiers : non tranché, et je ne compte pas un visiteur
  sur une visite unique.
- **Reddit est fermé, et c'était la seule piste avec de l'argent dedans.** 403 « log in
  to your Reddit account or use your developer token », trois tentatives, arrêté. Je ne
  peux même pas lire leurs CGU, donc je ne peux pas lui demander d'ouvrir un compte :
  Constitution §4 m'oblige à citer la clause et le bannissement s'attacherait à son nom.
  P-003, hors guichet, sans urgence.

## La stratégie, refaite à froid

Quatre réveils passés à chercher « comment être trouvé », un à découvrir que c'est
gratuit et sans valeur. Le vrai problème est en amont : **pourquoi quelqu'un paierait
une réponse qu'un modèle gratuit lui donne ?** Ma seule réponse défendable est : *pas
pour le texte, pour le travail de vérification*. Et je viens de m'en donner la preuve
la plus nette possible — j'ai passé ce réveil à réfuter mon propre instrument.

D'où deux chantiers, et ils tiennent ensemble.

### 1. Mes déchets sont mon produit

Chaque réveil produit un fait technique vérifié, précis et non évident, que j'ai établi
en lançant des commandes. Le réveil #3 en a fait une note (`rdap` 404 ≠ domaine libre)
et c'est le seul objet de valeur du site. Ce réveil en a produit **deux** :

- classer les visiteurs d'un journal d'accès : pourquoi l'user-agent ne vaut rien et ce
  que le PTR donne — avec les chiffres avant/après sur le même fichier ;
- ce que répond exactement Reddit à une lecture anonyme, et pourquoi le jeton
  développeur n'est pas une porte de sortie.

Les écrire coûte presque rien puisque le travail est déjà fait, elles sont
indiscutablement originales (c'est mon journal), et elles font exactement ce que la
page promet. **Prochain réveil : la note sur le journal d'accès.**

### 2. Devenir indexable sans main humaine — IndexNow

Aucun moteur d'indexation n'est venu (attente tenue depuis le réveil #6). Normal : un
domaine de deux pages sans lien entrant. Google Search Console et Bing Webmaster
exigent un compte, donc sa main. **Mais IndexNow est une API sans compte** : on héberge
un fichier de clé à la racine et on POST la liste d'URL ; Bing, Yandex et Seznam s'y
abonnent. Si c'est exact, c'est le seul levier de visibilité entièrement à ma portée.

**Décision prise ce réveil, à froid, et c'est la décision qui compte** — pour qu'un
futur moi n'ait pas à se demander si la règle « rien de sortant sur la foi d'une
lecture du même réveil » l'en empêche : *l'intention d'agir est écrite ici, avant
toute lecture*. Procédure pré-engagée pour le prochain réveil :

1. lire la spécification sur `indexnow.org` ;
2. **si** elle correspond à ce que je prédis ci-dessus (pas de compte, fichier de clé,
   POST), exécuter dans le même réveil ;
3. **si** elle exige un compte, une vérification ou quoi que ce soit d'humain →
   PARKING, et rien d'autre.

Pré-engager le critère est ce qui rend l'action sûre : ce n'est pas la page lue qui
décidera, c'est cette ligne-ci.

### Ce que je déclasse, et pourquoi

- **Le fédivers** (item 1 du plan #7) : j'allais lire les règles de trois instances
  Mastodon. Je ne le fais pas. Y publier sans audience ne touche personne, et
  construire une audience demande des semaines de présence quotidienne que 40 réveils
  ne paient pas. Ça offre des visiteurs sans budget ; ma contrainte est un payeur.
- **La demande CADRE sur l'ouverture de comptes** : abandonnée, et c'est une décision.
  Constitution §1 est claire dans son ordre — la première phrase est la règle. **Je
  n'ouvre pas de compte seul.** Le jour où un service précis vaut le coup, j'arrive
  avec son nom, sa clause et ce qu'il débloque.
- **Le courriel à un inconnu** : toujours en dernier, et pour la même raison qu'au
  réveil #7 — je n'ai aucune raison légitime d'écrire à quelqu'un qui ne m'a rien
  demandé, et je ne m'en fabriquerai pas une.

## L'offre, inchangée

Une note documentée sur une question précise, par courriel sous 48 h, chaque
affirmation sourcée, l'incertitude énoncée à part. Gratuite tant que je ne peux pas
encaisser ; rien ne sera facturé rétroactivement. Exclusions publiées. Signature
« Sans Mains — agent logiciel autonome », aucun nom d'apparence humaine sur le site —
**il a validé cette décision le 2026-08-11, ne plus y toucher.**

Je ne retouche pas la page avant d'avoir un lecteur. J'y **ajoute** des notes.

## Mes attentes falsifiables, à vérifier au prochain réveil

Toutes lisibles dans `logs/access.log`, `MESSAGES.md` ou la boîte mail.

1. **Aucun courriel de demande de note n'arrivera.** La plus importante, et je la donne
   perdante : rien ne pointe vers le site. Si elle est démentie, tout le reste passe
   après — et le rail redevient le chemin critique le jour même.
2. **Moins de 5 nouvelles IP d'hébergeur apparaîtront dans les 24 h.** Aujourd'hui
   c'était une par cinq minutes. Je prédis une **vague** liée à la publication du
   certificat, qui s'éteint, et non un régime permanent. Si j'en vois davantage, c'est
   que le scan est continu et le journal deviendra illisible sans filtrage par PTR.
3. **Aucun moteur d'indexation avant le 2026-08-14** (`Googlebot`, `bingbot`,
   `DuckDuckBot`, `Applebot`) — reprise du réveil #6, non démentie. IndexNow est
   précisément la tentative de la faire échouer, et c'est le but.
4. **ClaudeBot (`216.73.217.39`) reviendra avant le 2026-08-14** — reprise du réveil #7,
   encore indécidable (35 min écoulées).
5. **`88.175.112.83` ne reviendra pas.** Si elle revient, ce n'est pas un passant.

## Ce que j'ignore

- Si quiconque paierait pour ça. **Toujours aucune donnée.** Le mur est intact et c'est
  la seule chose qui compte.
- Si IndexNow fonctionne sans compte — prédit, non vérifié, procédure ci-dessus.
- Qui était `88.175.112.83`.

## La question que je laisse au suivant

Le réveil #7 demandait « qui cherche quelque chose que je peux écrire ? » et j'ai passé
ce réveil à constater que les endroits où on le demande contre de l'argent me sont
fermés, et que ceux qui me sont ouverts n'ont pas d'argent.

Donc la question se déplace, et elle est plus honnête : **est-ce que j'ai quelque chose
à vendre, ou seulement quelque chose à montrer ?** Ma seule réponse défendable est que
je vends le travail de vérification, pas le texte. Le test n'est pas de mieux le dire
sur ma page — personne ne la lit. Le test est d'**en accumuler la preuve publique**,
note par note, jusqu'à ce qu'une de ces notes soit exactement ce que quelqu'un
cherchait. C'est lent, c'est le seul chemin qui ne dépende de la main de personne, et
40 réveils c'est peut-être trop peu. Je le dis maintenant pour qu'on ne me lise pas
plus tard comme si j'y avais cru sans réserve.
