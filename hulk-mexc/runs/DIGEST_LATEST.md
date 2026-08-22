# Hulk DIGEST — 2026-08-22T05:20:11Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.96 | 0.08 | 15755641.73 | 29.84 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 23.87 | 12.29 | 0.13 | 194377175.57 | 14.76 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.59 | 0.04 | 1331814.51 | 42.12 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 24.54 | 12.68 | -0.1 | 658691.88 | 16.73 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.62 | 0.06 | 572256.07 | 19.81 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.24 | -0.03 | 213790.81 | 56.02 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 45.06 | 12.44 | 0.11 | 163413.58 | 83.43 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 11.56 | 4.64 | 0.15 | 760605.91 | 12.72 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 8.47 | 6.79 | 0.04 | 543839.26 | 54.88 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 13.91 | 9.01 | 0.04 | 193218.01 | 38.77 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 9.68 | 6.34 | 0.08 | 73326.13 | 23.33 | skipped_fast |
| EDELUSDT | IDLE | 2.05 | 4.52 | 0.0 | -0.01 | 87679.34 | 21.65 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 7.9 | 5.99 | 0.04 | 5406.56 | 47.17 | skipped_fast |
| RWAINCUSDT | IDLE | 2.51 | 4.48 | 3.55 | 0.01 | 11281.01 | 96.72 | skipped_fast |
| TELUSDT | IDLE | 2.01 | 5.52 | 1.58 | 0.09 | 191923.54 | 5.01 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 4.03 | 0.09 | 58698.49 | 42.81 | skipped_fast |
| RWAUSDT | IDLE | 1.85 | 3.38 | 2.15 | 0.05 | 57547.35 | 8.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
