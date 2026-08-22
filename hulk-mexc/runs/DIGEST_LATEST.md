# Hulk DIGEST — 2026-08-22T02:00:07Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 10.86 | 0.64 | 0.14 | 6868895.49 | 1.94 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 10.52 | 1.99 | 0.14 | 153918675.98 | 2.7 | skipped_fast |
| HBARUSDT | IDLE | 3.02 | 6.36 | 0.88 | 0.07 | 950618.11 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.83 | 0.09 | 549577.52 | 14.52 | skipped_fast |
| CCUSDT | IDLE | 1.81 | 7.36 | 0.93 | 0.15 | 662244.85 | 7.9 | skipped_fast |
| WUSDT | IDLE | 2.66 | 6.7 | 0.0 | 0.09 | 399127.4 | 14.13 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.79 | 0.02 | 510482.44 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.58 | 5.86 | 0.0 | 0.06 | 184613.52 | 15.29 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79546.07 | 11.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.87 | 0.11 | 61079.73 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.19 | 0.16 | 156894.38 | 12.15 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.17 | 0.06 | 0.13 | 61248.54 | 13.46 | skipped_fast |
| TELUSDT | IDLE | 2.58 | 6.19 | 1.07 | 0.05 | 180977.14 | 36.2 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| QNTUSDT | IDLE | 2.31 | 4.89 | 1.24 | 0.07 | 171326.53 | 16.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.03 | 9181.85 | 69.8 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54598.48 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 41.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
