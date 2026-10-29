# Hulk DIGEST — 2026-10-29T12:23:50Z

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
| ETHUSDT | IDLE | 0.56 | 1.08 | 0.25 | -0.01 | 233664515.16 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.41 | 0.74 | 0.53 | -0.02 | 23205075.88 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.32 | -0.01 | 339667767.52 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.49 | 4.97 | 0.02 | 0.01 | 416968.23 | 8.94 | skipped_fast |
| WUSDT | IDLE | 1.55 | 2.87 | 1.55 | -0.03 | 483873.96 | 14.6 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 2.41 | 2.34 | -0.03 | 444081.81 | 5.77 | skipped_fast |
| EDELUSDT | IDLE | 1.52 | 2.73 | 2.09 | -0.04 | 233324.16 | 28.98 | skipped_fast |
| CHIPUSDT | IDLE | 1.28 | 4.1 | 1.03 | -0.08 | 191572.6 | 10.39 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.13 | 0.61 | -0.02 | 559158.98 | 4.07 | skipped_fast |
| BIOUSDT | IDLE | 1.49 | 2.9 | 0.49 | -0.01 | 66881.66 | 8.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.35 | 4.82 | 1.6 | -0.1 | 34358.07 | 7.08 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 2.02 | 0.95 | -0.02 | 424488.89 | 4.66 | skipped_fast |
| ZBCNUSDT | IDLE | 0.62 | 1.1 | 1.0 | -0.01 | 249556.69 | 25.01 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.26 | 0.18 | -0.02 | 64590.11 | 10.08 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.19 | 0.25 | -0.02 | 60064.15 | 9.68 | skipped_fast |
| LAUSDT | IDLE | 2.06 | 3.7 | 2.81 | -0.03 | 57729.77 | 21.15 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 0.89 | 0.56 | -0.02 | 39643.14 | 49.3 | skipped_fast |
| RWAUSDT | IDLE | 1.15 | 2.01 | 1.9 | -0.01 | 55973.21 | 16.1 | skipped_fast |
| WAXLUSDT | IDLE | 1.32 | 3.33 | 0.17 | -0.04 | 54128.77 | 36.54 | skipped_fast |
| FLUIDUSDT | IDLE | 1.39 | 2.79 | 0.99 | -0.06 | 6322.22 | 21.25 | skipped_fast |
| IOTAUSDT | IDLE | 1.06 | 2.04 | 0.94 | -0.04 | 94304.1 | 29.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.72 | 0.16 | -0.01 | 36394.22 | 5.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
