# Hulk DIGEST — 2026-10-10T10:54:08Z

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
| XRPUSDT | IDLE | 0.43 | 0.79 | 0.49 | 0.02 | 21558559.84 | 0.71 | n/a |
| BTCUSDT | IDLE | 0.19 | 0.37 | 0.1 | 0.0 | 236853043.33 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.14 | 0.27 | 0.07 | 0.0 | 105654526.13 | 0.04 | no_map |
| WUSDT | IDLE | 1.86 | 3.79 | 2.15 | -0.03 | 1251473.91 | 5.92 | tvl≈1,650,718,263 |
| PYTHUSDT | IDLE | 1.07 | 2.92 | 2.55 | -0.07 | 1336517.98 | 3.84 | tvl≈177,215,533 |
| QNTUSDT | IDLE | 1.95 | 3.57 | 2.22 | 0.02 | 1217520.3 | 1.61 | n/a |
| EDELUSDT | IDLE | 2.46 | 7.89 | 2.34 | 0.09 | 236464.5 | 10.08 | no_map |
| CCUSDT | IDLE | 1.13 | 2.08 | 1.24 | -0.01 | 460326.57 | 9.12 | no_map |
| KITEUSDT | IDLE | 2.34 | 4.47 | 1.41 | 0.01 | 77325.71 | 12.75 | no_map |
| ZBCNUSDT | IDLE | 0.71 | 1.51 | 0.31 | -0.06 | 258920.26 | 13.98 | n/a |
| CHIPUSDT | IDLE | 1.17 | 3.78 | 2.88 | 0.07 | 98884.15 | 9.52 | no_map |
| REDUSDT | IDLE | 1.47 | 2.64 | 1.94 | 0.02 | 56135.1 | 10.08 | tvl≈3,700,279 |
| RWAINCUSDT | IDLE | 1.99 | 3.65 | 2.24 | 0.01 | 13251.17 | 73.51 | no_map |
| BIOUSDT | IDLE | 1.03 | 1.82 | 1.55 | 0.03 | 72325.7 | 3.49 | n/a |
| HBARUSDT | IDLE | 0.84 | 1.51 | 1.07 | 0.02 | 336773.65 | 2.16 | empty_tvl |
| RWAUSDT | IDLE | 1.65 | 2.92 | 2.53 | -0.01 | 53265.16 | 7.86 | no_map |
| TELUSDT | IDLE | 1.62 | 2.95 | 1.91 | -0.01 | 115279.69 | 37.87 | no_map |
| RIZEUSDT | IDLE | 0.32 | 1.72 | 0.83 | 0.12 | 62168.02 | 55.52 | no_map |
| MNSRYUSDT | IDLE | 0.39 | 0.77 | 0.13 | 0.01 | 40696.5 | 4.05 | no_map |
| FLUIDUSDT | IDLE | 0.24 | 1.42 | 0.83 | 0.02 | 17321.99 | 21.77 | tvl≈2,424,735,874 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
