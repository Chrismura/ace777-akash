# JUGE — juge.tranche

1. **Verdict global** : GO AVEC RÉSERVES — Le diagnostic est chirurgical, les faits concordent et le correctif est identifié.

2. **La zone fautive** : Les lignes 1599-1615 (`curl_with_retry` sur les depth/p1/p2). Le timing de 9 secondes correspond exactement à l'expiration des 3 tentatives de 5s de `curl_with_retry` lors d'un timeout réseau ou d'une réponse vide non interceptée par `set -e`.

3. **Pourquoi le trap ERR n'a pas écrit** : Sous `set -e`, un appel de commande échouant à l'intérieur d'une substitution de commande `$(...)`, d'un pipeline ou d'une condition (`if`, `while`) **n'invoque pas** le trap `ERR`. L'échec a tué le sous-shell silencieusement avant d'atteindre la ligne du trap principal.

4. **Correctif GO-sized** : Encapsuler l'appel réseau critique et les helpers Ruby dans un bloc sécurisé ou suffixer par `|| true` dans la boucle d'ALPHA, ex: `p1_resp=$(curl_with_retry ... || echo "{}")`, pour éviter que le rc=1 ne tue le process.

5. **Indicateur de confirmation au prochain retest** : Activer `set -x` temporairement sur la boucle d'ALPHA ou logger explicitement le code de retour (`$?`) de chaque sous-étape dans `runs/CRASH_DUMP_ALPHA_DEBUG.log`.
