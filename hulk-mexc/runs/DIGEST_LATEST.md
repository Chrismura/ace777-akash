# Hulk DIGEST — 2026-10-27T19:15:02Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.95 | 1.8 | 0.61 | 0.01 | 224896555.33 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.88 | 1.7 | 0.37 | 0.02 | 19377862.28 | 0.76 | n/a |
| BTCUSDT | IDLE | 0.59 | 1.15 | 0.21 | 0.01 | 315715629.12 | 0.0 | no_map |
| WUSDT | IDLE | 2.27 | 5.0 | 3.48 | 0.05 | 677874.34 | 19.39 | tvl≈1,509,464,671 |
| QNTUSDT | IDLE | 1.33 | 2.55 | 0.72 | -0.02 | 750065.47 | 4.99 | n/a |
| EDELUSDT | IDLE | 1.27 | 2.23 | 2.03 | 0.01 | 477416.21 | 24.73 | no_map |
| PYTHUSDT | IDLE | 1.41 | 2.75 | 0.48 | -0.02 | 399249.11 | 4.1 | tvl≈161,834,127 |
| CHIPUSDT | IDLE | 2.49 | 5.97 | 1.06 | -0.01 | 141060.51 | 16.58 | no_map |
| BIOUSDT | IDLE | 1.87 | 3.69 | 0.35 | 0.02 | 58654.95 | 8.82 | n/a |
| ZBCNUSDT | IDLE | 1.09 | 3.1 | 1.26 | 0.03 | 256878.95 | 32.21 | n/a |
| REDUSDT | IDLE | 1.86 | 3.72 | 0.76 | 0.06 | 59976.51 | 15.5 | tvl≈3,849,615 |
| CCUSDT | IDLE | 1.04 | 1.9 | 1.14 | -0.01 | 224597.47 | 5.05 | no_map |
| KITEUSDT | IDLE | 1.59 | 2.85 | 2.77 | 0.03 | 57013.98 | 11.04 | no_map |
| RWAINCUSDT | IDLE | 1.63 | 4.65 | 0.0 | -0.08 | 63272.68 | 19.61 | no_map |
| LAUSDT | IDLE | 2.92 | 6.04 | 1.95 | 0.04 | 58657.92 | 16.54 | no_map |
| RIZEUSDT | IDLE | 1.72 | 3.34 | 0.65 | -0.0 | 46017.67 | 55.84 | no_map |
| HBARUSDT | IDLE | 0.91 | 1.75 | 0.48 | -0.01 | 239397.13 | 9.19 | empty_tvl |
| IOTAUSDT | IDLE | 1.07 | 2.01 | 0.82 | -0.01 | 77279.91 | 18.95 | no_map |
| WAXLUSDT | IDLE | 0.78 | 1.5 | 0.43 | 0.03 | 55260.9 | 38.65 | no_map |
| RWAUSDT | IDLE | 0.7 | 1.37 | 0.16 | -0.0 | 57298.35 | 39.89 | no_map |
| FLUIDUSDT | IDLE | 0.73 | 1.47 | 0.0 | 0.05 | 3238.71 | 21.71 | tvl≈2,204,282,622 |
| MNSRYUSDT | IDLE | 0.42 | 0.78 | 0.34 | 0.0 | 37401.04 | 79.41 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
