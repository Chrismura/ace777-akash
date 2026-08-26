# Hulk DIGEST — 2026-08-26T05:45:58Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 3.32 | 7.01 | 0.9 | 0.01 | 2680196.37 | 1.9 | tvl≈112,350,117 |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 74.43 | 39.75 | 0.08 | 62510.18 | 57.92 | no_map |
| XRPUSDT | IDLE | 0.96 | 1.88 | 0.43 | -0.05 | 60206929.53 | 1.38 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.92 | 31.72 | 11.65 | 0.13 | 16220.03 | 21.57 | tvl≈2,590,725,714 |
| CHIPUSDT | IDLE | 1.64 | 4.71 | 1.64 | -0.03 | 377038.49 | 6.18 | no_map |
| CCUSDT | IDLE | 1.14 | 2.24 | 1.59 | -0.05 | 511922.65 | 5.89 | no_map |
| WUSDT | IDLE | 1.56 | 3.09 | 0.24 | -0.03 | 289798.33 | 11.55 | tvl≈1,560,036,122 |
| EDELUSDT | IDLE | 0.89 | 12.46 | 9.97 | 0.01 | 157152.37 | 28.45 | no_map |
| REDUSDT | IDLE | 2.0 | 4.97 | 3.27 | -0.02 | 75497.98 | 12.22 | tvl≈2,111,212 |
| BIOUSDT | IDLE | 1.98 | 3.51 | 2.95 | -0.04 | 93497.28 | 7.0 | n/a |
| KITEUSDT | IDLE | 2.08 | 4.0 | 1.03 | -0.0 | 60073.23 | 12.16 | no_map |
| ZBCNUSDT | IDLE | 1.56 | 2.99 | 0.87 | -0.02 | 159497.19 | 16.29 | n/a |
| HBARUSDT | IDLE | 0.97 | 1.84 | 0.61 | -0.05 | 552573.15 | 1.28 | empty_tvl |
| QAITUSDT | IDLE | 1.61 | 3.03 | 1.32 | 0.02 | 10748.98 | 63.14 | no_map |
| TELUSDT | IDLE | 1.22 | 2.33 | 0.71 | -0.03 | 93468.86 | 21.83 | no_map |
| QNTUSDT | IDLE | 0.62 | 1.17 | 0.49 | -0.04 | 130460.99 | 3.15 | n/a |
| RWAUSDT | IDLE | 1.13 | 2.01 | 1.72 | -0.05 | 56232.77 | 33.42 | no_map |
| RWAINCUSDT | IDLE | 0.78 | 1.37 | 1.3 | -0.01 | 1277.4 | 131.05 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
