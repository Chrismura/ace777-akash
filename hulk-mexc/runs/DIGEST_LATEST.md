# Hulk DIGEST — 2026-10-19T01:08:48Z

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
| XRPUSDT | IDLE | 2.13 | 4.24 | 0.13 | 0.01 | 29156553.8 | 1.53 | n/a |
| ETHUSDT | IDLE | 1.81 | 3.61 | 0.02 | 0.0 | 126686593.01 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.14 | 2.25 | 0.17 | 0.01 | 263607726.81 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.97 | 5.87 | 0.21 | -0.05 | 1303820.64 | 1.33 | tvl≈165,504,889 |
| WUSDT | IDLE | 1.78 | 4.62 | 0.02 | -0.05 | 817155.37 | 14.45 | tvl≈1,560,825,277 |
| CCUSDT | IDLE | 3.29 | 6.48 | 0.71 | -0.01 | 290151.13 | 2.93 | no_map |
| HBARUSDT | IDLE | 2.01 | 4.85 | 1.49 | -0.02 | 785900.62 | 5.91 | empty_tvl |
| ZBCNUSDT | IDLE | 3.01 | 6.46 | 0.07 | -0.02 | 261722.97 | 14.41 | n/a |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.34 | 9.75 | 6.55 | -0.01 | 62938.34 | 5.31 | no_map |
| QNTUSDT | IDLE | 2.6 | 6.22 | 0.99 | -0.03 | 593650.99 | 2.08 | n/a |
| EDELUSDT | IDLE | 2.19 | 5.12 | 0.97 | 0.01 | 251141.01 | 26.26 | no_map |
| REDUSDT | IDLE | 2.67 | 5.33 | 0.09 | -0.01 | 95471.31 | 9.37 | tvl≈3,435,095 |
| BIOUSDT | IDLE | 2.44 | 4.87 | 0.04 | -0.03 | 81253.49 | 8.44 | n/a |
| CHIPUSDT | IDLE | 2.25 | 7.23 | 0.0 | -0.04 | 79067.13 | 9.58 | no_map |
| KITEUSDT | IDLE | 2.14 | 4.25 | 0.2 | -0.01 | 66686.3 | 11.27 | no_map |
| IOTAUSDT | IDLE | 2.64 | 5.81 | 0.0 | -0.03 | 68201.28 | 28.8 | no_map |
| LAUSDT | IDLE | 2.21 | 5.38 | 0.36 | -0.05 | 58923.23 | 26.39 | no_map |
| RIZEUSDT | IDLE | 0.63 | 3.1 | 2.88 | -0.05 | 58957.15 | 50.76 | no_map |
| RWAUSDT | IDLE | 1.4 | 2.65 | 1.02 | 0.01 | 50386.23 | 7.91 | no_map |
| WAXLUSDT | IDLE | 1.07 | 5.04 | 1.3 | 0.02 | 79846.87 | 29.21 | no_map |
| FLUIDUSDT | IDLE | 1.31 | 2.75 | 0.0 | -0.04 | 4309.77 | 21.0 | tvl≈2,211,693,424 |
| MNSRYUSDT | IDLE | 0.56 | 1.05 | 0.41 | -0.0 | 35486.44 | 55.58 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
