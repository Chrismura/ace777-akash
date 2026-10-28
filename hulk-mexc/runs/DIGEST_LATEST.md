# Hulk DIGEST — 2026-10-28T16:41:39Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 1.07 | 1.92 | 1.5 | -0.01 | 214921789.5 | 0.13 | no_map |
| XRPUSDT | IDLE | 0.82 | 1.45 | 1.32 | -0.01 | 18663913.05 | 1.53 | n/a |
| BTCUSDT | IDLE | 0.76 | 1.34 | 1.21 | -0.0 | 281835859.86 | 0.0 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.5 | 17.04 | 14.12 | -0.1 | 191237.68 | 14.24 | no_map |
| CCUSDT | IDLE | 3.11 | 7.17 | 2.31 | 0.0 | 375811.95 | 1.0 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 9.65 | 8.56 | -0.01 | 37793.89 | 13.58 | no_map |
| PYTHUSDT | IDLE | 1.56 | 2.74 | 2.58 | -0.02 | 387908.53 | 1.41 | tvl≈158,727,627 |
| QNTUSDT | IDLE | 2.7 | 4.81 | 3.96 | -0.03 | 409367.31 | 2.58 | n/a |
| WUSDT | IDLE | 1.46 | 2.74 | 1.17 | -0.02 | 440317.17 | 17.28 | tvl≈1,497,982,251 |
| ZBCNUSDT | IDLE | 1.61 | 3.18 | 1.07 | -0.04 | 251083.07 | 36.13 | n/a |
| EDELUSDT | IDLE | 1.49 | 2.83 | 1.03 | 0.0 | 200369.56 | 12.22 | no_map |
| HBARUSDT | IDLE | 1.24 | 2.2 | 1.83 | -0.01 | 480603.39 | 10.64 | empty_tvl |
| BIOUSDT | IDLE | 1.62 | 3.02 | 1.49 | 0.0 | 83896.94 | 13.34 | n/a |
| KITEUSDT | IDLE | 1.19 | 2.15 | 1.51 | -0.03 | 59071.17 | 9.58 | no_map |
| REDUSDT | IDLE | 1.04 | 1.94 | 0.96 | -0.02 | 54094.67 | 15.87 | tvl≈3,765,901 |
| RIZEUSDT | IDLE | 0.95 | 1.79 | 0.79 | 0.03 | 37661.48 | 61.36 | no_map |
| IOTAUSDT | IDLE | 1.63 | 2.89 | 2.41 | -0.02 | 74335.09 | 21.77 | no_map |
| LAUSDT | IDLE | 1.52 | 2.68 | 2.41 | -0.04 | 57630.85 | 20.78 | no_map |
| FLUIDUSDT | IDLE | 1.15 | 3.48 | 2.59 | -0.01 | 6677.13 | 21.59 | tvl≈2,220,818,930 |
| WAXLUSDT | IDLE | 1.36 | 2.38 | 2.31 | -0.03 | 56194.0 | 64.59 | no_map |
| RWAUSDT | IDLE | 0.59 | 1.04 | 0.95 | -0.01 | 55568.9 | 40.05 | no_map |
| MNSRYUSDT | IDLE | 0.29 | 0.51 | 0.44 | 0.01 | 36006.33 | 54.03 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
