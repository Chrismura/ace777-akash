# Hulk DIGEST — 2026-10-06T19:13:17Z

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
| QNTUSDT | IDLE | 2.6 | 4.58 | 4.09 | 0.01 | 2603270.81 | 0.39 | n/a |
| XRPUSDT | IDLE | 1.01 | 1.78 | 1.61 | 0.0 | 27433088.13 | 2.0 | n/a |
| BTCUSDT | IDLE | 0.83 | 1.45 | 1.43 | -0.0 | 549764613.11 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.79 | 1.38 | 1.36 | -0.01 | 291907804.32 | 0.04 | no_map |
| PYTHUSDT | IDLE | 2.53 | 4.5 | 3.77 | 0.01 | 603318.21 | 2.59 | tvl≈173,807,960 |
| EDELUSDT | IDLE | 2.08 | 6.87 | 2.04 | -0.03 | 409914.26 | 34.88 | no_map |
| WUSDT | IDLE | 1.69 | 3.04 | 2.29 | -0.01 | 409887.97 | 9.68 | tvl≈1,958,908,451 |
| CCUSDT | IDLE | 1.13 | 2.07 | 1.27 | 0.02 | 422919.37 | 2.34 | no_map |
| RWAINCUSDT | IDLE | 3.29 | 6.07 | 3.46 | -0.02 | 16319.91 | 67.83 | no_map |
| CHIPUSDT | IDLE | 1.96 | 4.66 | 1.28 | 0.05 | 173397.86 | 13.39 | no_map |
| RIZEUSDT | IDLE | 1.36 | 15.5 | 0.63 | 0.26 | 112074.79 | 49.74 | no_map |
| ZBCNUSDT | IDLE | 1.35 | 2.62 | 0.5 | 0.02 | 244833.69 | 23.2 | n/a |
| BIOUSDT | IDLE | 1.69 | 3.76 | 2.24 | -0.02 | 102979.57 | 6.29 | n/a |
| FLUIDUSDT | IDLE | 2.18 | 8.67 | 7.92 | -0.12 | 83380.96 | 13.58 | tvl≈2,520,243,470 |
| TELUSDT | IDLE | 2.71 | 4.82 | 4.03 | -0.03 | 124405.42 | 53.22 | no_map |
| REDUSDT | IDLE | 1.27 | 2.21 | 2.15 | -0.05 | 59097.46 | 2.47 | tvl≈4,126,837 |
| KITEUSDT | IDLE | 1.26 | 2.21 | 2.05 | 0.01 | 62672.45 | 10.66 | no_map |
| HBARUSDT | IDLE | 0.69 | 1.3 | 0.51 | -0.01 | 476818.59 | 1.99 | empty_tvl |
| RWAUSDT | IDLE | 0.59 | 1.03 | 0.94 | 0.0 | 51883.31 | 14.66 | no_map |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.13 | 0.0 | 41477.94 | 21.85 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
