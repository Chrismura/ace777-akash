# Hulk DIGEST — 2026-09-26T03:50:04Z

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
| XRPUSDT | IDLE | 1.15 | 2.08 | 1.4 | 0.02 | 109841540.41 | 1.28 | n/a |
| ETHUSDT | IDLE | 0.32 | 0.59 | 0.28 | 0.0 | 304258390.18 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.23 | 0.43 | 0.22 | -0.0 | 656645533.99 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.4 | 3.48 | 3.04 | 0.06 | 1246139.36 | 2.74 | tvl≈168,536,691 |
| CCUSDT | IDLE | 1.48 | 6.39 | 1.97 | 0.14 | 913248.08 | 11.29 | no_map |
| HBARUSDT | IDLE | 1.35 | 2.41 | 1.91 | 0.03 | 887818.81 | 1.06 | empty_tvl |
| WUSDT | IDLE | 1.87 | 3.49 | 2.21 | 0.05 | 452810.78 | 8.18 | tvl≈1,832,151,535 |
| CHIPUSDT | IDLE | 1.85 | 4.72 | 4.02 | 0.05 | 148084.15 | 12.31 | no_map |
| KITEUSDT | IDLE | 2.11 | 6.01 | 0.39 | 0.1 | 79746.73 | 9.37 | no_map |
| QNTUSDT | IDLE | 1.14 | 3.94 | 0.3 | 0.09 | 556868.44 | 7.96 | n/a |
| REDUSDT | IDLE | 1.63 | 3.34 | 2.96 | 0.04 | 86647.14 | 12.93 | tvl≈3,162,950 |
| BIOUSDT | IDLE | 1.27 | 3.32 | 2.82 | 0.06 | 113539.05 | 6.17 | n/a |
| ZBCNUSDT | IDLE | 0.98 | 2.14 | 2.0 | 0.05 | 233619.21 | 25.2 | n/a |
| EDELUSDT | IDLE | 0.77 | 1.5 | 0.3 | -0.01 | 186738.54 | 10.13 | no_map |
| RIZEUSDT | IDLE | 0.2 | 2.64 | 1.13 | -0.08 | 89214.92 | 62.47 | no_map |
| TELUSDT | IDLE | 0.69 | 1.23 | 1.03 | 0.02 | 107425.04 | 18.39 | no_map |
| FLUIDUSDT | IDLE | 1.05 | 1.83 | 1.79 | 0.0 | 3437.87 | 21.15 | tvl≈2,580,493,643 |
| RWAUSDT | IDLE | 0.56 | 1.04 | 0.59 | -0.01 | 53225.01 | 7.39 | no_map |
| RWAINCUSDT | IDLE | 0.03 | 0.1 | 0.05 | -0.09 | 12811.79 | 95.89 | no_map |
| MNSRYUSDT | IDLE | 0.49 | 0.91 | 0.5 | 0.01 | 41197.62 | 40.84 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
