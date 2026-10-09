# Hulk DIGEST — 2026-10-09T10:29:36Z

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
| WUSDT | IDLE | 2.27 | 14.1 | 7.24 | 0.07 | 2950918.07 | 9.25 | tvl≈1,839,491,625 |
| PYTHUSDT | IDLE | 1.32 | 5.68 | 2.74 | 0.12 | 3322444.3 | 4.75 | tvl≈190,557,664 |
| QNTUSDT | IDLE | 1.6 | 5.38 | 1.56 | 0.02 | 2027843.59 | 3.29 | n/a |
| XRPUSDT | IDLE | 0.6 | 1.11 | 0.56 | -0.01 | 47905459.75 | 2.14 | n/a |
| ETHUSDT | IDLE | 0.47 | 0.89 | 0.36 | -0.02 | 497540894.73 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.32 | 0.62 | 0.1 | -0.0 | 416300828.21 | 0.0 | no_map |
| CCUSDT | IDLE | 1.25 | 2.48 | 0.13 | -0.01 | 645990.95 | 11.75 | no_map |
| HBARUSDT | IDLE | 0.83 | 1.54 | 1.24 | -0.03 | 852669.0 | 4.36 | empty_tvl |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 8.97 | 6.82 | 0.02 | 10914.29 | 112.72 | no_map |
| ZBCNUSDT | IDLE | 1.46 | 5.6 | 2.97 | 0.03 | 239193.23 | 14.3 | n/a |
| EDELUSDT | IDLE | 0.95 | 3.43 | 0.42 | 0.01 | 369454.86 | 39.1 | no_map |
| CHIPUSDT | IDLE | 1.17 | 2.91 | 2.67 | -0.03 | 113024.1 | 14.23 | no_map |
| REDUSDT | IDLE | 1.31 | 2.59 | 1.25 | -0.02 | 67152.61 | 16.22 | tvl≈3,703,242 |
| RIZEUSDT | IDLE | 1.04 | 6.61 | 3.13 | -0.04 | 71771.59 | 40.22 | no_map |
| BIOUSDT | IDLE | 0.88 | 1.85 | 1.81 | -0.04 | 83375.3 | 7.09 | n/a |
| KITEUSDT | IDLE | 0.97 | 2.33 | 1.4 | -0.08 | 65031.14 | 8.78 | no_map |
| TELUSDT | IDLE | 0.89 | 2.06 | 0.58 | -0.03 | 179079.32 | 21.39 | no_map |
| FLUIDUSDT | IDLE | 0.74 | 2.93 | 0.33 | 0.04 | 9167.79 | 20.37 | tvl≈2,457,784,143 |
| RWAUSDT | IDLE | 0.37 | 0.7 | 0.23 | -0.03 | 53924.94 | 15.58 | no_map |
| MNSRYUSDT | IDLE | 0.27 | 0.51 | 0.18 | -0.03 | 35581.52 | 16.36 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
