# Hulk DIGEST — 2026-10-26T19:28:20Z

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
| ETHUSDT | IDLE | 1.09 | 2.02 | 1.04 | -0.01 | 143273579.04 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.97 | 1.83 | 0.72 | -0.0 | 24404700.48 | 0.77 | n/a |
| BTCUSDT | IDLE | 0.84 | 1.53 | 0.95 | -0.01 | 352198177.03 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.89 | 7.97 | 6.31 | 0.06 | 1433548.51 | 4.89 | n/a |
| PYTHUSDT | IDLE | 2.34 | 4.16 | 3.52 | -0.0 | 915473.59 | 4.04 | tvl≈168,440,096 |
| WUSDT | IDLE | 3.06 | 6.36 | 1.04 | 0.03 | 648158.36 | 27.23 | tvl≈1,535,262,210 |
| CHIPUSDT | IDLE | 2.3 | 18.66 | 4.83 | 0.2 | 310995.55 | 16.6 | no_map |
| RWAINCUSDT | IDLE | 3.12 | 13.37 | 3.74 | -0.08 | 58699.23 | 11.96 | no_map |
| EDELUSDT | IDLE | 2.5 | 4.44 | 3.7 | 0.02 | 92813.39 | 15.6 | no_map |
| RIZEUSDT | IDLE | 2.32 | 4.4 | 1.57 | 0.0 | 45580.07 | 13.9 | no_map |
| ZBCNUSDT | IDLE | 1.41 | 2.78 | 2.25 | -0.06 | 200737.06 | 19.45 | n/a |
| CCUSDT | IDLE | 1.2 | 2.11 | 1.91 | -0.03 | 202922.1 | 8.03 | no_map |
| BIOUSDT | IDLE | 1.75 | 3.18 | 2.07 | -0.01 | 59485.5 | 4.5 | n/a |
| REDUSDT | IDLE | 1.61 | 2.9 | 2.1 | 0.01 | 63160.35 | 7.53 | tvl≈3,670,321 |
| KITEUSDT | IDLE | 1.14 | 2.22 | 0.36 | 0.02 | 54045.5 | 13.08 | no_map |
| HBARUSDT | IDLE | 1.14 | 2.07 | 1.37 | -0.01 | 250058.12 | 14.29 | empty_tvl |
| WAXLUSDT | IDLE | 2.23 | 4.01 | 2.94 | -0.02 | 53414.46 | 60.64 | no_map |
| LAUSDT | IDLE | 1.7 | 3.41 | 2.03 | 0.01 | 64359.34 | 24.03 | no_map |
| IOTAUSDT | IDLE | 1.55 | 2.83 | 1.78 | -0.02 | 84112.65 | 23.56 | no_map |
| FLUIDUSDT | IDLE | 1.32 | 2.35 | 2.0 | -0.06 | 712.75 | 21.32 | tvl≈2,186,313,222 |
| RWAUSDT | IDLE | 0.7 | 1.28 | 0.79 | -0.0 | 53917.95 | 23.89 | no_map |
| MNSRYUSDT | IDLE | 0.37 | 0.74 | 0.03 | -0.01 | 42125.6 | 76.46 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
