# AVIS GROK (task puter-grok.analyse · Google Gemini · 2026-08-21T19:02Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 85 %

HYPOTHÈSES : 
1. Le moteur envoie des ordres MARKET purs sans grouper ni gérer l'exécution par vagues, ce qui force l'exchange à splitter selon la liquidité dispo au carnet.
2. Le problème -1106 de Binance vient d'un mauvais formatage des paramètres STOP_MARKET (ex: `price` envoyé sur un ordre stop market pur, ou `workingType` manquant).
3. Hyperliquid encaisse 10x mieux le scalping haute fréquence grâce à son modèle L1 perp décentralisé avec 0% maker / 0.01% taker, mais impose une intégration SDK spécifique (pas de REST pur classique).

CE QUI CHANGERAIT L'AVIS : 
Un test grandeur nature sur Hyperliquid Testnet montrant le même taux de fragmentation (partial fills > 3 par ordre) avec la même taille de lot (0.005-0.13 BTC).

AMÉLIORATION PROPOSÉE : 
1. **Migration immédiate vers Hyperliquid Testnet** : Abandonner Binance pour le scalping ag尙ressif à cause des frais et du splitting destructeur. Le 0% maker / 0.01% taker est le seul modèle viable pour 1000+ trades/jour.
2. **Refonte de l'exécution (Smart Order Routing / TWAP-micro)** : Ne plus balancer des ordres MARKET bruts. Le moteur doit router les blocs en Post-Only ou utiliser des limites agressives pour forcer le rôle Maker (0% de frais sur HL et MEXC) au lieu de se faire massacrer en Taker.
3. **Réécriture du filet stop-loss** : Remplacer les STOP_MARKET natifs par des ordres gérés en interne dans la boucle de state du bot (logic-based stop) qui envoient un MARKET d'urgence uniquement si le prix traverse le seuil, évitant les erreurs de l'API exchange.

SYNTHÈSE (5 lignes max) :
Binance massacre le PnL avec ses partial fills et des frais Taker de 0.04% sur 1400 trades/jour. Le moteur est aveugle car il agrège mal les fills partiels dans le CSV. Il faut migrer d'urgence sur Hyperliquid pour diviser les frais par 4 (0.01%) et cesser d'envoyer des ordres MARKET aveugles. Sans passage en mode Maker et sans correction du routage, aucun exchange ne sauvera le bot.
