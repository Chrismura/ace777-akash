# AVIS DEEPSEEK (task deepseek.analyse · Google Gemini · 2026-09-01T07:51Z)

VERDICT : GO-AVEC-RÉSERVES  
CONFIANCE : 85 %  

### HYPOTHÈSES
1. **Bruit d'E/S CSV** : 18 997 SKIP saturent les logs et les écritures disque (environ 86 % dus à la volatilité `VOL`), ce qui impacte le débit I/O sans pour autant saturer le CPU de calcul pur.
2. **Obsolescence du cache de score** : Avec `POLL_SEC=20` et `SCORE_EVERY=3` (rafraîchissement toutes les 60s), les refus répétés sur `MUR-CASSE` ou `SPREAD` reposent sur des métriques potentiellement périmées.

### CE QUI CHANGERAIT L'AVIS
- Un profilage CPU (ex: `cProfile` ou `py-spy`) prouvant que l'évaluation des SKIP consomme < 1 % du temps d'exécution total de la boucle, rendant toute déduplication logicielle superflue face aux coûts réseau I/O (`fetch_all_prices`).
- Une preuve que la suppression des lignes de log SKIP dans le CSV perturbe le rejeu (backtest/replay) ou la télémétrie aval du cockpit.

### AMÉLIORATION PROPOSÉE
1. **Déduplication en mémoire à TTL court (ex: 60s) par paire/motif** : Implémenter un filtre dans le module de journalisation des SKIP (`logger` ou fonction dédiée de l'observabilité) qui supprime l'écriture répétée d'un même motif pour une même paire, tout en incrémentant un compteur interne purgé/affiché périodiquement.
2. **Instrumentation par phase (Chrono-marquage)** : Ajouter des mesures de temps (nanosecondes via `time.perf_counter`) avant et après `fetch_all_prices`, l'évaluation des scores et le filtrage des gates, sans modifier aucune logique de décision.
3. *Proposition architecturale (Christophe)* : **Indexation bitmap/bitset des états de skip par cycle** au lieu d'une collection de dictionnaires, pour réduire l'empreinte mémoire si le nombre de paires augmente, couplé à un flush asynchrone des métriques agrégées pour découpler l'I/O disque de la boucle critique.

### SYNTHÈSE
Les SKIP à 86 % liés à `VOL` polluent le CSV sans ralentir le calcul local, mais pèsent sur l'I/O. Une déduplication à TTL court combinée à une instrumentation par phase est sûre, à condition de conserver les compteurs agrégés en mémoire. Aucun seuil ne doit être touché. Validation conditionnée par le maintien strict de la traçabilité des sorties.
