# Hulk DIGEST — 2026-08-22T05:34:11Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.16 | 0.07 | 16662394.23 | 11.96 | tvl≈112,886,663 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 10.95 | 0.15 | 201335081.21 | 3.3 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 15.8 | 10.94 | 0.03 | 1355398.7 | 37.39 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.94 | -0.1 | 698785.25 | 10.02 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.55 | 0.06 | 593685.43 | 14.59 | tvl≈1,690,573,228 |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.3 | 0.11 | 164204.39 | 9.64 | tvl≈2,314,909 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.41 | -0.03 | 219024.23 | 13.19 | n/a |
| CCUSDT | IDLE | 2.18 | 11.56 | 2.41 | 0.19 | 760257.05 | 4.98 | no_map |
| ZBCNUSDT | IDLE | 3.15 | 8.47 | 4.79 | 0.06 | 545673.24 | 80.7 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 13.91 | 9.08 | 0.04 | 195368.14 | 12.4 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 6.0 | 0.08 | 73230.6 | 12.98 | no_map |
| RIZEUSDT | IDLE | 1.73 | 6.91 | 6.46 | 0.06 | 58914.28 | 28.08 | no_map |
| EDELUSDT | IDLE | 2.15 | 4.52 | 1.51 | -0.02 | 88506.7 | 54.73 | no_map |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5410.56 | 21.07 | tvl≈2,592,362,987 |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.01 | 11525.01 | 75.47 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | no_map |
| TELUSDT | IDLE | 2.09 | 5.52 | 3.06 | 0.07 | 195749.63 | 40.8 | no_map |
| RWAUSDT | IDLE | 1.86 | 3.38 | 2.31 | 0.05 | 57513.37 | 16.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
