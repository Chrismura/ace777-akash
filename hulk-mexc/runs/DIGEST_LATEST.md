# Hulk DIGEST — 2026-08-22T17:00:09Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 10.19 | 0.81 | 0.08 | 49200036.2 | 1.91 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.31 | 7.64 | 3.0 | 0.06 | 214602755.41 | 2.7 | n/a |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.91 | -0.0 | 1130587.77 | 6.45 | empty_tvl |
| CCUSDT | IDLE | 0.94 | 4.14 | 1.17 | 0.1 | 769337.44 | 10.13 | no_map |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.63 | -0.09 | 631148.69 | 3.34 | no_map |
| WUSDT | IDLE | 0.6 | 2.58 | 0.39 | -0.01 | 544324.03 | 12.67 | tvl≈1,556,368,553 |
| BIOUSDT | IDLE | 1.04 | 6.91 | 5.7 | -0.07 | 225783.96 | 3.34 | n/a |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.51 | -0.02 | 312686.47 | 28.13 | n/a |
| KITEUSDT | IDLE | 1.88 | 4.35 | 1.28 | 0.03 | 87691.77 | 13.31 | no_map |
| EDELUSDT | IDLE | 1.66 | 3.0 | 2.13 | -0.02 | 74798.2 | 11.44 | no_map |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.67 | -0.13 | 125797.05 | 10.0 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.44 | 3.47 | 0.5 | 0.05 | 46180.46 | 45.5 | no_map |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.77 | -0.01 | 181136.4 | 6.29 | n/a |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.15 | -0.0 | 136238.86 | 42.94 | no_map |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 102.34 | no_map |
| RWAUSDT | IDLE | 0.53 | 1.06 | 0.0 | 0.02 | 56331.91 | 8.09 | no_map |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 20.09 | tvl≈2,551,700,555 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
