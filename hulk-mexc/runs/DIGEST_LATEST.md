# Hulk DIGEST — 2026-08-22T05:41:27Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.51 | 0.08 | 16905283.12 | 3.96 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 10.95 | 0.16 | 203159043.61 | 3.97 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.74 | 0.05 | 1361149.13 | 19.13 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.5 | -0.1 | 708883.09 | 13.47 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.03 | 0.06 | 600237.98 | 10.36 | tvl≈1,690,573,228 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 13.14 | -0.04 | 232168.4 | 9.97 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.65 | 0.1 | 164347.18 | 20.3 | tvl≈2,314,909 |
| CCUSDT | IDLE | 2.22 | 11.56 | 4.06 | 0.17 | 762915.14 | 6.75 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 8.47 | 5.75 | 0.05 | 547279.34 | 33.44 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 13.91 | 9.25 | 0.04 | 197008.41 | 7.77 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 9.68 | 6.07 | 0.08 | 73332.79 | 11.16 | no_map |
| EDELUSDT | IDLE | 2.13 | 4.52 | 1.19 | -0.02 | 88491.95 | 21.86 | no_map |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.36 | 0.06 | 58946.96 | 28.08 | no_map |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.0 | 11498.71 | 75.47 | no_map |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5410.56 | 40.03 | tvl≈2,592,362,987 |
| TELUSDT | IDLE | 2.1 | 5.52 | 3.31 | 0.07 | 195424.9 | 35.74 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | no_map |
| RWAUSDT | IDLE | 1.85 | 3.38 | 2.07 | 0.05 | 57965.19 | 40.63 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
