# GEMINI — gemini.analyse

Compris. En tant qu'auditeur en chef ACE777, je vais droit au but. Pas de complaisance, analyse chirurgicale.

---

### 1. Verdict global
**NON**. La cause racine de la mort silencieuse n'est pas corrigée ; tant qu'elle persiste, relancer est un aveuglement.

### 2. La commande la plus probablement fautive
Les lignes **1599-1601 / 1613-1615** (`public_get` pour `depth_1`/`depth_2` via `curl_with_retry`). 
* **Justification :** Le timing correspond exactement (les 9 secondes de silence avant la mort englobent le timeout ou les 3 essais de `curl_with_retry` avec pauses). Si l'API publique tousse ou rate 3 fois, `curl_with_retry` renvoie un exit code non nul. Sans protection, sous `set -e`, cela tue le processus immédiatement sans laisser de trace textuelle si le stderr est redirigé/avalé.

### 3. Pourquoi le trap ERR n'a pas écrit FATAL_RC1
Sous `set -euo pipefail` et dans un pipeline (`... | while ...`), le trap `ERR` **ne s'hérite pas** dans les sous-shells, les blocs exécutés dans des pipelines, ou lors de l'évaluation de commandes conditionnelles/substitutions de commandes si elles font partie d'une logique de test implicite (ex: `var=$(...)` ou `cmd || true` manquant). De plus, bash n'active pas les traps `ERR` à l'intérieur des fonctions ou des boucles imbriquées de la même manière selon la version (macOS embarque souvent un vieux bash 3.2 où la gestion des traps dans les boucles/pipelines est notoirement défaillante).

### 4. Correctif GO-sized borné (bash 3.2 macOS)
Ne pas toucher à `genesis_manifest.txt` (règle d'or). On isole le correctif dans un wrapper de fonction ou une redéfinition locale pour sécuriser les appels `public_get` / `json_get` dans la boucle principale.

Ajouter juste avant la boucle ou dans un fichier de patch inclus :
```bash
# SÉCURISATION ANTI-MORT SILENCIEUSE (WRAPPER LOCAL)
# Empêche tout appel externe (curl/ruby) de faire mourir le shell sous set -e
safe_eval() {
    "$@" || true
}
```
*Et encapsuler les appels critiques identifiés (les `public_get` depth/klines et helpers `json_get`) par `safe_eval` ou suffixer par `|| true`.*

### 5. L'indicateur unique à mesurer au prochain retest
**Le code de retour exact (exit status) intercepté juste avant la mort**, en modifiant temporairement le piège de sortie pour logger `$?` et la dernière ligne exécutée (`BASH_COMMAND`) :
`trap 'echo "CRASH_DEBUG: cmd=${BASH_COMMAND} rc=$?" >> /tmp/ace777_debug_rc.log' ERR`
