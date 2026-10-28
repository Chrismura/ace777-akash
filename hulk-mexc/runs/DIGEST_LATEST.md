# Hulk DIGEST — 2026-10-28T20:36:56Z

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
| ETHUSDT | IDLE | 1.48 | 2.74 | 1.53 | 0.0 | 196890626.39 | 0.08 | skipped_fast |
| XRPUSDT | IDLE | 1.45 | 2.71 | 1.24 | 0.0 | 23332488.94 | 2.26 | skipped_fast |
| BTCUSDT | IDLE | 0.91 | 1.7 | 0.75 | 0.01 | 322255969.83 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.95 | 5.45 | 3.04 | -0.01 | 427481.93 | 4.16 | skipped_fast |
| CCUSDT | IDLE | 1.82 | 4.22 | 1.3 | 0.03 | 428860.6 | 6.93 | skipped_fast |
| WUSDT | IDLE | 1.79 | 3.26 | 2.15 | -0.0 | 417755.17 | 18.05 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 4.89 | 1.73 | -0.01 | 418873.78 | 3.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 7.31 | 3.54 | -0.09 | 238378.24 | 10.08 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.13 | 2.0 | -0.01 | 581827.24 | 6.63 | skipped_fast |
| BIOUSDT | IDLE | 2.34 | 4.39 | 1.93 | 0.01 | 88858.94 | 8.74 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 5.32 | 4.79 | -0.05 | 34719.79 | 13.8 | skipped_fast |
| ZBCNUSDT | IDLE | 1.26 | 2.42 | 0.72 | -0.03 | 283296.92 | 17.79 | skipped_fast |
| EDELUSDT | IDLE | 1.45 | 2.56 | 2.31 | -0.01 | 186515.32 | 34.26 | skipped_fast |
| KITEUSDT | IDLE | 1.64 | 3.01 | 1.8 | -0.02 | 59755.93 | 11.23 | skipped_fast |
| RIZEUSDT | IDLE | 2.0 | 3.51 | 3.21 | -0.0 | 39559.94 | 65.33 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.65 | 1.37 | -0.03 | 53887.07 | 14.46 | skipped_fast |
| IOTAUSDT | IDLE | 2.63 | 4.9 | 2.46 | 0.0 | 75915.41 | 28.61 | skipped_fast |
| LAUSDT | IDLE | 2.01 | 3.83 | 1.23 | -0.03 | 57240.9 | 22.13 | skipped_fast |
| WAXLUSDT | IDLE | 2.04 | 3.82 | 1.77 | -0.0 | 55188.52 | 30.65 | skipped_fast |
| RWAUSDT | IDLE | 0.73 | 1.37 | 0.56 | 0.0 | 55230.65 | 7.98 | skipped_fast |
| FLUIDUSDT | IDLE | 0.96 | 3.23 | 0.0 | 0.01 | 6418.19 | 19.11 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.13 | 0.01 | 35475.29 | 40.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
