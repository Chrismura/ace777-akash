# ULTRA — inferx.analyse

Ici ULTRA. On regarde la robustesse à l'échelle : ce qui casse en tempête et sous charge. 

Voici les 5 réponses nettes, sans concession :

1. **Verdict global :** 
**NON.** Le code en prod est une passoire à signaux d'erreur silencieux sous contrainte réseau.

2. **La zone la plus probablement fautive :** 
Les lignes **1599-1615** (`public_get` / `curl_with_retry`). 
*Justification :* Les 9 secondes de silence exactes correspondent au timeout cumulé des 3 tentatives de retry réseau (`3 x 5s` ou latence DNS/TCP). Un appel `curl` ou un helper Ruby interne (`json_get` / `num_*`) qui rate hors d'un contexte protégé déclenche un `set -e` dans un sous-shell non intercepté.

3. **Pourquoi le trap ERR n'a pas écrit :** 
Sous Bash, **le trap ERR ne s'hérite pas** dans les sous-shells, les pipelines (`|`), ou les substitutions de commandes (`$(...)`). Le `set -euo pipefail` couplé à la structure du lanceur `tail ... | bash` isole l'exécution : quand une commande critique échoue à l'intérieur d'un bloc ou d'un pipe sans `|| true`, le processus meurt net avec un `rc=1` sans que le trap global du script principal ne soit jamais déclenché.

4. **Le correctif GO-sized borné :**
Créer une fonction utilitaire wrapper `safe_eval()` dans le lanceur ou la zone d'appel externe (JAMAIS dans genesis directement) pour isoler les appels réseau et les parsers Ruby :
```bash
safe_call() {
    "$@" 2>>/tmp/ace777_stderr_debug.log || {
        local ec=$?
        echo "[WARN] Commande ignorée (rc=$ec): $*" >> /tmp/ace777_fatal_rc1.log
        return 0 # Neutralise la mort sèche sous set -e
    }
}
```
*Remplacer les appels `curl_with_retry` critiques et parsers par `safe_call [...]`.*

5. **Ce qu'il faut mesurer au prochain retest :** 
Ajouter un `trap 'echo "[DEBUG_EXIT] ligne $LINENO rc=$?" >> /tmp/ace777_debug_exit.log' EXIT` au niveau du bloc d'exécution pour capturer instantanément la *dernière ligne exacte* exécutée avant le signal de mort.
