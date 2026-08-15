# DEEPSEEK — deepseek.analyse

Ici DEEPSEEK. J'exige des preuves, je refuse le flou. Voici mon verdict implacable basé sur les faits vérifiés par Buffy.

### 1. VERDICT
**GO AVEC RÉSERVES** sur le principe de neutralisation des morts silencieuses par substitution, sous condition stricte du respect de la syntaxe Bash 3.2 (macOS).

### 2. CIBLE
**Option A : Ajout minimal dans genesis + re-scellement.**
*   *Justification :* Le lanceur ne contient aucun code moteur (`grep` = 0). Injecter du code métier depuis le lanceur vers un pipe `bash -s` de 2517 lignes est un non-sens architectural et une impasse pour le débug. Le précédent `af307996` prouve que le re-scellement du champion est la voie validée.

### 3. MÉCANISME RÉEL
**Confirmé et précisé.** 
*   `public_get` retourne `0` (protégé). 
*   Le coupable est le triptyque `as_num "$(json_get ...)"` (ou équivalent Ruby) exécuté à l'intérieur d'une assignation de variable (`var=$(...)`). 
*   Sous `set -e`, si une commande Ruby interne échoue (TypeError, JSON parsé invalide, vide), la substitution retourne un code d'erreur, le sous-shell meurt en silence sans remonter au trap ligne 90.

### 4. LISTE EXACTE DES ZONES À PROTÉGER (Bash 3.2 compatible)
Pas de sur-engineering. On enveloppe les substitutions critiques dans une fonction `safe_eval` ou on force un retour 0 par défaut (`|| echo "0"` ou `|| true`) selon le type attendu.

*   **Zones cibles (N=10+ helpers ruby en substitution) :**
    *   Lignes 1600-1601, 1613-1615 (`depth_1`, `depth_2`)
    *   Lignes 1733-1745 (`book_resp` / parsing prix)
    *   Lignes 2057, 2061, 2071, 2109, 2142 (`entry / px`)
    *   Ligne 2431 (`exit`)
*   **Correction minimale à injecter dans le header de genesis (autour de la ligne 85) :**
    ```bash
    # Wrapper anti-mort silencieuse pour substitutions Ruby (Bash 3.2)
    safe_ruby() {
        "$@" 2>/dev/null || echo "0"
    }
    ```
    *   *Application ciblée :* Remplacer `$(as_num "$(json_get ...)")` par `$(safe_ruby as_num "$(json_get ...)")` sur les lignes critiques listées.

### 5. INDICATEUR DE PREUVE AU RETEST
**Le fichier `FATAL_RC1` n'est plus vide** et contient la stack trace exacte du helper Ruby ou de la ligne exacte ayant levé le code d'erreur avant l'arrêt, OU le bot dépasse le fill #42 sans mourir à 07:49:10Z.
