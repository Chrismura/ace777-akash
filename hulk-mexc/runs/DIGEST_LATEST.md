# Hulk DIGEST — 2026-08-21T21:32:40Z

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
| PYTHUSDT | IDLE | 1.18 | 4.51 | 0.88 | 0.09 | 5637821.63 | 2.07 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.12 | 3.73 | 1.36 | 0.11 | 129119854.9 | 3.59 | n/a |
| CHIPUSDT | IDLE | 1.89 | 5.61 | 4.03 | 0.05 | 517496.92 | 6.22 | no_map |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.28 | 0.1 | 486870.9 | 35.38 | n/a |
| CCUSDT | IDLE | 1.13 | 3.17 | 0.0 | 0.1 | 645714.96 | 6.42 | no_map |
| HBARUSDT | IDLE | 1.53 | 3.04 | 0.18 | 0.07 | 815006.83 | 2.56 | empty_tvl |
| WUSDT | IDLE | 1.94 | 3.83 | 0.28 | 0.07 | 367588.19 | 14.61 | tvl≈1,602,784,605 |
| BIOUSDT | IDLE | 2.43 | 5.2 | 2.06 | 0.02 | 186920.16 | 6.27 | n/a |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.18 | 0.17 | 154028.35 | 10.64 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 2.02 | 4.12 | 2.31 | -0.05 | 83395.24 | 33.65 | no_map |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.85 | 0.02 | 10171.16 | 27.02 | no_map |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.35 | 0.02 | 56019.27 | 45.77 | no_map |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.48 | 0.11 | 61034.73 | 9.22 | no_map |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 119.76 | no_map |
| TELUSDT | IDLE | 1.89 | 4.81 | 0.78 | 0.03 | 182606.51 | 73.49 | no_map |
| QNTUSDT | IDLE | 1.39 | 2.65 | 0.88 | 0.04 | 63210.76 | 10.86 | n/a |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.41 | 0.03 | 53880.02 | 41.41 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 36.8 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
