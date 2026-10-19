# Hulk DIGEST — 2026-10-19T18:02:48Z

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
| ETHUSDT | IDLE | 0.99 | 1.83 | 1.01 | 0.01 | 159614157.05 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.9 | 1.67 | 0.8 | 0.02 | 28251823.31 | 0.77 | n/a |
| BTCUSDT | IDLE | 0.66 | 1.2 | 0.79 | 0.01 | 362867672.8 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.29 | 4.17 | 2.68 | -0.03 | 943903.73 | 12.34 | tvl≈163,756,094 |
| WUSDT | IDLE | 2.05 | 3.76 | 2.23 | 0.0 | 589250.32 | 15.34 | tvl≈1,562,409,680 |
| RIZEUSDT | IDLE | 3.12 | 10.68 | 4.41 | -0.07 | 53191.29 | 34.59 | no_map |
| QNTUSDT | IDLE | 1.05 | 3.0 | 1.97 | 0.03 | 810044.05 | 5.61 | n/a |
| CCUSDT | IDLE | 1.49 | 3.34 | 2.57 | 0.05 | 400538.47 | 6.76 | no_map |
| HBARUSDT | IDLE | 1.51 | 2.72 | 1.99 | -0.03 | 551320.88 | 6.06 | empty_tvl |
| RWAINCUSDT | IDLE | 2.19 | 5.17 | 1.11 | 0.03 | 83072.43 | 5.12 | no_map |
| KITEUSDT | IDLE | 1.94 | 5.44 | 2.63 | 0.07 | 65146.25 | 9.1 | no_map |
| ZBCNUSDT | IDLE | 1.09 | 3.78 | 2.49 | 0.03 | 258249.08 | 23.4 | n/a |
| EDELUSDT | IDLE | 1.34 | 2.86 | 0.77 | 0.04 | 223124.6 | 29.6 | no_map |
| CHIPUSDT | IDLE | 1.58 | 4.45 | 0.78 | 0.05 | 71833.52 | 11.96 | no_map |
| REDUSDT | IDLE | 1.52 | 2.72 | 2.18 | 0.01 | 59004.59 | 8.08 | tvl≈3,443,960 |
| BIOUSDT | IDLE | 1.14 | 2.07 | 1.43 | 0.01 | 71278.67 | 4.29 | n/a |
| LAUSDT | IDLE | 1.59 | 2.81 | 2.42 | 0.01 | 56232.96 | 23.05 | no_map |
| WAXLUSDT | IDLE | 1.47 | 3.84 | 2.89 | 0.02 | 77725.0 | 51.5 | no_map |
| IOTAUSDT | IDLE | 1.07 | 1.95 | 1.27 | 0.01 | 74555.52 | 15.78 | no_map |
| RWAUSDT | IDLE | 0.6 | 1.11 | 0.55 | 0.01 | 54860.92 | 7.89 | no_map |
| FLUIDUSDT | IDLE | 0.83 | 2.04 | 2.0 | 0.02 | 5687.98 | 21.11 | tvl≈2,221,001,573 |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.17 | -0.0 | 40156.05 | 15.67 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
