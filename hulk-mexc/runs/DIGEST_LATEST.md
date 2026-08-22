# Hulk DIGEST — 2026-08-22T00:42:47Z

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
| PYTHUSDT | IDLE | 1.9 | 7.1 | 0.04 | 0.13 | 6451499.24 | 2.0 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 2.11 | 8.72 | 2.38 | 0.14 | 147028777.83 | 4.84 | n/a |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.82 | 0.07 | 940212.31 | 2.52 | empty_tvl |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.73 | 0.12 | 544259.28 | 5.8 | n/a |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.4 | 0.14 | 640483.89 | 8.03 | no_map |
| WUSDT | IDLE | 2.71 | 6.91 | 0.54 | 0.09 | 387986.32 | 10.16 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.79 | 0.03 | 552973.55 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.5 | 5.62 | 0.34 | 0.03 | 186320.45 | 3.07 | n/a |
| EDELUSDT | IDLE | 2.55 | 5.5 | 0.87 | -0.01 | 79922.68 | 21.93 | no_map |
| RIZEUSDT | IDLE | 2.2 | 9.82 | 2.29 | 0.13 | 60071.31 | 43.33 | no_map |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | no_map |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.61 | 0.06 | 186400.38 | 30.9 | no_map |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.54 | 0.06 | 170547.75 | 4.55 | n/a |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.03 | 9787.93 | 21.55 | no_map |
| REDUSDT | IDLE | 0.73 | 6.54 | 1.23 | 0.24 | 158129.68 | 53.38 | tvl≈2,226,572 |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.09 | 0.1 | 61159.63 | 11.01 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 54764.88 | 8.21 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.73 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
