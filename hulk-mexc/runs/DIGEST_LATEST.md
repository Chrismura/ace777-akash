# Hulk DIGEST — 2026-08-21T10:24:34Z

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
| PYTHUSDT | IDLE | 2.44 | 10.03 | 4.53 | 0.09 | 3083963.91 | 2.06 | tvl≈108,595,989 |
| XRPUSDT | IDLE | 1.83 | 10.26 | 3.64 | 0.19 | 145799665.73 | 4.35 | n/a |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 17.05 | 6.98 | -0.01 | 43308.21 | 46.66 | no_map |
| CCUSDT | IDLE | 2.02 | 3.79 | 1.65 | -0.0 | 506690.77 | 8.71 | no_map |
| REDUSDT | IDLE | 3.17 | 6.34 | 2.17 | -0.05 | 109834.98 | 12.13 | tvl≈1,952,575 |
| BIOUSDT | IDLE | 2.7 | 6.19 | 2.87 | -0.01 | 176468.91 | 3.11 | n/a |
| WUSDT | IDLE | 2.18 | 4.67 | 1.13 | 0.06 | 309037.41 | 11.78 | tvl≈1,571,708,920 |
| ZBCNUSDT | IDLE | 1.51 | 7.13 | 1.28 | 0.08 | 413431.15 | 18.96 | n/a |
| CHIPUSDT | IDLE | 0.95 | 4.67 | 1.92 | 0.19 | 496298.41 | 3.01 | no_map |
| HBARUSDT | IDLE | 1.79 | 3.41 | 1.18 | 0.05 | 639599.67 | 1.31 | empty_tvl |
| EDELUSDT | IDLE | 2.62 | 4.74 | 3.37 | 0.02 | 82369.55 | 21.83 | no_map |
| KITEUSDT | IDLE | 2.5 | 6.07 | 0.48 | 0.09 | 62596.54 | 3.81 | no_map |
| TELUSDT | IDLE | 1.86 | 9.14 | 2.21 | 0.17 | 221094.67 | 41.03 | no_map |
| QAITUSDT | IDLE | 1.67 | 3.19 | 1.04 | -0.01 | 3944.27 | 62.72 | no_map |
| QNTUSDT | IDLE | 2.04 | 4.04 | 0.27 | 0.03 | 63962.26 | 10.94 | n/a |
| FLUIDUSDT | IDLE | 2.31 | 4.71 | 0.58 | 0.08 | 3862.27 | 21.25 | tvl≈2,550,334,542 |
| RWAINCUSDT | IDLE | 0.98 | 1.82 | 0.87 | 0.03 | 8611.27 | 27.33 | no_map |
| RWAUSDT | IDLE | 1.73 | 3.42 | 0.33 | 0.04 | 55611.43 | 16.56 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
