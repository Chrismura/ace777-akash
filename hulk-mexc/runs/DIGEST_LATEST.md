# Hulk DIGEST — 2026-08-22T01:43:25Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 10.86 | 0.73 | 0.16 | 6813481.21 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 9.48 | 0.13 | 0.16 | 151561099.23 | 2.01 | skipped_fast |
| HBARUSDT | IDLE | 3.0 | 6.36 | 0.54 | 0.08 | 959717.19 | 2.49 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.82 | 0.09 | 549686.14 | 18.88 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 7.36 | 0.21 | 0.16 | 663714.24 | 7.86 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.3 | 0.09 | 390750.53 | 17.23 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.19 | 0.02 | 512092.84 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.57 | 0.15 | 0.05 | 186865.72 | 6.11 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79541.14 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.8 | 0.11 | 60906.2 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.86 | 0.17 | 158290.07 | 11.2 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.17 | 0.38 | 0.13 | 61625.97 | 9.87 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 5.18 | 1.24 | 0.07 | 171642.08 | 9.07 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 6.19 | 1.53 | 0.05 | 182238.27 | 41.58 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9242.23 | 85.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.98 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54634.98 | 16.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
