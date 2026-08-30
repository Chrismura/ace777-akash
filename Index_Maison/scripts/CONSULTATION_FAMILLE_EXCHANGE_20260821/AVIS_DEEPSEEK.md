# AVIS DEEPSEEK (task deepseek.analyse · Google Gemini · 2026-08-21T19:02Z)

**VERDICT :** NON
**CONFIANCE :** 95 %

**HYPOTHÈSES :**
1. Le moteur ACE777 utilise l'API REST/WebSocket de Binance sans gérer l'écoute de l'événement d'exécution (`ORDER_TRADE_UPDATE`), se basant uniquement sur la réponse HTTP initiale de l'ordre, ce qui provoque la cécité sur les fills partiels.
2. Le code actuel calcule le PnL sur la base du volume théorique envoyé et non sur la somme réelle des `executionReport` reçus du carnet d'ordres.
3. L'erreur `-1106` sur les `STOP_MARKET` provient d'une mauvaise construction du payload (ex: paramètre `stopPrice` manquant ou incompatible avec le type de contrat/précision du symbole).

**CE QUI CHANGERAIT L'AVIS :**
- Un extrait de code prouvant que le moteur écoute et traite les messages `executionReport` de type `PARTIAL` et agrège dynamiquement les frais réels.
- Un log démontrant que le passage à un autre exchange résout le problème sans modifier la logique de gestion des ordres.

**AMÉLIORATION PROPOSÉE :**
1. **Architecture d'exécution (Propositions de remplacement) :** Abandonner l'ordre `MARKET` brut pour le scalping haute fréquence. Implémenter un routeur d'ordres avec **Post-Only (Limit Maker)** ou un algorithme TWAP/ICEBERG interne si la taille dépasse la profondeur de premier niveau, garantissant des fills uniques ou des rebates de maker (0% ou négatifs).
2. **Normalisation des Fills :** Refondre la classe de gestion des trades pour créer un objet unique `ExecutionGrouper` qui écoute le flux utilisateur WebSocket et ne valide un trade dans le CSV *qu'après* réception du flag `filled` final, en sommant mathématiquement chaque `commission` et `realizedPnl` reçus.
3. **Correction STOP_MARKET (-1106) :** Remplacer les ordres `STOP_MARKET` par des `STOP` avec déclenchement sur `MARK_PRICE` et vérifier dynamiquement les règles de prix de déclenchement (`filters.PRICE_FILTER` et `PERCENT_PRICE`) avant l'envoi.

**SYNTHÈSE :**
Le problème n'est pas l'exchange mais l'architecture aveugle du moteur face aux `partial fills`. Changer pour MEXC ou Hyperliquid sans corriger la gestion des websockets d'exécution déplacera simplement la fuite de capital. Le PnL du CSV est mathématiquement faux car basé sur une vue unitaire fictive des ordres. Une refonte complète de la boucle de réception des fills est impérative avant tout transfert de fonds.
