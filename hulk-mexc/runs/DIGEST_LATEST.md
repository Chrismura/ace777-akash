# Hulk DIGEST — 2026-10-20T09:12:19Z

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
| ETHUSDT | IDLE | 0.9 | 1.57 | 1.48 | -0.02 | 131771108.7 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.7 | 1.23 | 1.18 | -0.02 | 20525324.55 | 1.55 | n/a |
| BTCUSDT | IDLE | 0.62 | 1.09 | 1.0 | -0.02 | 304723751.18 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.71 | 3.09 | 2.23 | -0.04 | 994342.69 | 2.76 | tvl≈161,581,975 |
| WUSDT | IDLE | 2.08 | 3.83 | 2.24 | 0.02 | 720417.62 | 16.14 | tvl≈1,568,169,297 |
| CCUSDT | IDLE | 2.52 | 4.4 | 4.22 | 0.01 | 462009.41 | 8.73 | no_map |
| QNTUSDT | IDLE | 2.62 | 4.71 | 3.5 | -0.04 | 618140.53 | 0.52 | n/a |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.32 | 12.61 | 0.5 | 0.18 | 301291.99 | 21.89 | no_map |
| CHIPUSDT | IDLE | 2.04 | 5.16 | 2.7 | 0.03 | 92368.99 | 13.74 | no_map |
| KITEUSDT | IDLE | 2.06 | 3.6 | 3.47 | 0.03 | 78793.27 | 10.78 | no_map |
| ZBCNUSDT | IDLE | 1.33 | 2.41 | 1.71 | -0.03 | 170936.21 | 24.52 | n/a |
| HBARUSDT | IDLE | 1.17 | 2.05 | 1.97 | -0.02 | 368661.34 | 6.06 | empty_tvl |
| RWAINCUSDT | IDLE | 1.02 | 1.82 | 1.53 | 0.02 | 75308.88 | 5.19 | no_map |
| BIOUSDT | IDLE | 1.04 | 1.84 | 1.55 | -0.01 | 65979.96 | 8.53 | n/a |
| REDUSDT | IDLE | 1.09 | 1.9 | 1.81 | -0.0 | 58521.88 | 17.6 | tvl≈3,461,714 |
| RIZEUSDT | IDLE | 0.61 | 2.27 | 1.89 | -0.08 | 67248.28 | 64.29 | no_map |
| LAUSDT | IDLE | 1.51 | 2.65 | 2.52 | -0.03 | 55884.48 | 25.07 | no_map |
| IOTAUSDT | IDLE | 1.21 | 2.17 | 1.71 | 0.01 | 90206.59 | 24.25 | no_map |
| WAXLUSDT | IDLE | 1.47 | 2.98 | 2.41 | -0.06 | 57347.89 | 64.42 | no_map |
| FLUIDUSDT | IDLE | 1.29 | 2.38 | 1.4 | -0.01 | 4449.41 | 26.45 | tvl≈2,221,011,005 |
| MNSRYUSDT | IDLE | 0.13 | 0.26 | 0.04 | -0.0 | 39860.01 | 4.27 | no_map |
| RWAUSDT | IDLE | 0.21 | 0.39 | 0.24 | 0.01 | 51628.91 | 31.42 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
