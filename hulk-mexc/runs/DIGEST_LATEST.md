# Hulk DIGEST — 2026-08-25T21:44:32Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 8.61 | 6.54 | 0.01 | 2233297.62 | 36.01 | skipped_fast |
| XRPUSDT | IDLE | 2.32 | 5.46 | 3.09 | -0.03 | 75364327.39 | 0.7 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 4.28 | 3.72 | -0.04 | 511178.5 | 4.24 | skipped_fast |
| HBARUSDT | IDLE | 2.09 | 4.2 | 3.03 | -0.03 | 787198.88 | 2.56 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 4.92 | 2.75 | -0.01 | 489258.16 | 9.53 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.72 | 5.69 | 0.0 | 79711.89 | 28.7 | skipped_fast |
| WUSDT | IDLE | 2.28 | 4.36 | 2.54 | -0.03 | 356944.33 | 12.85 | skipped_fast |
| BIOUSDT | IDLE | 3.16 | 5.87 | 3.04 | -0.01 | 114782.12 | 13.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.96 | 5.37 | 4.79 | 0.01 | 199154.54 | 42.42 | skipped_fast |
| KITEUSDT | IDLE | 3.15 | 5.69 | 4.92 | -0.04 | 61907.22 | 11.83 | skipped_fast |
| RIZEUSDT | IDLE | 3.5 | 7.26 | 3.37 | 0.04 | 50025.31 | 47.09 | skipped_fast |
| EDELUSDT | IDLE | 1.01 | 14.25 | 12.24 | -0.01 | 166911.41 | 51.59 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 5.57 | 5.27 | -0.04 | 2047.56 | 21.54 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 4.3 | 1.69 | 0.0 | 12471.82 | 30.57 | skipped_fast |
| QNTUSDT | IDLE | 2.12 | 3.8 | 2.95 | -0.02 | 95312.01 | 1.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 2.0 | 1.67 | -0.01 | 2584.24 | 49.8 | skipped_fast |
| RWAUSDT | IDLE | 1.5 | 2.63 | 2.49 | -0.03 | 56122.41 | 24.64 | skipped_fast |
| TELUSDT | IDLE | 1.54 | 2.74 | 2.29 | -0.05 | 100750.03 | 61.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
