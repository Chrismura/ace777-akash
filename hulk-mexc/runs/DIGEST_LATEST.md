# Hulk DIGEST — 2026-08-22T05:54:51Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.35 | 0.08 | 17570677.34 | 39.46 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 23.87 | 9.83 | 0.17 | 205796967.9 | 11.79 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 15.8 | 8.96 | 0.05 | 1368578.8 | 1.26 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.0 | -0.09 | 710650.89 | 3.34 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.66 | 0.07 | 606382.64 | 13.42 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.07 | -0.03 | 246227.4 | 6.58 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 45.06 | 14.01 | 0.09 | 164951.88 | 19.48 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.87 | 0.18 | 767288.55 | 8.33 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 8.47 | 6.05 | 0.04 | 547512.5 | 14.99 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 13.91 | 8.72 | 0.04 | 197108.55 | 12.41 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 9.68 | 6.29 | 0.08 | 74096.1 | 13.96 | skipped_fast |
| EDELUSDT | IDLE | 2.15 | 4.52 | 1.51 | -0.01 | 88107.48 | 43.96 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.0 | 11600.95 | 64.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.71 | 6.91 | 6.0 | 0.06 | 58998.7 | 47.31 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.65 | 0.06 | 5383.27 | 21.85 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3293.96 | 7.99 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 5.52 | 2.52 | 0.08 | 196604.75 | 20.24 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.67 | 0.05 | 57879.14 | 32.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
