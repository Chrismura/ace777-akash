# Hulk DIGEST — 2026-10-19T17:55:13Z

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
| ETHUSDT | IDLE | 1.02 | 1.83 | 1.37 | 0.01 | 159221711.09 | 0.21 | skipped_fast |
| XRPUSDT | IDLE | 0.92 | 1.67 | 1.19 | 0.02 | 28248814.51 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 0.68 | 1.2 | 1.03 | 0.01 | 363039493.42 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.31 | 4.17 | 3.03 | -0.03 | 948576.83 | 4.13 | skipped_fast |
| WUSDT | IDLE | 2.89 | 5.38 | 2.63 | 0.0 | 588743.11 | 16.94 | skipped_fast |
| RIZEUSDT | IDLE | 3.13 | 10.75 | 4.27 | -0.07 | 53183.67 | 16.1 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 3.0 | 2.08 | 0.03 | 810918.37 | 1.53 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 3.34 | 2.67 | 0.05 | 400639.67 | 9.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.88 | 6.71 | 2.05 | 0.04 | 82367.92 | 25.46 | skipped_fast |
| HBARUSDT | IDLE | 1.52 | 2.72 | 2.08 | -0.03 | 550056.57 | 4.86 | skipped_fast |
| KITEUSDT | IDLE | 2.19 | 6.16 | 2.65 | 0.08 | 65005.29 | 9.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.14 | 3.81 | 3.52 | 0.02 | 256299.99 | 17.86 | skipped_fast |
| EDELUSDT | IDLE | 1.38 | 2.86 | 1.32 | 0.02 | 223496.14 | 22.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 4.45 | 1.02 | 0.05 | 72774.55 | 14.33 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.81 | 2.5 | 0.01 | 59130.36 | 19.9 | skipped_fast |
| BIOUSDT | IDLE | 1.17 | 2.07 | 1.86 | 0.01 | 71339.2 | 4.3 | skipped_fast |
| LAUSDT | IDLE | 1.61 | 2.81 | 2.68 | 0.02 | 56193.25 | 23.1 | skipped_fast |
| WAXLUSDT | IDLE | 1.47 | 4.38 | 3.49 | 0.03 | 77605.09 | 35.49 | skipped_fast |
| IOTAUSDT | IDLE | 1.09 | 1.95 | 1.49 | 0.01 | 74506.75 | 22.56 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 2.04 | 2.0 | 0.02 | 5687.98 | 21.57 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.11 | 0.63 | 0.01 | 54876.99 | 23.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.13 | -0.0 | 39961.0 | 15.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
