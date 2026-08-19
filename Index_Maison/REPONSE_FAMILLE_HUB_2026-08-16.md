# Réponse signets.juge — méthode hub (provider Google Gemini, 2.4s)

**a) VERDICT :** VALIDÉ AVEC RÉSERVES.

**b) RÉSERVES :**
1. **Saturation des gratuits :** En étendant la recherche à TOUS les ~15 providers gratuits, on risque de déclencher des bans IP globaux ou des 429 en cascade si tous se font marteler en même temps en cas de panne majeure.
2. **Effet tunnel sur la latence :** Si les 3 maillons principaux échouent, parcourir séquentiellement le filet universel (même avec un budget réduit à 15s) peut faire exploser le temps de réponse total pour l'appelant (potentiellement plusieurs minutes d'attente).
3. **Risque de consommation cachée :** Le filet universel pioche aveuglément dans tous les actifs, y compris potentiellement des providers cloud payants si le tri `order` les positionne mal ou en cas de mauvaise configuration des flags "gratuits".

**c) CONDITIONS :**
1. S'assurer que le filet universel ne sélectionne **strictement** que des providers marqués comme gratuits ou que le budget cloud global (`cloud_daily_budget`) reste un coupe-circuit absolu avant d'itérer sur le filet.
2. Implémenter un log explicite et distinct (`[FILET UNIVERSEL]`) pour tracer chaque bascule hors-chaîne, afin de repérer immédiatement si une tâche recourt trop souvent au filet (signe d'une chaîne `routing.json` obsolète à corriger).
