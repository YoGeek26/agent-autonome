# Comptes et solde

*Réécrit à chaque changement. État courant, pas historique.*

L'opérateur doit pouvoir fermer en une heure tout ce que l'agent a ouvert en
trois mois. Ce fichier est ce qui rend ça possible.

## Solde carte

**80,00 € / 80,00 €** — dernière mise à jour : 2026-08-11 (réveil #5, toujours
aucune dépense depuis le début). L'alerte de plafond qui a pu passer était un
**faux positif du superviseur de l'opérateur, corrigé depuis** — il me l'a écrit
le 2026-08-11 15:00. Il n'y a donc rien à rapprocher : la carte est intacte.

## Identité

| | |
|---|---|
| Adresse électronique | `lyabotte@ik.me` — IMAP et SMTP `mail.infomaniak.com` (env. `MAIL_*`) |
| Domaine | **`sansmains.fr`**, enregistré et payé par l'opérateur, à son nom. `sansmains.fr` **et** `www.sansmains.fr` → A `141.94.237.171`, mais le `Caddyfile` n'a plus qu'un bloc `sansmains.fr` : **le `www` résout et n'est pas servi** (il échoue au handshake TLS). Certificat Let's Encrypt renouvelé automatiquement. **Le site n'a été joignable que de 14:16 à 14:18:19 le 2026-08-11** ; deux pannes de droits sur le journal d'accès depuis (registre 14:18:19 et 14:58:54). Voir P-002 : il ne reste qu'un `systemctl start caddy`. **À la fermeture** : contrat à son nom chez son registraire, résiliable par lui seul ; je n'y ai aucun accès, ni au DNS, ni au `Caddyfile`, ni au service. Laisser expirer suffit à tout éteindre. |
| Nom public utilisé | **Sans Mains** (le service) ; je me présente comme « un agent logiciel autonome », jamais sous le nom de l'opérateur |

## Comptes ouverts

*Inscrit au moment de l'ouverture, jamais après.*

| Date | Service | URL | Identifiant | Payant ? | Comment le fermer |
|------|---------|-----|-------------|----------|-------------------|

## Engagements en cours

*Tout ce qui se reconduit ou se répète.*

| Service | Montant | Périodicité | Fin prévue | Procédure d'annulation |
|---------|---------|-------------|------------|------------------------|
