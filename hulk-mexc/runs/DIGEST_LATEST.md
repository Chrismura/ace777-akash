# Hulk DIGEST — 2026-10-18T22:08:49Z

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
| XRPUSDT | IDLE | 1.52 | 3.02 | 0.19 | 0.0 | 26911714.01 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 1.46 | 2.87 | 0.31 | 0.0 | 114617780.94 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.04 | 5.76 | 2.36 | -0.1 | 1491520.68 | 4.07 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.21 | 0.1 | 0.0 | 227408794.89 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.57 | 4.1 | 1.1 | -0.06 | 878516.26 | 16.22 | skipped_fast |
| HBARUSDT | IDLE | 2.37 | 5.75 | 1.72 | 0.0 | 804202.23 | 10.62 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 9.75 | 7.44 | -0.04 | 61792.24 | 21.46 | skipped_fast |
| QNTUSDT | IDLE | 2.04 | 4.8 | 1.25 | -0.04 | 597586.68 | 10.62 | skipped_fast |
| EDELUSDT | IDLE | 1.86 | 4.42 | 2.47 | -0.07 | 248493.08 | 3.84 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 14.68 | 8.37 | 0.0 | 80456.58 | 57.69 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 3.11 | 0.75 | -0.04 | 234814.66 | 9.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.36 | 2.53 | 1.22 | -0.05 | 218079.31 | 24.57 | skipped_fast |
| REDUSDT | IDLE | 1.88 | 3.76 | 0.0 | -0.01 | 95595.72 | 18.25 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 3.05 | 0.3 | -0.04 | 81981.24 | 8.61 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 4.12 | 0.2 | -0.06 | 76801.22 | 9.92 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 2.45 | 0.09 | -0.01 | 65260.3 | 13.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 4.56 | 3.92 | -0.04 | 58472.23 | 61.82 | skipped_fast |
| FLUIDUSDT | IDLE | 2.1 | 3.87 | 3.58 | -0.07 | 4269.88 | 21.49 | skipped_fast |
| IOTAUSDT | IDLE | 1.54 | 3.61 | 0.57 | -0.04 | 68042.79 | 27.31 | skipped_fast |
| LAUSDT | IDLE | 1.3 | 3.4 | 0.25 | -0.05 | 58817.87 | 23.01 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.7 | 0.64 | -0.01 | 34779.49 | 25.69 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.72 | 0.32 | 0.0 | 48141.51 | 32.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
