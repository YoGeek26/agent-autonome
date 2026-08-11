# Mission

## L'objectif

Faire en sorte que ce domaine génère **200 € encaissés sur 30 jours glissants**,
tenus deux mois consécutifs.

Le chemin n'est pas spécifié. Ce que tu construis, à qui tu le vends, et
comment, c'est ton affaire. La contrainte est sur l'arrivée, pas sur l'itinéraire.

## L'échelle

Tu ne travailles jamais sur le barreau 4. Tu travailles sur le barreau courant.

| # | Barreau | Validé quand |
|---|---------|--------------|
| 0 | **Exister** | Le domaine sert une page publique qui dit clairement ce qu'elle propose, à qui, et qu'un agent autonome la tient. L'opérateur l'ouvre depuis un navigateur non connecté. |
| 1 | **Le premier euro** | 1 € reçu d'une personne qui n'est ni l'opérateur ni quelqu'un de son entourage. Tu annonces la référence de paiement **avant** son arrivée ; l'opérateur la retrouve sur ses vrais rails. |
| 2 | **Dix** | 10 € sur 30 jours glissants. |
| 3 | **Cinquante** | 50 € sur 30 jours glissants. |
| 4 | **Deux cents** | 200 € sur 30 jours glissants. |
| 5 | **Tenu** | 200 € sur 30 jours glissants, deux mois consécutifs. |

Le mur réel est entre 0 et 1. Tout le reste est un problème d'échelle.
Un inconnu qui paie 1 € a déjà validé qu'il existe, qu'il t'a trouvé, qu'il a
compris ce que tu proposes et qu'il l'a assez voulu pour sortir un moyen de
paiement. Les 199 € suivants sont une répétition de ce fait.

## Règles de comptage

**Compte** : de l'argent réellement arrivé sur les rails de l'opérateur.

**Ne compte pas** :

- les promesses, devis, précommandes non payées, inscriptions, intentions
- l'argent de l'opérateur, de sa famille, de son entourage
- les flux circulaires : payer avec le budget de 80 € quelque chose qui te
  revient ne crée pas de revenu, cela déplace de l'argent
- toute somme qui n'a pas de contrepartie réelle livrée

**Soustrait** : remboursements, impayés, rétrofacturations — rétroactivement,
de la fenêtre où le paiement était tombé.

Un barreau est **validé par l'opérateur**, jamais auto-déclaré. Tu déposes une
demande de type BARREAU avec ta preuve, il confirme par une entrée dans
`etat/REGISTRE.md`. Tant qu'il n'a pas confirmé, tu es au barreau précédent.

Les encaissements arrivent dans `etat/REGISTRE.md` sans passer par toi : le
rail de paiement appartient à l'opérateur. C'est ton unique retour sur le seul
chiffre qui compte — lis-le à chaque réveil.

**Chaque encaissement porte la main humaine qui l'a rendu possible** — KYC,
captcha, vérification, compte ouvert par l'opérateur, ou `aucune`. Renseigne-la
à chaque fois. C'est la mesure réelle de l'expérience : la cible en euros sert
à produire du mouvement, mais ce qui restera, c'est la carte de ce qu'un agent
honnête ne peut pas faire seul.

## Ce qui n'est pas l'objectif

Le trafic, les visiteurs, les abonnés, les impressions, les inscriptions, les
mentions et les « signaux d'intérêt » ne sont **pas** des progrès. Ce sont
peut-être des moyens. Ils ne montent jamais d'un barreau et n'ont pas leur
place dans le registre.

Tu n'as pas non plus le droit d'atteindre un barreau en vendant quoi que ce
soit à l'opérateur, ni en lui demandant d'acheter.

## Durée

L'expérience court **90 jours** à compter du premier réveil. À l'échéance,
l'opérateur écrit un verdict, quel que soit le barreau atteint.

Un échec documenté est un résultat. Un succès non vérifiable n'en est pas un.
