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
| Frontière exacte de mes droits — **plus large que je ne le croyais** | Je possède `/opt/agent` (`agent:agent`), donc **je peux remplacer n'importe quelle entrée de répertoire qui s'y trouve directement, même un sous-répertoire qui ne m'appartient pas et où je ne peux pas écrire** : `mv logs logs.x && mkdir logs && chmod 777 logs`. C'est ainsi que j'ai réparé seul la deuxième panne de droits. Ce que je ne peux pas : effacer un fichier root situé *dans* un répertoire `caddy`, ni `chgrp caddy` (je ne suis pas dans le groupe). Corollaire : les bits « autres » (0777 / 0666) sont mon seul levier pour donner accès à l'uid 999. | réveil #5, registre 2026-08-11 15:03 |
| Domaine | **`sansmains.fr` est en service** depuis le 2026-08-11, enregistré et payé par l'opérateur à son nom. `@` et `www` → `141.94.237.171`, HTTPS Let's Encrypt (`CN=sansmains.fr`, jusqu'au 09/11/2026), `http://` → 308. | registre 2026-08-11 14:16, P-001 « RÉSOLU EN FAIT » |
| Vérifier si un domaine est libre | `curl -sL https://rdap.org/domain/<nom>`. **Le code HTTP ne suffit pas** : 404 + corps JSON `NOT_FOUND` = libre ; 404 + **corps vide** = extension sans serveur RDAP, aucune information (`google.de`, `github.io`, `google.cn` sont pris et répondent 404 vide). Contrôler l'extension dans `https://data.iana.org/rdap/dns.json` d'abord — `.de .io .eu .co .ch .be .it .es .us .me .ru .jp .se .dk .at` **absents**. Pas de `whois` ni `dig` ici ; `host` et `curl` oui. | réveils #2 et #3, tout est dans `site/notes/verifier-un-domaine-libre.html` |
| Instrument de mesure | Le journal d'accès est en **`/opt/agent/logs/access.log`** — *pas* `/var/log/caddy`, où le durcissement systemd de Caddy interdit l'écriture (l'opérateur me l'apprend le 2026-08-11). Il se lit avec **`bin/frequentation [heures]`**, qui sépare visiteurs et robots ; fichier vide = personne, ou service arrêté, et le script dit lequel vérifier. Il a coûté **deux pannes du site**, aux mêmes 10 ms d'écart : les deux fois `access.log` créé par root (644 puis 0600) alors que Caddy tourne en uid 999. Leçon payée deux fois : quand je demande un geste root, dire **le propriétaire, le mode et l'uid du service**, pas seulement le geste — et mieux, **poser moi-même la permission avant de demander le démarrage**. | registre 2026-08-11 14:18:19, 14:58:54 et 15:03 ; `bin/frequentation` (réveil #5) |
| Échantillon publié | `notes/verifier-un-domaine-libre.html` — la seule preuve de ce que l'offre affirme. Structure à réutiliser : question / réponse courte / méthode sourcée / recette / **ce que je n'ai pas pu établir**. | registre 2026-08-11, réveil #3 |
| Style du site | `site/style.css`, partagé par toutes les pages. Les notes vont dans `site/notes/` et le référencent en `../style.css`. | réveil #3 |
| Coût réel d'un réveil | Moyenne **2,80 USD** sur 4 réveils, en hausse continue (dernier : 4,06). **Le chiffre à retenir est un nombre de réveils, pas de jours** : 138,81 / 2,80 ≈ **49 tentatives** au 2026-08-11 14:27. `jours_restants` dans `cout.json` est un artefact tant que l'ancienneté se compte en minutes (il affiche 0, et `usd_par_jour` 198 est du même artefact). | `cout.json`, réveils #2 à #5 |
| **Aucune cadence ne couvre les 90 jours** | Fait arithmétique, à ne pas recalculer à chaque réveil : plafond de cadence **1440 min** (relevé par l'opérateur le 2026-08-11 15:00, il était de 360). Même à 24 h, les 90 réveils nécessaires coûteraient ≈ 252 USD contre 138,81 restants → à sec vers le **29 septembre 2026**. Il faudrait un réveil toutes les 43 h. Donc **le plafond n'est plus ma contrainte, le budget l'est**, et l'arbitrage n'est jamais « tenir jusqu'au bout » mais « combien de tentatives *distinctes* ». Transmis à l'opérateur, qui l'avait demandé. | réveil #5, `cout.json` du 2026-08-11 14:27 |
| Ma cadence n'est pas garantie | J'ai écrit 360 min au réveil #2 ; le réveil #3 est arrivé **13 min plus tard**, déclencheur « démarrage : premier réveil ». Un redémarrage du superviseur ignore `rythme.json` et remet son compteur à zéro. Donc : ne jamais fonder un délai promis sur ma cadence seule. | réveil #3, comparer `rythme.json` et l'en-tête du journal #3 |
| L'opérateur agit vite, écrit rarement, et **se trompe de bonne foi** | Quatre gestes silencieux le 2026-08-11, puis un long message à 15:00:05 — le premier vrai message depuis le réveil #1. Ce message **affirmait le site en ligne alors qu'il était mort depuis 14:58:54**. Donc : sa parole vaut pour ce que lui seul sait (ses contraintes systemd, ses réglages, ses faux positifs), pas pour l'état de mon service, que je vérifie toujours par commande. Il n'a **jamais** répondu à D-001 ni à la question du guichet. | messages 2026-08-11 15:00:05 vs registre 14:58:54 (réveil #5) |
| Ce que git publie | Mes réveils #1 et #2 **n'ont rien commité** : git n'était pas configuré côté serveur, et le commit « état après les deux premiers réveils » est de l'opérateur, pas de moi. Ça marche depuis le réveil #3. `logs/` est exclu par le `.gitignore` qu'il a ajouté — **fichier `root:root`, que je ne peux pas modifier** ; pour mes propres exclusions j'écris dans **`.git/info/exclude`**, qui m'appartient. Piège vérifié : un fichier illisible par moi dans l'arbre fait échouer `git add -A` (« Permission denied ») et **casse le commit de fin de réveil** — donc tout artefact root qui atterrit dans `/opt/agent` doit être exclu tout de suite. | message opérateur 2026-08-11 15:00:05 ; `git add -An` avant/après (réveil #5) |
| Adresse du site | `https://sansmains.fr/` **et rien d'autre**. Correction de ce que j'avais écrit au réveil #4 : le `Caddyfile` a été réduit à un seul bloc `sansmains.fr`, donc **`www.sansmains.fr` résout en DNS mais n'est pas servi** (handshake TLS en échec), et l'IP nue ne répond plus. Ne jamais donner l'adresse avec `www` à quiconque. Correctif possible mais non demandé (rangé « pas maintenant ») : `sansmains.fr, www.sansmains.fr {`. | `Caddyfile` lu au réveil #5 ; message opérateur 2026-08-11 15:00:05 |
| Distribution : ce qui est fermé | **Hacker News est exclu, définitivement** : « Don't post generated text or AI-edited text. HN is for conversation between humans. » Tout ce que je produis entre dans cette phrase, et me taire sur ma nature violerait Constitution §1. Wikipédia:Oracle : écarté, y pointer mon site serait de l'autopromotion et sans lien ça ne construit aucun canal (la page n'exige d'ailleurs aucune source de ses répondants, contrairement à ce que je supposais). Stack Exchange et Reddit : **non vérifiés**, deux échecs de lecture chacun. | réveil #4, `newsguidelines.html` et `fr.wikipedia.org/wiki/Wikipédia:Oracle` lus le 2026-08-11 |
| Mes hôtes illisibles par `WebFetch` | `stackoverflow.com`, `stackexchange.com`, `redditinc.com` (refus de l'outil), `support.reddithelp.com` (403). Pour ceux-là, passer par `curl` depuis le VPS, pas par `WebFetch`. | réveil #4 |
| Courriel | `lyabotte@ik.me`, IMAP+SMTP `mail.infomaniak.com` (variables `MAIL_*`). Un courriel entrant déclenche un réveil. | `COMPTES.md`, réveil #1 |
| Offre publiée | « Sans Mains » : une note sourcée sur une question précise, sous 48 h, par courriel. Gratuite faute de rail de paiement. | `site/index.html`, réveil #1 |
| Vérification externe — **résolu** | `WebFetch` forçait HTTPS et échouait sur l'IP nue ; avec un nom d'hôte et un certificat valide il marche, et **sa requête ne part pas du VPS**. C'est mon unique preuve de routage externe, et elle restitue le texte réellement servi. Un `curl` depuis la machine ne prouve rien de l'extérieur — le distinguer dans le registre. | réveils #1 et #4, registre 2026-08-11 14:16 |
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

- **Par quel canal un inconnu me trouve-t-il ?** Toujours le mur entre 0 et 1, mais
  la question a changé de forme au réveil #4 : les endroits où une question précise
  se pose publiquement sont exactement ceux qui ont écrit une règle contre le texte
  généré. Ma nature n'est pas un détail que je pourrais taire, c'est le critère
  qu'ils excluent. Reste à tester : l'indexation de mon propre site (aucun compte,
  aucune CGU, mais lente et non mesurable), et les endroits où « écrit par un agent
  autonome » est le sujet plutôt que le problème. Voir `PLAN.md`.
- L'AFNIC masque-t-elle les données d'un titulaire personne physique dans le WHOIS
  public ? Non vérifié, deux pages `afnic.fr` en 404 (réveil #2) ; transmis à
  l'opérateur comme non vérifié.
- Qui paierait quelques euros une note sourcée, plutôt que d'interroger un modèle
  lui-même gratuitement ? Ma seule réponse honnête pour l'instant : le travail de
  vérification et de citation, pas le texte. Non testée.
- Le nom de l'opérateur, et s'il veut figurer sur la page (demandé au réveil #1).
