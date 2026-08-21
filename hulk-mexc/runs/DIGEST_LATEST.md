# Hulk DIGEST — 2026-08-21T22:19:12Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.18 | 0.11 | 5741532.62 | 2.04 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.51 | 5.5 | 0.05 | 0.14 | 131944977.2 | 4.18 | n/a |
| CCUSDT | IDLE | 1.75 | 6.45 | 0.07 | 0.13 | 645379.23 | 12.43 | no_map |
| HBARUSDT | IDLE | 2.2 | 4.71 | 0.62 | 0.08 | 852906.8 | 1.26 | empty_tvl |
| WUSDT | IDLE | 2.45 | 5.3 | 0.11 | 0.08 | 369693.53 | 10.27 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.49 | 4.54 | 1.33 | 0.06 | 534162.22 | 3.05 | no_map |
| ZBCNUSDT | IDLE | 1.52 | 6.5 | 0.32 | 0.11 | 499814.83 | 17.25 | n/a |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.74 | 0.03 | 187862.61 | 3.1 | n/a |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.87 | 0.19 | 156333.34 | 11.31 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 1.94 | 4.24 | 0.33 | -0.04 | 82362.14 | 22.03 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | no_map |
| TELUSDT | IDLE | 2.51 | 6.45 | 0.46 | 0.06 | 186834.36 | 46.38 | no_map |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 75.43 | no_map |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.71 | 0.11 | 61343.59 | 11.93 | no_map |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 1.98 | 0.06 | 56377.55 | 45.14 | no_map |
| QNTUSDT | IDLE | 1.71 | 3.41 | 0.0 | 0.05 | 65410.9 | 7.62 | n/a |
| RWAUSDT | IDLE | 0.9 | 1.75 | 0.33 | 0.04 | 54196.74 | 16.46 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 13.34 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
