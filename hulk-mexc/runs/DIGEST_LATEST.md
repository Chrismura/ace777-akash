# Hulk DIGEST — 2026-08-22T05:37:26Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.08 | 0.09 | 16794587.22 | 7.88 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 23.87 | 9.73 | 0.17 | 202252056.76 | 12.39 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.59 | 0.05 | 1360257.8 | 35.68 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.18 | -0.1 | 706800.51 | 13.38 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.38 | 0.07 | 598487.96 | 13.38 | tvl≈1,690,573,228 |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 45.06 | 12.42 | 0.11 | 164364.43 | 22.63 | tvl≈2,314,909 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.66 | -0.03 | 219494.8 | 26.34 | n/a |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.7 | 0.19 | 761285.78 | 10.82 | no_map |
| ZBCNUSDT | IDLE | 3.15 | 8.47 | 4.81 | 0.06 | 547240.96 | 41.92 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 13.91 | 8.77 | 0.04 | 196297.46 | 24.79 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 9.68 | 5.54 | 0.08 | 73341.07 | 12.93 | no_map |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.33 | 0.06 | 58936.42 | 14.03 | no_map |
| EDELUSDT | IDLE | 2.1 | 4.52 | 0.86 | -0.01 | 88473.79 | 43.72 | no_map |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5410.56 | 21.81 | tvl≈2,592,362,987 |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 75.47 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | no_map |
| TELUSDT | IDLE | 2.07 | 5.52 | 2.62 | 0.08 | 195622.05 | 45.84 | no_map |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.05 | 57668.66 | 32.44 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
