# Hulk DIGEST — 2026-09-14T19:43:11Z

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
| XRPUSDT | IDLE | 2.39 | 6.3 | 1.49 | 0.08 | 62857201.6 | 1.37 | n/a |
| ETHUSDT | IDLE | 1.14 | 2.23 | 0.38 | 0.01 | 376179000.7 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.76 | 1.48 | 0.33 | 0.02 | 533178671.17 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.02 | 3.8 | 1.58 | -0.02 | 445015.87 | 1.79 | tvl≈123,454,477 |
| REDUSDT | IDLE | 2.48 | 8.59 | 5.95 | 0.06 | 184859.26 | 15.77 | tvl≈2,525,371 |
| EDELUSDT | IDLE | 1.75 | 8.78 | 1.36 | 0.12 | 268147.93 | 26.18 | no_map |
| CCUSDT | IDLE | 1.6 | 3.08 | 0.78 | 0.02 | 306623.79 | 10.25 | no_map |
| WUSDT | IDLE | 1.82 | 3.5 | 0.87 | -0.0 | 204339.35 | 6.96 | tvl≈1,488,461,683 |
| ZBCNUSDT | IDLE | 1.64 | 3.15 | 0.93 | 0.02 | 207558.18 | 9.9 | n/a |
| BIOUSDT | IDLE | 2.04 | 3.83 | 1.6 | 0.02 | 91674.54 | 3.86 | n/a |
| TELUSDT | IDLE | 3.18 | 8.53 | 2.43 | 0.06 | 100237.1 | 29.59 | no_map |
| RIZEUSDT | IDLE | 0.96 | 10.63 | 8.41 | -0.02 | 54447.29 | 4.21 | no_map |
| CHIPUSDT | IDLE | 1.68 | 3.17 | 2.23 | -0.04 | 90227.93 | 16.82 | no_map |
| HBARUSDT | IDLE | 1.56 | 2.99 | 0.8 | 0.02 | 317556.97 | 1.28 | empty_tvl |
| KITEUSDT | IDLE | 1.46 | 2.92 | 0.01 | 0.0 | 63053.64 | 9.29 | no_map |
| RWAINCUSDT | IDLE | 1.5 | 2.84 | 1.08 | 0.02 | 9883.54 | 5.48 | no_map |
| QNTUSDT | IDLE | 1.08 | 1.97 | 1.28 | -0.01 | 42733.06 | 4.69 | n/a |
| FLUIDUSDT | IDLE | 1.28 | 2.54 | 0.09 | 0.03 | 1014.14 | 21.74 | tvl≈2,686,693,274 |
| MNSRYUSDT | IDLE | 0.8 | 1.55 | 0.32 | 0.0 | 30424.68 | 37.36 | no_map |
| RWAUSDT | IDLE | 0.24 | 0.45 | 0.15 | 0.0 | 55822.64 | 29.63 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
