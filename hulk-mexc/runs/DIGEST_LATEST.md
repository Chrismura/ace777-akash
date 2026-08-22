# Hulk DIGEST — 2026-08-22T06:46:53Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 19.14 | 8.47 | 0.06 | 20322932.54 | 13.7 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 23.87 | 6.61 | 0.22 | 214209371.89 | 4.41 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 15.8 | 8.03 | 0.06 | 1389985.37 | 7.51 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.5 | -0.12 | 701703.68 | 6.72 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 17.58 | 6.94 | 0.07 | 617133.83 | 10.24 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.82 | -0.04 | 246524.73 | 3.31 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.57 | 0.06 | 162549.04 | 11.37 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 11.25 | 4.07 | 0.18 | 783910.62 | 8.33 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 8.47 | 5.02 | 0.04 | 546156.42 | 17.8 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.17 | 0.05 | 200384.84 | 7.68 | skipped_fast |
| KITEUSDT | IDLE | 2.79 | 9.68 | 3.64 | 0.1 | 74505.57 | 11.74 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.04 | 87698.07 | 44.54 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 21.86 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11421.15 | 91.72 | skipped_fast |
| TELUSDT | IDLE | 2.13 | 5.52 | 3.75 | 0.06 | 196946.28 | 25.67 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.13 | 0.09 | 59584.57 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.04 | 58026.0 | 16.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
