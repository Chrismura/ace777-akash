# INFERX — inferx.analyse

INFERX au rapport. Analyse de la logique interne, des pièges bash et des flux d'exécution.

1. **Verdict global**
   **NON** — Le mécanisme de résilience du lanceur masque l'erreur, empêchant le diagnostic et provoquant une mort silencieuse (rc=1) dans un sous-shell.

2. **La commande la plus probablement fautive**
   **`curl_with_retry` sur `depth_1` / `depth_2` (lignes 1599-1615)** ou l'appel API du LLM (ligne 1992).
   *Justification :* Les 9 secondes de silence correspondent exactement au timeout cumulé de 3 tentatives avec les pauses de l'appel REST (`curl_with_retry` : 3 essais × pause). Si l'API publique bafouille juste après un fill, le curl échoue et fait mourir le bloc si non protégé.

3. **Pourquoi le trap ERR n'a pas écrit FATAL_RC1**
   Sous `set -e`, un piège `ERR` **ne se propage pas** à l'intérieur d'un sous-shell, d'une substitution de commande `$(...)`, d'un pipeline (`|`), ou d'une condition (`if`, `while`). Comme le code exécute des `json_get` ou des `curl` dans des affectations de variables ou des pipelines sans `|| true`, le sous-shell meurt immédiatement avec `rc=1` sans remonter au script principal qui portait le trap.

4. **Correctif GO-sized borné (macOS Bash 3.2)**
   Isoler l'exécution critique dans la boucle pour capturer le retour sans tuer le processus parent, ou protéger les blocs d'appels externes par un wrapper `|| true` explicite. 
   Exemple sur les appels risqués :
   ```bash
   p1_resp="$(curl_with_retry ...)" || p1_resp=""
   ```
   *Règle d'or :* Ne jamais laisser une substitution de commande nue `$(...)` sans gestion de repli (`|| true` ou variable de statut locale) dans une boucle critique `set -e`.

5. **Ce qu'il faut mesurer au prochain retest**
   Activer le mode verbeux ciblé sur les appels réseaux : logger explicitement l'heure et le code de retour (`rc`) de chaque `curl_with_retry` dans un fichier dédié avant chaque assignation, pour capturer l'avant-dernière ligne avant le silence.
