# Hulk DIGEST — 2026-08-21T22:23:13Z

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
| PYTHUSDT | IDLE | 1.37 | 5.17 | 0.41 | 0.11 | 5757437.73 | 2.05 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.58 | 5.68 | 0.91 | 0.13 | 133313314.45 | 2.8 | n/a |
| CCUSDT | IDLE | 1.77 | 6.48 | 0.49 | 0.13 | 647593.72 | 8.93 | no_map |
| HBARUSDT | IDLE | 2.21 | 4.71 | 0.69 | 0.08 | 855725.63 | 3.8 | empty_tvl |
| WUSDT | IDLE | 2.47 | 5.3 | 0.35 | 0.08 | 371110.69 | 13.35 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.48 | 4.54 | 1.18 | 0.06 | 534485.25 | 6.09 | no_map |
| ZBCNUSDT | IDLE | 1.52 | 6.5 | 0.34 | 0.11 | 501217.58 | 38.95 | n/a |
| BIOUSDT | IDLE | 2.25 | 5.04 | 0.52 | 0.03 | 187947.26 | 3.09 | n/a |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.98 | 0.18 | 156218.59 | 17.82 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 2.02 | 4.47 | 0.0 | -0.03 | 82648.76 | 10.97 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | no_map |
| TELUSDT | IDLE | 2.51 | 6.45 | 0.56 | 0.06 | 186844.39 | 25.85 | no_map |
| KITEUSDT | IDLE | 1.21 | 3.58 | 0.98 | 0.11 | 61248.49 | 11.98 | no_map |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 86.25 | no_map |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.74 | 0.06 | 56377.75 | 45.14 | no_map |
| QNTUSDT | IDLE | 1.8 | 3.58 | 0.15 | 0.05 | 65382.52 | 12.2 | n/a |
| RWAUSDT | IDLE | 0.91 | 1.75 | 0.49 | 0.04 | 54112.45 | 24.66 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 2.11 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
