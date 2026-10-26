# Hulk DIGEST — 2026-10-26T07:15:37Z

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
| XRPUSDT | IDLE | 0.94 | 1.77 | 0.69 | -0.01 | 16868597.42 | 1.55 | n/a |
| ETHUSDT | IDLE | 0.82 | 1.59 | 0.39 | -0.01 | 105039718.08 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.58 | 1.14 | 0.2 | -0.01 | 206005954.65 | 0.28 | no_map |
| PYTHUSDT | IDLE | 1.33 | 2.73 | 2.61 | 0.03 | 786787.32 | 2.73 | tvl≈164,901,421 |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.06 | 10.26 | 1.62 | 0.04 | 101843.2 | 17.3 | no_map |
| WUSDT | IDLE | 1.34 | 2.38 | 2.04 | -0.04 | 463962.01 | 17.15 | tvl≈1,516,537,043 |
| LAUSDT | IDLE | 4.29 | 8.72 | 4.24 | -0.04 | 61723.94 | 24.46 | no_map |
| QNTUSDT | IDLE | 1.14 | 3.44 | 0.28 | 0.05 | 742237.11 | 4.12 | n/a |
| RWAINCUSDT | IDLE | 2.37 | 4.28 | 3.88 | -0.07 | 66762.21 | 35.15 | no_map |
| ZBCNUSDT | IDLE | 1.62 | 2.92 | 2.41 | 0.01 | 180186.25 | 22.53 | n/a |
| REDUSDT | IDLE | 1.97 | 3.63 | 2.13 | -0.02 | 60502.47 | 10.4 | tvl≈3,568,863 |
| KITEUSDT | IDLE | 1.64 | 3.01 | 1.81 | -0.0 | 53504.67 | 20.56 | no_map |
| BIOUSDT | IDLE | 1.39 | 2.52 | 1.7 | -0.02 | 60970.18 | 9.1 | n/a |
| CCUSDT | IDLE | 0.88 | 1.58 | 1.2 | 0.0 | 161132.57 | 0.99 | no_map |
| EDELUSDT | IDLE | 0.87 | 2.1 | 1.37 | 0.06 | 144410.49 | 34.62 | no_map |
| HBARUSDT | IDLE | 0.86 | 1.57 | 1.01 | -0.01 | 180583.66 | 5.21 | empty_tvl |
| WAXLUSDT | IDLE | 1.69 | 2.98 | 2.62 | -0.01 | 52798.94 | 52.53 | no_map |
| RIZEUSDT | IDLE | 0.53 | 1.0 | 0.39 | 0.0 | 33057.33 | 55.27 | no_map |
| IOTAUSDT | IDLE | 1.12 | 2.01 | 1.55 | -0.03 | 62756.81 | 23.78 | no_map |
| FLUIDUSDT | IDLE | 0.28 | 1.49 | 0.0 | -0.02 | 19116.06 | 21.42 | tvl≈2,176,151,080 |
| RWAUSDT | IDLE | 0.14 | 0.24 | 0.24 | -0.01 | 52739.53 | 23.89 | no_map |
| MNSRYUSDT | IDLE | 0.29 | 0.57 | 0.03 | -0.01 | 38157.63 | 60.17 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
