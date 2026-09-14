# Hulk DIGEST — 2026-09-14T21:44:11Z

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
| XRPUSDT | IDLE | 2.33 | 6.41 | 3.02 | 0.06 | 73438621.23 | 2.07 | n/a |
| ETHUSDT | IDLE | 2.36 | 4.36 | 2.46 | 0.01 | 446625042.61 | 0.78 | no_map |
| BTCUSDT | IDLE | 0.81 | 1.48 | 0.95 | 0.02 | 571046729.08 | 0.0 | no_map |
| EDELUSDT | IDLE | 2.31 | 13.42 | 4.77 | 0.15 | 284893.97 | 26.08 | no_map |
| PYTHUSDT | IDLE | 1.7 | 3.25 | 0.99 | -0.02 | 420273.14 | 7.11 | tvl≈125,785,864 |
| CCUSDT | IDLE | 2.03 | 3.82 | 1.57 | 0.02 | 316483.78 | 6.12 | no_map |
| ZBCNUSDT | IDLE | 2.42 | 4.6 | 1.57 | 0.02 | 195135.7 | 36.59 | n/a |
| WUSDT | IDLE | 1.95 | 3.63 | 1.79 | -0.01 | 214968.48 | 12.92 | tvl≈1,496,460,022 |
| KITEUSDT | IDLE | 2.28 | 4.38 | 1.19 | 0.0 | 64691.89 | 10.18 | no_map |
| TELUSDT | IDLE | 3.27 | 8.53 | 4.22 | 0.05 | 104850.84 | 36.23 | no_map |
| BIOUSDT | IDLE | 1.96 | 3.69 | 1.48 | 0.02 | 96790.51 | 19.19 | n/a |
| REDUSDT | IDLE | 1.33 | 4.94 | 0.92 | 0.08 | 188539.88 | 16.24 | tvl≈2,525,371 |
| HBARUSDT | IDLE | 1.85 | 3.5 | 1.29 | 0.02 | 363729.74 | 1.28 | empty_tvl |
| CHIPUSDT | IDLE | 1.71 | 3.17 | 2.63 | -0.04 | 90420.98 | 21.71 | no_map |
| RWAINCUSDT | IDLE | 1.35 | 2.44 | 1.79 | -0.0 | 4969.88 | 5.51 | no_map |
| RIZEUSDT | IDLE | 0.63 | 7.09 | 4.47 | -0.01 | 56232.94 | 91.67 | no_map |
| FLUIDUSDT | IDLE | 1.6 | 3.03 | 1.12 | 0.01 | 1624.56 | 23.33 | tvl≈2,706,334,533 |
| QNTUSDT | IDLE | 1.03 | 1.89 | 1.17 | 0.0 | 43355.93 | 6.25 | n/a |
| MNSRYUSDT | IDLE | 1.03 | 1.97 | 0.64 | 0.01 | 31207.68 | 41.23 | no_map |
| RWAUSDT | IDLE | 0.42 | 0.74 | 0.67 | -0.01 | 56291.93 | 22.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
