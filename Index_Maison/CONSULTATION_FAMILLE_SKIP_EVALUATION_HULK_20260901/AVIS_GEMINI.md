# AVIS GEMINI (task gemini.analyse · Google Gemini · 2026-09-01T07:51Z)

### VERDICT : GO-AVEC-RÉSERVES
### CONFIANCE : 85 %

### HYPOTHÈSES
1. **Bruit d'observabilité dominant :** Les 16 358 SKIP VOL (~86 %) génèrent un coût d'E/S disque (CSV) et de sérialisation non négligeable, mais pèsent peu sur le CPU pur comparé aux appels réseau (`fetch_all_prices`) et au calcul des sondes.
2. **Obsolescence du cache :** Le découplage `POLL_SEC=20` et `SCORE_EVERY=3` (refresh à ~60s) crée une fenêtre où des opportunités valides sont rejetées (ou l'inverse) sur la base de scores périmés, particulièrement en régime de forte volatilité.

### CE QUI CHANGERAIT L'AVIS
- La preuve par profiling que le goulet d'étranglement réside exclusivement dans l'appel réseau bloquant et non dans la boucle d'évaluation des paires exclues.
- Une augmentation de la latence de la boucle principale imputable à la gestion de la mémoire des dictionnaires de déduplication.

### AMÉLIORATION PROPOSÉE (Au-delà de la correction)
1. **Architecture de mémoïsation stateful par paire (TTL-State) :** Plutôt qu'une simple déduplication de logs, introduire un cache d'état de refus éphémère au niveau du gestionnaire de paires (expirant au prochain `SCORE_EVERY` ou sur variation de prix > $\Delta$ seuil). Cela évite de réévaluer stérilement la même condition de gate à chaque poll de 20s.
2. **Canal de log asynchrone (Ring Buffer / Queue) :** Déporter l'écriture des SKIP dans un thread/queue dédié non bloquant pour découpler totalement le débit d'observabilité de la boucle de trading principale, sans toucher aux gates.

### SYNTHÈSE (5 lignes max)
Les SKIP saturent l'observabilité et alourdissent la boucle sans altérer la logique de risque. Une déduplication intelligente combinée à une instrumentation des temps de phase est requise. Le GO est conditionné au maintien absolu des compteurs de traçabilité via des résumés périodiques. Les seuils et boucles existantes demeurent strictement intacts.
