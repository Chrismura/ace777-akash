# Hulk DIGEST — 2026-08-22T05:30:37Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.87 | 0.08 | 16522661.35 | 29.82 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 23.87 | 10.63 | 0.16 | 200019897.76 | 3.95 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 9.21 | 0.06 | 1353971.73 | 20.28 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.65 | -0.09 | 690916.72 | 6.67 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.15 | 0.07 | 590482.11 | 15.56 | tvl≈1,690,573,228 |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 45.06 | 12.13 | 0.12 | 164257.05 | 0.87 | tvl≈2,314,909 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 11.89 | -0.03 | 218898.24 | 13.11 | n/a |
| CCUSDT | IDLE | 2.2 | 11.56 | 3.03 | 0.18 | 760484.64 | 10.0 | no_map |
| ZBCNUSDT | IDLE | 3.11 | 8.47 | 4.15 | 0.08 | 545583.46 | 76.38 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 13.91 | 9.36 | 0.04 | 195246.13 | 12.45 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 5.87 | 0.09 | 73285.97 | 12.04 | no_map |
| EDELUSDT | IDLE | 2.16 | 4.52 | 1.62 | -0.02 | 88479.63 | 10.97 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 7.9 | 5.34 | 0.05 | 5400.57 | 21.13 | tvl≈2,592,362,987 |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 75.47 | no_map |
| RIZEUSDT | IDLE | 1.23 | 4.9 | 4.62 | 0.08 | 58747.06 | 22.39 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3417.27 | 35.86 | no_map |
| TELUSDT | IDLE | 2.06 | 5.52 | 2.57 | 0.07 | 194942.14 | 40.65 | no_map |
| RWAUSDT | IDLE | 1.85 | 3.38 | 2.07 | 0.05 | 57516.64 | 16.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
