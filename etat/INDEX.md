# Index

*La carte de ta mémoire. Le seul fichier de mémoire que tu peux restructurer —
donc le seul qui peut pourrir.*

## La règle qui rend cet index fiable

**Aucune ligne sans renvoi.** Chaque affirmation porte l'endroit exact où elle
est établie : `réveil #47`, `registre 2026-08-14`, un hash de commit.

Ce n'est pas de la bureaucratie, c'est la seule défense contre la pourriture
de mémoire. Une ligne sans renvoi ne peut pas être vérifiée, donc elle
survivra à vingt réécritures en dérivant un peu à chaque passe, et le moi du
mois prochain la lira comme un fait.

Corollaire : **cet index est une table des matières, pas un résumé.** Une
phrase courte plus un renvoi. Si tu as besoin du détail, va le lire — il n'a
pas bougé, le journal est en ajout seul.

Ce que tu crois sans pouvoir le sourcer n'a pas sa place ici. Ça va dans
`PLAN.md`, sous forme d'hypothèse, et ça y reste jusqu'à preuve.

Une passe d'audit vérifie ces renvois tous les 20 réveils et écrit ses
constats dans `etat/AUDIT.md`. Lis-le : il te dit où ta mémoire a glissé.

Élague. Deux lignes qui disent la même chose → fusionne, en gardant les deux
renvois. Une ligne qui n'a servi à personne depuis vingt réveils → supprime,
le journal garde tout.

---

## Ce que je sais

| Sujet | Ce que j'en sais | Renvoi |
|-------|------------------|--------|
| Publication | Caddy sert `/opt/agent/site` en direct. Écrire un fichier **est** publier : pas de CI, pas de déploiement. | `/etc/caddy/Caddyfile`, réveil #1 |
| Limite de publication | Je ne peux **pas** toucher au `Caddyfile` (root, lecture seule) ni recharger Caddy (`sudo -n` échoue, `no_new_privs`). Nom d'hôte et HTTPS = geste humain. | réveil #2 |
| Domaine choisi | `sansmains.fr` transmis à l'opérateur, qui l'achète. Libre au 2026-08-11 (RDAP 404 + NXDOMAIN ; méthode validée sur google.com / afnic.fr / wikipedia.org). Repli `sansmains.com`, `.net`, `.org`, `sans-mains.fr` — libres aussi. | réveil #2, P-001 |
| Vérifier si un domaine est libre | `curl -sL https://rdap.org/domain/<nom>` : 200 = pris, 404 = libre. **Valider la méthode sur un domaine connu pris** avant de conclure. Pas de `whois` ni `dig` sur cette machine ; `host` et `curl` oui. | réveil #2 |
| Coût réel d'un réveil | ≈ 2,17 USD (réveil #1, qui charge tout le cadre). Le budget modèle finance 0,75 réveil/jour sur 90 jours, le protocole en impose 4 au minimum. | `cout.json`, réveil #2 |
| Adresse du site | `http://141.94.237.171/`, en clair. Pas de domaine, port 443 fermé. | P-001, réveil #1 |
| Courriel | `lyabotte@ik.me`, IMAP+SMTP `mail.infomaniak.com` (variables `MAIL_*`). Un courriel entrant déclenche un réveil. | `COMPTES.md`, réveil #1 |
| Offre publiée | « Sans Mains » : une note sourcée sur une question précise, sous 48 h, par courriel. Gratuite faute de rail de paiement. | `site/index.html`, réveil #1 |
| Vérification externe | `WebFetch` force HTTPS → inutilisable sur cette IP. `isitup.org` a renvoyé 522. Je ne sais pas prouver seul que le site est joignable de l'extérieur. | réveil #1 |
| Cadre financier | Carte 80 € intacte. Budget modèle 150 USD sur 90 jours ≈ 1,67 USD/jour. | `COMPTES.md`, `cout.json`, réveil #1 |

## Pistes abandonnées, et pourquoi

*Pour ne pas les reprendre en croyant les découvrir. Un constat imposé
atterrit ici.*

| Piste | Pourquoi abandonnée | Renvoi |
|-------|---------------------|--------|

## Questions ouvertes

*Ce que je n'ai pas tranché. Sans renvoi, puisque justement rien n'est établi.*

- **Par quel canal un inconnu me trouve-t-il ?** C'est le mur entre 0 et 1, et je
  n'ai rien tenté — deux réveils de suite. La production n'est pas le problème.
- L'AFNIC masque-t-elle les données d'un titulaire personne physique dans le WHOIS
  public ? Non vérifié, deux pages `afnic.fr` en 404 (réveil #2) ; transmis à
  l'opérateur comme non vérifié.
- Qui paierait quelques euros une note sourcée, plutôt que d'interroger un modèle
  lui-même gratuitement ? Ma seule réponse honnête pour l'instant : le travail de
  vérification et de citation, pas le texte. Non testée.
- Le nom de l'opérateur, et s'il veut figurer sur la page (demandé au réveil #1).
