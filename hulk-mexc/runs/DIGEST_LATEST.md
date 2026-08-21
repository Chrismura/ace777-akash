# Hulk DIGEST — 2026-08-21T21:36:10Z

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
| PYTHUSDT | IDLE | 1.16 | 4.51 | 0.43 | 0.1 | 5644492.23 | 2.06 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.1 | 3.73 | 0.86 | 0.11 | 129297557.72 | 0.71 | n/a |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.58 | 0.06 | 517152.48 | 6.19 | no_map |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.21 | 0.1 | 488602.21 | 40.39 | n/a |
| CCUSDT | IDLE | 1.18 | 3.39 | 0.01 | 0.1 | 647375.51 | 7.32 | no_map |
| HBARUSDT | IDLE | 1.58 | 3.17 | 0.0 | 0.07 | 818006.82 | 2.55 | empty_tvl |
| WUSDT | IDLE | 1.93 | 3.83 | 0.18 | 0.07 | 368412.55 | 11.47 | tvl≈1,602,784,605 |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.9 | 0.02 | 187941.68 | 3.13 | n/a |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.79 | 0.17 | 154179.08 | 10.59 | tvl≈2,226,572 |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.23 | 0.02 | 56013.11 | 28.08 | no_map |
| RWAINCUSDT | IDLE | 2.24 | 4.3 | 1.22 | 0.03 | 10157.2 | 10.82 | no_map |
| EDELUSDT | IDLE | 1.97 | 4.12 | 1.54 | -0.05 | 83487.1 | 66.74 | no_map |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.42 | 0.11 | 61030.37 | 11.05 | no_map |
| TELUSDT | IDLE | 1.91 | 4.81 | 0.99 | 0.03 | 182963.7 | 73.88 | no_map |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 194.87 | no_map |
| QNTUSDT | IDLE | 1.37 | 2.65 | 0.57 | 0.04 | 62883.52 | 15.51 | n/a |
| RWAUSDT | IDLE | 0.63 | 1.17 | 0.66 | 0.03 | 53988.37 | 24.84 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.91 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
