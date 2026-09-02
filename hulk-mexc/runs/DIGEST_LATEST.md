# Hulk DIGEST — 2026-09-02T20:33:21Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.19 | 2.31 | 0.42 | -0.0 | 37126968.04 | 0.74 | n/a |
| ETHUSDT | IDLE | 0.7 | 1.33 | 0.46 | -0.01 | 364892755.42 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.54 | 1.06 | 0.19 | 0.0 | 509678730.01 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.25 | 5.36 | 1.87 | 0.15 | 1331467.1 | 1.72 | tvl≈129,737,310 |
| CHIPUSDT | IDLE | 1.6 | 6.3 | 1.31 | -0.08 | 1018100.21 | 4.74 | no_map |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.3 | 8.19 | 1.52 | -0.04 | 181495.34 | 31.54 | n/a |
| WUSDT | IDLE | 2.74 | 5.4 | 0.56 | -0.0 | 285827.76 | 11.23 | tvl≈1,500,872,621 |
| CCUSDT | IDLE | 1.37 | 2.52 | 1.41 | -0.03 | 394485.87 | 9.07 | no_map |
| KITEUSDT | IDLE | 1.95 | 9.23 | 4.92 | 0.13 | 131486.94 | 9.32 | no_map |
| EDELUSDT | IDLE | 0.91 | 4.68 | 4.39 | 0.07 | 166993.74 | 16.98 | no_map |
| BIOUSDT | IDLE | 1.28 | 2.39 | 1.17 | -0.01 | 67578.71 | 7.87 | n/a |
| REDUSDT | IDLE | 1.05 | 1.97 | 0.83 | 0.02 | 118153.08 | 12.16 | tvl≈2,123,536 |
| RWAINCUSDT | IDLE | 1.56 | 4.48 | 0.8 | 0.07 | 9634.94 | 65.29 | no_map |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.01 | 26.45 | 0.06 | 0.21 | 46170.19 | 1205.25 | no_map |
| QNTUSDT | IDLE | 1.92 | 3.44 | 2.6 | 0.01 | 59912.9 | 9.36 | n/a |
| HBARUSDT | IDLE | 0.76 | 1.5 | 0.13 | -0.01 | 195146.36 | 1.35 | empty_tvl |
| TELUSDT | IDLE | 1.62 | 3.03 | 1.44 | 0.04 | 74391.49 | 46.81 | no_map |
| RWAUSDT | IDLE | 1.25 | 2.31 | 1.28 | 0.01 | 52170.64 | 7.63 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.13 | 0.0 | -0.01 | 2460.23 | 21.56 | tvl≈2,604,030,332 |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.12 | -0.0 | 27219.42 | 30.25 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
