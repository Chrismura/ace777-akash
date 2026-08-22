# Hulk DIGEST — 2026-08-22T03:26:59Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 11.15 | 0.39 | 0.18 | 7758321.22 | 1.87 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.47 | 14.16 | 1.23 | 0.21 | 163931229.2 | 1.27 | n/a |
| HBARUSDT | IDLE | 2.3 | 6.29 | 0.04 | 0.11 | 1017318.96 | 4.82 | empty_tvl |
| CCUSDT | IDLE | 1.99 | 8.96 | 1.96 | 0.17 | 681591.38 | 2.56 | no_map |
| BIOUSDT | IDLE | 2.99 | 7.36 | 1.99 | 0.08 | 198097.06 | 5.98 | n/a |
| CHIPUSDT | IDLE | 2.0 | 4.43 | 0.36 | -0.01 | 452690.16 | 8.94 | no_map |
| ZBCNUSDT | IDLE | 1.42 | 5.16 | 1.59 | 0.13 | 538589.53 | 6.21 | n/a |
| WUSDT | IDLE | 1.79 | 5.79 | 0.04 | 0.13 | 422699.25 | 13.75 | tvl≈1,672,612,247 |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.42 | 0.1 | 59538.5 | 15.28 | no_map |
| EDELUSDT | IDLE | 2.05 | 3.95 | 3.8 | -0.04 | 79996.0 | 22.47 | no_map |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.22 | 0.22 | 157918.18 | 17.28 | tvl≈2,314,909 |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9338.84 | 21.62 | no_map |
| KITEUSDT | IDLE | 1.38 | 4.4 | 0.15 | 0.12 | 67709.4 | 13.36 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.76 | 4.26 | 0.09 | 0.1 | 174205.65 | 11.86 | n/a |
| RWAUSDT | IDLE | 1.29 | 2.56 | 0.16 | 0.05 | 56239.9 | 8.06 | no_map |
| TELUSDT | IDLE | 0.92 | 2.19 | 0.46 | 0.07 | 173228.95 | 46.12 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.26 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
