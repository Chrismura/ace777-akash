# Hulk DIGEST — 2026-08-22T05:45:08Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.89 | 0.07 | 16991546.27 | 13.91 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 11.07 | 0.16 | 203946570.35 | 3.31 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.98 | 0.04 | 1366440.2 | 24.28 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 24.54 | 12.97 | -0.1 | 709820.5 | 16.84 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.75 | 0.05 | 601516.08 | 12.53 | tvl≈1,690,573,228 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 29.98 | 13.83 | -0.05 | 245291.23 | 10.05 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 45.06 | 14.47 | 0.09 | 164671.23 | 14.2 | tvl≈2,314,909 |
| CCUSDT | IDLE | 2.22 | 11.56 | 4.05 | 0.17 | 763720.18 | 8.44 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 8.47 | 6.16 | 0.04 | 547355.73 | 33.0 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 13.91 | 9.52 | 0.03 | 196997.43 | 10.91 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 9.68 | 6.74 | 0.07 | 74503.16 | 10.27 | no_map |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.23 | 0.06 | 58953.12 | 47.31 | no_map |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.0 | 11498.71 | 70.06 | no_map |
| EDELUSDT | IDLE | 2.13 | 4.52 | 1.19 | -0.02 | 88573.42 | 76.71 | no_map |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5400.55 | 45.3 | tvl≈2,592,362,987 |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | no_map |
| TELUSDT | IDLE | 2.09 | 5.52 | 2.96 | 0.08 | 195058.13 | 45.77 | no_map |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.75 | 0.05 | 57952.55 | 32.52 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
