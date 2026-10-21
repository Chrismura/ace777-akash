# Hulk DIGEST — 2026-10-21T05:32:42Z

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
| ETHUSDT | IDLE | 0.51 | 0.93 | 0.66 | 0.02 | 173727107.78 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.46 | 0.86 | 0.37 | 0.03 | 24025442.04 | 1.49 | n/a |
| BTCUSDT | IDLE | 0.32 | 0.59 | 0.37 | 0.01 | 314498360.76 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.09 | 3.64 | 1.36 | 0.12 | 982356.16 | 1.24 | tvl≈178,836,516 |
| ZBCNUSDT | IDLE | 3.07 | 13.82 | 2.7 | 0.13 | 226514.2 | 27.04 | n/a |
| WUSDT | IDLE | 1.64 | 3.1 | 1.21 | 0.04 | 635812.87 | 17.75 | tvl≈1,600,129,748 |
| CHIPUSDT | IDLE | 1.69 | 4.2 | 0.33 | 0.03 | 437108.05 | 13.25 | no_map |
| QNTUSDT | IDLE | 1.19 | 2.18 | 1.29 | 0.01 | 783614.49 | 1.53 | n/a |
| EDELUSDT | IDLE | 1.22 | 6.45 | 4.82 | 0.19 | 361305.35 | 5.75 | no_map |
| RWAINCUSDT | IDLE | 1.49 | 7.16 | 2.99 | -0.06 | 77813.94 | 16.52 | no_map |
| CCUSDT | IDLE | 0.64 | 1.12 | 1.09 | 0.0 | 298179.71 | 8.58 | no_map |
| REDUSDT | IDLE | 1.66 | 3.19 | 0.87 | 0.04 | 57964.75 | 16.69 | tvl≈3,585,431 |
| KITEUSDT | IDLE | 0.94 | 1.86 | 0.08 | -0.0 | 71330.02 | 11.35 | no_map |
| HBARUSDT | IDLE | 0.94 | 1.64 | 1.61 | -0.0 | 333332.3 | 4.81 | empty_tvl |
| BIOUSDT | IDLE | 0.66 | 1.23 | 0.65 | 0.04 | 60457.35 | 8.13 | n/a |
| LAUSDT | IDLE | 1.97 | 4.82 | 1.73 | 0.06 | 56142.76 | 25.11 | no_map |
| RIZEUSDT | IDLE | 0.75 | 3.01 | 1.7 | 0.06 | 61031.29 | 59.81 | no_map |
| WAXLUSDT | IDLE | 1.77 | 3.28 | 1.79 | -0.03 | 57457.71 | 60.12 | no_map |
| IOTAUSDT | IDLE | 1.01 | 1.8 | 1.49 | 0.01 | 75673.56 | 17.34 | no_map |
| FLUIDUSDT | IDLE | 0.44 | 1.6 | 1.53 | 0.02 | 14691.99 | 21.26 | tvl≈2,238,819,653 |
| MNSRYUSDT | IDLE | 0.17 | 0.33 | 0.06 | 0.0 | 39934.26 | 9.98 | no_map |
| RWAUSDT | IDLE | 0.33 | 0.63 | 0.23 | 0.0 | 52390.45 | 39.2 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
