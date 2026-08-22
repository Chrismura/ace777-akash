# Hulk DIGEST — 2026-08-22T04:40:38Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 13.81 | 0.15 | 0.21 | 11595940.38 | 1.82 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.34 | 15.72 | 0.5 | 0.25 | 173695110.73 | 6.1 | n/a |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 8.8 | 0.09 | 0.14 | 1041520.1 | 5.85 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.61 | 0.19 | 736750.53 | 9.05 | no_map |
| CHIPUSDT | IDLE | 2.83 | 5.36 | 1.97 | 0.0 | 451340.57 | 6.0 | no_map |
| WUSDT | IDLE | 1.99 | 7.53 | 0.02 | 0.15 | 435123.67 | 10.61 | tvl≈1,672,612,247 |
| BIOUSDT | IDLE | 2.95 | 7.36 | 1.32 | 0.07 | 200780.86 | 2.97 | n/a |
| ZBCNUSDT | IDLE | 1.44 | 4.29 | 1.37 | 0.12 | 537676.38 | 45.1 | n/a |
| EDELUSDT | IDLE | 2.03 | 4.07 | 2.82 | -0.03 | 80286.63 | 11.17 | no_map |
| QNTUSDT | IDLE | 2.44 | 8.56 | 4.32 | 0.1 | 181813.41 | 8.84 | n/a |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.01 | 0.09 | 58561.14 | 44.52 | no_map |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.68 | 0.2 | 158273.28 | 11.17 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.29 | 0.13 | 68013.44 | 11.51 | no_map |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.0 | 9357.09 | 81.46 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| TELUSDT | IDLE | 1.73 | 4.48 | 0.0 | 0.09 | 177053.09 | 24.93 | no_map |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.16 | 0.06 | 56519.72 | 16.04 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 23.55 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
