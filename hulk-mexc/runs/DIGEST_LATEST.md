# Hulk DIGEST — 2026-09-14T22:42:56Z

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
| XRPUSDT | IDLE | 1.99 | 5.29 | 3.41 | 0.07 | 73318751.09 | 1.39 | n/a |
| ETHUSDT | IDLE | 2.01 | 3.59 | 2.91 | 0.02 | 442721280.25 | 0.28 | no_map |
| BTCUSDT | IDLE | 0.78 | 1.39 | 1.19 | 0.02 | 568923393.6 | 0.0 | no_map |
| EDELUSDT | IDLE | 2.81 | 26.84 | 4.27 | 0.29 | 322881.45 | 69.08 | no_map |
| ZBCNUSDT | IDLE | 2.52 | 4.79 | 1.64 | 0.04 | 209115.53 | 18.5 | n/a |
| CCUSDT | IDLE | 1.75 | 3.23 | 1.83 | 0.03 | 300260.95 | 4.09 | no_map |
| PYTHUSDT | IDLE | 1.21 | 2.17 | 1.64 | 0.0 | 395623.43 | 1.79 | tvl≈125,785,864 |
| TELUSDT | IDLE | 3.3 | 8.53 | 4.74 | 0.05 | 103897.34 | 30.35 | no_map |
| WUSDT | IDLE | 1.53 | 2.74 | 2.18 | 0.03 | 209671.38 | 11.97 | tvl≈1,483,991,975 |
| KITEUSDT | IDLE | 2.13 | 4.01 | 1.64 | 0.02 | 64675.42 | 12.09 | no_map |
| BIOUSDT | IDLE | 1.78 | 3.25 | 2.08 | 0.04 | 98977.08 | 7.73 | n/a |
| REDUSDT | IDLE | 0.97 | 3.44 | 1.76 | 0.09 | 189127.62 | 14.97 | tvl≈2,525,371 |
| HBARUSDT | IDLE | 1.46 | 2.61 | 2.13 | 0.04 | 359543.5 | 1.29 | empty_tvl |
| CHIPUSDT | IDLE | 1.26 | 2.42 | 1.35 | 0.0 | 75098.35 | 14.39 | no_map |
| RWAINCUSDT | IDLE | 1.11 | 2.0 | 1.47 | -0.01 | 5315.75 | 5.51 | no_map |
| RIZEUSDT | IDLE | 0.62 | 7.09 | 3.95 | -0.03 | 55927.87 | 103.67 | no_map |
| QNTUSDT | IDLE | 0.87 | 1.73 | 0.08 | 0.02 | 43545.58 | 6.19 | n/a |
| FLUIDUSDT | IDLE | 0.89 | 1.56 | 1.42 | 0.03 | 1502.72 | 21.8 | tvl≈2,696,741,901 |
| MNSRYUSDT | IDLE | 0.85 | 1.6 | 0.66 | 0.01 | 30733.04 | 34.38 | no_map |
| RWAUSDT | IDLE | 0.41 | 0.74 | 0.59 | -0.0 | 55523.12 | 22.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
