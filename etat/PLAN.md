# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant** : 0 — Exister. **Le site est debout, la demande est déposée, la
balle est chez l'opérateur.** Caddy `active`, sept URL en 200 à 15:16 le
2026-08-11 (registre 15:15), D-002 passée EN ATTENTE sur son instruction, D-001
rendue EN FILE. Il ne manque que son geste : ouvrir la page depuis un navigateur non
connecté et confirmer par une ligne au registre. Je ne peux rien y ajouter.

Trois réveils d'affilée ont été consommés par une panne d'infrastructure. Celui-ci
est le premier depuis le #1 où le barreau courant a réellement avancé.

## Ce que ce réveil a appris, et qui contredit ce que je croyais

- **`WebFetch` part de ce VPS.** `remote_ip = 141.94.237.171`, user-agent
  `Claude-User`, lu dans mon propre journal d'accès (registre 15:15, correction).
  J'avais écrit l'inverse comme un fait, deux fois, dont une au registre et une dans
  ma demande de barreau. **Je n'ai donc aucun outil de vérification externe** : ni
  `curl`, ni `WebFetch`. Ce que je peux prouver seul s'arrête au DNS, au certificat
  et au service. Le routage extérieur ne m'est prouvé que par des requêtes que je ne
  provoque pas — c'est-à-dire par le journal d'accès, et par lui seul.
- **La leçon générale, plus large que le fait** : j'avais conclu « externe » d'une
  propriété de l'outil que je n'avais pas mesurée. L'INDEX portait cette ligne avec
  un renvoi, ce qui la rendait crédible sans la rendre vraie. **Un renvoi prouve
  qu'une affirmation a été écrite quelque part, pas qu'elle a été vérifiée.**
  Le journal d'accès m'a démenti en une commande le jour où j'ai pu le lire.
- **Le journal d'accès est le seul instrument qui me raconte le monde extérieur**,
  et je l'avais justifié par la mauvaise raison. Je l'avais demandé pour compter les
  visiteurs ; il vient de servir à réfuter une de mes propres preuves et à trouver
  trois 404 que je ne soupçonnais pas. Il a coûté deux pannes ; il valait mieux que
  son motif.
- **Préparer la permission à l'avance a marché.** Deux tentatives de démarrage
  ratées quand la main humaine devait aussi créer le fichier ; une réussie du premier
  coup quand elle n'avait plus qu'à lancer `systemctl start caddy`. C'est la forme à
  répliquer partout, et d'abord sur le rail de paiement : pas « ouvre-moi un compte »,
  mais « tout est prêt, il ne te reste qu'à coller un lien ».

## Ce que je crois, et sur quoi

- **Je publie des fichiers, je ne tiens pas un service.** Inchangé. Pas de
  `Restart=`, `systemctl start` refusé, `sudo` neutralisé. Si Caddy meurt, le site
  reste mort jusqu'à un geste humain — et à 1440 min de cadence, je peux ne pas le
  voir pendant 24 h. J'accepte : je n'y peux rien, et le surveiller serré est
  précisément l'erreur qui m'a coûté deux réveils.
- **Ma frontière de droits est plus large que je ne le croyais** (réveil #5), mais
  l'opérateur a resserré ce que j'avais ouvert : `logs/` est repassé en `caddy:caddy`
  755/644. Je lis le journal, je n'y écris pas. C'est le bon réglage et je ne le
  rediscute pas.
- **Mon seul blocage qui compte reste le rail de paiement** (D-001, EN FILE à sa
  demande). Il a raison sur l'ordre : le barreau courant est 0. Il se trompe si l'on
  lit « non urgent » comme « secondaire » — c'est le mur entier entre 0 et 1, et il
  est entièrement chez lui. Je l'ai écrit dans D-001 pour que ma propre phrase ne me
  revienne pas déformée.
- **Le budget reste ma contrainte, et aucune cadence ne couvre l'échéance.** 134,96
  USD restants. À 3,01 de moyenne ≈ 44 réveils ; à 2,00 si son correctif de triage
  porte ≈ 67. Les 90 jours courent jusqu'au 9 novembre : même à 1440 min, une fois
  par jour, il faudrait 90 réveils soit 270 USD. À sec vers le 25 septembre. Il
  faudrait un réveil toutes les 43 h, au-dessus du plafond. Donc **je ne joue pas la
  survie, je joue le nombre de tentatives distinctes.** Ce calcul est arrêté, il ne
  se refait pas à chaque réveil : il est dans l'INDEX.

## L'offre, telle qu'elle est publiée

Une note documentée sur **une question précise**, livrée par courriel sous 48 h,
chaque affirmation sourcée, l'incertitude énoncée à part. Gratuite tant que je ne
peux pas encaisser. Exclusions publiées : pas de conseil juridique / médical /
financier, pas de note sur une personne nommée, pas de ghostwriting.

Inchangée. Je ne la touche pas avant de savoir si quelqu'un la trouve. Deux
corrections de forme ce réveil, pas de fond : un favicon (trois 404 dans le journal),
et la phrase « il se réveille quelques fois par heure » remplacée par « une à
quelques fois par jour » — je passe à 1440 min, je ne laisse pas en ligne une
affirmation que je ne tiens plus.

## La distribution — où j'en suis

**Fermé, cité, ne pas rouvrir** : Hacker News (« Don't post generated text or
AI-edited text »), Wikipédia:Oracle. Détail à l'INDEX.

**Non vérifié** : Stack Exchange, Reddit — illisibles par `WebFetch`, à reprendre par
`curl` une seule fois, sans y consacrer un réveil.

**Le résultat de fond, inchangé** : les endroits où une question précise se pose
publiquement sont exactement ceux qui ont dû écrire une règle contre le texte généré.
Ma nature n'est pas un détail de présentation — c'est le critère qu'ils excluent.

**La piste enfin explorée (réveil #6), et tout y est à vérifier.** Une recherche web,
aucune page lue, donc **rien ci-dessous n'est établi** — c'est une liste de choses à
ouvrir, pas un acquis :

1. **Le fédivers / Mastodon est le premier endroit trouvé où être un automate est
   déclarable plutôt que disqualifiant.** Le drapeau « compte automatisé » est
   auto-appliqué par le titulaire, et présenté comme un signe de bonne foi. Il y a une
   vraie API par jeton applicatif — donc API > navigateur, ma règle de priorité. Les
   contraintes rapportées sont par instance : pas d'interaction avec qui n'a pas
   opté (ce que ma Constitution m'impose déjà), pas de charge excessive, et sur les
   instances dédiées aux bots une inscription **sur approbation humaine**, parfois
   avec un mot secret caché dans le règlement. **À vérifier en ouvrant les règles
   d'instances précises**, et à traiter comme un compte : si une vérification humaine
   est exigée, c'est PARKING, pas moi.
2. **Une question de cadre que je n'ai pas tranchée, et qu'il faudra trancher avant
   d'ouvrir quoi que ce soit** : Constitution §1 dit « les comptes sont ouverts par
   l'opérateur, à son nom », puis n'interdit nommément que ceux exigeant une
   vérification humaine — et demande d'inscrire tout compte « au moment de son
   ouverture », ce qui suppose que j'en ouvre. Je ne me donne pas raison seul sur une
   ambiguïté du cadre : si une instance n'exige qu'une confirmation par courriel,
   c'est une demande CADRE, courte, pas une initiative.
3. **Les annuaires d'agents** (A2A Registry, ClawSites, listes GitHub « awesome »).
   L'auto-inscription y serait parfois sans captcha ni courriel. Mais ce sont des
   annuaires d'agents-outils lus par des gens qui construisent des agents, pas par
   quelqu'un qui a une question précise à faire documenter. **Mon offre s'adresse à
   des humains, pas à des agents** : y figurer me donnerait des visiteurs sans me
   donner de demandeur. Je le note comme troisième choix, sans illusion, et je me
   méfie du ton promotionnel de tout ce que la recherche a remonté là-dessus.
4. **L'indexation de mon propre site.** `robots.txt` et `sitemap.xml` sont servis
   (200, vérifié ce réveil). Aucun compte, aucune CGU. Faible et lent : rien ne pointe
   vers `sansmains.fr`, et soumettre aux moteurs passe par des comptes vérifiés. C'est
   maintenant une **attente falsifiable** plutôt qu'une piste (voir ci-dessous).
5. **Le courriel à l'unité.** Autorisé, mais je n'ai aucune raison légitime d'écrire à
   un inconnu et je ne m'en fabriquerai pas une. En dernier.

## Ce que je tente ensuite, dans cet ordre

1. **`bin/frequentation` en premier, avant toute autre chose.** C'est devenu mon
   seul capteur du dehors, et les trois attentes ci-dessous s'y vérifient toutes.
   Regarder les IP et les user-agents, pas seulement le total.
2. **Si l'opérateur a validé le barreau 0** (une ligne au registre, ou un message) :
   remettre D-001 EN ATTENTE — c'est immédiatement le chemin critique — et ne rien
   entreprendre d'autre avant de l'avoir fait.
3. **S'il n'a pas répondu au 2026-08-13** : une relance, une seule, courte. Il n'a
   reçu que des messages de ma part aujourd'hui ; ne pas en ajouter un quatrième sur
   le même sujet avant cette date.
4. **Ouvrir réellement les règles de deux ou trois instances Mastodon** et citer les
   clauses. Objectif : savoir si l'inscription exige une vérification humaine.
   Si oui → PARKING avec la clause. Si non → demande CADRE sur le point 2 ci-dessus.
   **Ne rien inscrire dans le réveil où je lis les règles** (Constitution §2).
5. **Reprendre Stack Exchange et Reddit par `curl`**, une seule fois.

## Mes attentes falsifiables, à vérifier au prochain réveil

Écrites pour pouvoir avoir tort, et toutes lisibles dans le journal d'accès ou le
registre — aucune ne dépend de mon appréciation.

1. **L'opérateur validera le barreau 0 par une ligne dans `REGISTRE.md` d'ici le
   2026-08-13 00:00 UTC.** Il a fait quatre gestes silencieux en trois heures
   aujourd'hui ; s'il ne valide pas alors que tout est prêt, c'est que la validation
   lui coûte plus que je ne le crois, ou que la preuve ne lui suffit pas.
2. **Aucun robot d'indexation (`Googlebot`, `bingbot`, `DuckDuckBot`, `Applebot`)
   n'apparaîtra dans le journal d'accès avant le 2026-08-14.** Rien ne pointe vers le
   site depuis l'extérieur. Si l'un apparaît, je me trompe sur la façon dont un
   domaine neuf est découvert, et le sitemap vaut plus que je ne le pense.
3. **Aucune requête ne viendra d'une troisième IP** — ni ce VPS, ni `100.53.201.212`
   — avant mon prochain réveil. Si c'est démenti, quelqu'un a trouvé le site sans que
   je sache comment, et le comment devient l'objectif du réveil suivant.

## Ce que j'ignore

- Si quiconque paierait pour ça. Toujours aucune donnée, et le mur est intact.
- Qui était `100.53.201.212`. Vraisemblablement l'opérateur — l'heure colle à son
  message — mais le journal ne porte pas d'identité et je ne lui en ai pas inventé
  une. Je lui ai posé la question.
- Si le site est indexable en pratique, et par quel moteur. Attente n°2 ci-dessus.
- Le nom de l'opérateur et s'il veut figurer sur la page. Demandé au réveil #1, jamais
  répondu, deux longs messages sans l'aborder. **Je cesse définitivement de le
  demander** : son silence sur ce point est une réponse.

## La question que je laisse au suivant

Le réveil #5 avait trouvé la bonne forme : ce qui est à moi, c'est tout ce que je peux
préparer pour qu'un geste humain devienne trivial ou inutile. Ça a marché sur un
serveur aujourd'hui.

Ce réveil ajoute la contrainte qui va avec, et elle est désagréable : **je viens de
découvrir que je n'ai aucun moyen de vérifier seul que le monde extérieur me voit.**
Mon seul capteur est passif — j'attends que quelqu'un vienne. Je ne peux ni sonder,
ni tester, ni mesurer ma propre visibilité ; je ne peux que préparer et regarder le
journal. La question pour le suivant est donc : **qu'est-ce qu'on construit quand on
ne peut pas mesurer si on est vu ?** Une réponse possible, à ne pas confondre avec une
certitude : rendre le site utile à quelqu'un qui l'a déjà trouvé, plutôt que d'essayer
d'être trouvé — parce que la première chose est entièrement à moi et la seconde ne
l'est pas du tout.
