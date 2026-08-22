# Hulk DIGEST — 2026-08-22T06:37:16Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.35 | 0.06 | 20086015.75 | 1.98 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 23.87 | 8.51 | 0.19 | 211834641.98 | 1.93 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 9.11 | 0.04 | 1387563.46 | 8.87 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.44 | -0.11 | 703096.61 | 6.72 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.14 | 0.06 | 616426.48 | 15.55 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 13.02 | -0.04 | 245889.82 | 3.32 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 42.58 | 12.39 | 0.06 | 164365.49 | 19.42 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 11.25 | 4.23 | 0.17 | 780745.37 | 10.01 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 8.47 | 6.39 | 0.02 | 546122.61 | 29.07 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.91 | 0.04 | 200303.86 | 20.11 | skipped_fast |
| KITEUSDT | IDLE | 2.83 | 9.68 | 4.62 | 0.09 | 74754.69 | 14.62 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 19.09 | skipped_fast |
| EDELUSDT | IDLE | 2.23 | 4.52 | 2.7 | -0.02 | 88112.78 | 44.54 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.01 | 11437.27 | 64.66 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.52 | 4.15 | 0.06 | 196472.26 | 51.47 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.59 | 0.09 | 59545.3 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.91 | 0.04 | 58192.62 | 24.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
