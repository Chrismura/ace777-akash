# Hulk DIGEST — 2026-10-27T22:17:22Z

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
| ETHUSDT | IDLE | 0.55 | 1.03 | 0.47 | 0.02 | 234910250.76 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.03 | 0.36 | 0.01 | 326922541.22 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.55 | 1.06 | 0.29 | 0.03 | 20351152.91 | 2.26 | skipped_fast |
| WUSDT | IDLE | 0.95 | 2.06 | 1.6 | 0.04 | 681490.29 | 22.74 | skipped_fast |
| EDELUSDT | IDLE | 1.53 | 2.89 | 1.09 | 0.02 | 465174.56 | 24.46 | skipped_fast |
| ZBCNUSDT | IDLE | 2.17 | 6.63 | 5.06 | -0.01 | 239458.87 | 41.67 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 2.66 | 0.66 | -0.0 | 394997.92 | 2.72 | skipped_fast |
| QNTUSDT | IDLE | 1.28 | 2.39 | 1.08 | -0.01 | 708707.77 | 3.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 3.57 | 2.03 | 0.06 | 132368.94 | 14.82 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 3.57 | 3.25 | -0.05 | 63050.13 | 20.21 | skipped_fast |
| CCUSDT | IDLE | 0.8 | 1.52 | 0.59 | 0.0 | 218911.76 | 8.09 | skipped_fast |
| RIZEUSDT | IDLE | 1.77 | 3.53 | 0.12 | 0.01 | 32985.82 | 46.24 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.39 | 1.17 | 0.06 | 59642.95 | 14.17 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 1.83 | 1.05 | 0.02 | 59151.66 | 8.85 | skipped_fast |
| KITEUSDT | IDLE | 0.76 | 1.47 | 0.52 | 0.04 | 57611.28 | 13.49 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.31 | 0.63 | -0.01 | 300904.1 | 9.17 | skipped_fast |
| LAUSDT | IDLE | 1.24 | 2.46 | 1.49 | 0.04 | 59030.47 | 23.05 | skipped_fast |
| IOTAUSDT | IDLE | 0.72 | 1.36 | 0.52 | 0.01 | 79411.79 | 30.84 | skipped_fast |
| WAXLUSDT | IDLE | 0.8 | 1.5 | 0.67 | 0.04 | 56865.8 | 30.6 | skipped_fast |
| FLUIDUSDT | IDLE | 0.32 | 0.63 | 0.12 | 0.02 | 2583.56 | 21.39 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.64 | 0.48 | -0.0 | 58120.17 | 55.98 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.81 | 0.06 | 0.01 | 37886.19 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
