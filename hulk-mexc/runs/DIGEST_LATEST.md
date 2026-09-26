# Hulk DIGEST — 2026-09-26T17:01:29Z

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
| XRPUSDT | IDLE | 0.6 | 1.12 | 0.51 | -0.01 | 42214633.04 | 2.59 | n/a |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.83 | 19.89 | 0.75 | 0.25 | 1244370.98 | 16.28 | n/a |
| ETHUSDT | IDLE | 0.27 | 0.52 | 0.17 | 0.0 | 128027486.45 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.08 | 0.0 | 340208683.46 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.56 | 4.19 | 1.79 | 0.08 | 997978.52 | 1.28 | tvl≈176,197,476 |
| CCUSDT | IDLE | 1.68 | 4.54 | 1.17 | 0.11 | 951276.19 | 5.76 | no_map |
| CHIPUSDT | IDLE | 3.94 | 8.54 | 2.76 | 0.04 | 115518.11 | 13.82 | no_map |
| WUSDT | IDLE | 1.94 | 4.83 | 0.54 | 0.09 | 450704.77 | 9.9 | tvl≈1,897,621,524 |
| EDELUSDT | IDLE | 2.25 | 4.2 | 2.01 | 0.03 | 162429.73 | 3.26 | no_map |
| KITEUSDT | IDLE | 2.66 | 6.16 | 0.06 | 0.11 | 79724.39 | 16.78 | no_map |
| RWAINCUSDT | IDLE | 2.95 | 9.15 | 4.83 | -0.02 | 8024.31 | 98.06 | no_map |
| ZBCNUSDT | IDLE | 1.49 | 2.74 | 1.64 | -0.02 | 220476.63 | 11.63 | n/a |
| HBARUSDT | IDLE | 1.22 | 2.42 | 0.14 | 0.02 | 529758.35 | 1.05 | empty_tvl |
| BIOUSDT | IDLE | 1.24 | 2.48 | 0.06 | -0.01 | 105645.8 | 3.03 | n/a |
| REDUSDT | IDLE | 0.66 | 1.27 | 0.34 | -0.03 | 57414.1 | 8.29 | tvl≈3,072,611 |
| RWAUSDT | IDLE | 1.48 | 2.86 | 0.71 | 0.02 | 55709.39 | 7.18 | no_map |
| RIZEUSDT | IDLE | 0.4 | 1.75 | 0.79 | -0.07 | 41439.87 | 61.89 | no_map |
| TELUSDT | IDLE | 1.13 | 2.22 | 0.31 | -0.02 | 127337.36 | 68.3 | no_map |
| MNSRYUSDT | IDLE | 0.26 | 0.52 | 0.06 | 0.0 | 39807.85 | 7.64 | no_map |
| FLUIDUSDT | IDLE | 0.27 | 0.49 | 0.28 | 0.01 | 750.49 | 21.93 | tvl≈2,585,024,890 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
