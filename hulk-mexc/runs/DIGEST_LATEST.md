# Hulk DIGEST — 2026-08-22T08:49:37Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.55 | 0.04 | 33418954.76 | 1.98 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 23.87 | 10.76 | 0.1 | 224282391.14 | 3.3 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 15.8 | 9.93 | 0.02 | 1321428.63 | 3.84 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.41 | -0.1 | 680532.15 | 6.71 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.81 | 0.02 | 602439.22 | 1.05 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 29.98 | 8.83 | -0.04 | 254070.09 | 3.17 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.47 | 0.04 | 155561.61 | 12.42 | skipped_fast |
| CCUSDT | IDLE | 2.08 | 11.25 | 3.36 | 0.16 | 803092.78 | 7.44 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 8.47 | 7.04 | -0.01 | 505100.7 | 24.25 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.08 | 0.01 | 192808.26 | 6.21 | skipped_fast |
| KITEUSDT | IDLE | 3.77 | 9.68 | 3.33 | 0.06 | 73716.4 | 9.92 | skipped_fast |
| FLUIDUSDT | IDLE | 3.79 | 7.38 | 4.56 | 0.03 | 6885.76 | 22.17 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 1.99 | 0.02 | 11077.79 | 5.33 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 4.52 | 3.89 | -0.04 | 86722.88 | 67.42 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 6.46 | 5.97 | -0.02 | 174620.77 | 52.52 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.88 | 3.73 | 1.74 | 0.01 | 52231.32 | 46.44 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.27 | 0.04 | 58266.69 | 8.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
