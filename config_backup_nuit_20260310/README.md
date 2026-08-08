# Backup config nuit 9-10 mars 2026

**Setup qui a tourné cette nuit** (runs MASTER_BASE_V8_5_IMPACT_4H_*).

Si la nouvelle config QWEN_TWEEN ne marche pas, revenir à ce setup.

## Fichiers de référence
- `runs/MASTER_BASE_V8_5_IMPACT_4H_BETA_X5.csv`
- `runs/MASTER_BASE_V8_5_IMPACT_4H_ALPHA_X13_BURST13.csv`

## Paramètres clés (V8.5 IMPACT)
- BETA: BUY_USDT=200, LEVERAGE=5, FORCE_ENTRY_SIDE=SELL, POSITION_SIDE=SHORT
- ALPHA: BUY_USDT=800, DUO_V6_BURST_X13=TRUE, FORCE_ENTRY_SIDE=BUY, POSITION_SIDE=LONG
- Durée: 4h (14400s)
- LLM gate: actif (ollama_skip dans les logs)

## Pour relancer le setup nuit
```bash
./launch_test_master_base_v8_5_impact.sh
# ou avec durée: RUN_DURATION=04:00:00 ./launch_test_master_base_v8_5_impact.sh
```
