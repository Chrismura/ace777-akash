# Hulk DIGEST — 2026-08-22T05:56:01Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.7 | 0.08 | 17632701.58 | 27.47 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 23.87 | 10.16 | 0.16 | 206127620.52 | 6.55 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 9.22 | 0.05 | 1368463.29 | 8.87 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.91 | -0.09 | 710203.96 | 3.34 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.63 | 0.07 | 607373.8 | 15.47 | tvl≈1,690,573,228 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.21 | -0.03 | 246607.16 | 9.84 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 45.06 | 14.04 | 0.09 | 164978.42 | 19.38 | tvl≈2,314,909 |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.88 | 0.18 | 767379.56 | 10.0 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 8.47 | 6.19 | 0.04 | 547538.16 | 20.52 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 13.91 | 8.87 | 0.04 | 197116.3 | 6.19 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 5.99 | 0.07 | 74120.58 | 12.07 | no_map |
| EDELUSDT | IDLE | 2.11 | 4.52 | 0.97 | -0.01 | 88102.44 | 32.88 | no_map |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.01 | 11600.95 | 64.66 | no_map |
| RIZEUSDT | IDLE | 1.71 | 6.91 | 6.05 | 0.06 | 59003.9 | 47.31 | no_map |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.65 | 0.06 | 5383.27 | 21.08 | tvl≈2,592,362,987 |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3293.96 | 7.99 | no_map |
| TELUSDT | IDLE | 2.06 | 5.52 | 2.47 | 0.07 | 196300.11 | 35.45 | no_map |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.75 | 0.05 | 57888.13 | 40.57 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
