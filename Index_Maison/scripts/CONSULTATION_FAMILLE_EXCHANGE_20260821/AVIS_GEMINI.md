# AVIS GEMINI (task gemini.analyse · Google Gemini · 2026-08-21T19:02Z)

**VERDICT :** NON  
**CONFIANCE :** 92 %  

**HYPOTHÈSES :**  
1. Le moteur ACE777 calcule ses fills en simulant une exécution unique (prix moyen estimé) alors que l'API de l'exchange retourne chaque exécution partielle (trade ID unique) avec sa propre structure de frais et de slippage.  
2. Le problème -1106 sur les `STOP_MARKET` de Binance provient d'un mauvais formatage des paramètres de déclenchement (ex: `stopPrice` fourni alors que le type d'ordre ou le mode de marge/position l'interdit, ou `reduceOnly` mal géré).  
3. Migrer sur MEXC ou Hyperliquid sans corriger la logique d'écoute des WebSockets/UserData Streams (qui gèrent les `ORDER_TRADE_UPDATE`) ne fera que masquer le problème sous un autre carnet d'ordres.

**CE QUI CHANGERAIT L'AVIS :**  
- Un test sur Hyperliquid prouvant que le moteur gère nativement l'agrégation des fills sans dérive du PnL sur 48h.  
- La correction validée du code d'envoi des `STOP_MARKET` montrant 0 rejet sur 100 ordres consécutifs.

**AMÉLIORATION PROPOSÉE :**  
1. **Refonte de la couche d'exécution (Moteur d'abord, Exchange ensuite) :** Remplacer le parsing naïf des réponses REST/CSV par un écouteur d'événements 100% orienté `executionReport` (WebSocket User Data Stream). Chaque `fill` individuel doit être injecté en base/log avec son propre trade ID et ses frais réels, avant même de songer à changer d'exchange.  
2. **Architecture de secours asymétrique :** Abandonner temporairement les `STOP_MARKET` exchange-side si l'API est instable sur le Testnet, et implémenter un *soft-stop* déterministe interne au moteur (fermeture MARKET immédiate par le code dès franchissement du seuil de prix), couplé à un ordre limite de réduction de risque (Reduce-Only).  
3. **Migration tactique vers Hyperliquid (Testnet) :** Pour un volume de 1400 trades/jour, Hyperliquid (maker 0%, taker 0.01%) et son carnet basé sur L1 éliminent structurellement la prédation des micro-frais vue sur Binance. C'est l'unité de destination évidente pour du scalping haute fréquence, mais *uniquement* après avoir validé l'amélioration #1.

**SYNTHÈSE :**  
Le problème n'est pas uniquement l'exchange : c'est l'aveuglement du moteur face au morcellement des ordres (partial fills) et la rupture de la protection (`STOP_MARKET` -1106). Changer pour Hyperliquid est une excellente cible pour réduire les frais à 0.01%, mais c'est insuffisant si le moteur continue d'ignorer 98% des exécutions réelles. Il faut d'abord réécrire le parseur de fills et sécuriser le risk management, puis migrer.
