# Hulk DIGEST — 2026-09-14T21:43:25Z

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
| XRPUSDT | IDLE | 2.33 | 6.41 | 3.02 | 0.06 | 73431552.71 | 2.76 | skipped_fast |
| ETHUSDT | IDLE | 2.37 | 4.36 | 2.5 | 0.01 | 446639881.26 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.48 | 0.95 | 0.02 | 570975793.03 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 13.42 | 4.77 | 0.15 | 284993.98 | 19.56 | skipped_fast |
| PYTHUSDT | IDLE | 1.7 | 3.25 | 1.02 | -0.02 | 420246.07 | 5.33 | skipped_fast |
| CCUSDT | IDLE | 2.03 | 3.82 | 1.57 | 0.02 | 316476.86 | 6.12 | skipped_fast |
| ZBCNUSDT | IDLE | 2.42 | 4.6 | 1.61 | 0.02 | 195099.13 | 38.18 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.63 | 1.74 | -0.01 | 214937.57 | 14.9 | skipped_fast |
| KITEUSDT | IDLE | 2.28 | 4.38 | 1.2 | 0.0 | 64669.61 | 10.18 | skipped_fast |
| TELUSDT | IDLE | 3.27 | 8.53 | 4.16 | 0.05 | 104887.05 | 36.23 | skipped_fast |
| BIOUSDT | IDLE | 1.96 | 3.69 | 1.48 | 0.01 | 96817.59 | 7.69 | skipped_fast |
| HBARUSDT | IDLE | 1.85 | 3.5 | 1.29 | 0.02 | 363731.15 | 1.28 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 4.94 | 0.98 | 0.08 | 188500.39 | 22.61 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 3.17 | 2.65 | -0.04 | 90478.0 | 19.29 | skipped_fast |
| RWAINCUSDT | IDLE | 1.35 | 2.44 | 1.79 | -0.0 | 4969.88 | 5.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 7.09 | 4.27 | -0.01 | 56238.29 | 95.85 | skipped_fast |
| FLUIDUSDT | IDLE | 1.6 | 3.03 | 1.12 | 0.01 | 1624.56 | 23.33 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 1.89 | 1.2 | 0.0 | 43355.93 | 9.37 | skipped_fast |
| MNSRYUSDT | IDLE | 1.03 | 1.97 | 0.66 | 0.01 | 31193.41 | 41.23 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.74 | 0.67 | -0.01 | 56275.72 | 22.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
