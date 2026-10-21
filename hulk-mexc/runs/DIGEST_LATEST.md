# Hulk DIGEST — 2026-10-21T06:33:17Z

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
| ETHUSDT | IDLE | 0.64 | 1.14 | 0.92 | 0.02 | 183434744.54 | 0.08 | no_map |
| XRPUSDT | IDLE | 0.47 | 0.86 | 0.48 | 0.02 | 23459817.78 | 1.5 | n/a |
| BTCUSDT | IDLE | 0.39 | 0.71 | 0.5 | 0.01 | 311083309.18 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.17 | 3.64 | 2.43 | 0.1 | 968631.21 | 2.5 | tvl≈178,836,516 |
| CHIPUSDT | IDLE | 2.53 | 6.15 | 1.32 | 0.03 | 458708.19 | 17.53 | no_map |
| WUSDT | IDLE | 1.63 | 3.1 | 1.02 | 0.04 | 641726.55 | 7.38 | tvl≈1,600,129,748 |
| ZBCNUSDT | IDLE | 2.96 | 13.11 | 4.23 | 0.12 | 249546.41 | 51.89 | n/a |
| QNTUSDT | IDLE | 1.17 | 2.33 | 0.0 | 0.03 | 798892.59 | 4.49 | n/a |
| EDELUSDT | IDLE | 1.4 | 6.6 | 5.97 | 0.13 | 312586.33 | 11.66 | no_map |
| CCUSDT | IDLE | 0.85 | 1.54 | 1.1 | 0.0 | 281305.72 | 8.58 | no_map |
| RWAINCUSDT | IDLE | 1.34 | 6.7 | 1.18 | -0.05 | 76271.48 | 5.43 | no_map |
| REDUSDT | IDLE | 1.44 | 2.8 | 0.58 | 0.04 | 59764.54 | 7.61 | tvl≈3,585,431 |
| KITEUSDT | IDLE | 1.01 | 2.0 | 0.14 | 0.01 | 71257.87 | 8.9 | no_map |
| HBARUSDT | IDLE | 0.97 | 1.77 | 1.11 | -0.0 | 339502.96 | 2.4 | empty_tvl |
| BIOUSDT | IDLE | 0.63 | 1.23 | 0.2 | 0.05 | 61255.88 | 8.09 | n/a |
| LAUSDT | IDLE | 1.74 | 5.14 | 0.0 | 0.1 | 56434.58 | 19.08 | no_map |
| RIZEUSDT | IDLE | 0.47 | 2.04 | 0.2 | 0.07 | 61103.73 | 26.46 | no_map |
| WAXLUSDT | IDLE | 1.61 | 2.95 | 1.79 | -0.02 | 57382.41 | 39.56 | no_map |
| IOTAUSDT | IDLE | 1.09 | 2.09 | 0.66 | 0.01 | 76801.53 | 25.78 | no_map |
| FLUIDUSDT | IDLE | 0.44 | 1.6 | 1.53 | 0.02 | 14691.99 | 21.65 | tvl≈2,238,195,141 |
| RWAUSDT | IDLE | 0.35 | 0.63 | 0.47 | 0.0 | 52649.0 | 23.52 | no_map |
| MNSRYUSDT | IDLE | 0.17 | 0.33 | 0.07 | 0.0 | 40126.46 | 8.55 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
