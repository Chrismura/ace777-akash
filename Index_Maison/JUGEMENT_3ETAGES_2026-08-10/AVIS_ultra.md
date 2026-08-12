# AVIS ULTRA (via OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte) — ultra.analyse — COMPLET (relance)

# ANALYSE ULTRA — SETUP 3 ÉTAGES (GROK)  
**Contexte** : Phase 0 validée. Hub intouchable (11435, 9 providers). 27 services → cible 12-14. C1-C6 + Loi 1quinquies. Mode probatoire C6 (1 action/jour). RAM 8 Go.  
**Posture** : Critique, factuelle, sans complaisance. Aucune exécution sans double signature.

---

## 1. SETUP GLOBAL — CORRECT, COMPLET, SÛR ? ÉTAPE CRITIQUE MANQUANTE ?

**NON.** Le setup n’est **ni complet ni sûr** en l’état. Trois trous majeurs :

| Trou | Pourquoi c’est bloquant |
|------|-------------------------|
| **Inventaire des 27 services absent** | Grok liste « 4 agents métier, mémoire, observabilité » + hub + prise-ia + cockpit-http + cockpit-pont = ~10. Les 17 autres ? Noms, labels, dépendances ? On ne fusionne/supprime pas à l’aveugle. |
| **Graphe de dépendances absent** | `cockpit-http` / `cockpit-pont` / `prise-ia` / agents métier : qui appelle qui ? Qui écrit où ? Supprimer 10-12 services « monitoring/tri » sans graphe = casser la prod. |
| **Étape CODEUR (Loi 1quinquies) sautée** | Grok passe de « Validation spec » (Étape 1) à « Création fichiers + load » (Étape 2). **Où est l’écriture du code par le codeur ?** La Loi 1quinquies impose : SPEC → Validation → **CODEUR** → Grille → Exécution. L’étape 2 de Grok *est* l’exécution, pas le code. |

**Étape critique manquante** : **Inventaire exhaustif + Graphe de dépendances + Spécification technique détaillée pour le codeur** (interfaces, formats `state.json`, blacklist, seuils RAM, signaux POSIX). Sans cela, toute fusion est un pari.

---

## 2. SUPERVISEUR UNIQUE — BONNE CONCEPTION ? QUELS SERVICES FUSIONNER/SUPPRIMER ?

**Conception : PARTIELLEMENT BONNE, DÉFAUTS ARCHITECTURAUX MAJEURS.**

| Point | Verdict | Détail |
|-------|---------|--------|
| **`KeepAlive: false` + `ThrottleInterval: 1800`** | **DANGEREUX** | Si le superviseur crashe (OOM, bug Python), **aucune relance pendant 30 min**. Aucun heartbeat visible actuellement. Le superviseur *doit* avoir `KeepAlive: true` (avec `ThrottleInterval` anti-boucle) **OU** un watchdog externe (mais ça ajoute un service). |
| **C1 : `chmod 444` auto sur déviation** | **INTERDIT** | Un superviseur qui modifie les droits `chmod 444` sur des fichiers « critiques » : 1) nécessite souvent `root` (LaunchAgent = user), 2) casse les apps légitimes qui écrivent (config, cache), 3) action irréversible sans audit. **C1 = détection + alerte + blocage écriture (via `chflags uchg` ou ACL), pas modification auto.** |
| **C6 Probatoire vs Boucle 30 min** | **CONTRADICTION** | Boucle 30 min = 48 cycles/jour. C6 = « 1 action autonome/jour max ». Si le superviseur détecte un service mort au cycle 3 → action (unload) = quota C6 épuisé. Cycle 4 : hub down → **superviseur paralysé, ne peut pas alerter/fallback**. Il faut : soit C6 = « 1 *type* d’action/jour », soit mode « observation seule » (dry-run) pendant la phase probatoire, soit compteur journalier persistant dans `state.json`. |
| **RAM < 25 Mo (Python + psutil + requests)** | **RISQUÉ** | Sur macOS, un script Python minimal avec `psutil` + `requests` + `json` + logging tourne ~35-50 Mo RSS. Cible < 25 Mo = **Cython / Rust / Go** ou Python *très* épuré (stdlib only, `urllib`, `subprocess` pour `vm_stat`/`launchctl`). |
| **Fusion « 10-12 services redondants »** | **FLOU** | Il faut la **liste explicite des 27 labels** + décision par label : `CONSERVER` / `FUSIONNER_DANS_SUPERVISEUR` / `SUPPRIMER`. Exemple : `com.ace777.heartbeat` → FUSIONNER. `com.ace777.jauge-8898` → SUPPRIMER (déjà fait). `com.ace777.surveillance-quotas` → FUSIONNER. Les 10 autres ? |

**Services à fusionner/supprimer (nécessite l’inventaire) — Principe :**
- **Fusionner dans Superviseur** : tout ce qui fait *heartbeat*, *healthcheck*, *quota RAM*, *surveillance fichiers*, *blacklist*, *watchdog*.
- **Supprimer** : doublons, services « tri » (si batch non critique), jauge remnants.
- **Conserver hors Superviseur** : Hub (intouchable), `prise-ia` (métier), `cockpit-http`/`pont` (API temps réel), agents métier (prod), mémoire/observabilité (si distincts du superviseur).

---

## 3. COCKPIT.PY — BONNE APPROCHE ? COMPATIBLE COCKPIT-HTTP/PONT ?

**Approche CLI unique : BONNE.**  
**Compatibilité : CONFLIT NON RÉSOLU.**

| Point | Analyse |
|-------|---------|
| **`cockpit-http` / `cockpit-pont` sont des services launchd VIVANTS** | Grok dit « Conservés » à l’étape 2, puis « remplacés progressivement » à l’étape 4. **Conflit de ports / données** : si `cockpit-http` écoute un port HTTP et `cockpit.py --etat` lit `launchctl list`, les deux coexistent mais doublonnent la surveillance. |
| **Remplacement progressif** | Nécessite : 1) `cockpit.py` expose *au moins* la même API (JSON sur stdout ou fichier `state.json`), 2) bascule des consommateurs (famille, scripts) vers `cockpit.py`, 3) **ensuite** `launchctl unload` des deux services. |
| **Intégration Superviseur** | Grok : « Pas de service launchd dédié (inté
