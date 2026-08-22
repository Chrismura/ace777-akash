# Hulk DIGEST — 2026-08-22T05:36:43Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.9 | 0.08 | 16749773.26 | 53.18 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 23.87 | 9.76 | 0.17 | 202148696.22 | 13.03 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.68 | 0.05 | 1360117.46 | 12.74 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.76 | -0.1 | 706789.72 | 16.72 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.35 | 0.07 | 598410.62 | 21.61 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 45.06 | 12.57 | 0.11 | 164341.96 | 12.99 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.66 | -0.03 | 219367.04 | 19.66 | skipped_fast |
| CCUSDT | IDLE | 2.18 | 11.56 | 2.49 | 0.19 | 761285.78 | 10.8 | skipped_fast |
| ZBCNUSDT | IDLE | 3.15 | 8.47 | 4.8 | 0.06 | 547224.71 | 40.38 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 13.91 | 8.72 | 0.04 | 196297.46 | 10.79 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 9.68 | 5.54 | 0.08 | 73336.96 | 20.26 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 4.52 | 1.41 | -0.02 | 88448.75 | 21.88 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.33 | 0.06 | 58925.66 | 14.03 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 70.06 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5410.56 | 21.73 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.07 | 5.52 | 2.62 | 0.08 | 195622.05 | 45.77 | skipped_fast |
| RWAUSDT | IDLE | 1.86 | 3.38 | 2.23 | 0.05 | 57579.77 | 24.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
