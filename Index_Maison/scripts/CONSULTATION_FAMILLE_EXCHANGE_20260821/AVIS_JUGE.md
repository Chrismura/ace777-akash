# AVIS JUGE (task juge.tranche · Google Gemini · 2026-08-21T19:02Z)

VERDICT : NON  
CONFIANCE : 95 %  

**HYPOTHÈSES :**  
1. Le moteur ACE777 ne lit pas le flux WebSocket des `executionReport` et se contente de la réponse REST initiale, ce qui aveugle complètement le système sur le morcellement des ordres.  
2. Le PnL brut du CSV est un artefact mathématique faussé par cette absence de lecture des fills partiels réels et des frais unitaires cumulés.  
3. L'erreur -1106 sur les `STOP_MARKET` est une défaillance de formatage du payload (ex: prix de déclenchement ou `reduceOnly`), indépendante de l'exchange utilisé.  

**CE QUI CHANGERAIT L'AVIS :**  
Un test en conditions réelles montrant que le moteur intègre et traite 100% des événements de fills partiels sans divergence de PnL sur 24h.  

**AMÉLIORATION PROPOSÉE :**  
1. **Refonte de l'écoute des exécutions :** Abandonner le suivi basé sur la réponse REST initiale. Implémenter un gestionnaire d'événements WebSocket (`User Data Stream`) capable d'agréger chaque `executionReport` partiel avec ses frais réels avant toute écriture en CSV.  
2. **Migration vers Hyperliquid (Testnet) couplée à une stratégie Maker :** Pour un volume de 1400 trades/jour, abandonner les ordres `MARKET` agresseurs de carnet (qui subissent les partial fills et le taker fee de 0.04% à 0.02%) au profit d'un routage d'ordres `Post-Only` sur Hyperliquid (maker 0%, taker 0.01%), éliminant structurellement la prédation des micro-frais.  
3. **Remplacement des STOP_MARKET par un Soft-Stop interne :** En attendant de stabiliser l'API exchange, coder un filet de sécurité logiciel synchrone dans le moteur qui déclenche une clôture `MARKET` immédiate dès franchissement du seuil de risque.  

**SYNTHÈSE :**  
Changer d'exchange ne résoudra rien : le moteur est structurellement aveugle aux partial fills et calcule un faux PnL. Il faut d'abord réécrire la gestion des WebSockets d'exécution et migrer vers Hyperliquid en mode Maker pour stopper l'hémorragie des frais.
