# Hulk DIGEST — 2026-08-22T05:27:52Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.85 | 0.08 | 16423254.16 | 15.89 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 23.87 | 10.28 | 0.16 | 198547713.92 | 4.59 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 15.8 | 8.44 | 0.05 | 1346644.13 | 20.12 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.15 | -0.1 | 687772.41 | 23.38 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.5 | 0.06 | 587769.32 | 14.55 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.64 | -0.03 | 218563.18 | 13.18 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 45.06 | 12.1 | 0.12 | 164296.13 | 13.85 | skipped_fast |
| CCUSDT | IDLE | 2.2 | 11.56 | 3.16 | 0.18 | 760910.33 | 9.19 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 8.47 | 6.25 | 0.05 | 544196.83 | 27.54 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 13.91 | 9.45 | 0.03 | 195318.65 | 9.34 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 5.97 | 0.08 | 73315.93 | 12.02 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 4.52 | 1.73 | -0.02 | 88475.72 | 21.95 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 48.45 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 7.9 | 5.34 | 0.05 | 5410.58 | 21.82 | skipped_fast |
| RIZEUSDT | IDLE | 1.23 | 4.9 | 4.67 | 0.08 | 58761.8 | 22.39 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.52 | 2.81 | 0.07 | 195489.18 | 40.59 | skipped_fast |
| RWAUSDT | IDLE | 1.86 | 3.38 | 2.23 | 0.04 | 57541.43 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
