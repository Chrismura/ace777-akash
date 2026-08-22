# Hulk DIGEST — 2026-08-22T05:29:27Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.1 | 0.08 | 16493260.65 | 13.95 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 23.87 | 10.15 | 0.17 | 199548674.08 | 5.24 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 15.8 | 8.81 | 0.06 | 1348657.7 | 22.71 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.59 | -0.09 | 690899.9 | 3.32 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.21 | 0.07 | 588158.15 | 12.46 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 11.95 | -0.03 | 218634.86 | 13.11 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 45.06 | 11.97 | 0.12 | 164589.65 | 21.59 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.85 | 0.18 | 760272.81 | 16.66 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 8.47 | 5.14 | 0.06 | 545211.95 | 48.27 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 13.91 | 9.36 | 0.04 | 195252.95 | 7.77 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.87 | 9.68 | 5.75 | 0.09 | 73285.46 | 10.18 | skipped_fast |
| EDELUSDT | IDLE | 2.13 | 4.52 | 1.3 | -0.02 | 88500.8 | 21.93 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 48.45 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 7.9 | 5.34 | 0.05 | 5400.57 | 21.79 | skipped_fast |
| RIZEUSDT | IDLE | 1.22 | 4.9 | 4.55 | 0.08 | 58739.14 | 22.39 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.07 | 5.52 | 2.62 | 0.08 | 195124.76 | 45.72 | skipped_fast |
| RWAUSDT | IDLE | 1.85 | 3.38 | 2.15 | 0.05 | 57543.91 | 24.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
