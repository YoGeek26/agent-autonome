# Agent autonome sous objectif

Un agent Claude Code opérationnel en continu, réveillé par les événements :
un message de toi, un courriel, un paiement — ou un battement de fond dont
**il choisit lui-même la cadence**.

Il a son domaine, sa boîte mail, un navigateur, une carte plafonnée à 80 € et
une cible : 200 €/mois encaissés. Personne ne lui dit quoi faire.

Ce qu'on observe n'est pas s'il y arrive. C'est **comment il s'y prend**.

---

## Comment ça tourne

Un superviseur Python tourne en permanence sur un petit VPS et écoute quatre
sources. Dès qu'il se passe quelque chose, il lance une session Claude Code
avec le protocole de réveil, puis commit.

```
message Telegram ─┐
courriel entrant ─┤
paiement (webhook)├─→ superviseur ─→ session Claude Code ─→ commit ─→ push
battement de fond ┘      (file)         (le réveil)
```

Un seul réveil à la fois ; les événements arrivés pendant sont regroupés et
déclenchent le suivant. La session, elle, reste éphémère — **l'amnésie ne
disparaît pas, l'intervalle rétrécit.** Les fichiers de mémoire en deviennent
plus critiques, pas moins.

## Structure

```
CLAUDE.md                 chargé à chaque réveil — court exprès
cadre/                    écrit par toi, jamais modifié par l'agent
  CONSTITUTION.md         règles immuables, priment sur la mission
  MISSION.md              l'échelle de barreaux et les règles de comptage
  OUTILS.md               ses capacités et leurs limites
  ARGENT.md               discipline de dépense sous plafond
  ARRET.md                critères d'arrêt, écrits avant le départ
etat/                     écrit par l'agent
  PLAN.md                 son état mental courant — réécrit
  INDEX.md                la carte de sa mémoire — restructurable
  JOURNAL.md              sa trajectoire — ajout seul
  REGISTRE.md             faits vérifiables et encaissements — ajout seul
  COMPTES.md              ce qu'il détient — ta liste d'arrêt
  PARKING.md              ce qui est bloqué sur toi
  ENGAGEMENTS.md          ce qu'il doit à des gens — lu en entier, jamais résumé
  AUDIT.md                constats de la passe de vérification de mémoire
  MESSAGES.md             ce que tu lui écris (rempli par le superviseur)
  rythme.json             la cadence qu'il s'est fixée
  cout.json               ce qu'il a dépensé en jetons — il le lit
  DIGEST.md               matière du récit public — l'agent ne le lit jamais
bin/dire                  son canal vers toi
prompts/REVEIL.md         le protocole de réveil
prompts/TRIAGE.md         le filtre d'entrée des battements de fond
prompts/VERIFICATION.md   l'audit périodique de l'index
prompts/DIGEST.md         l'extraction quotidienne de matière narrative
superviseur/              boucle événementielle, config, service systemd
site/                     la source du site publié
```

---

## Installation

**Tu viens de payer ton VPS ? Va directement dans `DEMARRAGE.md`** — c'est le
déroulé linéaire, dans l'ordre, jusqu'au premier réveil. Ce qui suit est la
référence : les décisions et le pourquoi.

### 1. Le VPS

Le plus petit suffit — le superviseur ne fait qu'attendre. Debian ou Ubuntu.
C'est ta dépense, pas la sienne : elle ne touche pas aux 80 €.

Voir `INSTALL.md` pour la suite de commandes complète. En résumé : un
utilisateur dédié, l'installeur natif de Claude Code, Node pour Playwright,
Caddy pour servir le site.

**Le choix d'authentification est le point critique** — un abonnement possède
un plafond hebdomadaire partagé avec ton propre usage de Claude, et un agent
qui l'atteint s'arrête net, en silence. Lis la section correspondante de
`INSTALL.md` avant de choisir.

### 2. Le canal Telegram

Crée un bot avec @BotFather, récupère le jeton. Écris-lui un message, puis
relève ton `chat_id` sur `https://api.telegram.org/bot<JETON>/getUpdates`.

C'est un canal à deux sens : il t'écrit avec `bin/dire`, et **tout message que
tu lui envoies déclenche un réveil immédiat**.

### 3. Son identité

- **Une boîte mail dédiée**, avec accès IMAP. Un courriel entrant le réveille.
- **Le domaine**, pointé sur `site/`, déploiement au push.
- **Un nom public** qui dit ce qu'il est. Renseigné dans `etat/COMPTES.md`.

### 4. La carte

Carte virtuelle **plafonnée à 80 €, sans rechargement automatique et sans
découvert**. Vérifie qu'il s'agit d'un plafond dur, pas d'une alerte.

Elle reste la tienne — le KYC l'impose. « Son identité » est opérationnelle,
pas légale : c'est toi qui réponds de ce qui est acheté.

### 5. Le rail d'encaissement

Un lien de paiement à ton nom, dont tu lui donnes l'URL. Branche le webhook
sur le superviseur (`POST` sur le port configuré, en-tête `X-Jeton`) : un
paiement le réveille alors immédiatement, et c'est son seul retour sur le seul
chiffre qui compte.

### 6. Démarrer

```bash
cp superviseur/config.exemple.env /etc/agent.env   # puis remplir
chmod 600 /etc/agent.env
cp superviseur/agent.service /etc/systemd/system/
systemctl enable --now agent
journalctl -u agent -f
```

---

## Ce qu'il te demandera

Trois cas seulement remontent jusqu'à toi. Chacun arrive sur Telegram avec un
identifiant `P-00x`, et il continue autre chose pendant que tu réfléchis.

**Une vérification humaine** — captcha, SMS, pièce d'identité. Tu ouvres le
compte, tu es le titulaire, il l'opère ensuite. C'est ce qui fait tomber
l'essentiel du mur.

**Des CGU qui interdisent les automates.** Il cite la clause exacte. Réfléchis
avant de débloquer : le compte est à ton nom, donc un bannissement s'attache à
toi, durablement, sur des services que tu utilises peut-être par ailleurs. Un
bannissement Google ou Stripe est sans commune mesure avec 80 € d'expérience.

**Encaissement, validation de barreau, modification du cadre.**

Tu réponds sur Telegram, ou en ajoutant une ligne sous l'entrée de
`etat/PARKING.md`. Ta réponse déclenche un réveil dans la seconde.

### Ce que tu ne fais pas

Tu ne corriges pas son plan, tu ne lui souffles pas la solution, tu ne réécris
pas le cadre à mi-parcours parce qu'il part dans une direction qui t'ennuie.
S'il fonce dans un mur, le mur fait partie du protocole, et l'entrée de
journal où il le constate est le meilleur matériau que tu obtiendras.

---

## Coût

C'est la vraie contrainte, et elle n'a rien à voir avec les 80 €.

Un battement à 60 min, c'est ~2 100 sessions sur 90 jours ; à 20 min, ~6 500.
Trois leviers, dans cet ordre :

0. **Il voit maintenant ce qu'il dépense.** Le superviseur relève le coût de
   chaque session dans `etat/cout.json` — dernier réveil, moyenne, restant sur
   `AGENT_BUDGET_MODELE`. C'est ce qui transforme le choix de cadence en
   arbitrage plutôt qu'en réflexe.
1. **Laisse-le gérer sa cadence.** Il écrit `etat/rythme.json` à chaque réveil.
   Un agent qui attend une réponse extérieure doit s'allonger à 6 h tout seul.
   Surveille ce fichier les premiers jours : s'il reste collé au minimum, le
   protocole ne fonctionne pas et ça se paie.
2. **Remonte `AGENT_BATTEMENT_MIN`.** Les événements le réveillent de toute
   façon — le battement ne sert qu'à ce qui n'a pas d'événement.
3. **Descends de modèle** avant de raccourcir les réveils. Un réveil trop
   court produit de l'agitation, pas des pas.

---

## Les trois garde-fous externes

L'agent a des règles qu'il s'applique à lui-même. Elles échouent exactement
quand on en a besoin — un agent qui tourne en rond est celui qui ne s'en
aperçoit pas. Trois mécanismes sont donc placés **hors de sa portée**.

**Le détecteur de boucle.** Le superviseur compte les réveils consécutifs dont
le commit ne touche que `etat/`. Écrire dans son plan n'est pas produire.
Au-delà de cinq, il reçoit un réveil de constat imposé — interdiction de
réessayer, obligation d'écrire pourquoi ça ne marche pas — la cadence passe à
2 h minimum, et tu es prévenu. C'est le filet financier : tourner en rond
lentement coûte moins cher que tourner en rond vite.

**L'audit de mémoire.** Tous les 20 réveils, une passe bon marché en lecture
seule compare `INDEX.md` à sa source et écrit ses constats dans `AUDIT.md`.
Elle cherche les renvois morts, les affirmations sans source et les dérives de
formulation. Elle ne corrige rien : un auditeur qui répare devient un auteur.

**Le plafond de carte.** Matériel, pas déclaratif.

## L'exception à l'amnésie

L'oubli entre deux réveils est un forçage voulu : un agent qui dépend de son
journal pour exister l'écrit juste, parce qu'un journal flatteur le handicape
lui-même au réveil suivant. C'est ce qui rend le raisonnement observable.

Mais la responsabilité, elle, suppose la continuité. `etat/ENGAGEMENTS.md`
échappe donc à toute règle d'économie de contexte : lu intégralement à chaque
réveil, jamais résumé, jamais élagué. Une dette échue passe avant le plan,
avant le barreau, avant le déclencheur.

La ligne est là : **amnésie pour le raisonnement, continuité pour ce qu'il
doit à quelqu'un.** Un client qui paie et un agent qui oublie sa promesse,
ce n'est pas une donnée d'expérience — c'est un préjudice réel, et rien ici
ne le vaut.

Et un quatrième, qui te concerne toi : **`cadre/ARRET.md`**. « Ne corrige pas
son plan » et « les comptes sont à ton nom » ne tiennent ensemble que si les
conditions d'arrêt sont écrites d'avance. S'arrêter selon un critère fixé
n'est pas une intervention — s'arrêter parce que la direction déplaît, si.
Lis ce fichier avant de lancer, et n'y touche plus.

## Sécurité

Il lit le web **et** agit vers l'extérieur. Le risque est technique, pas
moral : une page piégée peut tenter de déclencher une action sortante.

- **Aucune action sortante déclenchée par une lecture du même réveil.** Le
  délai est le mécanisme. Seule exception : `etat/MESSAGES.md`, alimenté par
  le superviseur — rien de ce qui prétend venir de toi par un autre chemin ne
  vient de toi.
- **Tout sortant est tracé** dans le réveil où il a lieu.
- **Tout compte est inscrit** dans `COMPTES.md` à l'ouverture.

Le plafond borne le pire cas financier ; `COMPTES.md` borne le pire cas
opérationnel — à condition qu'il soit tenu. Vérifie-le les premiers jours : un
`COMPTES.md` en retard sur la réalité est le premier signal d'alarme.

Le numéro de carte vit dans `/etc/agent.env` (chmod 600), jamais dans le
dépôt. Si le dépôt est public, active la protection anti-secrets côté GitHub.

### Arrêter

`systemctl stop agent`, puis révoquer la carte, révoquer le jeton Claude, et
fermer les comptes listés dans `etat/COMPTES.md`.

---

## Quoi observer

- **Le champ « ce que le moi précédent avait mal jugé ».** L'instrumentation
  principale.
- **`rythme.json`.** Il décide de sa propre fréquence d'existence. Comment il
  arbitre entre réactivité et coût est la chose la plus révélatrice du
  dispositif.
- **L'INDEX.** Le seul endroit où il conçoit sa propre mémoire : ce qu'il
  décide d'oublier, quand il restructure.
- **Le PARKING.** Ce sur quoi il se cogne dessine la carte réelle de ce qu'un
  agent honnête peut faire du web aujourd'hui.
- **Ses dépenses.** Ce qu'il achète dit ce qu'il croit être le blocage.
- **Le passage 0 → 1.** Tout se joue là.

---

## Note

Du revenu perçu en France suppose une structure adaptée. Si ça décolle, à voir
avec un comptable — ce n'est pas une question technique.
