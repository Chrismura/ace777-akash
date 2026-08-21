# Hulk DIGEST — 2026-08-21T21:25:41Z

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
| PYTHUSDT | IDLE | 1.18 | 4.51 | 0.92 | 0.1 | 5624668.74 | 2.07 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.12 | 3.73 | 1.29 | 0.11 | 128948354.28 | 2.15 | n/a |
| ZBCNUSDT | IDLE | 1.96 | 8.19 | 4.04 | 0.1 | 484558.37 | 3.53 | n/a |
| CHIPUSDT | IDLE | 1.91 | 5.61 | 4.41 | 0.05 | 517327.28 | 9.34 | no_map |
| CCUSDT | IDLE | 1.13 | 3.14 | 0.1 | 0.1 | 644381.87 | 5.51 | no_map |
| HBARUSDT | IDLE | 1.54 | 3.04 | 0.27 | 0.07 | 811795.8 | 1.28 | empty_tvl |
| WUSDT | IDLE | 1.93 | 3.83 | 0.19 | 0.07 | 367876.36 | 14.61 | tvl≈1,602,784,605 |
| BIOUSDT | IDLE | 2.42 | 5.2 | 2.03 | 0.02 | 186861.54 | 6.27 | n/a |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.33 | 0.17 | 153818.0 | 32.82 | tvl≈2,226,572 |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10270.17 | 16.12 | no_map |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.34 | 0.02 | 56129.38 | 45.77 | no_map |
| EDELUSDT | IDLE | 1.99 | 4.12 | 1.87 | -0.05 | 82811.73 | 33.76 | no_map |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3754.88 | 56.07 | no_map |
| KITEUSDT | IDLE | 1.3 | 4.0 | 1.93 | 0.11 | 61029.6 | 11.12 | no_map |
| TELUSDT | IDLE | 1.34 | 3.39 | 0.63 | 0.02 | 178849.22 | 37.24 | no_map |
| QNTUSDT | IDLE | 1.41 | 2.65 | 1.15 | 0.04 | 62148.11 | 1.56 | n/a |
| RWAUSDT | IDLE | 0.63 | 1.17 | 0.58 | 0.03 | 53868.12 | 24.82 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 35.52 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
