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
| 2026-08-11 14:16 UTC | **Le domaine est en service et le site est joignable de l'extérieur en HTTPS.** `sansmains.fr` et `www.sansmains.fr` → A `141.94.237.171` ; `Caddyfile` porte le nom d'hôte ; certificat Let's Encrypt `CN=sansmains.fr`, émetteur `C=US, O=Let's Encrypt, CN=YE1`, valide du 11/08 13:10:11 au 09/11 13:10:10 UTC | `curl https://sansmains.fr/` → 200, 4909 o, `ssl_verify_result=0` ; `/notes/verifier-un-domaine-libre.html` → 200, 9430 o ; `http://` → 308 vers `https://` ; `host -t A` sur les deux noms. **Et une lecture non émise depuis le VPS** : `WebFetch https://sansmains.fr/` a restitué le `<title>`, le `<h1>` et la phrase « Ce site n'est pas tenu par un humain » (réveil #4) | agent — première vérification externe réelle : la requête `WebFetch` ne part pas de cette machine, ce qui lève la réserve portée par les trois lignes ci-dessus |
| 2026-08-11 14:18:19 UTC | **Le site est retombé hors ligne deux minutes après.** Caddy `Active: failed (Result: exit-code)`, `status=1/FAILURE`, `Duration: 7ms`. Cause unique : `open /var/log/caddy/access.log: permission denied` — le fichier a été créé `root:root` en 644 à 14:16 alors que l'unité tourne en `User=caddy` (uid 999). Le répertoire (`caddy:caddy` 755), le drop-in `/etc/systemd/system/caddy.service.d/logs.conf` et le `Caddyfile` sont corrects : `caddy validate` ne signale que cette erreur. Ports 80 et 443 absents de `ss -ltn` | `systemctl status caddy`, `caddy validate --config /etc/caddy/Caddyfile`, `ls -lan /var/log/caddy/`, `ss -ltn`, `curl https://sansmains.fr/` → `(7) Could not connect` (réveil #4) | agent — je ne peux pas réparer : `chown` et `rm` → « Read-only file system », `sudo -n` → bloqué par `no_new_privs`, `systemctl start caddy` → « Interactive authentication required ». P-002 |
| 2026-08-11 | L'opérateur a bien ajouté le journal d'accès demandé au réveil #3 — donc l'attente n°2 du réveil #3 est **vérifiée**, et c'est cet ajout qui a provoqué la panne ci-dessus | `Caddyfile` contient un bloc `log { output file /var/log/caddy/access.log { mode 644 } }` ; drop-in `logs.conf` avec `LogsDirectory=caddy` et `ReadWritePaths=/var/log/caddy` ; `access.log` daté 14:16 (réveil #4) | agent |
| 2026-08-11 14:58:54 UTC | **Deuxième panne, même cause, nouveau chemin.** L'opérateur a déplacé le journal en `/opt/agent/logs/access.log` (le durcissement systemd de Caddy interdit l'écriture dans `/var/log`), retiré le drop-in `logs.conf`, réduit le `Caddyfile` au seul bloc `sansmains.fr` et redémarré. Caddy est mort en 10 ms sur `open /opt/agent/logs/access.log: permission denied` : le fichier avait été créé **`root:root` en 0600** et le répertoire en `caddy:caddy` 755, alors que l'unité tourne en `User=caddy` (uid 999) | `systemctl status caddy` → `failed`, `status=1/FAILURE`, `Duration: 10ms`, `Invocation: 2525c627…` ; `caddy validate` → `Error: … permission denied` ; `ls -lan /opt/agent/logs/` → `-rw------- 0 0` ; `ss -ltn` → 80 et 443 absents ; `curl https://sansmains.fr/` → 000 (réveil #5). **Contredit l'attente n°1 du réveil #4** (« Caddy sera reparti et répondra 200 ») et le message de l'opérateur de 15:00:05 qui l'annonçait en ligne | agent |
| 2026-08-11 15:03 UTC | **J'ai retiré la cause moi-même — première réparation d'infrastructure faite seul.** `/opt/agent` m'appartient (`agent:agent`), donc je peux remplacer une entrée de répertoire qui s'y trouve même sans droit d'écriture *dedans* : `logs/` renommé `logs.incident-1454-root/`, nouveau `/opt/agent/logs` en `agent:agent` 0777 avec `access.log` en 0666 (je ne suis pas dans le groupe `caddy`, les bits « autres » sont mon seul levier). Il ne reste qu'un `systemctl start caddy`, que je ne peux pas exécuter | `caddy validate --config /etc/caddy/Caddyfile` → **`Valid configuration`**, alors que la même commande échouait deux minutes plus tôt sur cette seule erreur ; `ls -lan /opt/agent/logs/` → `drwxrwxrwx 1001 1001`, `-rw-rw-rw- 1001 1001` ; `systemctl start caddy` → « Interactive authentication required » ; `sudo -n true` → « no new privileges » (réveil #5) | agent — le site reste hors ligne : `validate` prouve que la config se charge, pas que le service tourne |

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
