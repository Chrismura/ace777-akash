# Hulk DIGEST — 2026-10-20T04:09:53Z

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
| ETHUSDT | IDLE | 0.89 | 1.75 | 0.15 | -0.0 | 123156126.9 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.81 | 1.58 | 0.23 | -0.01 | 20135640.06 | 0.77 | n/a |
| BTCUSDT | IDLE | 0.6 | 1.18 | 0.14 | -0.01 | 299011012.9 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.44 | 2.75 | 0.81 | -0.02 | 1079776.35 | 5.47 | tvl≈161,674,860 |
| WUSDT | IDLE | 1.92 | 3.64 | 1.39 | 0.01 | 726117.15 | 19.1 | tvl≈1,565,988,095 |
| EDELUSDT | IDLE | 3.85 | 10.65 | 2.18 | 0.05 | 203135.07 | 20.92 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 13.3 | 10.99 | -0.07 | 66782.14 | 63.42 | no_map |
| CCUSDT | IDLE | 2.09 | 4.01 | 1.15 | 0.04 | 432212.88 | 5.63 | no_map |
| QNTUSDT | IDLE | 2.01 | 3.92 | 0.69 | 0.02 | 724554.74 | 3.55 | n/a |
| CHIPUSDT | IDLE | 2.23 | 4.4 | 0.4 | -0.0 | 75820.5 | 16.35 | no_map |
| BIOUSDT | IDLE | 1.5 | 2.94 | 0.34 | 0.01 | 66929.42 | 8.43 | n/a |
| HBARUSDT | IDLE | 1.31 | 2.56 | 0.36 | -0.01 | 395267.69 | 9.55 | empty_tvl |
| REDUSDT | IDLE | 1.53 | 3.0 | 0.45 | 0.0 | 58034.26 | 16.62 | tvl≈3,390,385 |
| ZBCNUSDT | IDLE | 1.02 | 2.03 | 0.11 | -0.01 | 154779.66 | 17.06 | n/a |
| KITEUSDT | IDLE | 1.23 | 2.62 | 0.11 | 0.07 | 77660.34 | 12.92 | no_map |
| RWAINCUSDT | IDLE | 0.87 | 1.83 | 0.92 | 0.03 | 72205.96 | 41.3 | no_map |
| IOTAUSDT | IDLE | 1.55 | 3.05 | 0.35 | 0.02 | 90364.95 | 28.42 | no_map |
| LAUSDT | IDLE | 1.48 | 2.92 | 0.28 | 0.0 | 55045.77 | 24.65 | no_map |
| WAXLUSDT | IDLE | 1.47 | 3.57 | 0.58 | -0.04 | 56247.73 | 63.16 | no_map |
| FLUIDUSDT | IDLE | 1.15 | 2.25 | 0.28 | -0.02 | 4562.18 | 21.46 | tvl≈2,220,670,961 |
| RWAUSDT | IDLE | 0.26 | 0.47 | 0.31 | -0.0 | 51917.76 | 23.54 | no_map |
| MNSRYUSDT | IDLE | 0.15 | 0.27 | 0.17 | -0.0 | 40219.59 | 22.81 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
