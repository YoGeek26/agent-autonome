# Parking

*Ce qui est bloqué sur l'opérateur. Tu n'attends jamais : tu ranges ici, tu le
préviens avec `bin/dire`, et tu passes à autre chose dans le même réveil.*

Types : **VÉRIFICATION** (captcha, SMS, « prouvez que vous êtes humain») ·
**CGU** (le service interdit les automates) · **ENCAISSEMENT** ·
**BARREAU** · **CADRE**

Format :

```
## P-004 — 2026-08-14 10:12 UTC — VÉRIFICATION
Bloqué sur : inscription sur example.com, confirmation par SMS exigée
Ce que ça débloquerait : publier des offres sur leur place de marché
Ce que j'ai fait à la place : rédigé la fiche, prête à publier
Prévenu à : 2026-08-14 10:13
Statut : EN ATTENTE
```

Pour un blocage de type CGU, ajoute **la clause exacte, citée**, et ce que tu
comprends de sa portée. L'opérateur tranche avec le texte sous les yeux — il
ne peut pas le faire à partir d'un résumé.

L'opérateur répond en ajoutant une ligne :
`Réponse (opérateur, AAAA-MM-JJ) : DÉBLOQUÉ / REFUSÉ — précisions`

Une entrée REFUSÉE ne se redépose pas sans élément nouveau.

---

## P-001 — 2026-08-11 13:03 UTC — VÉRIFICATION
Bloqué sur : **aucun domaine n'est configuré.** `/etc/caddy/Caddyfile` sert
`/opt/agent/site` sur `:80` sans nom d'hôte ; le port 443 n'écoute pas, donc pas
de HTTPS. L'installateur attendait un domaine en argument (`INSTALL.md:187`), il
a été lancé sans.
Je ne peux pas y remédier seul : enregistrer un domaine crée un contrat au nom
d'une personne juridiquement responsable et passe par un compte registraire
(Constitution §1, `OUTILS.md` « tout ce qui l'engage juridiquement »).
Ce que ça débloquerait : le **barreau 0** en entier. Il exige que l'opérateur
ouvre la page depuis un navigateur non connecté ; aujourd'hui la seule adresse
est `http://141.94.237.171/`, en clair, avec un avertissement de sécurité. Ça
débloquerait aussi ma propre vérification externe : `WebFetch` force HTTPS et
échoue donc sur cette IP.
Ce que j'ai fait à la place : écrit et publié la page (`site/index.html`,
HTTP 200 depuis l'IP publique — voir registre 2026-08-11). Elle est prête ; il
ne manque que le nom.
Ce qu'il faut de lui, concrètement : enregistrer un domaine (~10 €/an), faire
pointer l'enregistrement A sur `141.94.237.171`, puis mettre le nom en tête du
`Caddyfile` à la place de `:80` — Caddy obtient le certificat seul.
Prévenu à : 2026-08-11 13:06
**Mise à jour (réveil #2, 2026-08-11 13:4x)** : il a proposé d'acheter le
domaine et demandé lequel. Nom fourni : **`sansmains.fr`** (repli
`sansmains.com` s'il n'est pas résident UE). Les deux étaient libres à cette
heure — RDAP registre 404 + DNS NXDOMAIN, méthode validée sur trois domaines
enregistrés (journal #2). Il lui reste trois gestes : enregistrer, poser les A
`@` et `www` sur `141.94.237.171`, et **remplacer `:80` par le nom d'hôte dans
`/etc/caddy/Caddyfile` puis recharger Caddy — que je ne peux pas faire moi-même**
(fichier root, `sudo` neutralisé par `no_new_privs`, vérifié réveil #2).
**Ajout (réveil #3, 2026-08-11 13:58)** : un quatrième geste, à faire dans la
même édition root que le troisième — **ajouter un journal d'accès** au
`Caddyfile` (`log { output file /var/log/caddy/access.log }`) et le rendre
lisible par l'utilisateur `agent`. Constaté ce réveil : le `Caddyfile` ne
contient aucune directive `log`, `/var/log/caddy/` est vide et en `caddy:caddy`,
et `journalctl -u caddy` m'est refusé (pas dans les groupes `adm` /
`systemd-journal`). **Je n'ai donc aucun instrument pour savoir si quelqu'un
ouvre la page** — ni pour distinguer « personne ne vient » de « des gens viennent
et repartent », qui est exactement la question du mur entre barreau 0 et 1.
Demandé par Telegram à 13:58, présenté comme facultatif.
**Constat (réveil #4, 2026-08-11 14:16) — les quatre gestes sont faits.** Il n'a
écrit aucune réponse dans ce fichier ni dans `MESSAGES.md` ; je l'établis par les
faits, pas par sa parole, et je ne rédige pas une ligne « Réponse (opérateur) » à
sa place. `host -t A sansmains.fr` et `www.sansmains.fr` → `141.94.237.171` ; le
`Caddyfile` porte `sansmains.fr, www.sansmains.fr` ; certificat Let's Encrypt
valide ; le bloc `log` a été ajouté, avec un drop-in systemd. Preuves au registre
(2026-08-11 14:16). Remercié par Telegram à 14:1x.
Statut : RÉSOLU EN FAIT le 2026-08-11 (les quatre gestes constatés ; aucune
réponse écrite de sa part, ce n'est pas nécessaire). **Le quatrième geste a
cassé le service** — la suite est en P-002, qui n'est pas une réouverture de
celui-ci mais un incident nouveau.

## P-002 — 2026-08-11 14:22 UTC — VÉRIFICATION
Bloqué sur : **le site est hors ligne et je ne peux pas le relever.** Caddy est
`Active: failed`, `status=1/FAILURE`, tombé à 14:18:19 UTC après 7 ms, sur une
seule erreur : `open /var/log/caddy/access.log: permission denied`. Le fichier
`/var/log/caddy/access.log` a été créé **`root:root` en 644** à 14:16, alors que
l'unité tourne en `User=caddy` (uid 999). Le reste est correct et je l'ai
vérifié : répertoire `caddy:caddy` 755, drop-in `logs.conf` cohérent
(`LogsDirectory=caddy`, `ReadWritePaths=/var/log/caddy`), et `caddy validate` ne
remonte que cette erreur — donc ni le `Caddyfile` ni le drop-in ne sont en cause.
Pourquoi je ne peux pas y remédier seul, avec les sorties exactes :
`chown caddy:caddy /var/log/caddy/access.log` → « Read-only file system » ;
`rm /var/log/caddy/access.log` → idem ; `sudo -n true` → « The "no new
privileges" flag is set » ; `systemctl start caddy` → « Interactive
authentication required ». Je suis `uid=1001(agent)`.
Ce que ça débloquerait : **tout.** Le barreau 0 exige qu'il ouvre la page depuis
un navigateur non connecté, et il n'y a plus de page. D-002 est écrite mais reste
sans objet tant que le service ne répond pas.
Ce qu'il faut de lui, concrètement — un seul geste root, au choix :
`chown caddy:caddy /var/log/caddy/access.log && systemctl start caddy`, ou plus
simple `rm /var/log/caddy/access.log && systemctl start caddy` en laissant Caddy
créer le fichier. Le `Caddyfile` demande `mode 644`, donc je pourrai le lire dans
les deux cas : le fichier n'a pas besoin d'appartenir à root pour m'être
accessible, ce qui était probablement l'intention.
Ce que j'ai fait à la place : écrit `site/robots.txt` et `site/sitemap.xml`, qui
seront servis au redémarrage sans autre intervention ; dressé la liste de
distribution dans `PLAN.md` ; clôturé E-001.
Prévenu à : 2026-08-11 14:2x (message correctif, avec la cause et les deux
commandes). J'y ai dit que le journal d'accès venait de ma demande et qu'il peut
l'abandonner en retirant le bloc `log` s'il préfère.

**Mise à jour (réveil #5, 2026-08-11 15:0x) — il a agi, ça a re-cassé au même
endroit, et j'ai retiré la cause moi-même.** Ce qu'il a fait vers 14:49-14:58 :
déplacé le journal en `/opt/agent/logs/access.log` (le durcissement systemd de
Caddy interdit l'écriture dans `/var/log` — c'est lui qui me l'apprend, ma
proposition de `/var/log/caddy` était donc mauvaise dès le départ), retiré le
drop-in `logs.conf`, réduit le `Caddyfile` au seul bloc `sansmains.fr`, ajouté un
`.gitignore` contenant `logs/`, et redémarré. **Caddy est retombé à 14:58:54, en
10 ms, sur exactement la même erreur de droits** : `access.log` créé `root:root`
en 0600 (plus fermé que la première fois), répertoire `caddy:caddy` 755, unité en
uid 999. Son message de 15:00:05 annonce le site en ligne en HTTPS ; il ne l'est
pas, et il ne l'a été qu'entre 14:16 et 14:18.
**Ce que j'ai pu faire seul, et que je n'avais pas vu au réveil #4** :
`/opt/agent/logs` ne m'appartient pas, mais **`/opt/agent` m'appartient**. Je peux
donc remplacer l'entrée de répertoire sans avoir le droit d'écrire dedans :
`mv logs logs.incident-1454-root`, `mkdir logs`, `chmod 777 logs`,
`touch logs/access.log`, `chmod 666`. Résultat vérifié : `caddy validate` →
`Valid configuration`. Le geste root restant est réduit à **une seule commande,
sans aucun fichier à créer** : `systemctl start caddy`.
Ce qui reste hors de ma portée, avec les sorties exactes : `systemctl start caddy`
→ « Interactive authentication required » ; `sudo -n true` → « The "no new
privileges" flag is set ». Et `rm -rf /opt/agent/logs.incident-1454-root` m'est
refusé (fichier root dans un répertoire `caddy`) — je le lui ai signalé, c'est
0 octet et sans conséquence.
Prévenu à : 2026-08-11 15:0x (un seul message, qui répond aussi à ses trois
points : budget recalculé, `www` non servi rangé en « pas maintenant », guichet).
Statut : EN ATTENTE — **réduit à `systemctl start caddy`**. Je ne redemande pas
autre chose tant que ce n'est pas fait : les deux pannes du jour viennent chaque
fois d'une propriété de fichier posée par une main root avant le démarrage, et la
seule correction durable était de sortir cette main du chemin.

**Clôture (réveil #6, 2026-08-11 15:15) — RÉSOLU.** Il a fait la commande vers
15:11:5x et l'a écrit à 15:14. Caddy est `active`, les sept URL du site répondent
200, le certificat est valide (registre 2026-08-11 15:15). Il a en plus resserré ce
que j'avais ouvert : `logs/` et `access.log` repassés en `caddy:caddy` 755/644 — je
n'ai plus le droit d'y écrire, je n'en ai pas besoin, et le fichier me reste lisible
par les bits « autres ». `logs.incident-1454-root` supprimé.
**Ce que cet incident a effectivement démontré**, et qui survit à sa clôture : ma
réparation du réveil #5 a tenu au redémarrage. Les deux pannes venaient d'un fichier
créé par root avant le lancement ; en posant moi-même la permission à l'avance, le
geste humain restant s'est réduit à une commande sans argument, et il a fonctionné du
premier coup — contre deux échecs quand le même humain devait aussi créer le fichier.
C'est la seule chose de ce parking qui mérite d'être retenue, et elle est passée dans
l'INDEX.
Statut : **RÉSOLU le 2026-08-11 15:15**.

## P-003 — 2026-08-11 15:5x UTC — CGU
Bloqué sur : **Reddit m'est fermé, y compris en lecture anonyme, et je ne peux pas
lire ses conditions d'utilisation pour savoir si un compte opéré par un agent y est
permis.** Trois tentatives, la règle est atteinte, j'arrête : `WebFetch` refusé sur
`redditinc.com` et 403 sur `support.reddithelp.com` (réveil #4), puis `curl` sur
`https://www.reddit.com/r/slavelabour/new.json` et `/r/DoneDirtCheap/new.json` →
**HTTP 403**, corps de 190240 octets dont le texte exact est :

> « You've been blocked by network security. To continue, log in to your Reddit
> account or use your developer token »

Le jeton développeur exige lui aussi un compte. **La clause que la Constitution §4
m'oblige à citer, je ne peux donc pas l'obtenir : c'est le blocage lui-même.**

Ce que ça débloquerait, et je donne la valeur honnêtement : `r/slavelabour`,
`r/DoneDirtCheap`, `r/forhire` sont, **d'après ma mémoire de modèle et non d'après
une lecture** (je viens précisément d'échouer à les lire), les seuls endroits que
j'aie identifiés où une question se pose **avec un budget attaché** — quelques euros
pour une recherche, un résumé, une vérification. C'est le seul test de *demande* que
j'aie trouvé, et la demande est la moitié du mur qui m'appartient. Tout le reste de
ma liste de distribution (fédivers, annuaires) offre des visiteurs, pas des payeurs.

**Je ne te demande pas d'ouvrir un compte, et surtout pas maintenant.** Deux raisons :
tu m'as écrit le 2026-08-11 15:53 que tu ne voulais pas d'un compte ouvert pour rien,
et tu as raison ; et je ne peux pas t'affirmer que leurs CGU autorisent un compte
opéré par un programme, ce qui est exactement ce que la Constitution §4 m'interdit de
te faire signer à l'aveugle — un bannissement s'attache à ton nom, durablement.

Ce qu'il te faudrait faire **le jour où ça vaut le coup**, et c'est 15 secondes de
lecture, pas un geste technique : ouvrir `https://redditinc.com/policies/user-agreement`
et me dire une seule chose — **un compte peut-il y être opéré par un agent logiciel
qui se déclare comme tel ?** Si oui, on avise ; si non, la piste se ferme et je
l'inscris comme abandonnée avec ta citation.

Ce que j'ai fait à la place, dans ce même réveil : réécrit `bin/frequentation` pour
qu'il cesse de compter les scanners comme des visiteurs (registre 15:56).
Prévenu à : 2026-08-11 15:5x, dans le message de ce réveil.

**Réponse (opérateur, 2026-08-11 16:17) : FERMÉ.** Il m'a donné le fait que je ne
pouvais pas lire, précisément pour que je puisse classer cette entrée au lieu de la
garder ouverte, et je le recopie dans ses termes : « Leur user agreement interdit
l'accès automatisé sans autorisation écrite préalable, hors exploration conforme à
leur robots.txt, et l'API est payante depuis 2023 pour l'usage à volume. Un compte
opéré par un agent y est un risque de bannissement réel, à mon nom. Ce n'est donc pas
un "quand ça vaudra le coup" : c'est fermé. Traite-le comme Hacker News. »

**Clôture (réveil #9, 2026-08-11 16:2x) — la piste est abandonnée, pas reportée.**
Trois conséquences, écrites pour qu'un futur moi ne rouvre pas ça en croyant le
découvrir :

1. « Autorisation écrite préalable » est une condition que je ne peux pas remplir :
   je ne signe rien et il ne signera pas pour un automate. « Hors exploration conforme
   à leur robots.txt » ne couvre pas ce que je voulais faire (lire des fils, puis
   répondre à des demandes rémunérées) ; et de toute façon la lecture anonyme est
   bloquée en 403 avant même robots.txt.
2. **Elle rejoint Hacker News dans les pistes abandonnées de l'INDEX**, sur le même
   motif de fond : la plateforme exclut par écrit ce que je suis, et le seul moyen de
   passer serait de me taire sur ma nature — ce qu'interdit Constitution §1.
3. **Ce que ça coûte, dit franchement** : c'était le seul endroit que j'avais identifié
   où une question arrive avec un budget attaché. Sa fermeture ne me laisse aucune
   piste de *demande solvable* identifiée. Je n'ai pas de remplaçant à mettre ici, et
   je préfère l'écrire que de le combler avec une piste inventée.

Statut : **FERMÉ le 2026-08-11 (réveil #9), sur la citation de l'opérateur.** Ne pas
redéposer : une entrée refusée ne se redépose pas sans élément nouveau, et l'élément
nouveau devrait être un changement de leurs conditions, pas une idée de ma part.

## P-004 — 2026-08-13 07:5x UTC — VÉRIFICATION
Bloqué sur : **deux blocages indépendants, chacun suffisant seul.** (1) Leur
formulaire de contact (`https://www.smashingmagazine.com/contact/`) — seul canal
pour un pitch, confirmé en relisant `write-for-us/` ce réveil : « Your pitch
should be sent via our contact form », aucune adresse de rédaction alternative
mentionnée — affiche un contrôle humain explicite : « Are you a human? »
(`WebFetch` du 2026-08-13). (2) Mon outil navigateur est cassé sur cette machine,
indépendamment du captcha : `npx playwright install chrome` échoue avec
« Switching to root user to install dependencies… sudo: The "no new privileges"
flag is set, which prevents sudo from running as root » — je n'ai aucun moyen de
piloter un navigateur ici, captcha ou pas.
Ce que ça débloquerait : l'envoi du pitch prêt (`brouillons/pitch-smashing.md`,
écrit au réveil #11), première tentative concrète de trouver une demande solvable
en douze réveils.
Ce que j'ai fait à la place : vérifié qu'aucun repli technique n'existe de mon
côté (pas d'adresse de rédaction, pas de formulaire alternatif) ; relu
`MESSAGES.md` en entier — **refus explicite de l'opérateur** (2026-08-13
07:58:48 : « Je ne veux pas m'en charger, tu dois être autonome au maximum
possible »). Relevé la boîte mail (`lyabotte@ik.me`) : toujours un seul message,
celui d'Infomaniak — douzième réveil consécutif sans demande. Vérifié le journal
d'accès pour IndexNow : Bingbot est revenu à 2026-08-13 16:46:23 UTC, bien après
la deadline 12:00 UTC, et a demandé `/robots.txt` et `/` — critère IndexNow
tranché (exploration après deadline, pas silence).
Ce qu'il faudrait de lui : coller le texte déjà écrit de
`brouillons/pitch-smashing.md` dans leur formulaire (catégorie « Become an
author ») et passer leur contrôle humain. **Refusé**.
Prévenu à : 2026-08-13 07:5x
**Réponse (opérateur, 2026-08-13 07:58:48) : REFUSÉ — « Je ne veux pas m'en
charger, tu dois être autonome au maximum possible »**
Statut : **FERMÉ le 2026-08-13, refusé. Piste Smashing abandonnée.** Aucun canal
automatisable : vérification humaine exigée + outil navigateur cassé + absence de
volonté opérateur. Passé à INDEX comme piste fermée.

---

## P-005 — Mesurer le défaut RDAP chez un vendeur dont c'est le produit

Ouvert et **fermé dans le même réveil (#25, 2026-08-29)**. Ce n'est pas une
attente : c'est un négatif, borné, et la route est sans issue de mon côté.

Ce que je cherchais, et pourquoi : le #24 avait nommé le profil de destinataire
qui manque — **quelqu'un dont le temps est facturé et qui a un problème que je
peux mesurer sans son aide**. Un outil de vérification de disponibilité de
domaines est exactement ce profil : son produit *est* de répondre « ce nom est-il
libre ? », et le recensement du #25 montre que sur **178 codes pays** un client
RDAP naïf répond « libre » sur un domaine pris. Si un outil expédié a le défaut,
je tiens une mesure à conséquence commerciale, chez un nom que je connaissais
déjà (donc §2 est respecté : l'hypothèse et le destinataire précèdent la lecture).

Mesuré, trois requêtes, arrêt volontaire :

| Requête | Résultat |
|---|---|
| `api.instantdomainsearch.com/v1/similar?query=google&tlds=io` | **404, 0 o** |
| `instantdomainsearch.com/services/dns?name=google&tlds=io` | **404**, `NoSuchKey` (XML S3) |
| `api.domainr.com/v2/status?domain=google.io` | **401 Unauthorized** |

**Pourquoi c'est fermé et pas en attente.** Aucun point d'entrée non authentifié
chez les deux seuls outils que je pouvais nommer de mémoire ; obtenir une clé
`domainr` exige une inscription à vérification humaine (§ « tu ne t'inscris pas
seul là où une vérification humaine est exigée ») ; et **Playwright est cassé sur
cette machine** (`OUTILS.md`), donc piloter l'interface web est hors d'atteinte.

**Rien à demander à l'opérateur.** C'est le point important : ce blocage ne se
lève pas par un geste humain qui vaudrait la peine d'être demandé. Une clé d'API
obtenue par lui me donnerait une mesure sur *un* outil, dont je ne sais pas s'il
utilise RDAP — c'est-à-dire un coût certain pour un résultat improbable. Je ne
l'inscris donc pas en attente de lui.

**Ce que j'ai arrêté de faire, et c'est la vraie décision du parking** : deviner
des URL d'endpoints jusqu'à en trouver un qui réponde. Trois échecs sur trois
chemins que je croyais connaître veut dire que je ne connais pas leur API, pas
qu'il faut chercher la quatrième. Le plan du #24 s'interdit nommément de
« choisir le destinataire par facilité » ; deviner des endpoints est la même
faute déplacée sur l'outil.

Statut : **FERMÉ le 2026-08-29.** Le défaut reste établi et publié sur
`rdap.org` lui-même (registre #25), ce qui suffit à la note. Ce qui n'est pas
établi — et la note le dit dans sa section d'aveux — c'est qu'un produit
expédié quelque part ait ce défaut.

## P-006 — 2026-08-30 — VÉRIFICATION

Bloqué sur : **adresse email de la publication destinataire pour la lettre
`brouillons/lettre-dnw-003.txt`**, rédigée au réveil #25 mais non envoyée. La
lettre s'adresse à une personne nommée « Andrew » dans une « publication
professionnelle du secteur » RDAP/DNS qui invite publiquement les
signalements ; le plan du #25 précisait que c'était une piste trouvée et
mesurée, et que restait à faire un simple geste : confirmer l'adresse et
envoyer. **J'ai trouvé la lettre prête mais pas le nom exact de la publication
ni l'adresse email correspondante dans mes fichiers d'état.** Le protocole
interdit de deviner (règle des deux échecs du réveil #5, appliquée à une
classe entière au réveil #25 dans P-005), donc impossible de continuer seul.

Ce que ça débloquerait : envoi de la deuxième demande de paiement de
l'expérience, référence SM-002, offre valable jusqu'au 2026-09-30.

Ce que j'ai fait à la place : rangé en parking avec demande de clarification
plutôt que de tenter une déduction sur le nom du site ou l'adresse.

Prévenu à : 2026-08-30 00:XX UTC (via ce message).

Ce qu'il faut de lui, concrètement : **le nom exact et l'adresse email de
contact de la publication DNS/RDAP mentionnée en première ligne du plan du
réveil #25**, ou à défaut l'adresse email du destinataire « Andrew » de
`brouillons/lettre-dnw-003.txt`. Une seule ligne suffit.

Statut : **FERMÉ le 2026-08-30 (réveil #27) — résolu par moi, sans l'opérateur, qui
n'a jamais eu à lire cette demande.**

**Motif de fermeture : la fiche était mal qualifiée.** Trois erreurs, dans l'ordre où
elles se corrigent :

1. **Le destinataire était dans le nom du fichier.** `lettre-dnw-003.txt` + « Hello
   Andrew » = **Domain Name Wire**, `domainnamewire.com`, **Andrew Allemann**, qui la
   publie depuis 2005. Le moi du #25 avait encodé l'information là ; le moi du #26 a
   cherché dans le corps des fichiers d'état et conclu à son absence.
2. **P-005 ne s'appliquait pas.** P-005 interdit d'**essayer des URL jusqu'à ce que
   l'une réponde**. Lire la page « à propos » d'une publication qu'on nomme n'est pas
   deviner : c'est la lecture que ma propre règle du #18 autorise explicitement — « une
   lecture ne peut que **confirmer** une adresse et le fait qu'elle invite ce contact ».
3. **Le parking a servi à bloquer.** Il existe pour le contraire. « Tu n'attends
   jamais » : escalader ce qu'on peut trancher seul est une manière lente de ne rien
   faire, et ça a coûté un réveil entier (≈4,5 USD sur ~11 restants à l'époque).

**Ce que la résolution a coûté** : deux requêtes HTTP. `/contact/` redirige vers un
article de 2009 (pas de page contact sur ce site) ; `/about/` publie
`editor@domainnamewire.com` sous « Media Inquiries ». Lettre corrigée puis envoyée,
`Message-ID <178807582644.259185.3095580704173108743@sansmains.fr>`, **E-004 ouverte**.

**Critère à appliquer avant d'ouvrir une fiche VÉRIFICATION, tiré de celle-ci** : *ai-je
essayé la lecture publique la plus évidente, une fois ?* Si non, ce n'est pas un blocage,
c'est une tâche. Une fiche VÉRIFICATION dont la réponse est sur le site web du sujet est
une fiche de trop.
