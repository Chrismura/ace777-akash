# Hulk DIGEST — 2026-08-21T20:00:34Z

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
| PYTHUSDT | IDLE | 1.38 | 4.78 | 4.42 | 0.06 | 5451135.68 | 6.42 | skipped_fast |
| XRPUSDT | IDLE | 1.16 | 4.21 | 3.33 | 0.12 | 128945366.95 | 1.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.79 | 0.16 | 153931.11 | 21.38 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 10.86 | 8.74 | 0.07 | 481691.26 | 20.18 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 3.91 | 1.53 | 0.07 | 634745.19 | 10.26 | skipped_fast |
| HBARUSDT | IDLE | 1.62 | 3.1 | 2.95 | 0.05 | 793700.45 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.37 | 4.81 | 4.32 | 0.09 | 513863.58 | 6.24 | skipped_fast |
| WUSDT | IDLE | 2.19 | 3.92 | 3.13 | 0.05 | 364029.18 | 5.37 | skipped_fast |
| BIOUSDT | IDLE | 2.64 | 5.33 | 4.42 | -0.0 | 190090.75 | 6.43 | skipped_fast |
| EDELUSDT | IDLE | 2.44 | 4.29 | 3.9 | -0.05 | 79684.82 | 33.8 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.63 | 0.02 | 56425.72 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.44 | 0.1 | 61416.6 | 11.29 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 80.49 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2868.1 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 3.39 | 2.54 | 0.01 | 183671.83 | 32.57 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 2.65 | 2.08 | 0.04 | 59934.73 | 1.57 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.08 | 0.99 | 0.04 | 54281.98 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.14 | 0.07 | 4276.39 | 21.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
