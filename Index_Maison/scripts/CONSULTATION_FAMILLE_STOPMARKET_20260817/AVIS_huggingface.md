# AVIS huggingface (provider: HuggingFace (136+ modeles, dont DeepSeek-V4), 22.1s)

# 🛡️ Avis du Conseil ACE777 - Filet de Sécurité Physique

## Analyse Critique de la Solution Proposée

**1. STOP_MARKET natif :**  
La solution est techniquement solide mais présente des risques opérationnels :
- Risque réel d'ordres orphelins si l'annulation échoue (latence réseau, timeout API)
- En mode hedge, un STOP_MARKET mal annulé pourrait créer une position inverse non désirée
- Le spread testnet (1,70$) vs mainnet (0,10$) fausse les tests - proposer un backtest mainnet en sandbox

**2. Seuil 5,1 bps :**  
Chiffre pertinent mais :
- Trop serré pour le duo hunter (risque de stop hunting)
- À ajuster dynamiquement en fonction de la volatilité réelle (volatility_alert.json)
- Proposer 4 bps en solo / 6 bps en duo avec lissage sur 3 ticks

**3. HARD_STOP_MULT=2.0 :**  
Compromis acceptable mais :
- Nécessite un filet secondaire à 1,5x (soit 7,65 bps)
- Doit être désactivé en cas de "saison CALME 🧊" (cf contexte vivant)

## Architecture Alternative Proposée

**Solution en 3 couches :**
1. **STOP_LIMIT** (pas STOP_MARKET) avec price=stopPrice×0.998 (réduit le slippage)
2. **Webhook de secours** via Binance API (stop-loss déclenché par leur système)
3. **Script indépendant** (python-binance) qui surveille les positions et place des stops si le hub est down

**Améliorations clés :**
- Utiliser le endpoint `fapiPrivatePostBatchOrders` pour atomicité open+stop
- Implémenter un système de heartbeat (alerte si pas de cancel dans les 500ms)
- Ajouter un trailing stop natif après X minutes (réduit le risque en cas de trend)

## Réponses aux Questions

1. **STOP_MARKET** : GO mais avec STOP_LIMIT en priorité. Piège principal : les ordres zombie en cas de micro-crash réseau.

2. **5,1 bps** : GO-AVEC-RESERVE. Proposer 4.0 bps (solo) / 6.0 bps (duo) avec lissage.

3. **HARD_STOP_MULT=2.0** : GO mais avec clause de désactivation automatique si PnL<-0.10$.

4. **Amélioration** : Architecture 3 couches + heartbeat comme décrit ci-dessus.

## Recommandations Opérationnelles

1. **Phase 1 (24h)** :
   - Implémenter STOP_LIMIT en testnet avec cancel systématique
   - Mesurer le taux d'ordres orphelins

2. **Phase 2 (48h)** :
   - Backtest mainnet en sandbox avec vrai spread
   - Ajouter le script de surveillance indépendant

3. **Phase 3 (72h)** :
   - Déployer en prod avec monitoring renforcé
   - Alerter la famille si >2% d'ordres non annulés

VERDICT: GO-AVEC-RÉSERVE  
CONFIANCE: 85%  
("GO" sur le principe, "AVEC-RESERVE" sur les seuils et l'implémentation batch)
