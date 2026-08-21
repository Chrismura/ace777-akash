# Hulk DIGEST — 2026-08-21T22:04:57Z

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
| PYTHUSDT | IDLE | 1.25 | 4.74 | 0.27 | 0.1 | 5698091.23 | 2.05 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.08 | 3.73 | 0.25 | 0.12 | 129832303.64 | 2.13 | n/a |
| HBARUSDT | IDLE | 2.2 | 4.71 | 0.63 | 0.08 | 840738.18 | 1.27 | empty_tvl |
| CCUSDT | IDLE | 1.31 | 3.97 | 0.0 | 0.11 | 636283.67 | 6.37 | no_map |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.14 | 0.06 | 531131.23 | 6.15 | no_map |
| WUSDT | IDLE | 2.27 | 4.52 | 0.08 | 0.08 | 368413.44 | 12.42 | tvl≈1,602,784,605 |
| ZBCNUSDT | IDLE | 1.45 | 6.22 | 0.07 | 0.12 | 494885.18 | 22.19 | n/a |
| BIOUSDT | IDLE | 2.26 | 5.01 | 0.74 | 0.04 | 185396.88 | 3.1 | n/a |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.66 | 0.18 | 153818.29 | 19.55 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 1.88 | 4.12 | 0.22 | -0.04 | 82452.99 | 33.17 | no_map |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.28 | 0.05 | 186661.02 | 25.99 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | no_map |
| RWAINCUSDT | IDLE | 2.1 | 4.07 | 0.9 | 0.02 | 10204.87 | 58.74 | no_map |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.86 | 0.11 | 61292.18 | 12.89 | no_map |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.77 | 0.06 | 56408.14 | 45.14 | no_map |
| QNTUSDT | IDLE | 1.25 | 2.49 | 0.02 | 0.05 | 62381.5 | 1.54 | n/a |
| RWAUSDT | IDLE | 0.83 | 1.67 | 0.0 | 0.04 | 54121.89 | 24.7 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 20.37 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
