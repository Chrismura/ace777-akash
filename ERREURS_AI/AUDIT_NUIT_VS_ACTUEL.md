# Audit — Setup nuit vs setup actuel (limitation des pertes)

**Date :** 27 février 2026

---

## Contexte

Le setup de la nuit (9–10 mars 2026) limitait les pertes. Le setup actuel (`launch_250_4h.sh`) permet des pertes plus importantes. Cet audit compare les deux configurations.

---

## 1. Comparaison des paramètres

| Paramètre | Nuit (config_nuit.env + fortress) | Actuel (launch_250_4h) | Impact |
|-----------|-----------------------------------|------------------------|--------|
| **BUY_USDT_BETA** | 200 | 250 | +25 % d’exposition par trade BETA |
| **BUY_USDT_ALPHA** | 800 | 250 | ALPHA beaucoup plus léger |
| **STOP_LOSS_BPS** | 16 | 16 | Identique |
| **GLOBAL_STOP** | -45 HALT | -45 HALT | Identique |
| **LLM gate** | qwen2.5-coder:1.5b | qwen2.5-coder:1.5b | Identique |
| **MOM, WALL_DROP** | 0.96, 6.5% | 0.96, 6.5% | Identique |

---

## 2. Différence principale : la masse (BUY_USDT)

### Nuit
- **BETA** : 200 USDT → positions plus petites, pertes limitées par trade
- **ALPHA** : 800 USDT → rôle de « chasseur » avec plus de capital

### Actuel
- **BETA** : 250 USDT → +25 % d’exposition par trade
- **ALPHA** : 250 USDT → symétrique, ALPHA moins agressif

### Effet sur les pertes

Avec 250 au lieu de 200 pour BETA :
- Chaque trade BETA = **25 % de perte en plus** par point de base
- Exemple : -33 bps ≈ -1,16 USDT (actuel) vs ≈ -0,93 USDT (nuit)
- Sur 12 trades, l’écart cumulé augmente

---

## 3. Pourquoi la nuit limitait mieux les pertes

1. **Masse BETA plus faible** = pertes plus petites par trade
2. **Masse ALPHA plus forte** = stratégie différente (nuit : ALPHA lourd, actuel : symétrique)
3. **SOFT anomaly** : même logique (cooldown, masse réduite, stop plus serré), mais avec 250 USDT les pertes restent plus élevées par trade

---

## 4. Recommandations

### Pour revenir au comportement limitant les pertes

1. **Revenir à la masse nuit** :
   ```bash
   export BUY_USDT_BETA="200"
   export BUY_USDT_ALPHA="800"
   ```
   Ou lancer avec la config nuit :
   ```bash
   source config_backup_nuit_20260310/config_nuit.env
   ./launch_test_master_base_v8_6_fortress.sh --duration 04:00:00
   ```

2. **Ou garder 250** et réduire le risque :
   - Augmenter `STOP_LOSS_BPS` (ex. 12 au lieu de 16) pour sortir plus tôt
   - Ou augmenter `ANOMALY_PNL_USDT` pour déclencher plus souvent le mode SOFT

3. **Créer un launch « nuit »** : script qui source `config_nuit.env` puis lance fortress.

---

## 5. Résumé

| Cause | Explication |
|-------|-------------|
| **Masse BETA 250 vs 200** | +25 % d’exposition → pertes plus grandes par trade |
| **Config nuit non chargée** | `launch_250_4h` ne source pas `config_nuit.env` |
| **Même stop loss** | STOP_LOSS_BPS=16 identique, mais les montants en USDT sont plus élevés avec 250 |

**Conclusion :** La différence principale est la masse BETA (250 vs 200). Pour limiter les pertes comme la nuit, utiliser `BUY_USDT_BETA=200` ou `BUY_USDT_ALPHA=800` selon la config nuit.
