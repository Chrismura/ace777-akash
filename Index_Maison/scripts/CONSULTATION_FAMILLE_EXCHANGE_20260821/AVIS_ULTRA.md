# AVIS ULTRA (task inferx.analyse · Google Gemini · 2026-08-21T19:02Z)

VERDICT : NON
CONFIANCE : 95%
HYPOTHÈSES : 
1. Le carnet d'ordres du testnet Binance ne reflète pas la profondeur du mainnet, aggravant artificiellement les partial fills.
2. Le moteur actuel traite chaque message WebSocket de remplissage unitaire comme un événement isolé au lieu d'agréger par `orderId`, faussant totalement le CSV.

CE QUI CHANGERAIT L'AVIS : Un test en production sur un exchange alternatif (Hyperliquid) montrant une divergence PnL CSV vs Exchange inférieure à 1% sur 1000 trades.

AMÉLIORATION PROPOSÉE : 
1. **Migration immédiate vers Hyperliquid** : Abandonner Binance pour le scalping haute fréquence ; les frais de maker à 0% et taker à 0.01% couplés à une gestion native des fills par l'API résolvent structurellement le problème des 98% de trades fantômes.
2. **Refonte de la couche d'écoute WebSocket (Engine)** : Ne plus logger les fills bruts (trade par trade) mais écouter l'événement `ORDER_TRADE_UPDATE` consolidé par `orderId` pour garantir l'unicité de la ligne CSV par ordre envoyé.
3. **Implantation d'un filet de sécurité asynchrone** : Remplacer le `STOP_MARKET` natif défaillant par une logique de "Client-Side Stop-Loss" gérée par le bot en local avec annulation/remplacement agressive si l'API rejette le stop (-1106).

SYNTHÈSE (5 lignes max) :
Le bot est structurellement mort sur Binance à cause des micro-fills et des frais qui détruisent la marge. 
Le moteur compte mal les trades et les stops physiques sautent, créant une illusion de profit (+18$ vs -131$).
Il faut fuir sur Hyperliquid et réécrire la couche de réconciliation des ordres pour tracker les `orderId` et non les exécutions brutes.
