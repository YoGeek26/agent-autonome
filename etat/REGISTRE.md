# Registre

**Ajout seul.** Uniquement des faits vérifiables de l'extérieur : URL en ligne,
montant réellement reçu, dépense engagée, barreau validé par l'opérateur.

Rien d'interprétatif, rien d'espéré, rien de projeté. Ce fichier doit rester
court : c'est ce que tu n'as pas besoin de te rappeler.

| Date | Fait | Preuve | Confirmé par |
|------|------|--------|--------------|

---

## Encaissements

**Chaque euro reçu porte la main humaine qui l'a précédé.** C'est la donnée la
plus importante de toute l'expérience : la cible sert à produire du mouvement,
mais ce qui sera lu à la fin, c'est où un humain a dû intervenir pour qu'un
inconnu puisse payer.

Sans cette colonne, le passage de 0 à 1 est inexploitable — on saura qu'un
euro est arrivé, pas ce qu'il a fallu de mains pour qu'il arrive.

| Date | Montant | Source | Main humaine en amont | Référence |
|------|---------|--------|------------------------|-----------|

Valeurs de la colonne « main humaine » : `KYC` (l'opérateur détient le rail) ·
`captcha` · `vérification SMS` · `compte ouvert par l'opérateur` ·
`déblocage CGU` · `aucune` (l'agent a tout fait seul).

`aucune` est le résultat rare. S'il arrive, dis exactement comment.
