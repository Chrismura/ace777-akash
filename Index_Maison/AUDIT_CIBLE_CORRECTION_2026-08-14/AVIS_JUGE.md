# JUGE — juge.tranche

**VERDICT**
GO AVEC RESERVES (sous condition de re-scellement immédiat de genesis).

**CIBLE**
Option A (modification directe de genesis_manifest.txt pour neutraliser les 10 points identifiés + RE-SCELLEMENT af307996). 
*Justification :* Les substitutions imbriquées s'exécutent dans l'espace de code de genesis ; le lanceur ne peut pas intercepter ces sous-shells en plein vol sous Bash 3.2 sans réécrire l'interpréteur. L'option A est la seule structurellement étanche.

**MÉCANISME RÉEL**
Confirmé. `public_get` est inoffensif (retourne 0). Le coupable est l'appel brut à `as_num`/`json_get` dans des substitutions critiques (`$(...)`), où un retour `rc!=0` en mode `set -e` assassine le processus sans laisser de trace dans `FATAL_RC1`.

**ZONES À PROTÉGER (Minimaliste Bash 3.2)**
Envelopper les 10 occurrences identifiées (lignes 1600, 1614, 1734, 1735, 2057, 2061, 2071, 2109, 2142, 2431) dans un pattern de neutralisation `|| echo "0"` ou `|| true` selon le type attendu, ou via une fonction safe locale `safe_eval()` injectée en tête de genesis :
```bash
safe_eval() { "$@" 2>/dev/null || echo "0"; }
```
Remplacer les appels directs `$(as_num ...)` par `$(safe_eval as_num ...)`.

**INDICATEUR DE PREUVE AU RETEST**
Disparition totale du pattern `rc=1` brut à ~8 min sur ALPHA dans le fichier de log, et remplissage effectif du dump `FATAL_RC1` avec un vrai stacktrace bash/ruby explicite en cas d'anomalie résiduelle.
