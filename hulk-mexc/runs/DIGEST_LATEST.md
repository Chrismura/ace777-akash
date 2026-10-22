# Hulk DIGEST — 2026-10-22T09:28:17Z

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
| WUSDT | IDLE | 1.51 | 6.56 | 5.68 | -0.04 | 3483674.83 | 13.25 | tvl≈1,567,890,807 |
| ETHUSDT | IDLE | 1.25 | 2.2 | 2.03 | -0.03 | 258823369.87 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.15 | 2.02 | 1.89 | -0.02 | 34826196.33 | 1.51 | n/a |
| BTCUSDT | IDLE | 0.92 | 1.62 | 1.47 | -0.02 | 517809111.33 | 0.0 | no_map |
| HBARUSDT | IDLE | 1.73 | 3.09 | 2.48 | -0.05 | 1381800.03 | 8.67 | empty_tvl |
| QNTUSDT | IDLE | 1.75 | 4.13 | 3.61 | -0.02 | 1265411.2 | 1.02 | n/a |
| CHIPUSDT | IDLE | 2.39 | 9.22 | 8.29 | -0.03 | 345431.11 | 13.83 | no_map |
| PYTHUSDT | IDLE | 1.45 | 3.74 | 3.33 | -0.07 | 637275.22 | 5.4 | tvl≈166,252,005 |
| EDELUSDT | IDLE | 1.51 | 2.68 | 2.29 | -0.02 | 543386.64 | 14.84 | no_map |
| CCUSDT | IDLE | 1.13 | 3.07 | 2.32 | -0.03 | 392574.27 | 5.74 | no_map |
| ZBCNUSDT | IDLE | 1.2 | 3.33 | 2.53 | -0.05 | 249017.92 | 13.92 | n/a |
| BIOUSDT | IDLE | 1.61 | 3.25 | 3.02 | -0.05 | 78675.83 | 8.42 | n/a |
| REDUSDT | IDLE | 1.6 | 2.96 | 2.7 | -0.02 | 80585.86 | 16.24 | tvl≈3,601,320 |
| RWAINCUSDT | IDLE | 1.98 | 3.81 | 1.06 | -0.06 | 60778.77 | 44.99 | no_map |
| KITEUSDT | IDLE | 0.98 | 1.82 | 0.88 | -0.02 | 59568.44 | 12.52 | no_map |
| IOTAUSDT | IDLE | 2.02 | 3.84 | 3.16 | -0.04 | 78680.49 | 31.07 | no_map |
| RIZEUSDT | IDLE | 1.16 | 2.32 | 0.36 | 0.04 | 44956.29 | 56.93 | no_map |
| LAUSDT | IDLE | 1.8 | 4.63 | 3.54 | -0.06 | 62739.48 | 23.48 | no_map |
| WAXLUSDT | IDLE | 1.8 | 6.13 | 4.68 | -0.09 | 57872.09 | 41.12 | no_map |
| FLUIDUSDT | IDLE | 0.44 | 2.22 | 1.49 | -0.0 | 19847.24 | 21.38 | tvl≈2,225,671,718 |
| RWAUSDT | IDLE | 0.36 | 0.63 | 0.55 | -0.0 | 52854.71 | 15.75 | no_map |
| MNSRYUSDT | IDLE | 0.5 | 0.88 | 0.82 | -0.0 | 40071.85 | 55.51 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
