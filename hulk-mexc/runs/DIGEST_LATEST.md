# Hulk DIGEST — 2026-09-28T20:42:28Z

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
| HBARUSDT | IDLE | 1.59 | 14.78 | 7.19 | 0.28 | 11429091.4 | 7.41 | empty_tvl |
| WUSDT | IDLE | 1.0 | 4.77 | 2.44 | -0.14 | 2138198.34 | 11.75 | tvl≈1,812,436,572 |
| QNTUSDT | IDLE | 0.85 | 18.61 | 4.69 | 0.27 | 21915618.29 | 8.5 | n/a |
| XRPUSDT | IDLE | 1.71 | 3.16 | 1.79 | -0.02 | 68451860.82 | 2.01 | n/a |
| ETHUSDT | IDLE | 1.33 | 2.45 | 1.34 | -0.0 | 406160454.95 | 0.19 | no_map |
| BTCUSDT | IDLE | 1.01 | 1.88 | 0.92 | -0.01 | 845282917.2 | 0.0 | no_map |
| CCUSDT | IDLE | 1.51 | 5.9 | 1.79 | -0.04 | 1352545.61 | 9.14 | no_map |
| PYTHUSDT | IDLE | 1.86 | 3.93 | 1.63 | -0.06 | 1262130.03 | 3.77 | tvl≈177,971,605 |
| TELUSDT | IDLE | 3.55 | 27.82 | 3.1 | 0.21 | 297768.65 | 26.64 | no_map |
| RWAINCUSDT | IDLE | 3.49 | 9.08 | 2.58 | 0.01 | 16290.03 | 23.89 | no_map |
| KITEUSDT | IDLE | 1.66 | 6.35 | 2.46 | -0.09 | 101039.38 | 9.42 | no_map |
| CHIPUSDT | IDLE | 1.64 | 3.9 | 1.91 | -0.06 | 74271.28 | 9.16 | no_map |
| RIZEUSDT | IDLE | 1.97 | 6.81 | 0.23 | 0.09 | 51937.08 | 54.08 | no_map |
| ZBCNUSDT | IDLE | 1.4 | 2.77 | 0.26 | -0.04 | 232024.24 | 65.49 | n/a |
| BIOUSDT | IDLE | 1.2 | 3.62 | 1.41 | -0.07 | 115265.8 | 3.41 | n/a |
| REDUSDT | IDLE | 1.56 | 3.05 | 1.71 | -0.07 | 59945.5 | 14.96 | tvl≈2,939,149 |
| EDELUSDT | IDLE | 0.51 | 3.12 | 2.17 | 0.1 | 169657.97 | 20.8 | no_map |
| FLUIDUSDT | IDLE | 1.54 | 3.66 | 2.11 | -0.06 | 5202.95 | 21.38 | tvl≈2,578,424,391 |
| RWAUSDT | IDLE | 0.82 | 1.52 | 0.85 | -0.02 | 60064.73 | 28.72 | no_map |
| MNSRYUSDT | IDLE | 0.42 | 0.76 | 0.53 | -0.02 | 34786.44 | 16.76 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
