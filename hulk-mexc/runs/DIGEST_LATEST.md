# Hulk DIGEST — 2026-10-20T05:10:11Z

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
| ETHUSDT | IDLE | 0.93 | 1.8 | 0.36 | -0.01 | 122589026.75 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.85 | 1.66 | 0.28 | -0.01 | 20015102.31 | 0.77 | n/a |
| BTCUSDT | IDLE | 0.66 | 1.28 | 0.3 | -0.01 | 299669028.62 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.72 | 3.21 | 1.51 | -0.02 | 1087491.89 | 5.49 | tvl≈161,674,860 |
| WUSDT | IDLE | 2.13 | 3.98 | 1.81 | 0.01 | 728673.77 | 16.07 | tvl≈1,565,988,095 |
| EDELUSDT | IDLE | 3.86 | 10.65 | 2.29 | 0.04 | 200232.55 | 24.49 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 13.3 | 10.53 | -0.07 | 66714.35 | 65.54 | no_map |
| QNTUSDT | IDLE | 2.15 | 3.97 | 2.21 | -0.0 | 723964.04 | 0.51 | n/a |
| CCUSDT | IDLE | 2.12 | 4.01 | 1.58 | 0.03 | 431317.2 | 9.43 | no_map |
| CHIPUSDT | IDLE | 3.16 | 6.88 | 0.34 | 0.03 | 87698.31 | 13.68 | no_map |
| KITEUSDT | IDLE | 1.59 | 3.41 | 1.43 | 0.06 | 78805.89 | 12.96 | no_map |
| BIOUSDT | IDLE | 1.58 | 3.03 | 0.84 | -0.0 | 67878.01 | 8.47 | n/a |
| ZBCNUSDT | IDLE | 1.17 | 2.14 | 1.37 | -0.01 | 154983.14 | 13.42 | n/a |
| HBARUSDT | IDLE | 1.37 | 2.62 | 0.78 | -0.01 | 382576.45 | 6.0 | empty_tvl |
| REDUSDT | IDLE | 1.52 | 2.93 | 0.74 | 0.01 | 57929.08 | 15.23 | tvl≈3,390,385 |
| RWAINCUSDT | IDLE | 0.84 | 1.83 | 0.46 | 0.03 | 75514.77 | 5.16 | no_map |
| FLUIDUSDT | IDLE | 2.26 | 4.4 | 0.8 | -0.01 | 7604.75 | 21.24 | tvl≈2,220,670,961 |
| IOTAUSDT | IDLE | 1.79 | 3.5 | 0.52 | 0.02 | 89730.9 | 32.71 | no_map |
| LAUSDT | IDLE | 1.69 | 3.32 | 0.34 | -0.01 | 54649.82 | 26.39 | no_map |
| WAXLUSDT | IDLE | 1.51 | 3.59 | 1.1 | -0.05 | 56556.63 | 63.61 | no_map |
| RWAUSDT | IDLE | 0.27 | 0.47 | 0.47 | -0.0 | 51808.2 | 23.54 | no_map |
| MNSRYUSDT | IDLE | 0.14 | 0.27 | 0.09 | -0.0 | 40013.39 | 18.53 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
