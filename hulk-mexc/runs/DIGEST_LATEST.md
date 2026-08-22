# Hulk DIGEST — 2026-08-22T16:30:56Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.54 | 7.6 | 0.0 | 0.07 | 51433125.46 | 3.88 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.76 | 0.05 | 215250203.24 | 2.72 | n/a |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.44 | 0.08 | 764460.02 | 3.42 | no_map |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.1 | -0.01 | 1125784.25 | 3.88 | empty_tvl |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.9 | -0.1 | 627531.95 | 3.35 | no_map |
| WUSDT | IDLE | 0.62 | 2.58 | 1.03 | -0.01 | 544131.82 | 21.21 | tvl≈1,556,368,553 |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.31 | -0.04 | 316083.06 | 25.03 | n/a |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.19 | -0.06 | 219821.13 | 3.29 | n/a |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.44 | 0.03 | 85173.75 | 11.57 | no_map |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.13 | -0.03 | 74856.17 | 22.83 | no_map |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.2 | 0.03 | 56613.89 | 23.57 | no_map |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.14 | -0.13 | 132922.27 | 21.01 | tvl≈2,005,037 |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2320.37 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.16 | -0.02 | 183293.62 | 6.31 | n/a |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.03 | 8171.79 | 69.84 | no_map |
| TELUSDT | IDLE | 0.95 | 2.37 | 1.21 | 0.01 | 137699.72 | 47.78 | no_map |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.32 | 0.02 | 56354.94 | 16.22 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 22.38 | tvl≈2,551,700,555 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
