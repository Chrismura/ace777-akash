# Hulk DIGEST — 2026-10-10T21:03:27Z

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
| ETHUSDT | IDLE | 0.32 | 0.58 | 0.38 | 0.01 | 102777076.17 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.26 | 0.51 | 0.08 | 0.01 | 13261726.86 | 1.42 | n/a |
| BTCUSDT | IDLE | 0.12 | 0.22 | 0.13 | 0.01 | 170515455.23 | 0.0 | no_map |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.86 | 33.98 | 1.02 | 0.36 | 213136.55 | 7.29 | no_map |
| WUSDT | IDLE | 0.99 | 3.34 | 0.86 | 0.03 | 1251933.89 | 13.38 | tvl≈1,652,141,982 |
| QNTUSDT | IDLE | 1.62 | 2.93 | 2.07 | -0.02 | 1226166.27 | 3.32 | n/a |
| PYTHUSDT | IDLE | 0.86 | 1.65 | 0.5 | -0.02 | 783081.97 | 1.26 | tvl≈177,352,946 |
| EDELUSDT | IDLE | 1.82 | 3.92 | 1.2 | -0.03 | 224525.75 | 2.58 | no_map |
| CCUSDT | IDLE | 1.38 | 2.54 | 1.51 | -0.02 | 299935.26 | 5.04 | no_map |
| RWAINCUSDT | IDLE | 2.28 | 4.24 | 2.18 | -0.03 | 9489.24 | 49.38 | no_map |
| BIOUSDT | IDLE | 1.52 | 3.05 | 0.0 | 0.06 | 88227.96 | 13.45 | n/a |
| KITEUSDT | IDLE | 1.02 | 2.47 | 2.32 | 0.07 | 71386.1 | 10.16 | no_map |
| ZBCNUSDT | IDLE | 0.48 | 0.88 | 0.56 | 0.01 | 204189.84 | 14.83 | n/a |
| RIZEUSDT | IDLE | 1.14 | 2.0 | 1.88 | -0.02 | 36682.89 | 34.26 | no_map |
| TELUSDT | IDLE | 1.75 | 3.46 | 0.33 | -0.0 | 135567.86 | 27.54 | no_map |
| REDUSDT | IDLE | 0.59 | 1.1 | 0.58 | 0.03 | 54320.96 | 15.25 | tvl≈3,764,014 |
| HBARUSDT | IDLE | 0.6 | 1.13 | 0.47 | 0.02 | 315341.37 | 5.39 | empty_tvl |
| FLUIDUSDT | IDLE | 1.29 | 2.45 | 0.87 | 0.0 | 8531.47 | 21.11 | tvl≈2,428,484,898 |
| RWAUSDT | IDLE | 0.44 | 0.79 | 0.63 | 0.01 | 53974.64 | 7.87 | no_map |
| MNSRYUSDT | IDLE | 0.42 | 0.76 | 0.53 | 0.0 | 37080.04 | 63.81 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
