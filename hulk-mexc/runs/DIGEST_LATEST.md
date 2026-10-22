# Hulk DIGEST — 2026-10-22T08:27:02Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 1.68 | 7.06 | 6.29 | -0.02 | 3481631.78 | 15.41 | tvl≈1,581,491,256 |
| XRPUSDT | IDLE | 0.93 | 1.62 | 1.58 | -0.01 | 35342326.37 | 2.25 | n/a |
| ETHUSDT | IDLE | 0.85 | 1.49 | 1.45 | -0.02 | 255377936.69 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.7 | 1.22 | 1.2 | -0.01 | 518912380.45 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.0 | 4.78 | 3.67 | -0.02 | 1233043.74 | 2.55 | n/a |
| PYTHUSDT | IDLE | 2.1 | 4.9 | 4.37 | -0.06 | 634965.7 | 1.34 | tvl≈173,912,677 |
| CHIPUSDT | IDLE | 2.42 | 8.08 | 7.37 | -0.03 | 356698.66 | 13.55 | no_map |
| HBARUSDT | IDLE | 1.25 | 2.2 | 1.99 | -0.04 | 989364.46 | 6.16 | empty_tvl |
| EDELUSDT | IDLE | 1.46 | 2.68 | 1.54 | -0.01 | 525487.96 | 14.76 | no_map |
| CCUSDT | IDLE | 1.55 | 4.08 | 3.67 | -0.02 | 393742.73 | 8.62 | no_map |
| BIOUSDT | IDLE | 1.8 | 3.58 | 3.13 | -0.04 | 78494.7 | 4.19 | n/a |
| REDUSDT | IDLE | 1.85 | 3.31 | 2.82 | -0.01 | 80738.56 | 8.42 | tvl≈3,601,320 |
| ZBCNUSDT | IDLE | 1.15 | 3.07 | 2.7 | -0.06 | 249532.27 | 25.23 | n/a |
| RWAINCUSDT | IDLE | 0.94 | 3.81 | 2.0 | -0.04 | 67947.17 | 5.66 | no_map |
| KITEUSDT | IDLE | 1.15 | 2.07 | 1.59 | -0.02 | 60285.16 | 10.86 | no_map |
| RIZEUSDT | IDLE | 1.18 | 2.32 | 0.63 | 0.04 | 44965.61 | 42.33 | no_map |
| IOTAUSDT | IDLE | 2.08 | 3.83 | 3.51 | -0.04 | 79155.41 | 26.69 | no_map |
| WAXLUSDT | IDLE | 2.0 | 6.55 | 5.76 | -0.1 | 58043.56 | 51.67 | no_map |
| LAUSDT | IDLE | 1.8 | 4.38 | 4.0 | -0.05 | 63094.83 | 18.1 | no_map |
| FLUIDUSDT | IDLE | 0.36 | 1.7 | 1.5 | -0.0 | 19898.73 | 21.66 | tvl≈2,239,011,687 |
| RWAUSDT | IDLE | 0.29 | 0.55 | 0.24 | -0.0 | 52252.5 | 23.59 | no_map |
| MNSRYUSDT | IDLE | 0.5 | 0.88 | 0.86 | -0.0 | 39524.26 | 55.51 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
