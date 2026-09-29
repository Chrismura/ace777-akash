# Hulk DIGEST — 2026-09-29T11:45:16Z

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
| QNTUSDT | IDLE | 2.06 | 17.29 | 10.72 | -0.0 | 9740327.09 | 11.19 | n/a |
| ETHUSDT | IDLE | 1.14 | 2.21 | 0.43 | 0.02 | 403241348.2 | 0.04 | no_map |
| HBARUSDT | IDLE | 0.86 | 3.06 | 0.77 | 0.0 | 8083625.81 | 6.74 | empty_tvl |
| XRPUSDT | IDLE | 0.71 | 1.39 | 0.17 | 0.01 | 55446904.43 | 1.32 | n/a |
| BTCUSDT | IDLE | 0.56 | 1.1 | 0.14 | 0.01 | 619527054.37 | 0.0 | no_map |
| WUSDT | IDLE | 2.31 | 6.61 | 1.61 | 0.04 | 1099049.61 | 6.82 | tvl≈1,833,588,849 |
| CCUSDT | IDLE | 1.97 | 3.53 | 2.8 | -0.02 | 1005440.44 | 6.9 | no_map |
| PYTHUSDT | IDLE | 1.66 | 3.03 | 1.89 | -0.0 | 979800.95 | 3.76 | tvl≈179,900,383 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 22.27 | 9.19 | 0.18 | 323918.3 | 29.04 | n/a |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 13.69 | 9.92 | -0.07 | 57304.46 | 81.49 | no_map |
| BIOUSDT | IDLE | 2.88 | 8.4 | 2.51 | 0.06 | 103685.62 | 9.54 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 18.09 | 8.43 | 0.08 | 14307.24 | 21.77 | tvl≈2,615,218,523 |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 8.47 | 6.94 | 0.04 | 38408.15 | 78.61 | no_map |
| KITEUSDT | IDLE | 2.36 | 4.54 | 1.24 | 0.03 | 72401.69 | 7.8 | no_map |
| CHIPUSDT | IDLE | 1.88 | 4.34 | 0.46 | 0.01 | 71225.56 | 17.73 | no_map |
| REDUSDT | IDLE | 1.34 | 2.67 | 0.1 | -0.0 | 57156.11 | 13.49 | tvl≈2,903,336 |
| TELUSDT | IDLE | 0.77 | 7.55 | 1.29 | 0.29 | 425942.38 | 39.28 | no_map |
| EDELUSDT | IDLE | 0.46 | 2.05 | 0.61 | -0.12 | 107331.99 | 15.26 | no_map |
| MNSRYUSDT | IDLE | 1.14 | 2.24 | 0.24 | -0.0 | 36287.22 | 23.23 | no_map |
| RWAUSDT | IDLE | 0.52 | 1.02 | 0.07 | 0.0 | 57078.32 | 7.2 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
