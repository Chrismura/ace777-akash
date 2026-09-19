# Hulk DIGEST — 2026-09-19T22:00:12Z

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
| XRPUSDT | IDLE | 1.68 | 2.99 | 2.48 | 0.01 | 57910971.25 | 1.42 | n/a |
| ETHUSDT | IDLE | 1.08 | 1.94 | 1.5 | 0.0 | 264108329.44 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.69 | 1.23 | 0.99 | -0.0 | 452802042.22 | 0.07 | no_map |
| CCUSDT | IDLE | 2.65 | 4.64 | 4.36 | -0.02 | 331933.71 | 9.2 | no_map |
| PYTHUSDT | IDLE | 1.31 | 2.37 | 1.66 | -0.0 | 652108.13 | 6.63 | tvl≈136,715,653 |
| WUSDT | IDLE | 1.67 | 2.98 | 2.45 | 0.01 | 546353.55 | 3.66 | tvl≈1,605,459,515 |
| ZBCNUSDT | IDLE | 2.66 | 10.45 | 4.34 | 0.11 | 220534.44 | 24.46 | n/a |
| HBARUSDT | IDLE | 1.59 | 2.88 | 1.98 | 0.02 | 644698.18 | 2.48 | empty_tvl |
| EDELUSDT | IDLE | 1.93 | 7.26 | 6.31 | -0.12 | 141100.16 | 49.46 | no_map |
| RWAINCUSDT | IDLE | 2.9 | 6.81 | 2.35 | -0.02 | 6707.66 | 58.72 | no_map |
| BIOUSDT | IDLE | 1.84 | 3.36 | 2.17 | 0.02 | 87475.34 | 10.72 | n/a |
| KITEUSDT | IDLE | 1.76 | 3.15 | 2.42 | 0.02 | 76944.84 | 11.41 | no_map |
| CHIPUSDT | IDLE | 1.21 | 3.47 | 1.57 | -0.04 | 132609.72 | 16.21 | no_map |
| REDUSDT | IDLE | 0.33 | 1.56 | 0.17 | 0.02 | 136284.1 | 9.42 | tvl≈2,680,263 |
| RIZEUSDT | IDLE | 1.41 | 5.75 | 4.2 | 0.02 | 37579.4 | 149.38 | no_map |
| FLUIDUSDT | IDLE | 1.77 | 3.09 | 3.0 | 0.02 | 9393.64 | 21.8 | tvl≈2,639,763,731 |
| TELUSDT | IDLE | 1.21 | 3.76 | 3.49 | -0.03 | 119660.23 | 46.9 | no_map |
| QNTUSDT | IDLE | 1.23 | 2.25 | 1.44 | 0.03 | 58418.35 | 10.68 | n/a |
| RWAUSDT | IDLE | 0.81 | 1.48 | 0.95 | 0.01 | 53435.64 | 14.71 | no_map |
| MNSRYUSDT | IDLE | 0.34 | 0.63 | 0.28 | -0.01 | 35243.01 | 43.72 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
