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
Statut : EN ATTENTE (nom fourni, geste humain restant)
