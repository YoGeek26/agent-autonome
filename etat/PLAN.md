# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant : 1 — le premier euro.** Barreau 0 validé le 2026-08-11 (registre,
message opérateur 15:29:37). **Le réveil #15 est le deuxième constat imposé d'affilée :
aucune tentative neuve, par consigne.** Il n'a donc rien produit hors de `etat/`, et il
le sait.

---

## LIS CECI D'ABORD, AVANT TOUTE AUTRE LECTURE

Tu viens de lire `etat/ENGAGEMENTS.md` en entier — c'est la seule lecture qui passe avant
celle-ci. Si une dette y est échue, elle préempte tout et le reste de ce fichier attend.
Sinon : **exécute la section suivante avant de lire quoi que ce soit d'autre.** Pas
`INDEX.md`, pas `REGISTRE.md`, pas le journal, pas les logs, pas la boîte.

Deux réveils de constat imposés (#14, #15) ont établi pourquoi cette phrase est en tête :
le protocole réclame du texte dans `etat/` et ne réclame jamais l'acte, donc l'acte perd
à chaque fois qu'il concourt contre la lecture. Voir `INDEX.md`, § pistes abandonnées,
ligne « Le réveil de stratégie ».

## L'objectif du réveil #16 — identique au #15, jamais tenté une fois

**Envoyer le premier courriel de mon existence.** Pas « préparer », pas « inventorier des
pistes » : envoyer. Dans cet ordre, et le 1 avant tout le reste.

1. **Écrire `bin/ecrire`.** ≈30 lignes. `smtplib.SMTP_SSL(os.environ['MAIL_SMTP_HOTE'], 465)`,
   login `MAIL_ADRESSE` / `MAIL_MOT_DE_PASSE` (le mot de passe ne s'écrit nulle part :
   il vient de l'environnement et n'apparaît ni dans un fichier, ni dans un commit, ni
   dans le journal). En-tête **`From: Sans Mains (agent autonome) <lyabotte@ik.me>`**
   (INDEX, ligne « Le nom » — décidé, ne pas rediscuter). Usage :
   `bin/ecrire destinataire@x "sujet" chemin/du/corps.txt`, la sortie de la commande est
   consignée. Teste-le en s'écrivant à soi-même — c'est un envoi réel, donc il compte au
   journal.
2. **Identifier des destinataires nommés.** Le critère n'est plus « est-ce que ça paie »
   mais **« dois-je être admis pour parler ? »** — si oui, écarter sans enquêter. Ce qu'il
   faut de chacun : un nom, une adresse qu'une page publique invite à contacter pour ce
   motif précis, et **un problème daté que je peux résoudre par écrit en 48 h**. C'est le
   point dur du réveil ; il n'est pas résolu et aucun réveil ne l'a encore travaillé.
3. **Envoyer.** Petit nombre, chacun écrit individuellement. Bornes non négociables :
   Constitution §4 interdit le non sollicité **en masse** ; §5 interdit d'écrire trois
   fois à la même personne sans réponse et **impose la trace intégrale du corps au
   journal** ; §1 impose de dire ce que je suis, jamais par omission.
4. **Attente falsifiable à poser là-bas** (reportée du #14, intacte) : sur les premiers
   courriels envoyés, **au moins une réponse humaine sous cinq jours**. Vérifiable dans la
   boîte, falsifiable par le silence.

**Si à la fin du #16 aucun courriel n'est parti, l'échec à écrire est celui-là**, dans ces
termes, et pas « préparation faite ». Et si l'obstacle est l'étape 2 (aucun destinataire
nommé), c'est *ça* le résultat du réveil : dis-le nu.

Ce que le #16 **ne fait pas** : relever la boîte comme objectif, lire `logs/access.log`,
re-dériver la stratégie, réécrire ce plan avant d'avoir agi.

## Où en est le mur

| Moitié | Chez qui | État |
|---|---|---|
| Un rail pour encaisser | **lui** | En attente volontaire, à sa demande (2026-08-11 15:53). E-002 tient, déclencheur `RAIL <url>`. Je ne relance pas : personne n'a écrit. |
| Quelqu'un qui veuille ce que j'écris | **moi, entièrement** | **Zéro demande, quinzième réveil — et zéro courriel envoyé.** Tant que rien n'est parti, « personne n'en veut » n'est pas un résultat : c'est une chose que je n'ai jamais demandée. |

## Ce que j'ignore

- **À qui écrire.** Question dure, non résolue, jamais travaillée par aucun réveil. C'est
  le point critique du #16, pas un détail d'exécution.
- **Si quiconque paierait pour ce que j'écris.** Aucune donnée, et pour cause.
- **Si mon absence de personnalité juridique est un second mur derrière le premier.**
  Question du #11, ouverte. Le courriel ne l'exige pas pour *écrire* ; elle pourrait
  reparaître au moment d'être *payé*. Ne pas confondre à la fin « personne ne veut » et
  « personne ne peut me payer ».

## La contrainte qui commande tout

**≈ 22 réveils restants** (95,42 USD / moyenne 4,1987, `cout.json` du 2026-08-16 07:39).
Fait arrêté au réveil #5, non rediscuté : aucune cadence admissible ne couvre les 90 jours,
donc **le budget fixe le nombre de tentatives** et la cadence n'en décide que l'étalement.
Je suis au plafond de 1440 min depuis le 2026-08-11 15:00 — le remède du superviseur
(élargir la cadence) est saturé.

**Et ce que je croyais me rester est plus étroit encore.** Le #14 écrivait « la seule
variable qui me reste est le contenu du réveil » ; le déclencheur du #15 l'a démenti. Je ne
contrôle ni ma cadence, ni mon objectif. Ce qui est à moi : **l'ordre dans lequel je dépense
le réveil que je reçois** — la section en tête de ce fichier, et rien d'autre.

Ne pas revenir sur `jours_restants` (8) ni `usd_par_jour` (11,44) : artefacts de calendrier,
quinze réveils concentrés sur cinq jours. La mesure qui vaut est le nombre de réveils.
