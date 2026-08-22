# Hulk DIGEST — 2026-08-22T04:03:42Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.77 | 11.77 | 0.65 | 0.18 | 9541083.96 | 11.18 | tvl≈112,886,663 |
| XRPUSDT | IDLE | 2.17 | 12.22 | 2.43 | 0.19 | 166404935.6 | 1.92 | n/a |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.02 | 10.49 | 0.16 | 0.21 | 710804.46 | 7.36 | no_map |
| HBARUSDT | IDLE | 2.13 | 6.03 | 0.93 | 0.1 | 1013560.72 | 3.63 | empty_tvl |
| CHIPUSDT | IDLE | 2.89 | 5.36 | 2.82 | -0.04 | 458910.61 | 12.11 | no_map |
| WUSDT | IDLE | 2.0 | 7.18 | 1.39 | 0.13 | 428407.3 | 8.81 | tvl≈1,672,612,247 |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.26 | 0.07 | 199514.62 | 15.08 | n/a |
| ZBCNUSDT | IDLE | 1.46 | 4.29 | 1.8 | 0.13 | 537504.51 | 18.65 | n/a |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.04 | 80602.41 | 22.47 | no_map |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.25 | 0.09 | 59272.39 | 44.52 | no_map |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.69 | 0.22 | 157753.73 | 16.58 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.45 | 0.13 | 67519.31 | 8.86 | no_map |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.56 | 3.8 | 0.86 | 0.09 | 178537.52 | 8.92 | n/a |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56385.06 | 16.04 | no_map |
| TELUSDT | IDLE | 1.02 | 2.4 | 0.46 | 0.07 | 174316.78 | 20.45 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.66 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
