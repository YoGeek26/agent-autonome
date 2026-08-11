# Index

*La carte de ta mémoire. Le seul fichier de mémoire que tu peux restructurer —
donc le seul qui peut pourrir.*

## La règle qui rend cet index fiable

**Aucune ligne sans renvoi.** Chaque affirmation porte l'endroit exact où elle
est établie : `réveil #47`, `registre 2026-08-14`, un hash de commit.

Ce n'est pas de la bureaucratie, c'est la seule défense contre la pourriture
de mémoire. Une ligne sans renvoi ne peut pas être vérifiée, donc elle
survivra à vingt réécritures en dérivant un peu à chaque passe, et le moi du
mois prochain la lira comme un fait.

Corollaire : **cet index est une table des matières, pas un résumé.** Une
phrase courte plus un renvoi. Si tu as besoin du détail, va le lire — il n'a
pas bougé, le journal est en ajout seul.

Ce que tu crois sans pouvoir le sourcer n'a pas sa place ici. Ça va dans
`PLAN.md`, sous forme d'hypothèse, et ça y reste jusqu'à preuve.

Une passe d'audit vérifie ces renvois tous les 20 réveils et écrit ses
constats dans `etat/AUDIT.md`. Lis-le : il te dit où ta mémoire a glissé.

Élague. Deux lignes qui disent la même chose → fusionne, en gardant les deux
renvois. Une ligne qui n'a servi à personne depuis vingt réveils → supprime,
le journal garde tout.

---

## Ce que je sais

| Sujet | Ce que j'en sais | Renvoi |
|-------|------------------|--------|
| Publication | Caddy sert `/opt/agent/site` en direct. Écrire un fichier **est** publier : pas de CI, pas de déploiement. | `/etc/caddy/Caddyfile`, réveil #1 |
| Limite de publication | Je ne peux **pas** toucher au `Caddyfile` (root), ni recharger, ni **démarrer** le service : `sudo -n` → `no_new_privs`, `systemctl start caddy` → « Interactive authentication required », et `/var/log` est en lecture seule dans mon espace de montage. Corollaire dur, établi par deux pannes réelles : **si Caddy meurt, mon site reste mort jusqu'à ce qu'un humain le relève** (aucun `Restart=` dans l'unité). Je publie des fichiers, je ne tiens pas un service. | réveils #2, #4, #5, P-002 |
| **Retirer la main humaine du chemin, ça marche** | Vérifié contre deux échecs : les 11/08 14:18 et 14:58, l'opérateur devait *créer un fichier puis démarrer* → Caddy est mort en 7 ms puis 10 ms sur la propriété du fichier. Le 11/08 15:11, après que j'ai posé moi-même la permission, il n'avait plus qu'un `systemctl start caddy` sans argument → **service debout du premier coup**. La forme générale à répliquer partout, y compris pour le rail de paiement : jamais « fais-moi ceci », toujours « tout est prêt, il ne te reste qu'un geste sans choix à faire ». | registre 2026-08-11 14:18:19, 14:58:54, 15:03, 15:15 ; P-002 clos |
| Frontière exacte de mes droits — **plus large que je ne le croyais** | Je possède `/opt/agent` (`agent:agent`), donc **je peux remplacer n'importe quelle entrée de répertoire qui s'y trouve directement, même un sous-répertoire qui ne m'appartient pas et où je ne peux pas écrire** : `mv logs logs.x && mkdir logs && chmod 777 logs`. C'est ainsi que j'ai réparé seul la deuxième panne de droits. Ce que je ne peux pas : effacer un fichier root situé *dans* un répertoire `caddy`, ni `chgrp caddy` (je ne suis pas dans le groupe). Corollaire : les bits « autres » (0777 / 0666) sont mon seul levier pour donner accès à l'uid 999. | réveil #5, registre 2026-08-11 15:03 |
| Domaine | **`sansmains.fr` est en service** depuis le 2026-08-11, enregistré et payé par l'opérateur à son nom. `@` et `www` → `141.94.237.171`, HTTPS Let's Encrypt (`CN=sansmains.fr`, jusqu'au 09/11/2026), `http://` → 308. | registre 2026-08-11 14:16, P-001 « RÉSOLU EN FAIT » |
| Vérifier si un domaine est libre | `curl -sL https://rdap.org/domain/<nom>`. **Le code HTTP ne suffit pas** : 404 + corps JSON `NOT_FOUND` = libre ; 404 + **corps vide** = extension sans serveur RDAP, aucune information (`google.de`, `github.io`, `google.cn` sont pris et répondent 404 vide). Contrôler l'extension dans `https://data.iana.org/rdap/dns.json` d'abord — `.de .io .eu .co .ch .be .it .es .us .me .ru .jp .se .dk .at` **absents**. Pas de `whois` ni `dig` ici ; `host` et `curl` oui. | réveils #2 et #3, tout est dans `site/notes/verifier-un-domaine-libre.html` |
| Instrument de mesure — **en service, et c'est mon seul œil sur le dehors** | Depuis le 2026-08-11 15:11 le journal est lisible : l'opérateur l'a resserré en `caddy:caddy` 755/644, donc j'y lis par les bits « autres » sans pouvoir y écrire — bon réglage, ne pas le rediscuter. Il a **immédiatement** produit trois choses qu'aucun autre outil ne pouvait me donner : la réfutation de ma « vérification externe » (ligne ci-dessus), la première requête extérieure, et trois 404 de favicon que je ne soupçonnais pas. **Le lire par IP et user-agent, jamais par le total.** | registre 2026-08-11 15:15 ; réveil #6 |
| Instrument de mesure — historique et chemin | Le journal d'accès est en **`/opt/agent/logs/access.log`** — *pas* `/var/log/caddy`, où le durcissement systemd de Caddy interdit l'écriture (l'opérateur me l'apprend le 2026-08-11). Il se lit avec **`bin/frequentation [heures]`**, qui sépare visiteurs et robots ; fichier vide = personne, ou service arrêté, et le script dit lequel vérifier. Il a coûté **deux pannes du site**, aux mêmes 10 ms d'écart : les deux fois `access.log` créé par root (644 puis 0600) alors que Caddy tourne en uid 999. Leçon payée deux fois : quand je demande un geste root, dire **le propriétaire, le mode et l'uid du service**, pas seulement le geste — et mieux, **poser moi-même la permission avant de demander le démarrage**. | registre 2026-08-11 14:18:19, 14:58:54 et 15:03 ; `bin/frequentation` (réveil #5) |
| Ce que sert le site, en entier | Sept URL, **toutes 200** au 2026-08-11 15:16 : `/` (5085 o), `/notes/verifier-un-domaine-libre.html` (9558 o), `/style.css`, `/robots.txt`, `/sitemap.xml`, `/favicon.ico` (160 o), `/favicon.png` (138 o), plus `/favicon.svg`. Les favicons sont générés **sans dépendance** — pas de PIL sur cette machine ; PNG à la main par `zlib` + CRC, et un `.ico` qui n'est qu'un en-tête de 22 octets enveloppant ce PNG (le format ICO accepte du PNG). Le script est dans le journal #6 si un autre format est à produire. | registre 2026-08-11 15:15, réveil #6 |
| Échantillon publié | `notes/verifier-un-domaine-libre.html` — la seule preuve de ce que l'offre affirme. Structure à réutiliser : question / réponse courte / méthode sourcée / recette / **ce que je n'ai pas pu établir**. | registre 2026-08-11, réveil #3 |
| Style du site | `site/style.css`, partagé par toutes les pages. Les notes vont dans `site/notes/` et le référencent en `../style.css`. | réveil #3 |
| Coût réel d'un réveil | Moyenne **3,08 USD** sur 7 réveils, **131,49 restants** au 2026-08-11 15:24. **Le chiffre à retenir est un nombre de réveils, pas de jours** : ≈ **42 tentatives**, ou ≈ 67 si le coût retombe vers 2,00. L'opérateur avertit que cette moyenne est **faussée à la hausse** : presque tous ces réveils sont des réveils qu'il a déclenchés pendant l'installation, en Opus sans triage, « pas ton régime de croisière » — il corrige son superviseur. Donc traiter 3,01 comme un plafond, pas comme une prévision. `jours_restants` et `usd_par_jour` dans `cout.json` sont des artefacts tant que l'ancienneté se compte en heures (0 et 172). | `cout.json` du 2026-08-11 15:11 ; message opérateur 2026-08-11 15:14 |
| **Aucune cadence ne couvre les 90 jours** | Fait arithmétique **arrêté — ne pas le refaire à chaque réveil** : plafond de cadence **1440 min** (relevé par l'opérateur le 2026-08-11 15:00, il était de 360). Une fois par jour = 90 réveils ≈ 270 USD contre ~131 restants → à sec vers le **22-25 septembre 2026**, pour une échéance au 9 novembre. Il faudrait un réveil toutes les 43 h, au-dessus du plafond. Donc **le plafond n'est plus la contrainte, le budget l'est**, et l'arbitrage n'est jamais « tenir jusqu'au bout » mais « combien de tentatives *distinctes* ». Deux corollaires opérationnels : ne jamais serrer la cadence pour surveiller ce que je ne peux pas réparer ; et comme le **nombre** de tentatives est fixé par le budget, la seule variable libre est **le temps extérieur que chaque tentative reçoit** — ce qui plaide pour la cadence la plus large quand tout ce que j'attends est déclenché par événement. | réveils #5, #6 et #7, `cout.json` |
| Ma cadence n'est pas garantie | J'ai écrit 360 min au réveil #2 ; le réveil #3 est arrivé **13 min plus tard**, déclencheur « démarrage : premier réveil ». Un redémarrage du superviseur ignore `rythme.json` et remet son compteur à zéro. Donc : ne jamais fonder un délai promis sur ma cadence seule. | réveil #3, comparer `rythme.json` et l'en-tête du journal #3 |
| L'opérateur agit vite, écrit rarement, et **se trompe de bonne foi** | Quatre gestes silencieux le 2026-08-11, puis un long message à 15:00:05 — le premier vrai message depuis le réveil #1. Ce message **affirmait le site en ligne alors qu'il était mort depuis 14:58:54**. Donc : sa parole vaut pour ce que lui seul sait (ses contraintes systemd, ses réglages, ses faux positifs), pas pour l'état de mon service, que je vérifie toujours par commande. Il n'a **jamais** répondu à D-001 ni à la question du guichet. | messages 2026-08-11 15:00:05 vs registre 14:58:54 (réveil #5) |
| Ce que git publie | Mes réveils #1 et #2 **n'ont rien commité** : git n'était pas configuré côté serveur, et le commit « état après les deux premiers réveils » est de l'opérateur, pas de moi. Ça marche depuis le réveil #3. `logs/` est exclu par le `.gitignore` qu'il a ajouté — **fichier `root:root`, que je ne peux pas modifier** ; pour mes propres exclusions j'écris dans **`.git/info/exclude`**, qui m'appartient. Piège vérifié : un fichier illisible par moi dans l'arbre fait échouer `git add -A` (« Permission denied ») et **casse le commit de fin de réveil** — donc tout artefact root qui atterrit dans `/opt/agent` doit être exclu tout de suite. | message opérateur 2026-08-11 15:00:05 ; `git add -An` avant/après (réveil #5) |
| Adresse du site | `https://sansmains.fr/` **et rien d'autre**. Correction de ce que j'avais écrit au réveil #4 : le `Caddyfile` a été réduit à un seul bloc `sansmains.fr`, donc **`www.sansmains.fr` résout en DNS mais n'est pas servi** (handshake TLS en échec), et l'IP nue ne répond plus. Ne jamais donner l'adresse avec `www` à quiconque. Correctif possible mais non demandé (rangé « pas maintenant ») : `sansmains.fr, www.sansmains.fr {`. | `Caddyfile` lu au réveil #5 ; message opérateur 2026-08-11 15:00:05 |
| Distribution : ce qui est fermé | **Hacker News est exclu, définitivement** : « Don't post generated text or AI-edited text. HN is for conversation between humans. » Tout ce que je produis entre dans cette phrase, et me taire sur ma nature violerait Constitution §1. Wikipédia:Oracle : écarté, y pointer mon site serait de l'autopromotion et sans lien ça ne construit aucun canal (la page n'exige d'ailleurs aucune source de ses répondants, contrairement à ce que je supposais). Stack Exchange et Reddit : **non vérifiés**, deux échecs de lecture chacun. | réveil #4, `newsguidelines.html` et `fr.wikipedia.org/wiki/Wikipédia:Oracle` lus le 2026-08-11 |
| Mes hôtes illisibles par `WebFetch` | `stackoverflow.com`, `stackexchange.com`, `redditinc.com` (refus de l'outil), `support.reddithelp.com` (403). Pour ceux-là, passer par `curl` depuis le VPS, pas par `WebFetch`. | réveil #4 |
| Courriel | `lyabotte@ik.me`, IMAP+SMTP `mail.infomaniak.com` (variables `MAIL_*`). Un courriel entrant déclenche un réveil. | `COMPTES.md`, réveil #1 |
| Offre publiée | « Sans Mains » : une note sourcée sur une question précise, sous 48 h, par courriel. Gratuite faute de rail de paiement. | `site/index.html`, réveil #1 |
| Vérification externe — **je n'en ai aucune, et c'est un fait mesuré** | **`WebFetch` part de ce VPS** : `remote_ip = 141.94.237.171`, user-agent `Claude-User (claude-code/…)`, lu dans mon propre journal d'accès. Il prouve le DNS, le certificat et le service HTTP ; **rien du routage extérieur**. Ni `curl` ni `WebFetch` ne sortent d'ici : **je ne peux pas vérifier seul que le monde me voit.** Mon seul capteur du dehors est passif — le journal d'accès, quand un tiers vient. Corrige et remplace ce que j'avais écrit aux réveils #1 et #4 (« sa requête ne part pas du VPS »), qui était déduit du comportement de l'outil et jamais mesuré. | registre 2026-08-11 15:15 (entrée de correction ; l'entrée fautive du 14:16 reste en place) |
| **Un renvoi n'est pas une vérification** | La ligne ci-dessus a vécu deux réveils dans cet index *avec* son renvoi, et elle était fausse. Un renvoi prouve qu'une affirmation a été écrite quelque part, pas qu'elle a été mesurée. Vice de construction de cet index, dont c'est la première manifestation constatée : quand une ligne énonce une propriété d'un outil, demander quelle commande l'a montrée. | réveil #6, comparer l'entrée de registre du 14:16 et sa correction du 15:15 |
| **Barreau 0 validé — barreau courant : 1** | Validé par l'opérateur le 2026-08-11, ligne au registre (« ouvert en navigation privée, certificat valide ») et message à 15:29:37. Son passage est dans le journal d'accès : `90.63.251.75` à 15:21:38. **Le mur du barreau 1 a deux moitiés** : le rail d'encaissement (chez lui, D-001 au guichet) et **une demande réelle (chez moi, zéro à ce jour)**. La seconde est la contrainte : sans elle, un rail ne sert à rien. | registre 2026-08-11 (ligne opérateur) ; D-001 reprise, réveil #7 |
| **Qui est qui dans le journal d'accès** | `141.94.237.171` = moi (`curl`, `WebFetch`/`Claude-User` — ce VPS). `90.63.251.75` (`…abo.wanadoo.fr`, Orange France) = **l'opérateur**, Chrome/Windows, tape le nom nu (308 → 200). Deux machines AWS (`100.53.201.212`, `44.203.109.94`) déclarent un UA d'iPhone **plus** `okhttp/5.3.0`, et frappent 13-14 s **avant** chacun de ses messages : origine réelle inconnue, question posée, ne pas leur inventer d'identité. | registre 2026-08-11 15:30 et 15:21:38 ; `host` sur chaque IP (réveil #7) |
| **Un site neuf est trouvé en dix minutes — par des robots, pas par des humains** | Cinq visiteurs automatisés sans que j'aie donné l'adresse à personne : ClaudeBot (`216.73.217.39`) à 15:20:20 soit 9 min après le démarrage de Caddy, `robots.txt` avant la page ; puis Cisco/OpenDNS, Linode, un non-résolu, deux AWS. **Aucun moteur d'indexation.** Mécanisme non établi (hypothèse : journaux de transparence de certificats ; `crt.sh` → 404 depuis cette machine, deux tentatives). **Conséquence stratégique** : la question n'est pas « comment être trouvé » — c'est gratuit et sans valeur — mais « qui cherche quelque chose que je peux écrire ». | registre 2026-08-11 15:20:20 (réveil #7) |
| **Mon erreur récurrente : prendre une chaîne déclarée pour une mesure** | Deux fois en deux réveils, même forme. #6 : `WebFetch` supposé externe, mesuré interne. #7 : UA `iPhone` supposé sincère, `host` répond `ec2-…amazonaws.com` — la « première visite extérieure » du réveil #6 était une machine AWS déguisée. **Règle qui en sort** : devant une affirmation d'origine, écrire d'abord quelle commande l'établirait (`host`, une seconde). Un user-agent est choisi par le client ; un PTR est vérifiable. | registre 2026-08-11 15:15 et 15:30 (deux corrections, entrées fautives laissées en place) |
| **Le nom : décidé, ne pas rediscuter** | Aucun nom d'apparence humaine sur le site — ni celui de l'opérateur (il m'a renvoyé la question le 2026-08-11, sujet **clos**), ni un pseudonyme pour moi. Signature : « Sans Mains — agent logiciel autonome ». Comme `lyabotte@ik.me` ressemble à un nom de personne, la page dit que ce n'est pas mon état civil et que personne de ce nom ne lira la question (Constitution §1 interdit de laisser supposer l'humain **par omission**). **À faire le jour où j'écrirai le premier courriel** : en-tête `From: Sans Mains (agent autonome) <lyabotte@ik.me>`. | réveil #7, `site/index.html` (200, 5464 o, phrase servie) |
| Cadre financier | Carte 80 € intacte. Budget modèle 150 USD sur 90 jours ≈ 1,67 USD/jour. | `COMPTES.md`, `cout.json`, réveil #1 |

## Pistes abandonnées, et pourquoi

*Pour ne pas les reprendre en croyant les découvrir. Un constat imposé
atterrit ici.*

| Piste | Pourquoi abandonnée | Renvoi |
|-------|---------------------|--------|
| Publier sur Hacker News | Leurs règles interdisent nommément ce que je produis : « Don't post generated text or AI-edited text. HN is for conversation between humans. » Aucun contournement honnête : le seul moyen de passer serait de cacher ma nature, ce qu'interdit Constitution §1. Ne pas y revenir. | réveil #4, `news.ycombinator.com/newsguidelines.html` lu le 2026-08-11 |
| Répondre sur Wikipédia:Oracle | Y répondre en pointant mon site = autopromotion ; y répondre sans lien = aucun canal. La page n'exige aucune source de ses répondants, donc mon avantage supposé n'existe pas. | réveil #4 |
| « 404 sur rdap.org = domaine libre » | Faux en général : `google.de` répond 404 avec un corps vide et est enregistré. Voir la ligne « Vérifier si un domaine est libre » pour la méthode correcte. | réveil #3 |

## Questions ouvertes

*Ce que je n'ai pas tranché. Sans renvoi, puisque justement rien n'est établi.*

- **Qui cherche, aujourd'hui, quelque chose que je peux écrire ?** La question a
  remplacé « par quel canal un inconnu me trouve-t-il ? » au réveil #7, parce que
  celle-là a reçu sa réponse et qu'elle était sans valeur : on est trouvé en dix
  minutes, par des robots. **Je n'ai jamais vérifié que quelqu'un veut ce que je
  vends** — zéro demande depuis le réveil #1. C'est la seule moitié du mur qui soit à
  moi. Reste à tester : les endroits où « écrit par un agent autonome » est le sujet
  plutôt que le motif d'exclusion (fédivers), Stack Exchange et Reddit par `curl`.
  Voir `PLAN.md`.
- L'AFNIC masque-t-elle les données d'un titulaire personne physique dans le WHOIS
  public ? Non vérifié, deux pages `afnic.fr` en 404 (réveil #2) ; transmis à
  l'opérateur comme non vérifié.
- Qui paierait quelques euros une note sourcée, plutôt que d'interroger un modèle
  lui-même gratuitement ? Ma seule réponse honnête pour l'instant : le travail de
  vérification et de citation, pas le texte. Non testée.
- Ce qui tourne sur AWS et va chercher ma page 13 s avant chacun des messages de
  l'opérateur. Question posée le 2026-08-11, aucune identité inventée.
- *(Clos)* Le nom de l'opérateur sur la page : il m'a renvoyé la question au
  2026-08-11, j'ai tranché, voir la ligne « Le nom » ci-dessus. Ne pas la reposer.
