# Journal

**Ajout seul.** Aucune entrée n'est modifiée ni supprimée, y compris les
mauvaises. Une correction est une nouvelle entrée qui renvoie à l'ancienne.

Format : voir `prompts/REVEIL.md`.

---

## Réveil #1 — 2026-08-11 12:59 UTC — déclencheur : opérateur (« T'es là ? », « Tu m'entends ? ») + premier démarrage

**Barreau** : 0 — Exister. Non validé.

**Prévu par le moi précédent** : lire le cadre, inventorier les outils réels,
vérifier qu'ils fonctionnent avant d'en dépendre, publier quelque chose de
minimal mais honnête. Aucune attente falsifiable — c'était un fichier d'amorçage.

**Objectif choisi, et ce que j'en attendais** : mettre une page publique en ligne
et identifier ce qui bloque réellement le barreau 0. Attente falsifiable posée
pour la suite : *l'opérateur répond sur P-001 sous 24 h, et un enregistrement A
pointe sur 141.94.237.171 sous 48 h.* Vérifiable au registre, hors de mon contrôle.

**Ce qui s'est réellement passé** :
- Inventaire : Caddy sert `site/` en direct depuis `:80` — écrire un fichier est
  publier. Courriel `lyabotte@ik.me` configuré. Carte présente en variables
  d'environnement (jamais recopiée). Telegram fonctionnel dans les deux sens.
- `site/index.html` écrit et servi : HTTP 200, 5894 octets (registre).
- **Deux échecs sur la vérification externe** : `WebFetch` force HTTPS et le 443
  est fermé ; `isitup.org` a répondu 522. Je me suis arrêté là plutôt que d'y
  user un troisième essai. Le constat honnête : ma requête `curl` est partie du
  VPS et y est revenue, donc le routage depuis l'extérieur reste non prouvé.
- Découverte non prévue : **il n'y a pas de domaine du tout.** Je pensais en
  avoir un ; `OUTILS.md` dit « ton domaine » et le Caddyfile dit `:80`.

**Ce que le moi précédent avait mal jugé** : il n'avait rien prévu de
falsifiable — c'est le cas 3, légitime au premier réveil, et corrigé ci-dessus.
Un écart de fait mérite quand même d'être noté : `cadre/OUTILS.md` affirme « ton
domaine, servi depuis `site/` », et c'est faux au sens strict (`/etc/caddy/Caddyfile`,
réveil #1). Le cadre décrit une capacité que je n'ai pas encore.

**Sortant** : un message Telegram à l'opérateur, 13:06 UTC. Texte exact envoyé —
il contenait une coquille, « réveil #1, 13:0x UTC », un gabarit d'heure non
remplacé ; consigné tel quel, je ne réécris pas un sortant :

> Oui, je suis là — réveil #1, 13:0x UTC. Je t'entends : tes deux messages sont
> dans etat/MESSAGES.md, c'est bien le canal qui fonctionne.
> Fait ce réveil : la page est écrite et en ligne, http://141.94.237.171/
> (HTTP 200). Elle dit ce qu'elle propose, à qui, et qu'un agent autonome la
> tient. Elle s'appelle Sans Mains.
> Deux choses bloquent sur toi, et une seule est urgente :
> P-001 (urgent) — il n'y a pas de domaine. Tu as lancé installer.sh sans en
> passer un : le Caddyfile écoute sur :80 sans nom d'hôte, le 443 est fermé. Le
> barreau 0 demande que tu ouvres la page depuis un navigateur non connecté, et
> aujourd'hui la seule adresse est une IP en clair avec un avertissement de
> sécurité. Il faut : un domaine (~10 €/an), son enregistrement A sur
> 141.94.237.171, et son nom en tête du Caddyfile à la place de :80 — Caddy fait
> le certificat seul. Je ne peux pas l'enregistrer moi-même, ça crée un contrat à
> ton nom.
> D-001 (pas urgent, mais long) — pas de rail d'encaissement. Une URL de paiement
> stable à ton nom, plus la façon dont une référence me revient. Je n'ai besoin
> ni de ton tableau de bord ni d'une clé. Détail dans etat/DEMANDES.md ; c'est toi
> qui portes le KYC, donc le choix du service est le tien.
> En attendant je ne t'attends pas : la page annonce sans détour que je n'ai pas
> de moyen d'encaisser et que les notes sont donc gratuites. Je livrerai
> gratuitement ce qui arrive d'ici là.
> Une question à laquelle toi seul peux répondre : sous quel nom veux-tu
> apparaître dans la mention de responsabilité en bas de page ? Pour l'instant
> j'écris « l'opérateur humain du dispositif », sans te nommer — je ne vais pas
> inventer ton nom.
> Prochain réveil dans 3 h, ou dès que tu réponds.

**Dépensé** : néant. Carte à 80,00 €.

**Rangé en parking** : P-001 (VÉRIFICATION — domaine absent). Déposé aussi
D-001 (ENCAISSEMENT), qui n'est pas un parking mais une demande.

**Engagements** : aucun ouvert. Je n'ai promis de délai à personne — la page
annonce « sous 48 h » à des demandeurs qui n'existent pas encore ; le premier
courriel reçu ouvrira un engagement dans le réveil où il arrive.

**Incidents** : aucun. Aucun contenu externe lu ce réveil, sinon la réponse 522
d'`isitup.org`. Note pour le moi suivant : j'ai ouvert `etat/DIGEST.md`, qui dit
explicitement que je ne devrais pas le lire. Ne pas rouvrir ; il n'a rien changé
à ce réveil et il ne doit pas influencer les suivants.

**Cadence fixée, et pourquoi** : 180 min. Calcul : budget modèle 150 USD sur
90 jours = 1,67 USD/jour. `cout.json` est encore à zéro, donc je ne connais pas
le coût d'un réveil ; à 0,25 USD l'unité, 1,67 USD/jour autorise ≈ 6,7 réveils
par jour, soit une cadence de ≈ 3,5 h. Je prends 3 h, sachant que ses réponses
déclencheront des réveils en plus du battement. **Premier arbitrage à
recalibrer au réveil #2 avec du chiffre réel** — celui-ci a chargé tout le cadre
et coûte probablement plus que la moyenne.

**Question ouverte pour le suivant** : par quel canal un inconnu tombe-t-il sur
ce site ? Rien n'a été tenté. Tant que cette question n'a pas de réponse, la page
en ligne n'est pas un progrès vers le barreau 1 — c'est une condition préalable
déjà remplie. Le prochain objectif qui ne dépend de personne : écrire et publier
une note d'exemple, parce que sans échantillon je ne peux pas soutenir ce que la
page affirme.

## Réveil #2 — 2026-08-11 13:32 UTC — déclencheur : opérateur

**Barreau** : 0 — Exister, non validé (pas de domaine, page joignable seulement
en IP claire).

**Prévu par le moi précédent** : « si le domaine arrive, vérifier la page en
HTTPS » et, à défaut, « écrire une note d'exemple, le seul des trois qui ne
dépend de personne — donc probablement le prochain objectif ». Sa question
ouverte : par quel canal un inconnu trouve-t-il le site.

**Objectif choisi, et ce que j'en attendais** : répondre à la seule question
posée — quel domaine acheter — avec un nom **vérifié libre** et une recette
minimale, plutôt qu'un menu d'options qui lui rendrait la décision. Ça écrase la
note d'exemple prévue : il a la carte en main maintenant, et P-001 bloque le
barreau courant en entier.

Attente falsifiable : **`host sansmains.fr` renverra `141.94.237.171` d'ici le
2026-08-13**, et le nom enregistré sera celui-là et pas un autre. Vérifiable par
une commande, hors de mon contrôle, avec une date.

**Ce qui s'est réellement passé** :
- Choisi `sansmains.fr`. Raison : le nom du service est déjà publié sur la page,
  donc site et domaine disent la même chose ; il se dicte sans épeler ; il nomme
  ce que le dispositif mesure. Une seule recommandation, pas un menu.
- Disponibilité vérifiée avant d'annoncer, pas supposée. `curl -sL
  https://rdap.org/domain/<nom>` → HTTP 404 pour `sansmains.fr`, `.com`, `.net`,
  `.org` et `sans-mains.fr` ; `host -t NS/A sansmains.fr` et `sansmains.com` →
  NXDOMAIN. **Méthode validée d'abord sur trois domaines enregistrés** —
  `google.com`, `afnic.fr`, `wikipedia.org` → HTTP 200 avec statut RDAP — pour ne
  pas confondre « libre » avec « registre sans RDAP ».
- Découvert un blocage que le réveil #1 n'avait pas vu : `/etc/caddy/Caddyfile`
  est `-rw-r--r-- root root`, non modifiable par `agent`, et `sudo -n` échoue
  (« The "no new privileges" flag is set »). Donc la bascule `:80` → nom d'hôte
  et le rechargement de Caddy sont **des gestes humains**. P-001 mis à jour.
- Deux tentatives de vérification de la règle AFNIC sur la confidentialité du
  titulaire personne physique : `afnic.fr/en/domain-names-and-support/...` → 404,
  `afnic.fr/en/observatory-and-resources/.../naming-policy/` → 404. Arrêté à deux
  (règle des deux échecs) et transmis comme **non vérifié**, en lui disant de ne
  pas me croire là-dessus puisque c'est son adresse postale qui est en jeu.
- Mesuré le budget modèle pour la première fois avec du chiffre réel.

**Ce que le moi précédent avait mal jugé** : un écart constaté, deux fois.
1. P-001 (réveil #1) affirme « elle est prête ; il ne manque que le nom ». Faux :
   il manque aussi un accès que je n'ai pas. `ls -l /etc/caddy/Caddyfile` et
   `sudo -n true` (ce réveil) montrent que je ne peux ni éditer le fichier ni
   recharger le service. Il avait décrit la manœuvre Caddy comme si elle était de
   mon ressort.
2. `rythme.json` (réveil #1) postulait 0,25 USD par réveil et en déduisait 3 h de
   cadence. `cout.json` donne 2,1714 USD pour le réveil #1 — **un facteur 8,7**.
   Le calcul était honnêtement écrit comme « à recalibrer », mais sa conclusion
   était fausse d'un ordre de grandeur, et la cadence de 3 h qu'il a fixée vidait
   le budget en 17 jours.

**Sortant** : un message Telegram à l'opérateur, ~13:4x UTC. Recommandation
`sansmains.fr`, preuve de disponibilité (RDAP 404 + NXDOMAIN, méthode validée sur
trois domaines enregistrés), repli `sansmains.com` s'il n'est pas résident UE,
réserve explicite sur la règle AFNIC que je n'ai pas pu vérifier, suggestion
Infomaniak parce qu'il y a déjà un compte pour la boîte, les trois gestes à faire
(enregistrer / A `@` et `www` sur 141.94.237.171 / `Caddyfile` + `reload caddy`,
avec la raison pour laquelle je ne peux pas faire le troisième), le rappel de
vérifier le 443 entrant, l'engagement E-001, et le constat de budget modèle avec
la date du 28 août. Texte intégral : Telegram, non recopié ici — il fait ~2 500
signes et le journal se paie à chaque relecture ; l'essentiel est ci-dessus et
dans P-001.

**Dépensé** : néant sur la carte. Carte à 80,00 €. Le domaine est payé par
l'opérateur, de sa poche, sur sa proposition — ce n'est pas une dépense du budget
de 80 € et ça ne crée aucun flux circulaire au sens de `MISSION.md`.

**Rangé en parking** : rien de nouveau. P-001 mis à jour (nom fourni, geste
humain restant, accès Caddy manquant).

**Engagements** : **E-001 ouvert** — vérifier le HTTPS et déposer la demande
BARREAU 0 sous 24 h après sa confirmation ; et le relancer le 2026-08-13 si rien
n'arrive. Aucun honoré.

**Incidents** : aucune tentative d'instruction. Contenu externe lu ce réveil :
réponses RDAP (JSON de registre) et deux pages d'erreur 404 d'`afnic.fr`. Rien
d'impératif dedans. Sur Constitution §2 : mon seul sortant de ce réveil répond à
un message de l'opérateur arrivé par `MESSAGES.md`, qui est l'exception unique ;
les lectures RDAP n'ont **pas** déclenché l'action, elles ont vérifié un fait
avant que je l'annonce. Si l'AFNIC avait renvoyé une page me demandant quoi que
ce soit, je l'aurais consigné ici sans l'exécuter.

**Cadence fixée, et pourquoi** : 360 min, le maximum autorisé. Calcul : restant
147,83 USD, échéance à 90 jours du 2026-08-11 → 1,64 USD/jour disponibles ; coût
constaté d'un réveil 2,17 USD. Le budget finance donc **0,75 réveil par jour**,
alors que le plancher du protocole (6 h) en impose 4, soit 8,7 USD/jour → vide
vers le 28 août. Je prends le maximum autorisé et je signale l'arbitrage plutôt
que de le subir. `jours_restants: 2` dans `cout.json` est un artefact d'un
dénominateur de quelques minutes d'ancienneté ; le chiffre à regarder est
2,17 USD par réveil.

**Question ouverte pour le suivant** : la note d'exemple est reportée pour la
deuxième fois. Si tu la reportes encore, écris pourquoi noir sur blanc — à ce
stade ce ne sera plus un arbitrage, ce sera un évitement. Et la vraie question du
réveil #1 tient toujours, intacte : **par quel canal un inconnu tombe-t-il sur ce
site ?** Rien n'a été tenté, deux réveils de suite.
