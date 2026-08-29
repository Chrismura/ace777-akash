# Hulk DIGEST — 2026-08-29T01:09:17Z

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
| XRPUSDT | IDLE | 0.77 | 1.42 | 0.78 | -0.05 | 50545136.17 | 1.45 | skipped_fast |
| CHIPUSDT | IDLE | 0.99 | 6.52 | 1.1 | 0.07 | 1178606.59 | 4.73 | skipped_fast |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 33.82 | 23.55 | -0.1 | 83065.99 | 61.51 | skipped_fast |
| PYTHUSDT | IDLE | 1.59 | 3.06 | 0.86 | -0.04 | 670081.11 | 2.11 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 13.66 | 10.02 | -0.12 | 91989.43 | 58.08 | skipped_fast |
| CCUSDT | IDLE | 1.21 | 2.25 | 1.14 | -0.02 | 301733.84 | 9.03 | skipped_fast |
| ZBCNUSDT | IDLE | 1.34 | 3.36 | 2.77 | -0.09 | 171899.88 | 7.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.93 | 4.74 | 3.44 | -0.04 | 33843.4 | 55.56 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 1.68 | 1.64 | -0.05 | 473732.3 | 1.32 | skipped_fast |
| WUSDT | IDLE | 0.81 | 1.54 | 0.79 | -0.06 | 221277.86 | 13.17 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.67 | 0.72 | -0.01 | 79119.62 | 12.47 | skipped_fast |
| REDUSDT | IDLE | 1.28 | 3.12 | 1.19 | -0.03 | 63078.67 | 14.89 | skipped_fast |
| RWAINCUSDT | IDLE | 2.28 | 4.28 | 1.92 | -0.02 | 3438.94 | 98.25 | skipped_fast |
| BIOUSDT | IDLE | 0.74 | 1.38 | 0.61 | -0.06 | 85605.52 | 3.6 | skipped_fast |
| TELUSDT | IDLE | 0.79 | 1.97 | 0.34 | -0.07 | 98863.15 | 22.75 | skipped_fast |
| QNTUSDT | IDLE | 0.46 | 0.86 | 0.42 | -0.03 | 42205.11 | 6.56 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.75 | 0.08 | 0.0 | 54578.43 | 16.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 0.69 | 0.0 | -0.05 | 3932.96 | 21.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
