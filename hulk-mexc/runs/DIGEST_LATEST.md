# Hulk DIGEST — 2026-08-21T21:39:46Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.57 | 0.1 | 5649475.25 | 2.07 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.11 | 3.73 | 1.04 | 0.1 | 129346202.68 | 1.43 | n/a |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.7 | 0.05 | 516885.23 | 6.21 | no_map |
| ZBCNUSDT | IDLE | 1.95 | 8.19 | 3.63 | 0.1 | 489544.0 | 34.64 | n/a |
| CCUSDT | IDLE | 1.27 | 3.75 | 0.03 | 0.1 | 651333.08 | 8.21 | no_map |
| HBARUSDT | IDLE | 1.63 | 3.24 | 0.13 | 0.07 | 817727.94 | 1.28 | empty_tvl |
| WUSDT | IDLE | 1.95 | 3.83 | 0.42 | 0.06 | 368986.99 | 9.4 | tvl≈1,602,784,605 |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.9 | 0.02 | 187932.93 | 3.13 | n/a |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.12 | 0.17 | 154196.97 | 18.82 | tvl≈2,226,572 |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.06 | 0.03 | 55928.08 | 28.08 | no_map |
| EDELUSDT | IDLE | 1.91 | 4.12 | 0.66 | -0.04 | 83558.76 | 33.31 | no_map |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.03 | 10249.04 | 42.69 | no_map |
| KITEUSDT | IDLE | 1.29 | 4.0 | 1.53 | 0.11 | 61066.02 | 9.22 | no_map |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 119.76 | no_map |
| TELUSDT | IDLE | 1.93 | 4.81 | 1.46 | 0.02 | 182895.48 | 47.56 | no_map |
| QNTUSDT | IDLE | 1.39 | 2.65 | 0.86 | 0.04 | 62630.53 | 6.2 | n/a |
| RWAUSDT | IDLE | 0.63 | 1.17 | 0.58 | 0.03 | 53955.36 | 24.82 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 44.56 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
