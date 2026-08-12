# AVIS DEEPSEEK (via NVIDIA build.nvidia.com (100+ modeles), task mission) — 2026-08-11T14:23:36

# VALIDATION COCKPIT ACE777 — ANALYSE CRITIQUE

## 1. INcASSABLE — Scénarios de panne et comportement actuel

### Scénario A : Bridge down (port 17777)
**Comportement actuel** : Cockpit JS fait fetch vers bridge → échec réseau → pas de données affichées. Le cockpit devient une coquille vide.
**Problème** : Aucun fallback côté front. Pas de cache local, pas de mode dégradé.
**Verdict** : **INSUFFISANT** — le cockpit muet est pire que pas de cockpit.

### Scénario B : Hub down (port 11435)
**Impact** : veille_hub.py échoue sur toutes les sources (timeout 20-25s chacun → 9 sources × 25s = 225s max). Le fichier VEILLE_HUB_<date>.md n'est pas créé.
**Comportement actuel** : brief_offres.py lit un fichier absent → sortie silencieuse code 0. OK pour le brief, mais le cockpit affiche « veille pas encore passée » même si la veille a échoué.
**Problème** : Pas de distinction entre « veille pas passée » et « veille a échoué ». L'utilisateur ne sait pas si c'est un problème ou juste tôt.
**Verdict** : **MOYEN** — silencieux mais trompeur.

### Scénario C : Fichier veille corrompu (JSON mal formé, sections cassées)
**Comportement actuel** : veille_hub.py écrit en Markdown, pas en JSON. Si le fichier est tronqué (crash pendant écriture), brief_offres.py peut parser des sections incomplètes.
**Problème** : Pas de validation de structure avant traitement. Pas de mécanisme de détection de fichier partiel.
**Verdict** : **INSUFFISANT** — un fichier tronqué peut produire un brief vocal avec des offres incomplètes.

### Scénario D : JS exception dans le cockpit
**Comportement actuel** : Node --check passe, mais une erreur runtime (ex: fetch timeout non géré, JSON.parse sur réponse vide) peut geler tout le rendu.
**Problème** : Pas de try/catch global, pas de gestion d'erreur par section. Une seule section qui plante peut tuer tout le dashboard.
**Verdict** : **INSUFFISANT** — pas de séparation des erreurs par composant.

### Scénario E : Quota épuisé (openrouter, nvidia, etc.)
**Comportement actuel** : try/except par source → la source échoue, les autres continuent. Le rapport marque la section en erreur.
**Problème** : Pas de mécanisme de backoff ou de retry. Si le quota est épuisé à 07:00, la veille est perdue pour la journée.
**Verdict** : **MOYEN** — pas bloquant mais pas auto-réparant.

### Scénario F : Bridge lancé mais pas de fichier CHOIX_OFFRES.json
**Comportement actuel** : POST /decoller écrit atomiquement (tmp+replace). Si le répertoire n'existe pas ou est en lecture seule → exception non gérée.
**Problème** : Pas de vérification de permissions avant écriture.
**Verdict** : **INSUFFISANT** — crash silencieux possible.

---

## 2. RÉSILIENT — Ce qui manque

### 2.1 Cache local systématique
- **Manquant** : Le cockpit devrait lire un cache local (dernier état connu) si le bridge est down.
- **Concret** : `cockpit_http_server.py` sert un JSON statique mis à jour à chaque POST /decoller et GET /offres réussi. Le front lit ce JSON en fallback.

### 2.2 Timeouts front
- **Manquant** : Les fetch JS n'ont pas de timeout explicite. Un bridge qui répond lentement (pas down, juste lent) peut geler le rendu indéfiniment.
- **Concret** : `AbortController` avec timeout 5s sur chaque fetch.

### 2.3 Dégradation progressive
- **Manquant** : Si une section du dashboard échoue, les autres doivent continuer.
- **Concret** : try/catch par bloc de rendu, affichage d'un placeholder « ⚠ section indisponible » au lieu de tout casser.

### 2.4 Données en cache pour le brief vocal
- **Manquant** : Si la veille échoue à 07:00, brief_offres.py sort silencieusement. Mais si la veille d'hier existe, pourquoi ne pas la relire ?
- **Concret** : brief_offres.py lit le dernier VEILLE_HUB_*.md disponible si le fichier du jour est absent, avec mention « données d'hier ».

---

## 3. AUTO-RÉPARANT — Ce qui doit se réparer seul

### 3.1 Relance automatique du bridge
- **Actuel** : launchd KeepAlive est configuré, mais pas vérifié.
- **Concret** : Ajouter un health-check dans `cockpit_http_server.py` qui ping le bridge toutes les 60s. Si down → relance via `launchctl kickstart -k`. Log dans un fichier dédié.

### 3.2 Nettoyage des fichiers orphelins
- **Actuel** : Les `.bak-*` s'accumulent. Pas de purge.
- **Concret** : Script de purge quotidien (cron ou launchd) qui supprime les `.bak-*` de plus de 7 jours.

### 3.3 Fichier veille corrompu → régénération
- **Actuel** : Si VEILLE_HUB_<date>.md est corrompu, rien ne se passe.
- **Concret** : veille_hub.py écrit d'abord dans un fichier temporaire, puis rename atomique. Si le fichier du jour existe mais est vide/corrompu → relance automatique de la veille (max 2 tentatives).

### 3.4 Quota épuisé → retry différé
- **Actuel** : Une source en erreur quota est perdue pour la journée.
- **Concret** : veille_hub.py retente les sources en erreur à 12:00 et 18:00 (3 passages max). Les résultats s'ajoutent au rapport existant.

---

## 4. AUTO-ADAPTATIF — Le maillon manquant

**Constat** : La veille détecte de nouveaux providers (github, hf, rss) et les affiche dans le panneau exploration. Mais **rien ne les rend testables automatiquement**.

**Le maillon manquant** : Il n'y a pas de pipeline « découverte → intégration → test ».

**Concret** :
1. **Détection** : veille_hub.py identifie un nouveau provider (ex: `inferx` découvert hier).
2. **Intégration** : Un script `integrate_provider.py` (à créer) :
   - Ajoute le provider à `providers.json` avec un statut `pending`.
   - Génère un template de test (endpoint, clé API placeholder, modèle par défaut).
3. **Validation** : `eval_offres.py` inclut les providers `pending` en mode observation uniquement (jamais actif).
4. **Promotion** : Après 3 jours sans erreur en observation → passage en `active`.

**Actuellement** : Ce pipeline n'existe pas. La découverte est passive (affichage) mais pas active (intégration).

---

## 5. AUTO-INTELLIGENT — 3 améliorations à plus forte valeur

### 5.1 Score de fiabilité par source
- **Mécanique** : Chaque source de veille accumule un score (nb de succès / nb de tentatives sur 30 jours).
- **Usage** : Le cockpit affiche le score à côté de chaque section. Les sources avec score < 0.5 sont automatiquement rétrogradées en bas de liste.
- **Valeur** : Évite de perdre du temps sur des sources peu fiables.

### 5.2 Détection de doublons intelligente
- **Mécanique** : Avant d'ajouter une offre au rapport, comparer avec les 7 derniers rapports (hash du nom du modèle + provider).
- **Usage** : Les offres déjà vues sont marquées « déjà vu » et ne comptent pas dans le compteur de nouveautés.
- **Valeur** : Évite la fatigue de veille (le même modèle qui revient chaque jour).

### 5.3 Alerte de dérive de justesse
- **Mécanique** : Le bridge calcule la justesse moyenne sur 7 jours. Si elle chute de plus de 20% par rapport à la moyenne 30 jours → alerte dans le cockpit + log.
- **Usage** : Détecte une dégradation progressive du hub (ex: un provider qui se dégrade sans crash).
- **Valeur** : Anticipe les pannes avant qu'elles ne deviennent critiques.

---

## 6. VERDICT FINAL

Le système est **fonctionnel** et **bien structuré** pour un usage quotidien. Mais il n'est **PAS incassable** : les scénarios de panne les plus probables (bridge down, fichier corrompu, JS exception) ne sont pas couverts. Le maillon auto-adaptatif est incomplet (découverte sans intégration).

Les garde-fous à renforcer en priorité :
1. Cache local côté cockpit (fallback si bridge down).
2. Timeouts front + try/catch par section.
3. Écriture atomique + validation du fichier veille.
4. Pipeline découverte → intégration → test.
5. Health-check du bridge avec relance automatique.

Le système est **prometteur** mais **pas encore prêt** pour une utilisation avec de l'argent réel sans supervision humaine.

VERDICT FINAL : GARDER AVEC GARDE-FOUS RENFORCES
CONFIANCE : moyenne
