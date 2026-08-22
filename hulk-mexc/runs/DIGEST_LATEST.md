# Hulk DIGEST — 2026-08-22T06:02:04Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.11 | 19.14 | 8.17 | 0.08 | 18055766.37 | 29.24 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 23.87 | 9.86 | 0.18 | 207007736.26 | 6.53 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 15.8 | 8.9 | 0.06 | 1370656.29 | 11.38 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.03 | -0.09 | 700417.42 | 13.37 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.48 | 0.06 | 610495.99 | 12.37 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.76 | -0.03 | 245227.45 | 3.31 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.2 | 0.1 | 165843.97 | 19.22 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 8.47 | 5.52 | 0.04 | 547562.77 | 39.36 | skipped_fast |
| CCUSDT | IDLE | 1.85 | 9.8 | 2.0 | 0.18 | 763843.65 | 10.74 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.73 | 0.04 | 197963.86 | 1.55 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 5.67 | 0.08 | 74307.63 | 8.32 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.01 | 11565.56 | 64.66 | skipped_fast |
| EDELUSDT | IDLE | 2.17 | 4.52 | 1.84 | -0.01 | 88167.53 | 66.15 | skipped_fast |
| FLUIDUSDT | IDLE | 3.24 | 7.9 | 4.42 | 0.06 | 5376.25 | 26.92 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3283.04 | 7.99 | skipped_fast |
| TELUSDT | IDLE | 2.07 | 5.52 | 2.67 | 0.07 | 195804.85 | 35.49 | skipped_fast |
| RIZEUSDT | IDLE | 1.0 | 3.99 | 3.65 | 0.06 | 59018.8 | 47.31 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.67 | 0.05 | 57867.37 | 24.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
