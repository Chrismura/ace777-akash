# Hulk DIGEST — 2026-10-19T23:05:50Z

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
| ETHUSDT | IDLE | 0.6 | 1.14 | 0.37 | 0.01 | 128636719.44 | 0.21 | no_map |
| XRPUSDT | IDLE | 0.61 | 1.15 | 0.43 | 0.0 | 21552086.24 | 1.53 | n/a |
| BTCUSDT | IDLE | 0.3 | 0.57 | 0.22 | 0.0 | 325662871.36 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.9 | 3.64 | 1.09 | -0.01 | 818244.15 | 1.36 | tvl≈162,110,455 |
| WUSDT | IDLE | 2.19 | 4.1 | 1.91 | 0.03 | 706284.06 | 14.33 | tvl≈1,557,104,883 |
| QNTUSDT | IDLE | 1.3 | 2.46 | 0.99 | 0.03 | 707971.27 | 0.51 | n/a |
| EDELUSDT | IDLE | 2.04 | 3.95 | 0.88 | 0.03 | 200501.42 | 33.14 | no_map |
| CCUSDT | IDLE | 1.04 | 1.99 | 0.64 | 0.04 | 369613.59 | 5.74 | no_map |
| KITEUSDT | IDLE | 1.84 | 3.71 | 1.51 | 0.07 | 76156.68 | 10.63 | no_map |
| ZBCNUSDT | IDLE | 0.99 | 2.64 | 1.14 | 0.02 | 229454.01 | 22.98 | n/a |
| CHIPUSDT | IDLE | 1.54 | 2.93 | 0.94 | 0.03 | 78537.95 | 14.27 | no_map |
| REDUSDT | IDLE | 1.39 | 2.7 | 0.48 | 0.01 | 56919.98 | 5.79 | tvl≈3,411,415 |
| HBARUSDT | IDLE | 0.92 | 1.79 | 0.31 | -0.03 | 468560.99 | 8.44 | empty_tvl |
| BIOUSDT | IDLE | 1.08 | 2.11 | 0.38 | 0.01 | 68870.35 | 4.24 | n/a |
| RWAINCUSDT | IDLE | 0.85 | 1.7 | 1.42 | 0.04 | 71453.81 | 10.3 | no_map |
| RIZEUSDT | IDLE | 0.62 | 1.98 | 1.78 | -0.05 | 53444.31 | 53.51 | no_map |
| WAXLUSDT | IDLE | 1.23 | 3.21 | 2.74 | -0.04 | 62793.32 | 41.77 | no_map |
| IOTAUSDT | IDLE | 1.16 | 2.28 | 0.29 | 0.01 | 90521.02 | 33.23 | no_map |
| LAUSDT | IDLE | 1.21 | 2.3 | 0.74 | 0.0 | 55941.33 | 24.74 | no_map |
| RWAUSDT | IDLE | 0.44 | 0.87 | 0.08 | 0.01 | 54362.66 | 23.5 | no_map |
| MNSRYUSDT | IDLE | 0.16 | 0.29 | 0.14 | 0.0 | 40664.85 | 7.13 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.04 | 4713.92 | 21.19 | tvl≈2,223,621,681 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
