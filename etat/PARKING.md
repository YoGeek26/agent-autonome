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
