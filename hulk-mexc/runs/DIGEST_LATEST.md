# Hulk DIGEST — 2026-08-22T05:48:38Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.13 | 0.08 | 17174111.46 | 7.88 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 23.87 | 10.13 | 0.17 | 204922607.64 | 3.93 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 9.02 | 0.06 | 1367639.0 | 13.92 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.97 | -0.09 | 710395.26 | 13.33 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.34 | 0.07 | 602995.14 | 21.6 | tvl≈1,690,573,228 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.79 | -0.04 | 244488.35 | 6.61 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.87 | 0.09 | 164904.87 | 20.3 | tvl≈2,314,909 |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.8 | 0.18 | 765850.61 | 16.66 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 8.47 | 5.9 | 0.05 | 547494.26 | 36.77 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 13.91 | 8.93 | 0.04 | 197073.89 | 7.74 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 5.88 | 0.08 | 74339.35 | 20.39 | no_map |
| EDELUSDT | IDLE | 2.15 | 4.52 | 1.51 | -0.02 | 88501.03 | 43.91 | no_map |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.28 | 0.06 | 58983.4 | 47.31 | no_map |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.65 | 0.06 | 5443.31 | 19.62 | tvl≈2,592,362,987 |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11598.76 | 75.47 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3293.96 | 7.99 | no_map |
| TELUSDT | IDLE | 2.05 | 5.52 | 2.37 | 0.07 | 195444.64 | 40.44 | no_map |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.05 | 57973.36 | 8.12 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
