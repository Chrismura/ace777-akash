# Hulk DIGEST — 2026-08-22T05:15:11Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.07 | 0.07 | 15114636.4 | 57.86 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 11.25 | 0.14 | 190796783.83 | 11.95 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 9.15 | 0.05 | 1323639.6 | 30.39 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.56 | -0.09 | 598050.36 | 16.65 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.66 | 0.06 | 552573.2 | 16.66 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.59 | -0.03 | 209214.5 | 55.77 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 45.06 | 12.55 | 0.11 | 162666.2 | 76.75 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 11.56 | 4.76 | 0.15 | 758096.34 | 32.29 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.97 | 7.86 | 5.34 | 0.06 | 542273.02 | 66.46 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 13.91 | 10.24 | 0.03 | 189245.91 | 79.05 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 9.68 | 6.44 | 0.08 | 72390.4 | 17.71 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.0 | 11017.47 | 5.42 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 4.18 | 1.52 | -0.02 | 86366.44 | 43.48 | skipped_fast |
| FLUIDUSDT | IDLE | 3.17 | 7.9 | 4.43 | 0.06 | 5296.55 | 57.42 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.99 | 5.52 | 1.14 | 0.09 | 189251.26 | 29.96 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 3.96 | 0.09 | 58691.0 | 44.52 | skipped_fast |
| RWAUSDT | IDLE | 1.86 | 3.38 | 2.31 | 0.05 | 57578.98 | 32.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
