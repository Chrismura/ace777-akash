# Hulk DIGEST — 2026-09-22T08:09:42Z

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
| XRPUSDT | IDLE | 1.11 | 2.2 | 0.15 | 0.05 | 118910662.28 | 1.31 | n/a |
| ETHUSDT | IDLE | 0.54 | 1.01 | 0.43 | 0.02 | 707250283.77 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.39 | 0.74 | 0.3 | 0.04 | 1160510945.86 | 0.0 | no_map |
| HBARUSDT | IDLE | 2.29 | 5.08 | 0.06 | 0.09 | 1324874.82 | 3.13 | empty_tvl |
| PYTHUSDT | IDLE | 2.32 | 4.22 | 2.77 | 0.03 | 856690.79 | 1.58 | tvl≈144,376,589 |
| CCUSDT | IDLE | 1.48 | 2.92 | 0.26 | 0.06 | 667729.74 | 5.86 | no_map |
| WUSDT | IDLE | 1.58 | 2.97 | 1.3 | -0.0 | 449139.5 | 5.93 | tvl≈1,772,571,352 |
| KITEUSDT | IDLE | 3.09 | 6.12 | 0.39 | 0.08 | 82327.35 | 17.45 | no_map |
| ZBCNUSDT | IDLE | 1.7 | 3.17 | 1.58 | 0.03 | 274963.69 | 39.46 | n/a |
| CHIPUSDT | IDLE | 1.72 | 5.15 | 0.16 | 0.09 | 180506.8 | 10.32 | no_map |
| EDELUSDT | IDLE | 1.18 | 6.79 | 2.43 | 0.1 | 232947.66 | 9.43 | no_map |
| REDUSDT | IDLE | 1.93 | 3.83 | 0.18 | 0.05 | 97704.93 | 20.79 | tvl≈2,814,179 |
| BIOUSDT | IDLE | 1.39 | 2.56 | 1.51 | 0.02 | 130269.11 | 3.47 | n/a |
| RIZEUSDT | IDLE | 1.55 | 15.97 | 1.19 | -0.15 | 50882.83 | 125.0 | no_map |
| RWAINCUSDT | IDLE | 0.76 | 1.79 | 1.16 | 0.07 | 25416.35 | 5.59 | no_map |
| TELUSDT | IDLE | 1.76 | 3.15 | 2.44 | 0.06 | 118693.31 | 62.31 | no_map |
| QNTUSDT | IDLE | 1.29 | 2.46 | 0.74 | 0.02 | 126155.09 | 7.4 | n/a |
| RWAUSDT | IDLE | 0.57 | 1.02 | 0.8 | 0.0 | 57018.24 | 21.89 | no_map |
| FLUIDUSDT | IDLE | 0.43 | 0.87 | 0.0 | 0.07 | 12475.48 | 15.58 | tvl≈2,655,911,203 |
| MNSRYUSDT | IDLE | 0.2 | 0.36 | 0.21 | 0.02 | 41736.01 | 16.78 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
