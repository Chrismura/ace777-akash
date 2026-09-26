# Hulk DIGEST — 2026-09-26T23:32:02Z

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
| QNTUSDT | IDLE | 2.26 | 34.96 | 6.73 | 0.51 | 1899990.67 | 17.39 | n/a |
| XRPUSDT | IDLE | 1.23 | 2.38 | 0.57 | -0.02 | 40575961.8 | 0.65 | n/a |
| ETHUSDT | IDLE | 0.58 | 1.15 | 0.03 | 0.0 | 114985146.78 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.36 | 0.72 | 0.06 | 0.0 | 341976571.48 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.12 | 6.07 | 0.99 | 0.08 | 1089491.93 | 6.23 | tvl≈178,469,146 |
| CCUSDT | IDLE | 1.73 | 3.73 | 1.14 | 0.04 | 841446.03 | 0.74 | no_map |
| WUSDT | IDLE | 2.51 | 5.22 | 1.24 | 0.06 | 565128.98 | 16.07 | tvl≈1,851,860,679 |
| EDELUSDT | IDLE | 3.2 | 5.7 | 4.72 | 0.01 | 172144.15 | 23.56 | no_map |
| CHIPUSDT | IDLE | 2.56 | 6.17 | 2.94 | -0.03 | 103431.29 | 16.4 | no_map |
| KITEUSDT | IDLE | 1.95 | 7.67 | 0.75 | 0.14 | 133853.31 | 8.51 | no_map |
| BIOUSDT | IDLE | 2.13 | 3.95 | 2.05 | -0.04 | 110949.63 | 6.24 | n/a |
| ZBCNUSDT | IDLE | 1.67 | 2.97 | 2.47 | -0.03 | 191253.81 | 12.02 | n/a |
| HBARUSDT | IDLE | 1.35 | 2.57 | 0.85 | -0.02 | 535891.88 | 1.07 | empty_tvl |
| RIZEUSDT | IDLE | 2.36 | 6.03 | 0.79 | 0.09 | 49190.25 | 55.24 | no_map |
| REDUSDT | IDLE | 1.58 | 2.99 | 1.16 | -0.03 | 59134.63 | 14.2 | tvl≈3,065,259 |
| RWAINCUSDT | IDLE | 1.4 | 4.65 | 4.44 | 0.03 | 10088.3 | 68.23 | no_map |
| TELUSDT | IDLE | 1.72 | 3.43 | 0.12 | 0.01 | 121186.77 | 60.5 | no_map |
| FLUIDUSDT | IDLE | 1.23 | 2.29 | 1.16 | 0.0 | 643.13 | 21.53 | tvl≈2,582,735,850 |
| RWAUSDT | IDLE | 0.6 | 1.15 | 0.36 | 0.03 | 56407.46 | 7.15 | no_map |
| MNSRYUSDT | IDLE | 0.25 | 0.5 | 0.05 | -0.0 | 38536.78 | 20.4 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
