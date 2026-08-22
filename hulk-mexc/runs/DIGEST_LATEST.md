# Hulk DIGEST — 2026-08-22T10:26:11Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 16.77 | 12.54 | -0.01 | 51633634.76 | 8.36 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.94 | 23.87 | 15.54 | 0.04 | 216758944.1 | 5.58 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.47 | 15.8 | 12.42 | 0.0 | 1251337.79 | 6.57 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.05 | 22.93 | 12.87 | -0.12 | 664957.79 | 6.84 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 16.84 | 11.26 | -0.01 | 598934.52 | 12.98 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 13.11 | -0.06 | 237926.18 | 6.63 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.52 | 0.11 | 816122.3 | 6.11 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 37.92 | 12.28 | 0.02 | 155409.92 | 14.57 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 9.65 | 8.71 | -0.03 | 428478.98 | 56.86 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 9.28 | 6.06 | 0.02 | 73163.98 | 12.11 | skipped_fast |
| EDELUSDT | IDLE | 2.72 | 4.76 | 4.54 | -0.03 | 78848.08 | 11.33 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 9.75 | 7.51 | -0.01 | 189346.21 | 14.24 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 8.77 | 8.06 | -0.05 | 168547.72 | 43.01 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5825.49 | 14.29 | skipped_fast |
| QAITUSDT | IDLE | 1.6 | 2.91 | 1.98 | -0.01 | 3205.44 | 63.29 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.41 | 0.0 | 49249.74 | 46.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11368.82 | 75.88 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.23 | 0.01 | 57559.54 | 24.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
