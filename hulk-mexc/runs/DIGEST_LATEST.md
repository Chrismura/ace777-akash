# Hulk DIGEST — 2026-09-28T01:15:07Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 101.31 | 31.37 | 0.53 | 15453910.45 | 11.71 | skipped_fast |
| PYTHUSDT | IDLE | 2.06 | 4.5 | 3.24 | 0.01 | 2122983.77 | 2.39 | skipped_fast |
| WUSDT | IDLE | 1.32 | 6.47 | 5.63 | 0.12 | 5156437.87 | 9.15 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 2.11 | 1.59 | -0.01 | 44717371.6 | 2.65 | skipped_fast |
| ETHUSDT | IDLE | 0.76 | 1.34 | 1.22 | -0.01 | 226614088.44 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.71 | 1.25 | 1.18 | -0.0 | 439932407.82 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.47 | 4.83 | 0.72 | 0.03 | 678959.12 | 10.68 | skipped_fast |
| HBARUSDT | IDLE | 2.05 | 4.01 | 0.61 | 0.04 | 851816.09 | 7.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.87 | 5.08 | 4.41 | -0.01 | 219392.27 | 26.38 | skipped_fast |
| EDELUSDT | IDLE | 1.82 | 8.75 | 5.77 | -0.14 | 150455.06 | 66.94 | skipped_fast |
| KITEUSDT | IDLE | 1.95 | 3.53 | 3.3 | -0.01 | 106177.38 | 8.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 3.87 | 3.68 | -0.07 | 98547.09 | 13.14 | skipped_fast |
| BIOUSDT | IDLE | 1.82 | 3.31 | 2.25 | -0.01 | 82639.91 | 6.31 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 2.17 | 1.87 | 0.01 | 66233.93 | 13.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.01 | 9.68 | 5.24 | -0.23 | 61790.75 | 77.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.03 | 10.64 | 1.73 | 0.24 | 30445.64 | 82.56 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 2.8 | 1.12 | 0.11 | 177005.32 | 21.6 | skipped_fast |
| FLUIDUSDT | IDLE | 1.82 | 3.39 | 1.68 | 0.04 | 3564.24 | 21.51 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.86 | 0.57 | 0.0 | 59739.06 | 14.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.66 | 0.2 | 0.01 | 39553.18 | 25.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
