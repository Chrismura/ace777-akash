# Hulk DIGEST — 2026-09-24T17:22:11Z

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
| XRPUSDT | IDLE | 2.58 | 5.08 | 0.49 | 0.02 | 68111576.51 | 1.3 | n/a |
| PYTHUSDT | IDLE | 3.47 | 12.86 | 3.67 | 0.09 | 1264341.49 | 1.46 | tvl≈149,630,889 |
| ETHUSDT | IDLE | 1.31 | 2.49 | 0.87 | 0.01 | 326442043.87 | 0.22 | no_map |
| BTCUSDT | IDLE | 1.14 | 2.14 | 0.87 | 0.0 | 725317227.97 | 0.0 | no_map |
| HBARUSDT | IDLE | 3.27 | 6.19 | 2.35 | 0.03 | 908294.98 | 1.08 | empty_tvl |
| CCUSDT | IDLE | 3.43 | 6.62 | 1.65 | 0.04 | 475540.25 | 8.01 | no_map |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.87 | 12.77 | 1.86 | 0.06 | 73189.14 | 15.39 | no_map |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.36 | 10.97 | 1.26 | 0.1 | 85095.44 | 6.4 | n/a |
| WUSDT | IDLE | 2.79 | 5.44 | 0.95 | 0.03 | 241552.08 | 4.23 | tvl≈1,757,102,628 |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.56 | 13.97 | 0.75 | 0.15 | 11992.11 | 56.55 | no_map |
| ZBCNUSDT | IDLE | 2.61 | 5.08 | 0.89 | 0.04 | 214710.04 | 22.71 | n/a |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.15 | 18.76 | 0.23 | 0.2 | 176950.95 | 16.33 | n/a |
| EDELUSDT | IDLE | 2.45 | 6.41 | 2.36 | -0.02 | 157768.25 | 14.41 | no_map |
| REDUSDT | IDLE | 2.03 | 5.56 | 0.61 | 0.05 | 100878.17 | 13.02 | tvl≈2,830,941 |
| KITEUSDT | IDLE | 1.7 | 3.29 | 0.72 | -0.0 | 84932.46 | 8.25 | no_map |
| RIZEUSDT | IDLE | 1.97 | 10.0 | 4.78 | 0.13 | 49896.71 | 95.63 | no_map |
| TELUSDT | IDLE | 3.03 | 5.45 | 4.11 | -0.04 | 108396.33 | 49.02 | no_map |
| FLUIDUSDT | IDLE | 2.69 | 5.37 | 0.0 | 0.04 | 2717.35 | 17.77 | tvl≈2,617,259,860 |
| RWAUSDT | IDLE | 1.1 | 2.15 | 0.29 | 0.02 | 55804.68 | 7.29 | no_map |
| MNSRYUSDT | IDLE | 0.67 | 1.3 | 0.25 | 0.01 | 37094.57 | 10.37 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
