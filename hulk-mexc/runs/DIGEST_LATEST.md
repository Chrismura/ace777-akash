# Hulk DIGEST — 2026-08-22T06:49:36Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.88 | 0.05 | 20438506.25 | 11.79 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 23.87 | 7.24 | 0.21 | 214394613.88 | 3.81 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 15.8 | 8.28 | 0.06 | 1392304.45 | 1.25 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.21 | -0.12 | 701799.97 | 3.36 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.17 | 0.07 | 617491.41 | 15.39 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 12.93 | -0.04 | 246545.57 | 3.32 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.58 | 0.05 | 161554.12 | 11.37 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 11.25 | 3.99 | 0.18 | 784596.9 | 7.49 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 8.47 | 5.15 | 0.04 | 546299.26 | 29.71 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.29 | 0.04 | 200309.86 | 4.61 | skipped_fast |
| KITEUSDT | IDLE | 2.79 | 9.68 | 3.47 | 0.11 | 74382.35 | 9.02 | skipped_fast |
| EDELUSDT | IDLE | 2.26 | 4.52 | 3.14 | -0.04 | 87674.12 | 33.43 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 20.41 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11421.15 | 91.72 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.52 | 3.95 | 0.06 | 196846.88 | 15.41 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.13 | 0.09 | 59592.81 | 27.31 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.75 | 0.04 | 57947.57 | 8.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
