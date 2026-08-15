# INFERX — inferx.analyse

INFERX / ACE777 — Analyse des flux internes, garde-fous et chemins d'erreur.

### 1. VERDICT
**GO AVEC RÉSERVES** sur le principe de neutralisation des substitutions à risque.

---

### 2. CIBLE
**Option A : Ajout minimal dans `genesis_manifest.txt` + RE-SCELLEMENT du champion.**
* **Justification :** Le lanceur (`launch_test_master_base_v8_5_impact.sh`) est un simple passe-plat (`tail -n +85 | bash -s`). Injecter la logique depuis le lanceur pour modifier le comportement de sous-shells imbriqués profonds dans le pipe est un piège bash (problèmes de portée, d'expansion et d'interprétation). Puisque le champion est INTANGIBLE (C1) et que le précédent du trap ligne 90 a déjà validé la procédure de re-scellement (`af307996`), l'Option A est la seule voie robuste, auditable et pérenne.

---

### 3. MÉCANISME RÉEL
**Confirmé à 100%.**
* `public_get` renvoie `0` quoiqu'il arrive (filet `NET_RETRY_EXHAUSTED -> return 0`).
* Le piège mortel réside dans les **substitutions imbriquées** (ex: `p1="$(as_num "$(json_get "$p1_resp" "price")")"`). Si `json_get` ou `as_num` échoue (Ruby absent, JSON invalide, clé absente, chaîne vide) et retourne un `rc != 0`, le `set -e` actif dans le sous-shell provoque une **mort silencieuse immédiate** (le trap `ERR` ligne 90 ne se propageant pas hors des `$(...)`).

---

### 4. LISTE EXACTE DES ZONES À PROTÉGER (Bash 3.2 macOS)
Création d'un helper universel `safe_call` directement dans les définitions de `genesis` (autour de la ligne 690), puis enveloppement des 10 points critiques identifiés.

* **Helper à injecter (dans genesis, section helpers ~ligne 690) :**
  ```bash
  safe_call() {
      "$@" 2>/dev/null || echo "0"
  }
  ```
* **Points critiques à corriger (remplacement du pattern nu par `safe_call`) :**
  Lignes **1600, 1614, 1734, 1735, 2057, 2061, 2071, 2109, 2142, 2431** (les patterns `$(as_num "$(json_get ...)")` et similaires).
  * *Exemple de transformation :*
    Avant : `p1="$(as_num "$(json_get "$p1_resp" "price")")"`
    Après : `p1="$(safe_call as_num "$(safe_call json_get "$p1_resp" "price")")"`

---

### 5. INDICATEUR DE PREUVE AU RETEST
* **Indicateur unique :** L'absence de sortie brutale en `rc=1` à ~07:49Z (ou après le fill #42) dans les logs, couplée à l'écriture effective d'un fallback `0` ou d'un log d'erreur explicite dans le fichier de crash dump si un helper échoue, confirmant que le flux survit à une anomalie Ruby/JSON.
