# Hulk DIGEST — 2026-08-21T22:15:33Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.14 | 0.11 | 5722251.64 | 2.04 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.53 | 5.44 | 0.77 | 0.13 | 131610142.42 | 2.81 | n/a |
| CCUSDT | IDLE | 1.75 | 6.45 | 0.02 | 0.14 | 644325.37 | 8.9 | no_map |
| HBARUSDT | IDLE | 2.2 | 4.71 | 0.6 | 0.08 | 849279.31 | 1.26 | empty_tvl |
| WUSDT | IDLE | 2.45 | 5.3 | 0.1 | 0.08 | 368762.5 | 10.27 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.47 | 4.54 | 1.05 | 0.06 | 534610.61 | 6.09 | no_map |
| ZBCNUSDT | IDLE | 1.51 | 6.5 | 0.08 | 0.11 | 498614.7 | 21.15 | n/a |
| BIOUSDT | IDLE | 2.25 | 5.04 | 0.46 | 0.02 | 187650.18 | 6.18 | n/a |
| REDUSDT | IDLE | 1.32 | 11.01 | 8.01 | 0.19 | 155815.42 | 19.43 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 1.92 | 4.24 | 0.0 | -0.03 | 82338.18 | 33.02 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | no_map |
| TELUSDT | IDLE | 2.52 | 6.45 | 0.62 | 0.06 | 186820.33 | 36.15 | no_map |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.75 | 0.11 | 61385.86 | 10.11 | no_map |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10212.63 | 107.35 | no_map |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.72 | 0.06 | 56365.82 | 45.14 | no_map |
| QNTUSDT | IDLE | 1.54 | 3.09 | 0.0 | 0.05 | 65348.15 | 3.06 | n/a |
| RWAUSDT | IDLE | 0.92 | 1.75 | 0.57 | 0.04 | 54149.96 | 16.45 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.71 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
