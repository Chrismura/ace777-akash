# Hulk DIGEST — 2026-08-22T04:49:26Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.96 | 15.45 | 0.5 | 0.21 | 12133157.02 | 9.0 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 16.63 | 0.64 | 0.26 | 177414410.34 | 6.67 | n/a |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 8.93 | 0.06 | 0.14 | 1074488.77 | 4.67 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.04 | 0.2 | 737985.86 | 6.54 | no_map |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.32 | 0.01 | 451073.78 | 2.98 | no_map |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.11 | 8.62 | 0.1 | 0.16 | 434930.2 | 21.96 | tvl≈1,672,612,247 |
| BIOUSDT | IDLE | 2.93 | 7.36 | 0.94 | 0.06 | 200943.09 | 5.92 | n/a |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 0.96 | 0.11 | 537840.99 | 28.89 | n/a |
| QNTUSDT | IDLE | 2.43 | 8.56 | 4.2 | 0.1 | 182329.63 | 7.36 | n/a |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.54 | 0.09 | 58577.66 | 46.02 | no_map |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.51 | 0.21 | 158087.73 | 17.53 | tvl≈2,314,909 |
| EDELUSDT | IDLE | 1.97 | 4.07 | 1.95 | -0.03 | 80170.47 | 44.35 | no_map |
| KITEUSDT | IDLE | 1.62 | 5.84 | 0.0 | 0.14 | 67909.95 | 11.45 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | no_map |
| TELUSDT | IDLE | 1.97 | 5.52 | 0.69 | 0.1 | 182717.89 | 14.9 | no_map |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.01 | 9540.48 | 103.06 | no_map |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.16 | 0.06 | 56623.28 | 16.0 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 23.51 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
