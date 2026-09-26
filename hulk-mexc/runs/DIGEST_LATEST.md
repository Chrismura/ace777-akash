# Hulk DIGEST — 2026-09-26T08:57:57Z

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
| XRPUSDT | IDLE | 0.72 | 1.29 | 0.95 | 0.01 | 109163791.05 | 1.29 | n/a |
| ETHUSDT | IDLE | 0.28 | 0.53 | 0.23 | 0.0 | 277203438.65 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.28 | 0.54 | 0.13 | -0.0 | 583481218.75 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.06 | 3.99 | 0.82 | 0.06 | 1169477.84 | 4.01 | tvl≈167,416,854 |
| CCUSDT | IDLE | 1.65 | 7.25 | 2.85 | 0.13 | 1056017.81 | 5.89 | no_map |
| QNTUSDT | IDLE | 2.43 | 9.16 | 4.35 | 0.04 | 771555.88 | 19.44 | n/a |
| WUSDT | IDLE | 2.15 | 4.98 | 0.02 | 0.08 | 475651.14 | 5.47 | tvl≈1,848,318,253 |
| HBARUSDT | IDLE | 0.73 | 1.42 | 0.27 | 0.02 | 833019.29 | 1.06 | empty_tvl |
| KITEUSDT | IDLE | 1.97 | 4.32 | 2.72 | 0.05 | 77293.83 | 9.56 | no_map |
| RWAINCUSDT | IDLE | 2.31 | 4.42 | 1.31 | 0.02 | 8387.4 | 19.81 | no_map |
| ZBCNUSDT | IDLE | 1.26 | 2.82 | 1.24 | 0.04 | 246448.35 | 25.42 | n/a |
| CHIPUSDT | IDLE | 1.5 | 2.89 | 0.87 | 0.04 | 145423.61 | 16.29 | no_map |
| EDELUSDT | IDLE | 1.58 | 3.04 | 0.76 | 0.02 | 175812.87 | 46.68 | no_map |
| BIOUSDT | IDLE | 0.54 | 1.3 | 0.55 | 0.04 | 122339.76 | 3.07 | n/a |
| REDUSDT | IDLE | 0.84 | 1.53 | 1.04 | 0.03 | 59505.46 | 6.45 | tvl≈3,123,109 |
| RIZEUSDT | IDLE | 0.25 | 3.43 | 1.01 | -0.25 | 61593.38 | 33.23 | no_map |
| TELUSDT | IDLE | 0.9 | 1.61 | 1.28 | -0.01 | 118563.64 | 30.85 | no_map |
| FLUIDUSDT | IDLE | 0.96 | 1.83 | 0.62 | 0.0 | 3382.73 | 21.56 | tvl≈2,580,811,423 |
| RWAUSDT | IDLE | 0.62 | 1.19 | 0.29 | -0.01 | 53089.59 | 14.73 | no_map |
| MNSRYUSDT | IDLE | 0.32 | 0.63 | 0.13 | 0.01 | 40752.51 | 8.92 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
