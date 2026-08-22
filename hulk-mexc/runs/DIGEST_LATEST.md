# Hulk DIGEST — 2026-08-22T05:26:26Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.64 | 0.09 | 16301542.52 | 13.88 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 23.87 | 11.81 | 0.14 | 197761226.69 | 4.01 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 15.8 | 8.61 | 0.06 | 1344530.17 | 16.39 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.38 | -0.09 | 686854.95 | 16.71 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.48 | 0.06 | 585234.24 | 13.53 | tvl≈1,690,573,228 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.27 | -0.03 | 214279.56 | 3.29 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 45.06 | 12.07 | 0.12 | 164083.94 | 23.31 | tvl≈2,314,909 |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.95 | 0.19 | 760807.09 | 27.55 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 8.47 | 6.3 | 0.05 | 544211.56 | 32.04 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 13.91 | 9.7 | 0.03 | 195320.11 | 20.32 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.87 | 9.68 | 5.8 | 0.08 | 73293.62 | 26.86 | no_map |
| EDELUSDT | IDLE | 2.16 | 4.52 | 1.62 | -0.02 | 88495.79 | 32.91 | no_map |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.02 | 11449.52 | 64.66 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 7.9 | 5.34 | 0.05 | 5410.58 | 41.5 | tvl≈2,592,362,987 |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | no_map |
| TELUSDT | IDLE | 2.1 | 5.52 | 3.21 | 0.07 | 195445.81 | 50.86 | no_map |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 3.99 | 0.09 | 58711.81 | 42.81 | no_map |
| RWAUSDT | IDLE | 1.87 | 3.38 | 2.39 | 0.04 | 57566.67 | 32.63 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
