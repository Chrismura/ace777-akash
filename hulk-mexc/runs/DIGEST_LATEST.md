# Hulk DIGEST — 2026-10-25T01:56:06Z

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
| XRPUSDT | IDLE | 0.73 | 1.43 | 0.15 | 0.01 | 25479838.71 | 1.53 | n/a |
| ETHUSDT | IDLE | 0.66 | 1.3 | 0.12 | -0.01 | 121578482.25 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.39 | 0.77 | 0.1 | -0.0 | 246906553.27 | 0.0 | no_map |
| WUSDT | IDLE | 1.24 | 2.79 | 1.24 | -0.05 | 782285.05 | 30.28 | tvl≈1,502,800,555 |
| PYTHUSDT | IDLE | 1.78 | 3.36 | 1.35 | 0.01 | 522674.35 | 1.41 | tvl≈156,270,678 |
| EDELUSDT | IDLE | 1.3 | 3.24 | 1.15 | -0.06 | 587309.76 | 29.81 | no_map |
| ZBCNUSDT | IDLE | 2.35 | 5.28 | 3.48 | 0.01 | 227838.75 | 16.09 | n/a |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.09 | 8.8 | 1.89 | -0.01 | 42309.44 | 62.58 | no_map |
| CHIPUSDT | IDLE | 2.4 | 7.21 | 3.03 | 0.03 | 87504.11 | 15.62 | no_map |
| LAUSDT | IDLE | 2.1 | 11.5 | 9.29 | -0.09 | 104981.49 | 25.4 | no_map |
| QNTUSDT | IDLE | 1.59 | 3.11 | 0.42 | -0.01 | 365346.94 | 2.21 | n/a |
| REDUSDT | IDLE | 1.32 | 3.09 | 3.0 | 0.01 | 99248.94 | 14.96 | tvl≈3,668,942 |
| KITEUSDT | IDLE | 1.56 | 2.86 | 1.76 | -0.04 | 60193.59 | 13.96 | no_map |
| CCUSDT | IDLE | 0.66 | 1.19 | 0.85 | -0.02 | 222751.18 | 9.89 | no_map |
| BIOUSDT | IDLE | 1.23 | 2.25 | 1.38 | -0.03 | 66147.15 | 4.38 | n/a |
| WAXLUSDT | IDLE | 2.34 | 5.99 | 4.9 | 0.0 | 56662.3 | 43.34 | no_map |
| RWAINCUSDT | IDLE | 0.74 | 1.49 | 0.0 | 0.01 | 54004.52 | 10.84 | no_map |
| FLUIDUSDT | IDLE | 1.73 | 3.56 | 1.39 | -0.05 | 13084.07 | 22.62 | tvl≈2,188,440,831 |
| HBARUSDT | IDLE | 0.59 | 1.14 | 0.28 | -0.0 | 198412.57 | 6.42 | empty_tvl |
| IOTAUSDT | IDLE | 1.09 | 2.01 | 1.11 | -0.03 | 68064.74 | 27.42 | no_map |
| RWAUSDT | IDLE | 0.32 | 0.64 | 0.0 | -0.0 | 54204.3 | 55.53 | no_map |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.64 | -0.01 | 37669.6 | 77.07 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
