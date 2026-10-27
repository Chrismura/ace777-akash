# Hulk DIGEST — 2026-10-27T01:35:27Z

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
| XRPUSDT | IDLE | 1.15 | 2.19 | 0.69 | 0.01 | 24788260.03 | 0.77 | n/a |
| ETHUSDT | IDLE | 0.69 | 1.3 | 0.48 | 0.0 | 131487988.38 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.44 | 0.83 | 0.32 | 0.0 | 356054423.57 | 0.22 | no_map |
| QNTUSDT | IDLE | 0.47 | 1.99 | 1.38 | 0.06 | 1396378.16 | 3.96 | n/a |
| PYTHUSDT | IDLE | 1.73 | 3.12 | 2.27 | -0.01 | 697650.01 | 2.71 | tvl≈164,006,083 |
| WUSDT | IDLE | 1.5 | 2.99 | 1.36 | 0.04 | 640989.01 | 20.99 | tvl≈1,516,296,021 |
| CHIPUSDT | IDLE | 0.74 | 5.48 | 4.84 | 0.17 | 328674.5 | 19.74 | no_map |
| RWAINCUSDT | IDLE | 1.55 | 5.5 | 4.72 | -0.12 | 60021.97 | 19.31 | no_map |
| REDUSDT | IDLE | 1.62 | 2.95 | 1.94 | 0.02 | 61792.71 | 15.04 | tvl≈3,642,722 |
| CCUSDT | IDLE | 1.05 | 1.96 | 0.95 | -0.02 | 187615.47 | 9.08 | no_map |
| EDELUSDT | IDLE | 1.17 | 2.16 | 1.26 | 0.02 | 172554.45 | 24.81 | no_map |
| ZBCNUSDT | IDLE | 0.92 | 1.78 | 0.39 | -0.04 | 218033.75 | 30.2 | n/a |
| BIOUSDT | IDLE | 1.16 | 2.19 | 0.8 | 0.0 | 56980.59 | 13.51 | n/a |
| KITEUSDT | IDLE | 0.69 | 1.22 | 1.11 | 0.01 | 54093.19 | 11.45 | no_map |
| HBARUSDT | IDLE | 0.87 | 1.66 | 0.54 | -0.0 | 241448.07 | 7.78 | empty_tvl |
| IOTAUSDT | IDLE | 1.49 | 2.75 | 1.58 | -0.01 | 90083.32 | 21.25 | no_map |
| RIZEUSDT | IDLE | 0.77 | 1.4 | 0.88 | -0.01 | 44079.78 | 65.34 | no_map |
| LAUSDT | IDLE | 1.49 | 2.89 | 2.35 | 0.03 | 67785.18 | 25.75 | no_map |
| WAXLUSDT | IDLE | 1.66 | 3.11 | 1.41 | -0.03 | 53021.53 | 37.95 | no_map |
| FLUIDUSDT | IDLE | 1.35 | 2.68 | 0.18 | 0.04 | 2288.53 | 21.79 | tvl≈2,187,847,033 |
| RWAUSDT | IDLE | 0.64 | 1.21 | 0.48 | -0.0 | 53335.75 | 15.96 | no_map |
| MNSRYUSDT | IDLE | 0.37 | 0.74 | 0.0 | -0.0 | 41469.49 | 76.46 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
