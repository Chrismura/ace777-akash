# Hulk DIGEST — 2026-08-22T05:12:35Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 19.09 | 15.05 | 0.02 | 14743924.45 | 54.97 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 23.87 | 16.12 | 0.08 | 188353055.22 | 30.14 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 15.55 | 12.89 | 0.02 | 1209223.07 | 47.44 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 24.54 | 17.85 | -0.16 | 564545.21 | 31.94 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 17.58 | 13.31 | -0.0 | 518877.02 | 46.2 | skipped_fast |
| CCUSDT | IDLE | 2.36 | 11.56 | 8.92 | 0.12 | 755307.09 | 13.31 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.94 | 7.59 | 6.59 | 0.04 | 541447.46 | 68.11 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 45.06 | 24.94 | -0.11 | 161182.29 | 639.57 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 29.98 | 21.16 | -0.14 | 206623.58 | 538.9 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.99 | 9.66 | 8.81 | 0.05 | 72315.45 | 115.05 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 13.91 | 10.66 | 0.03 | 188534.75 | 256.89 | skipped_fast |
| RWAINCUSDT | IDLE | 2.36 | 4.48 | 1.62 | 0.02 | 10400.07 | 21.38 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 7.9 | 6.63 | 0.03 | 4883.36 | 64.34 | skipped_fast |
| TELUSDT | IDLE | 2.01 | 5.52 | 1.43 | 0.09 | 188470.67 | 15.01 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 4.03 | 0.09 | 58684.41 | 23.95 | skipped_fast |
| EDELUSDT | IDLE | 1.55 | 3.28 | 0.98 | -0.02 | 83813.31 | 98.96 | skipped_fast |
| RWAUSDT | IDLE | 1.78 | 3.38 | 1.2 | 0.06 | 57098.77 | 32.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
