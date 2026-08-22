# Hulk DIGEST — 2026-08-22T04:36:45Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 13.61 | 0.31 | 0.2 | 11396524.19 | 1.83 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 15.08 | 0.37 | 0.25 | 172006100.91 | 11.03 | n/a |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.51 | 0.2 | 734493.6 | 9.04 | no_map |
| HBARUSDT | IDLE | 2.3 | 7.63 | 0.02 | 0.13 | 1035673.84 | 1.18 | empty_tvl |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.29 | 0.01 | 451023.25 | 11.99 | no_map |
| WUSDT | IDLE | 1.99 | 7.53 | 0.13 | 0.15 | 435008.18 | 13.49 | tvl≈1,672,612,247 |
| BIOUSDT | IDLE | 2.96 | 7.36 | 1.49 | 0.07 | 200607.52 | 5.96 | n/a |
| ZBCNUSDT | IDLE | 1.47 | 4.29 | 2.12 | 0.11 | 537574.38 | 101.6 | n/a |
| EDELUSDT | IDLE | 2.03 | 4.07 | 2.82 | -0.03 | 80261.61 | 11.18 | no_map |
| QNTUSDT | IDLE | 2.44 | 8.56 | 4.39 | 0.1 | 181987.31 | 7.38 | n/a |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.04 | 0.09 | 58561.4 | 44.52 | no_map |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.48 | 0.21 | 158348.83 | 8.75 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.37 | 0.13 | 68037.58 | 11.49 | no_map |
| RWAINCUSDT | IDLE | 2.04 | 3.6 | 3.16 | -0.0 | 9331.56 | 43.55 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| TELUSDT | IDLE | 1.62 | 3.91 | 0.1 | 0.09 | 177284.1 | 65.28 | no_map |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.16 | 0.06 | 56498.11 | 16.05 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 23.6 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
