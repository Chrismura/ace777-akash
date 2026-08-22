# Hulk DIGEST — 2026-08-22T04:15:39Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 13.13 | 0.2 | 0.2 | 10395375.68 | 1.83 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 12.22 | 1.11 | 0.21 | 167552686.06 | 3.16 | n/a |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 11.56 | 0.71 | 0.22 | 724060.85 | 6.52 | no_map |
| HBARUSDT | IDLE | 2.13 | 6.36 | 0.0 | 0.11 | 1005339.49 | 1.19 | empty_tvl |
| CHIPUSDT | IDLE | 2.86 | 5.36 | 2.35 | 0.0 | 448971.08 | 3.02 | no_map |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.26 | 0.07 | 199878.51 | 6.0 | n/a |
| WUSDT | IDLE | 1.96 | 7.18 | 0.51 | 0.14 | 429532.92 | 11.66 | tvl≈1,672,612,247 |
| ZBCNUSDT | IDLE | 1.43 | 4.29 | 1.17 | 0.12 | 535347.7 | 23.25 | n/a |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.58 | -0.05 | 80307.11 | 22.5 | no_map |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.98 | 0.1 | 59145.61 | 44.52 | no_map |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.4 | 0.2 | 160312.16 | 22.25 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.46 | 0.13 | 67599.72 | 13.31 | no_map |
| RWAINCUSDT | IDLE | 2.01 | 3.6 | 2.74 | 0.01 | 9442.75 | 59.44 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | no_map |
| QNTUSDT | IDLE | 1.53 | 3.8 | 0.41 | 0.09 | 178512.28 | 4.44 | n/a |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.4 | 0.06 | 56302.18 | 8.02 | no_map |
| TELUSDT | IDLE | 1.02 | 2.4 | 0.51 | 0.07 | 173862.11 | 35.81 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 51.5 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
