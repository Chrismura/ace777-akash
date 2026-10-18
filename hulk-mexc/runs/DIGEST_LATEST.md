# Hulk DIGEST — 2026-10-18T14:03:18Z

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
| PYTHUSDT | IDLE | 2.35 | 7.03 | 6.47 | -0.12 | 1487407.33 | 5.35 | skipped_fast |
| XRPUSDT | IDLE | 1.2 | 2.12 | 1.92 | -0.01 | 21045470.14 | 2.35 | skipped_fast |
| ETHUSDT | IDLE | 1.06 | 1.89 | 1.51 | -0.01 | 89831681.24 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.66 | 1.17 | 1.03 | -0.0 | 209778477.84 | 0.09 | skipped_fast |
| WUSDT | IDLE | 2.13 | 4.41 | 4.15 | -0.07 | 970665.21 | 16.1 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 4.51 | 16.61 | 14.04 | -0.01 | 72536.04 | 45.85 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 6.37 | 5.0 | 0.02 | 21101.36 | 5.2 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.54 | 2.8 | 0.05 | 593545.73 | 3.44 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 3.29 | 3.1 | -0.04 | 495414.71 | 4.14 | skipped_fast |
| RIZEUSDT | IDLE | 2.81 | 5.3 | 2.15 | 0.03 | 47590.89 | 57.65 | skipped_fast |
| CHIPUSDT | IDLE | 2.11 | 4.01 | 3.86 | -0.08 | 69685.68 | 9.72 | skipped_fast |
| EDELUSDT | IDLE | 1.25 | 3.33 | 1.19 | -0.07 | 228075.6 | 15.01 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 3.23 | 3.13 | -0.03 | 77658.22 | 16.16 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 1.73 | 1.57 | -0.04 | 252269.38 | 9.0 | skipped_fast |
| BIOUSDT | IDLE | 1.59 | 2.78 | 2.7 | -0.04 | 82373.71 | 8.56 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 2.38 | 2.33 | -0.05 | 68029.52 | 13.27 | skipped_fast |
| ZBCNUSDT | IDLE | 0.63 | 1.15 | 0.71 | -0.02 | 176372.93 | 15.77 | skipped_fast |
| LAUSDT | IDLE | 2.15 | 3.76 | 3.62 | -0.07 | 54663.42 | 20.97 | skipped_fast |
| IOTAUSDT | IDLE | 2.19 | 3.82 | 3.68 | -0.05 | 68707.03 | 33.9 | skipped_fast |
| FLUIDUSDT | IDLE | 1.97 | 3.44 | 3.33 | -0.02 | 2526.38 | 33.25 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.69 | 0.09 | -0.0 | 34342.79 | 12.78 | skipped_fast |
| RWAUSDT | IDLE | 0.25 | 0.48 | 0.16 | 0.0 | 50324.73 | 15.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
