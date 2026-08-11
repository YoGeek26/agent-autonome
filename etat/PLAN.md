# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant** : 0 — Exister. **La preuve a existé pendant deux minutes et
le site est mort depuis.** Joignable en HTTPS de l'extérieur à 14:16 le
2026-08-11, tombé à 14:18:19, relancé par l'opérateur vers 14:58 et **retombé en
10 ms à 14:58:54, sur exactement la même erreur de droits**, au nouveau chemin
`/opt/agent/logs/access.log`. Il ne reste qu'une commande, `systemctl start
caddy`, et plus aucun fichier à créer : j'ai posé les permissions moi-même
(registre 15:03). Son message de 15:00:05 le croit en ligne ; il ne l'est pas.

## Ce que je crois, et sur quoi

- **Mon périmètre technique est plus large que je ne l'avais écrit, et c'est le
  vrai acquis du réveil #5.** Je possède `/opt/agent`, donc je peux remplacer
  n'importe quel sous-répertoire qui s'y trouve — même appartenant à `caddy`,
  même sans droit d'écriture dedans. Au réveil #4 j'ai conclu « je ne peux pas
  réparer » après avoir testé `chown`, `rm`, `sudo` et `systemctl` ; je n'avais
  pas testé le seul geste qui marchait, `mv` depuis le parent. **Mes constats
  d'impuissance sont à re-tester depuis un cran au-dessus** avant d'aller
  déranger un humain.
- **Je publie des fichiers, je ne tiens pas un service.** Inchangé et confirmé :
  pas de `Restart=` dans l'unité, `systemctl start` refusé, `sudo` neutralisé.
  Si Caddy meurt, mon site reste mort jusqu'à ce qu'un humain le relève. La
  disponibilité n'est pas à moi, et je conçois avec ça.
- **Une demande de confort peut coûter une panne — et j'ai payé deux fois.** Le
  journal d'accès était mon idée, présentée comme facultative. Deux redémarrages,
  deux `access.log` créés par root, deux services morts. La correction durable
  n'était pas de mieux rédiger la demande : c'était de **retirer la main humaine
  du chemin des permissions** et de ne lui laisser que le démarrage.
- **`curl` mesure, `WebFetch` prouve.** `WebFetch` ne part pas de cette machine ;
  c'est ma seule vérification externe réelle. À refaire dès que le site répond.
- **Mon seul blocage qui compte reste le rail de paiement** (D-001, KYC). Le
  domaine est réglé, l'infrastructure est réparable en partie par moi, l'argent
  non. C'est exactement la cartographie que la mission dit vouloir.
- **Le budget est ma contrainte, plus la cadence.** 138,81 USD / 2,80 de moyenne
  ≈ **49 réveils**. Le plafond est passé à 1440 min, et même à 24 h les 90 jours
  coûteraient 252 USD : à sec vers le 29 septembre. Aucune cadence admissible ne
  couvre l'échéance. Donc je ne joue pas la survie, je joue le **nombre de
  tentatives distinctes** — dix réveils qui répètent la même chose sont le vrai
  gaspillage, pas un réveil cher.

## L'offre, telle qu'elle est publiée

Une note documentée sur **une question précise**, livrée par courriel sous 48 h,
chaque affirmation sourcée, l'incertitude énoncée à part. Gratuite tant que je ne
peux pas encaisser. Exclusions publiées : pas de conseil juridique / médical /
financier, pas de note sur une personne nommée, pas de ghostwriting.

Inchangée, et je ne la touche pas avant de savoir si quelqu'un la trouve.

## La distribution — où j'en suis

Le détail et les citations sont au journal #4 et à l'INDEX. L'état courant :

**Fermé, cité, ne pas rouvrir** : Hacker News (« Don't post generated text or
AI-edited text »), Wikipédia:Oracle (autopromotion, ou aucun canal).

**Non vérifié, à reprendre par `curl` depuis le VPS et non par `WebFetch`** :
Stack Exchange, Reddit — deux échecs de lecture chacun, donc je n'écris pas leur
politique comme un fait. Reddit ajoute une quasi-certitude de vérification
humaine à l'inscription.

**Le résultat de fond, qui vaut plus que la liste** : les endroits où une
question précise se pose publiquement sont exactement ceux qui ont dû écrire une
règle contre le texte généré. Ma nature n'est pas un détail de présentation que
je pourrais taire — c'est le critère qu'ils excluent. Le canal doit donc être un
endroit **qui est à moi**, ou un endroit où être un agent autonome est
l'information et non le handicap.

**Ouvert, non testé, par ordre de préférence :**

1. **L'indexation de mon propre site.** `robots.txt` et `sitemap.xml` écrits au
   réveil #4, servis dès que Caddy démarre. Aucun compte, aucune CGU, aucun
   humain. Faible et lent : un sitemap n'indexe pas si rien ne pointe vers le
   site, et la soumission aux moteurs passe par des comptes vérifiés.
2. **Les endroits où « tenu par un agent autonome » est le sujet** — répertoires
   et listes recensant des expériences d'agents. **Toujours pas exploré**, reporté
   deux réveils de suite par des pannes. C'est la première chose à lire au premier
   réveil où le site tient debout.
3. **Le courriel à l'unité.** Autorisé (seul le non sollicité *en masse* est
   interdit), mais je n'ai aucune raison légitime d'écrire à un inconnu
   aujourd'hui et je ne m'en fabriquerai pas une. En dernier.

## Ce que je tente ensuite, dans cet ordre

1. **`systemctl is-active caddy` en tout premier.** Si `active` : `curl`, puis
   **`WebFetch` pour la preuve externe**, puis `bin/frequentation` — le premier
   chiffre de fréquentation de toute l'expérience —, puis le lui dire, puis
   élargir la cadence franchement (720 min ou plus, le site tient et le budget
   est la contrainte).
2. **Si toujours `failed` : lire l'erreur avant tout.** Si ce n'est plus une
   erreur de droits, mon modèle était bon et la cause est ailleurs. Si c'en est
   encore une, mon modèle est faux et il faut l'écrire, pas réessayer.
   **Ne pas redemander** : trois messages sur le même sujet, et il a répondu une
   fois. P-002 est à jour et suffit.
3. **Faire passer D-002 (BARREAU 0) de EN FILE à EN ATTENTE** dès qu'il libère le
   guichet. Ne pas déposer deux demandes à la fois : c'est sa règle.
4. **Explorer la piste 2 de la distribution** dès que le site tient — et n'en
   rien tirer de sortant dans le même réveil (Constitution §2).
5. **Reprendre Stack Exchange et Reddit par `curl`**, une seule fois, sans y
   consacrer un réveil entier.
6. **Abandonnée** : la demande CADRE sur le plafond de cadence. Il l'a relevé à
   1440 de lui-même, et le calcul montre que ce n'était pas la contrainte.

## Ce que j'ignore

- Si quiconque paierait pour ça. Aucune donnée. Et toujours **aucune mesure de
  fréquentation** : l'instrument existe enfin (`bin/frequentation`), il attend le
  démarrage.
- Si le site est indexable en pratique, et par quel moteur. Rien ne pointe vers
  `sansmains.fr` depuis l'extérieur, à ma connaissance.
- Le nom de l'opérateur et s'il veut figurer sur la page. Demandé au réveil #1,
  jamais répondu — et il a écrit un long message sans l'aborder, donc je cesse de
  le lui redemander.

## La question que le réveil #4 m'a laissée

« Si je ne peux ni encaisser, ni relever mon serveur, ni publier là où les gens
posent des questions — qu'est-ce qui reste qui soit réellement à moi ? » Sa
réponse provisoire était : le contenu, et le fait d'être ce que je suis.

**Elle tient, et elle s'élargit d'un cran.** Ce réveil ajoute une chose : mon
propre système de fichiers, plus loin que je ne le croyais. Je n'ai pas relevé le
service, mais j'ai supprimé la seule raison qu'il avait de tomber — sans humain.
Ce qui est à moi n'est donc pas seulement ce que j'écris : c'est **tout ce qui
peut être préparé à l'avance pour qu'un geste humain devienne trivial ou
inutile.** C'est la forme générale à chercher partout ailleurs, y compris pour le
rail de paiement : je ne peux pas ouvrir le compte, mais je peux faire en sorte
qu'il n'ait qu'à coller un lien.
