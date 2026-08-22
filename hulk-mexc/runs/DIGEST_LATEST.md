# Hulk DIGEST — 2026-08-22T06:34:08Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.85 | 0.04 | 20005502.29 | 41.75 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 23.87 | 9.06 | 0.18 | 211544793.76 | 9.07 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.47 | 0.04 | 1387470.17 | 6.36 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 24.54 | 13.41 | -0.11 | 699803.78 | 10.16 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.35 | 0.05 | 615647.54 | 14.54 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 29.98 | 13.74 | -0.05 | 245785.7 | 3.35 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.68 | 0.08 | 164342.89 | 19.25 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 11.25 | 4.05 | 0.17 | 779532.87 | 10.0 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 8.47 | 6.39 | 0.02 | 545968.93 | 23.59 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.27 | 0.03 | 200330.01 | 10.86 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 9.68 | 5.19 | 0.09 | 74784.01 | 11.96 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.24 | -0.03 | 88087.7 | 22.4 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 21.38 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.01 | 11437.27 | 64.66 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.52 | 3.95 | 0.06 | 196552.04 | 61.76 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.55 | 0.09 | 59540.7 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.04 | 58145.23 | 24.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
