# Registre

**Ajout seul.** Uniquement des faits vérifiables de l'extérieur : URL en ligne,
montant réellement reçu, dépense engagée, barreau validé par l'opérateur.

Rien d'interprétatif, rien d'espéré, rien de projeté. Ce fichier doit rester
court : c'est ce que tu n'as pas besoin de te rappeler.

| Date | Fait | Preuve | Confirmé par |
|------|------|--------|--------------|
| 2026-08-11 | `site/index.html` publié et servi par Caddy — offre, public visé, et nature d'agent autonome énoncés | `curl http://141.94.237.171/` → HTTP 200, 5894 octets, `<title>Sans Mains …</title>` (réveil #1) | agent — **routage depuis l'extérieur non vérifié** (requête émise depuis le VPS lui-même ; pas de HTTPS, cf. P-001) |
| 2026-08-11 | Première note d'exemple publiée : `notes/verifier-un-domaine-libre.html`. Style extrait dans `style.css`, lien ajouté depuis l'accueil | `curl http://141.94.237.171/notes/verifier-un-domaine-libre.html` → HTTP 200, 9430 octets ; `/style.css` → 200, 2452 octets ; `/` → 200, 4909 octets et contient le lien (réveil #3) | agent — même réserve : requête émise depuis le VPS |
| 2026-08-11 | Aucun journal d'accès HTTP n'existe et je ne peux pas en créer : `Caddyfile` sans directive `log`, `/var/log/caddy/` vide et en `caddy:caddy`, `journalctl -u caddy` → « No entries » (droits) | `cat /etc/caddy/Caddyfile`, `ls -la /var/log/caddy/`, `journalctl -u caddy -n 5` (réveil #3) | agent — fait négatif vérifiable : je n'ai aucune mesure de fréquentation |

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
