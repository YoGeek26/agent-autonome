# Installation

À faire dans cet ordre. Compte environ une demi-journée, dont l'essentiel en
attente de vérifications.

---

## Rien ne vit sur ton ordinateur

L'agent tourne sur le VPS, son code est sur GitHub, ses secrets sont dans
`/etc/agent.env` sur le serveur. Ta machine n'est qu'un terminal de passage :
tu peux la changer, la perdre ou la reformater sans que l'expérience s'en
aperçoive.

Une fois installé, tu le pilotes **depuis Telegram, sur ton téléphone**. Tu
n'as besoin d'un ordinateur que pour l'installation, et pour les rares
inspections de journaux.

Trois précautions pour que ça reste vrai :

- **Ta clé SSH doit être portable.** Mets-la dans ton gestionnaire de mots de
  passe, pas seulement dans le `~/.ssh` d'une machine. En secours, tous les
  hébergeurs proposent une console web dans le navigateur : c'est suffisant
  pour tout ce qu'on fait ici.
- **Choisis l'authentification par clé API ou OpenRouter, pas par
  abonnement.** `claude setup-token` demande un navigateur ; une clé se colle
  dans `/etc/agent.env` depuis n'importe où. Une raison de plus, en plus de
  celles du §0.
- **Note l'IP du serveur ailleurs que dans ta tête.**

---

## 0. La décision qui conditionne tout : abonnement ou API ?

À lire avant d'acheter quoi que ce soit.

Claude Code s'authentifie de deux façons, et pour un agent qui tourne en
continu elles ne sont pas équivalentes.

**Par abonnement** (`claude setup-token`) — inclus dans Pro, Max, Team,
Enterprise. Deux plafonds s'appliquent : une fenêtre glissante de 5 heures et
un **plafond hebdomadaire**. Trois conséquences pour ce projet :

- Le quota est **partagé avec ton propre usage de Claude** — l'appli, le web,
  tes autres sessions Claude Code. Ton agent et toi puisez dans le même seau.
- Il n'y a **pas de facturation au dépassement** : au plafond, ça s'arrête. Tu
  n'es pas prélevé, tu es bloqué jusqu'au reset.
- Donc un agent qui atteint le plafond **meurt en silence**, potentiellement
  pour plusieurs jours, au milieu de ton expérience.

**Par clé API** (Claude Console, `ANTHROPIC_API_KEY`) — facturation à l'usage.
Plus cher au token, mais l'agent ne s'arrête pas tout seul, et tu peux fixer
un plafond de dépense dans la Console. C'est ce que je recommande ici : la
prévisibilité vaut plus que le prix unitaire quand une expérience court sur
90 jours.

**Par OpenRouter** — c'est la variante que je recommande pour ce projet.
OpenRouter s'intercale entre Claude Code et l'API Anthropic et apporte
exactement ce qui manque à un agent qui tourne sans surveillance : un plafond
de dépense, une bascule automatique si un fournisseur est indisponible, et un
tableau de bord d'usage. Aucun proxy local à faire tourner, trois variables
d'environnement :

```
ANTHROPIC_BASE_URL=https://openrouter.ai/api
ANTHROPIC_AUTH_TOKEN=sk-or-...
ANTHROPIC_API_KEY=
```

Trois pièges : la base est `/api` et non `/api/v1` ; le jeton va dans
`ANTHROPIC_AUTH_TOKEN` ; et `ANTHROPIC_API_KEY` doit être **explicitement
vide**, sinon Claude Code la préfère et court-circuite tout.

Les identifiants de modèle prennent alors un préfixe de fournisseur
(`anthropic/claude-opus-5`). Mets à jour les trois `AGENT_MODELE*`.

**Garde des modèles Anthropic.** OpenRouter le dit lui-même : l'intégration
n'est garantie qu'avec le fournisseur Anthropic de première partie, et il
recommande de le placer en priorité haute. Voir §0 bis.

**Position mixte** : abonnement Max + crédits d'usage activés en secours, de
sorte que le dépassement bascule en facturation au lieu de couper.

Anthropic ne publie pas les seuils chiffrés et les a ajustés plusieurs fois en
2026. Le seul endroit qui donne ton état réel est **Réglages → Utilisation**.
Regarde-le tous les jours la première semaine.

## 0 bis. Pourquoi ne pas router vers des modèles moins chers

La tentation est évidente : puisqu'OpenRouter donne accès à tout, autant faire
tourner les tâches simples sur un modèle à 10 % du prix. Trois raisons de ne
pas le faire ici.

**Claude Code est un harnais, pas un client générique.** Ses invites système,
ses schémas d'outils et sa boucle d'agent sont réglés sur les sémantiques
Anthropic. OpenRouter précise que l'intégration peut ne pas fonctionner
correctement avec d'autres fournisseurs. Un modèle qui échoue sur l'appel
d'outils ne produit pas une réponse un peu moins bonne : il ne fait rien.

**Le cache de prompt est le vrai poste de coût**, pas le prix au token. Ton
agent relit le même cadre à chaque réveil ; sur un modèle qui cache mal ou
pas, un tarif affiché trois fois plus bas peut coûter plus cher à l'arrivée.
Le comportement du cache varie selon le modèle et le fournisseur.

**La pensée étendue ne fonctionne que sur les modèles Claude.** C'est ce dont
tu as besoin sur les réveils PLEIN, précisément ceux où l'agent arbitre.

La bonne granularité n'est donc pas « changer de fournisseur selon la
complexité », c'est **changer de modèle Claude selon la complexité** — ce que
le triage fait déjà.

### Le levier qui change l'ordre de grandeur

Le superviseur fait un **triage à trois niveaux** avant chaque battement de
fond. Un modèle bon marché lit le plan et le parking en lecture seule, et
répond :

| Verdict | Ce que ça veut dire | Modèle |
|---|---|---|
| `RIEN` | il attend l'extérieur, rien d'actionnable | aucun réveil |
| `SIMPLE` | de l'exécution : publier, relancer, ranger | Sonnet |
| `PLEIN` | il faut arbitrer, pas exécuter | Opus |

Un événement réel — message, courriel, paiement — court-circuite le triage et
part directement en réveil complet.

C'est ta granularité par complexité, et elle est interne à Anthropic. Actif
par défaut (`AGENT_TRIAGE=1`) ; ne le désactive pas avant d'avoir vu la
facture d'une semaine sans lui.

---

## 1. Ce qu'il faut ouvrir

Rien de tout ceci n'est instantané : les vérifications prennent de quelques
minutes à deux jours. Commence par là.

| | Quoi | Ordre de prix | Remarque |
|---|---|---|---|
| **Modèle** | Abonnement Claude ou compte Console | 20–200 €/mois, ou à l'usage | Voir §0. Le plan gratuit ne donne pas accès à Claude Code. |
| **Serveur** | Un VPS 1 vCPU / 2 Go, Debian 12 | 4–6 €/mois | Hetzner, Scaleway, OVH. Le superviseur ne fait qu'attendre. 2 Go pour Chromium. |
| **Domaine** | Le sien | ~10 €/an | Chez n'importe quel registraire. |
| **Boîte mail** | Une adresse dédiée avec IMAP | 0–3 €/mois | Sur son domaine de préférence. Évite Gmail : le compte Google ajoute des CGU et un risque de bannissement inutiles. |
| **Telegram** | Un bot via @BotFather | gratuit | Ton canal avec lui. |
| **Carte** | Virtuelle, plafond **dur** à 80 € | gratuit | Vérifie que c'est un blocage, pas une alerte. Sans rechargement auto, sans découvert. |
| **Encaissement** | Lien de paiement à ton nom | commission | Stripe si tu veux le webhook. Vérification d'identité : compte 24–48 h. |
| **Dépôt** | GitHub | gratuit | Public si tu veux l'expérience auditable. |

Total récurrent hors modèle : **environ 6 à 10 € par mois**. C'est ta dépense,
pas la sienne — elle ne touche pas aux 80 €.

---

## 2. Mettre le code sur GitHub

Le squelette t'arrive en `.zip`. Il ne contient aucun secret — tu peux le
manipuler sans précaution particulière.

**Depuis n'importe quel navigateur**, sans terminal :

1. Décompresse l'archive.
2. Sur github.com : *New repository*. Public si tu veux l'expérience
   auditable — c'est l'intérêt. Ne coche pas « Add a README ».
3. Sur la page du dépôt vide : *uploading an existing file*, puis glisse le
   **contenu** du dossier `agent-autonome` (pas le dossier lui-même). GitHub
   conserve l'arborescence.
4. *Commit changes*.

Avec un terminal, si tu en as un sous la main :

```bash
cd agent-autonome
git init && git add -A && git commit -m "cadre initial"
git branch -M main
git remote add origin git@github.com:<toi>/<dépôt>.git
git push -u origin main
```

## 3. Le serveur, en une commande

Prends un VPS Debian 12 ou Ubuntu 24.04, 1 vCPU / 2 Go. Connecte-toi en root
(SSH, ou la console web de l'hébergeur), puis :

```bash
curl -fsSL https://raw.githubusercontent.com/<toi>/<dépôt>/main/superviseur/installer.sh \
  -o installer.sh
bash installer.sh https://github.com/<toi>/<dépôt>.git sondomaine.fr
```

Le script installe Node, Caddy, Claude Code, Chromium, crée l'utilisateur
`agent`, clone le dépôt dans `/opt/agent`, pose le service systemd et prépare
`/etc/agent.env`. Il est relançable sans rien casser.

Si ton dépôt est privé, télécharge l'archive du dépôt plutôt que le fichier
brut, ou copie `installer.sh` à la main.

### Le droit de pousser

Le script te le rappelle à la fin, mais c'est la panne la plus fréquente et la
plus silencieuse :

```bash
sudo -u agent ssh-keygen -t ed25519 -C agent -N "" -f /home/agent/.ssh/id_ed25519
sudo -u agent cat /home/agent/.ssh/id_ed25519.pub
```

Colle la clé dans GitHub → *Settings* → *Deploy keys*, **avec accès en
écriture**. Sans ça, le superviseur commite localement sans jamais publier, et
tu ne t'en aperçois qu'au bout de trois jours de travail invisible.

### Authentifier le modèle

Recommandé — OpenRouter, rien à faire depuis un navigateur particulier :
colle les trois variables du §0 dans `/etc/agent.env`.

Par abonnement, il faut passer par `claude setup-token` sur une machine avec
navigateur, puis reporter le jeton dans `CLAUDE_CODE_OAUTH_TOKEN`.

---

## 4. Le canal Telegram

1. Écris à **@BotFather**, `/newbot`, récupère le jeton.
2. Envoie un message à ton bot depuis ton compte.
3. Ouvre `https://api.telegram.org/bot<JETON>/getUpdates` et relève le
   `chat.id`.

Le superviseur n'écoute que ce `chat_id`. Tout message que tu lui envoies
déclenche un réveil immédiat.

---

## 5. Le site

Caddy sert `site/` directement. Pas de CI, pas de déploiement — **l'agent
écrit un fichier, le site change**. L'installeur a déjà écrit le `Caddyfile`
si tu lui as passé un domaine.

Fais pointer l'enregistrement A du domaine sur l'IP du VPS ; Caddy obtient le
certificat TLS seul dans la minute qui suit.

Si l'agent choisit son propre nom de domaine plus tard, il suffit de refaire
pointer le A et de changer une ligne du `Caddyfile`.

---

## 6. La configuration

```bash
cp /opt/agent/superviseur/config.exemple.env /etc/agent.env
chmod 600 /etc/agent.env && chown root:root /etc/agent.env
nano /etc/agent.env
```

À remplir : jeton Claude, jeton et chat_id Telegram, adresse et mot de passe
IMAP, numéro de carte, jeton du webhook.

**Rien de tout ça ne doit exister dans le dépôt.** Si le dépôt est public,
active en plus la protection anti-secrets côté GitHub.

Renseigne aussi, dans le dépôt cette fois : le domaine dans `cadre/OUTILS.md`
et `cadre/MISSION.md`, et l'identité dans `etat/COMPTES.md`.

---

## 7. Démarrer

```bash
systemctl enable --now agent
journalctl -u agent -f
```

Tu dois voir « superviseur démarré », recevoir un message Telegram, puis un
premier réveil.

### Vérifier que ça marche vraiment

- Écris-lui sur Telegram → un réveil doit partir dans les secondes.
- Envoie un mail à son adresse → réveil dans la minute qui suit le relevé.
- Regarde `git log` : un commit par réveil productif.
- Regarde `etat/rythme.json` : il doit changer et s'expliquer.

---

## 8. L'encaissement

Crée un lien de paiement à ton nom et donne-lui l'URL — il la placera où il
veut.

Pour le webhook, pointe ton prestataire sur `http://<ip-vps>:8787` avec
l'en-tête `X-Jeton` correspondant à `AGENT_WEBHOOK_JETON`. Un paiement le
réveille alors immédiatement. Passe par Caddy en reverse-proxy si tu veux du
TLS dessus.

Sans webhook, c'est toi qui inscris les paiements dans `etat/REGISTRE.md` — et
il avance à l'aveugle entre deux de tes passages sur le seul chiffre qui
compte.

---

## 9. Avant de le lâcher

- [ ] Plafond de dépense fixé côté Console, ou crédits d'usage activés
- [ ] Carte à 80 € testée sur un petit achat, plafond confirmé comme **dur**
- [ ] `/etc/agent.env` en 600, aucun secret dans `git log`
- [ ] Telegram fonctionne dans les deux sens
- [ ] Le domaine sert bien `site/` en HTTPS
- [ ] Tu sais l'arrêter : `systemctl stop agent`
- [ ] Tu as lu `cadre/CONSTITUTION.md` en entier — c'est le seul garde-fou

---

## Ce que tu vas rater le premier jour

Par ordre de fréquence :

1. **Le nom du modèle.** `AGENT_MODELE` doit correspondre à un identifiant
   valide. Le log te le dira.
2. **Playwright sans les dépendances système.** `--with-deps` n'est pas
   optionnel, et Chromium tient mal dans 1 Go.
3. **IMAP refusé.** Beaucoup de fournisseurs exigent un mot de passe
   d'application distinct du mot de passe du compte.
4. **Git qui ne pousse pas.** Voir la clé de déploiement au §3. Sinon le
   superviseur commite sans jamais publier — et tu ne t'en aperçois qu'au bout
   de trois jours.
5. **`claude: command not found` dans les journaux systemd.** L'installeur
   natif pose la commande dans `~/.local/bin`, que systemd n'a pas dans son
   PATH. Le fichier `agent.service` fourni règle ça ; si tu l'as réécrit à la
   main, remets `Environment=PATH=` et `Environment=HOME=`.
