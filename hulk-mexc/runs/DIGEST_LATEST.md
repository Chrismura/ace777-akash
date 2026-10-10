# Hulk DIGEST — 2026-10-10T13:57:12Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 3.79 | 7.31 | 1.75 | -0.01 | 1052626.7 | 13.68 | tvl≈1,631,808,985 |
| XRPUSDT | IDLE | 0.35 | 0.65 | 0.4 | 0.02 | 17606597.04 | 0.71 | n/a |
| ETHUSDT | IDLE | 0.13 | 0.26 | 0.02 | 0.0 | 85709816.03 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.11 | 0.2 | 0.12 | 0.0 | 201738912.54 | 0.0 | no_map |
| PYTHUSDT | IDLE | 0.88 | 2.45 | 1.61 | -0.09 | 1084338.27 | 1.27 | tvl≈177,215,533 |
| QNTUSDT | IDLE | 1.75 | 3.31 | 1.28 | 0.01 | 1184374.12 | 8.34 | n/a |
| EDELUSDT | IDLE | 3.59 | 7.46 | 4.15 | 0.02 | 231733.86 | 25.75 | no_map |
| KITEUSDT | IDLE | 2.53 | 6.59 | 1.65 | 0.05 | 74933.11 | 11.62 | no_map |
| CCUSDT | IDLE | 1.09 | 1.96 | 1.42 | -0.03 | 393845.13 | 0.83 | no_map |
| ZBCNUSDT | IDLE | 0.59 | 1.08 | 0.7 | -0.01 | 224186.38 | 14.04 | n/a |
| REDUSDT | IDLE | 1.16 | 2.19 | 0.85 | 0.03 | 55043.63 | 14.62 | tvl≈3,785,310 |
| CHIPUSDT | IDLE | 0.85 | 2.58 | 1.67 | 0.08 | 87752.36 | 15.27 | no_map |
| BIOUSDT | IDLE | 0.91 | 1.76 | 0.45 | 0.03 | 78824.85 | 6.94 | n/a |
| RIZEUSDT | IDLE | 0.49 | 1.56 | 1.04 | 0.04 | 50194.15 | 7.95 | no_map |
| HBARUSDT | IDLE | 0.58 | 1.14 | 0.14 | 0.02 | 335026.94 | 4.3 | empty_tvl |
| RWAINCUSDT | IDLE | 0.97 | 1.88 | 0.39 | -0.02 | 9630.91 | 53.62 | no_map |
| TELUSDT | IDLE | 1.6 | 2.82 | 2.58 | -0.02 | 109246.31 | 38.62 | no_map |
| RWAUSDT | IDLE | 0.35 | 0.63 | 0.47 | -0.01 | 53640.66 | 15.74 | no_map |
| MNSRYUSDT | IDLE | 0.35 | 0.67 | 0.2 | 0.0 | 39409.95 | 17.59 | no_map |
| FLUIDUSDT | IDLE | 0.38 | 1.2 | 0.1 | 0.02 | 9778.7 | 19.71 | tvl≈2,426,076,238 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
