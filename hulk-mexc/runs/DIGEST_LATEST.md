# Hulk DIGEST — 2026-08-22T10:59:21Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 16.77 | 12.04 | -0.01 | 51654319.85 | 4.15 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 23.87 | 12.92 | 0.07 | 218202779.11 | 5.41 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.36 | -0.0 | 1248660.25 | 6.49 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.59 | -0.1 | 656211.78 | 3.37 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 16.84 | 9.51 | 0.01 | 594864.12 | 12.72 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.81 | -0.06 | 240633.71 | 3.27 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.53 | 0.12 | 817920.28 | 6.05 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 9.72 | 8.11 | -0.03 | 423571.3 | 14.9 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.84 | 37.92 | 10.21 | 0.03 | 154143.99 | 10.71 | skipped_fast |
| KITEUSDT | IDLE | 4.1 | 9.28 | 4.29 | 0.03 | 73278.44 | 11.89 | skipped_fast |
| EDELUSDT | IDLE | 3.35 | 5.96 | 4.97 | -0.04 | 78999.53 | 34.07 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 9.75 | 6.41 | -0.01 | 189120.01 | 6.24 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.59 | 9.12 | 7.62 | -0.04 | 169059.01 | 58.84 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.38 | 5.33 | -0.01 | 5711.25 | 20.88 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.01 | 2418.23 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 59.83 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.33 | -0.0 | 49227.63 | 46.66 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.23 | 0.01 | 57414.29 | 16.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
