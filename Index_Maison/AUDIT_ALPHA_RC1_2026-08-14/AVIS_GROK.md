# GROK — puter-grok.analyse

GO AVEC RÉSERVES. 

Le diagnostic pose le bon piège (Trap ERR) pour attraper le coupable, mais il pèche sur un point : se fier uniquement au log du lanceur. En prod réelle, un `set -euo pipefail` qui encaisse un faux positif réseau sur une substitution de commande (`$(...)`) ou un parseur JSON sous-jacent (Ruby/Python/jq) meurt net sans bruit si le stderr est redirigé au mauvais endroit.

### 2. Le coupable probable
**La substitution de commande non tolérante dans un helper (genre `json_get` ou parsing de prix post-fill) combinée à `set -u` ou `set -e`.**
*   **Mécanisme précis :** À 18:25:34, Alpha encaisse un fill (`shock_inversion_stop`). Le bot entre immédiatement dans sa boucle de recalcul ou d'appel API post-trade (extraction de position, calcul de taille, etc.). Si une commande interne (un appel `curl`, un parseur Ruby `ruby -e`, ou une lecture de variable non initialisée sous `set -u`) rate ou renvoie un code de sortie non-zéro pendant ces 8 secondes de silence, et que le résultat est stocké dans une variable (`PRIX=$(...)`), le `pipefail` ou le `set -e` tue le script instantanément, en silence, avant que le handler d'erreur standard ne puisse respirer.

### 3. L'amélioration concrète (Stabilité absolue)
**Généraliser la tolérance d'échec sur les blocs non-fatals et implémenter une auto-relance propre au niveau du lanceur.**
Ne jamais laisser un sous-processus trader mourir bêtement pour une erreur de parsing ou un timeout réseau transitoire. 
*   *Côté bot :* Envelopper les appels API et parsings critiques dans des blocs protégés (`{ commande || true; }`) ou des boucles de retry internes.
*   *Côté lanceur :* Implémenter un superviseur léger pour chaque unité (`while [ run_allowed ]; do run_unit() || sleep 5; done`). Un Hunter (Alpha) qui crashe ne doit **jamais** laisser le Scout (Beta) tout seul pendant 2 heures : si Alpha tombe, le lanceur le relance proprement et réaligne l'état E-DUO, ou stoppe tout le binôme par sécurité. Fin du bricolage, place au roc.
