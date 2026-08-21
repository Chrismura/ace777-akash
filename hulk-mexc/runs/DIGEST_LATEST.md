# Hulk DIGEST — 2026-08-21T22:54:26Z

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
| PYTHUSDT | IDLE | 1.43 | 5.43 | 0.22 | 0.11 | 5904902.52 | 4.08 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.67 | 6.52 | 0.3 | 0.15 | 136623958.94 | 2.07 | n/a |
| CCUSDT | IDLE | 1.88 | 7.44 | 0.12 | 0.14 | 660298.73 | 9.69 | no_map |
| HBARUSDT | IDLE | 2.16 | 4.73 | 0.05 | 0.08 | 876357.9 | 1.26 | empty_tvl |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.16 | 9.31 | 0.08 | 0.15 | 508259.18 | 28.26 | n/a |
| WUSDT | IDLE | 2.65 | 6.69 | 0.08 | 0.09 | 371969.01 | 13.17 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.53 | 4.54 | 2.2 | 0.05 | 541734.19 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.83 | 0.03 | 187760.29 | 6.21 | n/a |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.84 | 0.19 | 157352.83 | 10.47 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.33 | -0.03 | 82593.53 | 21.86 | no_map |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10244.46 | 16.16 | no_map |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.05 | 186797.23 | 20.7 | no_map |
| QAITUSDT | IDLE | 2.31 | 4.38 | 1.63 | -0.01 | 3896.16 | 63.29 | no_map |
| KITEUSDT | IDLE | 1.21 | 3.58 | 1.01 | 0.11 | 61311.51 | 9.21 | no_map |
| QNTUSDT | IDLE | 2.35 | 4.7 | 0.02 | 0.07 | 88346.72 | 1.51 | n/a |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 1.94 | 0.06 | 56407.96 | 46.99 | no_map |
| RWAUSDT | IDLE | 0.92 | 1.83 | 0.0 | 0.04 | 54085.39 | 16.37 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 7.73 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
