# Hulk DIGEST — 2026-10-13T22:09:35Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 1.63 | 11.08 | 3.01 | -0.12 | 4683849.03 | 7.55 | tvl≈1,685,529,027 |
| PYTHUSDT | IDLE | 1.12 | 3.46 | 2.95 | -0.07 | 2218639.71 | 2.56 | tvl≈175,284,878 |
| QNTUSDT | IDLE | 2.93 | 10.52 | 3.85 | -0.06 | 1687666.48 | 2.34 | n/a |
| XRPUSDT | IDLE | 0.57 | 1.06 | 0.59 | 0.01 | 36058994.29 | 2.19 | n/a |
| ETHUSDT | IDLE | 0.38 | 0.74 | 0.12 | 0.01 | 229595588.19 | 0.12 | no_map |
| BTCUSDT | IDLE | 0.34 | 0.67 | 0.12 | 0.01 | 391555314.69 | 0.0 | no_map |
| CCUSDT | IDLE | 1.15 | 3.33 | 2.92 | 0.04 | 617342.79 | 7.12 | no_map |
| RWAINCUSDT | IDLE | 2.67 | 4.82 | 3.51 | 0.0 | 31814.59 | 14.76 | no_map |
| EDELUSDT | IDLE | 1.21 | 2.48 | 1.44 | 0.01 | 235871.2 | 8.75 | no_map |
| ZBCNUSDT | IDLE | 1.25 | 2.23 | 1.79 | -0.02 | 218161.31 | 29.13 | n/a |
| REDUSDT | IDLE | 1.14 | 2.37 | 0.74 | 0.0 | 132129.6 | 16.09 | tvl≈3,913,224 |
| CHIPUSDT | IDLE | 1.16 | 2.56 | 1.5 | -0.03 | 103279.56 | 12.24 | no_map |
| RIZEUSDT | IDLE | 1.59 | 5.26 | 2.33 | -0.01 | 49801.59 | 61.51 | no_map |
| BIOUSDT | IDLE | 0.98 | 2.16 | 0.43 | -0.01 | 75207.86 | 10.82 | n/a |
| TELUSDT | IDLE | 1.95 | 3.74 | 1.0 | 0.02 | 118523.27 | 27.99 | no_map |
| KITEUSDT | IDLE | 0.75 | 1.64 | 0.17 | 0.01 | 59945.29 | 12.48 | no_map |
| HBARUSDT | IDLE | 0.69 | 1.28 | 0.71 | -0.01 | 298115.96 | 4.57 | empty_tvl |
| FLUIDUSDT | IDLE | 1.32 | 2.98 | 0.0 | 0.05 | 23036.44 | 21.19 | tvl≈2,376,887,759 |
| RWAUSDT | IDLE | 0.21 | 0.39 | 0.15 | -0.0 | 52693.72 | 15.47 | no_map |
| MNSRYUSDT | IDLE | 0.23 | 0.42 | 0.21 | -0.02 | 37800.46 | 34.93 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
