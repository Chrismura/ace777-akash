# Hulk DIGEST — 2026-08-22T06:04:42Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.62 | 0.07 | 18257039.07 | 11.76 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 23.87 | 9.87 | 0.17 | 207281492.37 | 5.88 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 15.8 | 8.91 | 0.05 | 1375710.87 | 17.7 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.91 | -0.09 | 699940.26 | 3.34 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.56 | 0.06 | 612512.18 | 12.35 | tvl≈1,690,573,228 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.41 | -0.04 | 246185.6 | 16.48 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.37 | 0.1 | 165709.56 | 15.7 | tvl≈2,314,909 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 8.47 | 5.63 | 0.04 | 547763.77 | 29.34 | n/a |
| CCUSDT | IDLE | 1.85 | 9.8 | 2.13 | 0.18 | 765597.7 | 10.76 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.73 | 0.04 | 198300.23 | 1.55 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.87 | 9.68 | 5.41 | 0.08 | 74394.39 | 13.86 | no_map |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.01 | 11531.83 | 64.66 | no_map |
| FLUIDUSDT | IDLE | 3.24 | 7.9 | 4.42 | 0.06 | 5356.23 | 20.38 | tvl≈2,592,362,987 |
| EDELUSDT | IDLE | 2.16 | 4.52 | 1.62 | -0.01 | 88143.56 | 66.15 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3283.04 | 7.99 | no_map |
| TELUSDT | IDLE | 2.08 | 5.52 | 2.86 | 0.07 | 195687.34 | 45.7 | no_map |
| RIZEUSDT | IDLE | 0.99 | 3.99 | 3.6 | 0.07 | 59024.76 | 47.31 | no_map |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.75 | 0.05 | 57868.84 | 8.11 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
