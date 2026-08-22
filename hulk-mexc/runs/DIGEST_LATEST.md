# Hulk DIGEST — 2026-08-22T07:59:11Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 19.14 | 8.51 | 0.01 | 24416233.41 | 17.62 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.41 | 23.87 | 7.93 | 0.19 | 224122678.8 | 3.84 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.6 | 0.04 | 1349879.07 | 6.37 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.82 | -0.09 | 686800.1 | 6.68 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.26 | 0.04 | 616170.3 | 14.54 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.61 | -0.04 | 247474.31 | 3.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.46 | 0.06 | 158783.04 | 9.64 | skipped_fast |
| CCUSDT | IDLE | 2.03 | 11.25 | 2.6 | 0.2 | 811452.97 | 5.74 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.1 | 0.03 | 537850.6 | 17.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.67 | 0.04 | 194448.92 | 4.63 | skipped_fast |
| KITEUSDT | IDLE | 3.44 | 9.68 | 3.88 | 0.08 | 74123.2 | 12.7 | skipped_fast |
| EDELUSDT | IDLE | 2.23 | 4.52 | 2.7 | -0.04 | 87091.28 | 55.46 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.91 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11276.39 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 5.36 | 4.15 | -0.01 | 175208.45 | 36.05 | skipped_fast |
| QAITUSDT | IDLE | 1.69 | 3.32 | 0.35 | 0.01 | 3170.95 | 67.05 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 0.98 | 0.01 | 52392.99 | 41.01 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 1.04 | 0.05 | 58422.77 | 16.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
