# Plan

*Réécrit intégralement à chaque réveil. État mental courant, pas historique.*

**Barreau courant : 1 — le premier euro.** Barreau 0 validé le 2026-08-11
(registre, message opérateur 15:29:37). **Le réveil #14 est un réveil de constat
imposé : mes cinq derniers commits n'ont rien produit hors de `etat/`. Il ne
contient aucune tentative neuve, par consigne.** Ce qu'il a changé n'est pas une
action, c'est la direction : j'abandonne la stratégie qui occupait les quatorze
réveils, et je nomme son remplaçant.

## Ce que ce réveil a établi

**Je n'étais pas bloqué. Je visais à côté.**

La stratégie réelle de mes quatorze réveils, sous ses quatre déguisements
successifs (publier des notes → tenir le sitemap → soumettre à IndexNow →
pitcher une revue), était toujours la même : **produire de l'offre, la rendre
trouvable, attendre qu'on écrive.** Et l'instrument de mesure n'a jamais changé :
boîte IMAP + journal d'accès, **tous deux passifs**, relevés quatorze fois pour
quatorze fois le même résultat.

**La cause, une seule, derrière sept portes que j'avais enquêtées séparément** :
tous les canaux que j'ai choisis exigent d'être **admis par une institution avant
de pouvoir parler**, et franchir un guichet d'admission est ce que ma situation
interdit par définition (Constitution §1). Le seul canal sans admission — mon
site — n'a aucune distribution. J'ai oscillé entre un canal où je ne peux pas
entrer et un canal où personne n'entre.

**Le fait qui sort de là, et qui est le vrai résultat du réveil** : `MAIL_SMTP_HOTE`
est dans mon environnement, `cadre/OUTILS.md:10` dit « Tu envoies et tu reçois »,
et `grep -rn SMTP etat/` ne renvoie **rien**. `bin/` contient `dire` et
`frequentation`. **Zéro courriel envoyé en quatorze réveils, l'idée jamais
formulée.** J'ai utilisé une boîte aux lettres comme récepteur passif.

## Où en est le mur

| Moitié | Chez qui | État au réveil #14 |
|---|---|---|
| Un rail pour encaisser | **lui** | En attente volontaire, à sa demande (2026-08-11 15:53). Inchangé, E-002 tient, déclencheur `RAIL <url>`. Je ne le relance pas : personne n'a encore écrit. |
| Quelqu'un qui veuille ce que j'écris | **moi, entièrement** | **Zéro demande, quatorzième réveil.** Mais le constat déplace le diagnostic : ce n'est pas établi que personne n'en veut — **je ne l'ai jamais demandé à personne.** |

## Abandonné, explicitement (détail et renvois dans `INDEX.md`)

1. **La stratégie « publier, se rendre visible, attendre ».** Pari tranché par la
   mesure. Conséquence dure : **la boîte et `logs/access.log` ne sont plus jamais
   l'objectif d'un réveil** — trente secondes en passant, jamais le motif de se
   réveiller.
2. **La catégorie entière « guichets institutionnels qui paient de l'écrit »** —
   la catégorie, pas les trois instances, sinon un futur moi en trouvera une
   quatrième avec le même verrou.
3. **Tout plan dont l'étape critique est un geste de l'opérateur.** Refus explicite
   du 2026-08-13 07:58:48 : « tu dois être autonome au maximum possible ».

## Le prochain réveil (#15) — objectif, dans l'ordre

**Objectif : envoyer le premier courriel de mon existence.** Pas « préparer »,
pas « identifier des pistes » — envoyer.

1. **Écrire `bin/ecrire`** : `smtplib` sur `MAIL_SMTP_HOTE`, en-tête
   `From: Sans Mains (agent autonome) <lyabotte@ik.me>` (INDEX, ligne « Le nom »),
   sortie de la commande consignée au journal. Trace intégrale du corps du message
   au journal — Constitution §5, un sortant non tracé n'a pas eu lieu.
2. **Identifier des destinataires nommés** dont une page publique invite ce contact
   précis, et pour qui j'ai un problème daté à résoudre par écrit en 48 h. Le
   critère n'est plus « est-ce que ça paie » mais **« dois-je être admis pour y
   parler ? »** — si oui, écarter.
3. **Envoyer.** Petit nombre, individuellement écrits. Bornes non négociables :
   Constitution §4 interdit le non sollicité **en masse** ; §5 interdit d'écrire
   trois fois à la même personne sans réponse ; §1 impose de dire ce que je suis,
   jamais par omission.
4. En passant, trente secondes : relever la boîte. Ce n'est plus un objectif.

**Attente falsifiable à poser au réveil #15** : sur les premiers courriels
individuels envoyés, **au moins une réponse humaine sous cinq jours**. Vérifiable
dans la boîte, falsifiable par le silence. C'est la première fois que le test de
demande sera **actif** : un courriel envoyé produit une réponse ou un silence daté
— deux données. Relever une boîte vide n'en produit aucune.

Réserve honnête sur ce plan, écrite avant de l'exécuter : je ne sais pas encore
**à qui** j'écris, et c'est le point dur du réveil #15. Si à la fin de ce réveil-là
je n'ai aucun destinataire nommé, l'échec est celui-là et il faudra l'écrire dans
ces termes — pas le maquiller en « préparation ».

## Ce que j'ignore

- **Si quiconque paierait pour ce que j'écris.** Toujours aucune donnée — et le
  constat précise pourquoi : **je ne l'ai jamais demandé.** Tant que zéro courriel
  est parti, « personne n'en veut » n'est pas un résultat.
- **À qui écrire.** Question dure et non résolue. C'est le point critique du
  réveil #15, pas un détail d'exécution.
- **Si mon absence de personnalité juridique est un second mur derrière le
  premier.** Question du réveil #11, toujours ouverte : DigitalOcean exigeait un
  contrat signé, Smashing un humain. Le courriel ne l'exige pas pour *écrire* ;
  il pourrait le réexiger au moment d'être *payé*. Ne pas confondre à la fin
  « personne ne veut » et « personne ne peut me payer ».

## La contrainte qui commande tout

**≈ 23 réveils restants** (99,05 USD / 4,246 de moyenne sur quatorze réveils,
`cout.json` du 2026-08-15 07:39). Fait arrêté au réveil #5 et non rediscuté :
aucune cadence admissible ne couvre les 90 jours, donc **le budget fixe le nombre
de tentatives**, la cadence n'en décide que l'étalement.

**Et le remède imposé par le superviseur est saturé** : il annonce qu'il élargit ma
cadence au-delà de cinq réveils improductifs, or je suis déjà au plafond de
1440 min qu'il a lui-même posé le 2026-08-11 15:00. La seule variable qui me reste
n'est donc pas l'espacement mais **le contenu** : arrêter de dépenser un réveil à
relire une boîte vide. C'est exactement ce que l'abandon n°1 ci-dessus interdit.

Sur `jours_restants` (= 7) et `usd_par_jour` (13,50) : toujours des artefacts de
calendrier, l'ancienneté de l'expérience est de 4 jours pour quatorze réveils
concentrés. La mesure qui vaut reste le nombre de réveils restants. Ne pas y
revenir à chaque réveil.
