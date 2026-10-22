# Hulk DIGEST — 2026-10-22T13:13:15Z

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
| WUSDT | IDLE | 0.79 | 3.71 | 3.54 | -0.09 | 3166318.48 | 16.54 | tvl≈1,578,515,866 |
| XRPUSDT | IDLE | 0.89 | 1.56 | 1.49 | -0.03 | 32559052.97 | 1.52 | n/a |
| ETHUSDT | IDLE | 0.83 | 1.46 | 1.33 | -0.04 | 218510894.77 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.43 | 0.75 | 0.75 | -0.03 | 531511733.41 | 0.0 | no_map |
| HBARUSDT | IDLE | 0.79 | 1.44 | 0.97 | -0.06 | 1371969.02 | 8.68 | empty_tvl |
| EDELUSDT | IDLE | 2.96 | 5.26 | 4.59 | -0.05 | 546520.43 | 15.33 | no_map |
| QNTUSDT | IDLE | 0.87 | 2.08 | 1.59 | -0.02 | 1268228.12 | 1.03 | n/a |
| PYTHUSDT | IDLE | 0.84 | 2.34 | 1.21 | -0.07 | 635727.16 | 2.69 | tvl≈166,252,005 |
| ZBCNUSDT | IDLE | 2.27 | 6.18 | 2.8 | -0.06 | 224484.54 | 17.52 | n/a |
| CCUSDT | IDLE | 0.82 | 2.48 | 2.02 | -0.04 | 397475.09 | 7.77 | no_map |
| RWAINCUSDT | IDLE | 2.27 | 4.49 | 0.39 | 0.02 | 65135.59 | 11.07 | no_map |
| CHIPUSDT | IDLE | 0.86 | 3.43 | 3.1 | -0.05 | 338883.56 | 18.51 | no_map |
| RIZEUSDT | IDLE | 1.62 | 4.3 | 0.27 | 0.06 | 43700.98 | 55.6 | no_map |
| KITEUSDT | IDLE | 0.98 | 1.83 | 0.8 | -0.02 | 60135.13 | 10.84 | no_map |
| REDUSDT | IDLE | 0.86 | 1.72 | 0.87 | -0.03 | 85882.36 | 15.46 | tvl≈3,561,575 |
| BIOUSDT | IDLE | 0.66 | 1.39 | 0.83 | -0.05 | 77706.74 | 8.39 | n/a |
| WAXLUSDT | IDLE | 0.94 | 3.18 | 2.48 | -0.1 | 58808.52 | 24.8 | no_map |
| FLUIDUSDT | IDLE | 0.77 | 4.14 | 3.97 | -0.03 | 19552.58 | 18.06 | tvl≈2,216,960,780 |
| IOTAUSDT | IDLE | 0.7 | 1.34 | 1.19 | -0.06 | 79336.87 | 17.84 | no_map |
| LAUSDT | IDLE | 0.75 | 1.91 | 1.54 | -0.04 | 57808.73 | 25.43 | no_map |
| RWAUSDT | IDLE | 0.62 | 1.11 | 0.86 | -0.01 | 52843.75 | 31.65 | no_map |
| MNSRYUSDT | IDLE | 0.29 | 0.53 | 0.38 | -0.0 | 39891.26 | 55.51 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
