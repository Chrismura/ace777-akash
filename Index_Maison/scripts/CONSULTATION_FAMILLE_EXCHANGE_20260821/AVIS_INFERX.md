# AVIS INFERX (task inferx.analyse · Google Gemini · 2026-08-21T19:02Z)

**VERDICT :** GO-AVEC-RÉSERVES  
**CONFIANCE :** 78 %  

**HYPOTHÈSES :**  
1. Le problème des *partial fills* (split d'ordres) n'est pas exclusif à Binance mais exacerbé par sa gestion du carnet d'ordres en Testnet et son modèle de frais taker (0.04%).  
2. Le moteur ACE777 enregistre l'état logique de l'ordre au lieu d'écouter le flux d'exécution réel (*UserDataStream / WebSocket execution reports*), ce qui crée l'écart de 98% de trades fantômes.  
3. L'erreur `-1106` sur les STOP_MARKET (paramètre invalide ou manquant, ex: `reduceOnly` mal positionné ou prix hors borne) est un bug de payload API et non une limitation structurelle inhérente à l'exchange.  

**CE QUI CHANGERAIT L'AVIS :**  
- La preuve que Hyperliquid ou MEXC présente exactement le même taux de fragmentation (split > 3) sur des ordres market de taille similaire en conditions réelles.  
- Une analyse prouvant qu'en corrigeant la logique de comptabilisation des frais réels, le PnL net reste négatif malgré des spreads favorables.  

**AMÉLIORATION PROPOSÉE :**  
1. **Architecture d'écoute (WebSocket UserDataStream) :** Remplacer le logging basé sur la réponse de l'ordre envoyé par l'écoute synchrone des messages d'exécution (`executionReport`). C'est le seul moyen infaillible de capturer 100% des *partial fills* et leurs frais associés en temps réel.  
2. **Migration vers Hyperliquid (Testnet) :** Tester immédiatement Hyperliquid pour son modèle 0% Maker / 0.01% Taker et son carnet basé sur L1, intrinsèquement plus propre pour le scalping haute fréquence (évite le massacre des commissions par micro-fills).  
3. **Refonte du filet STOP_MARKET :** Valider le payload exact accepté par l'API (souvent lié au mode de couverture *Hedge Mode* vs *One-Way Mode* et au drapeau `reduceOnly`).  

**SYNTHÈSE :**  
Le bot n'est pas structurellement perdant par sa stratégie, mais aveugle face à la fragmentation des ordres et aux frais réels de Binance. Le problème vient d'un moteur qui logue des "intentions" plutôt que des "exécutions" réelles. Il faut migrer vers Hyperliquid (frais minimes, exécution propre) tout en refondant l'écoute des *UserDataStreams* pour stopper l'hémorragie des commissions cachées.
