# Hulk DIGEST — 2026-08-22T05:22:36Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 19.14 | 10.59 | 0.07 | 15948768.73 | 30.07 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 23.87 | 12.04 | 0.14 | 195257443.74 | 14.06 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.32 | 0.05 | 1332599.15 | 26.74 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.88 | -0.09 | 676692.12 | 13.38 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.93 | 0.06 | 575173.9 | 21.98 | tvl≈1,690,573,228 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.7 | -0.02 | 213950.34 | 16.52 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.14 | 0.1 | 164118.72 | 55.98 | tvl≈2,314,909 |
| CCUSDT | IDLE | 2.24 | 11.56 | 4.53 | 0.16 | 759893.79 | 13.55 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 8.47 | 6.67 | 0.04 | 544074.79 | 39.73 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 9.68 | 6.67 | 0.08 | 73345.8 | 25.25 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 13.91 | 10.48 | 0.04 | 194187.52 | 145.02 | n/a |
| RWAINCUSDT | IDLE | 2.51 | 4.48 | 3.55 | 0.02 | 11252.9 | 75.31 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 7.9 | 5.99 | 0.04 | 5406.56 | 38.89 | tvl≈2,592,362,987 |
| EDELUSDT | IDLE | 2.13 | 4.52 | 1.19 | -0.01 | 88445.77 | 76.88 | no_map |
| TELUSDT | IDLE | 2.03 | 5.52 | 1.92 | 0.08 | 192463.0 | 15.12 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | no_map |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 3.94 | 0.09 | 58709.44 | 42.81 | no_map |
| RWAUSDT | IDLE | 1.87 | 3.38 | 2.39 | 0.05 | 57558.77 | 40.77 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
