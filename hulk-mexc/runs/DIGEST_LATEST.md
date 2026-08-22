# Hulk DIGEST — 2026-08-22T04:47:26Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.94 | 15.22 | 0.16 | 0.22 | 11985797.28 | 14.38 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.36 | 16.18 | 0.58 | 0.26 | 176578254.37 | 3.04 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 8.85 | 0.32 | 0.14 | 1072781.48 | 2.34 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.34 | 0.2 | 737230.87 | 10.67 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 5.36 | 1.41 | 0.01 | 450982.06 | 5.97 | skipped_fast |
| WUSDT | IDLE | 2.02 | 7.75 | 0.18 | 0.15 | 433861.47 | 5.77 | skipped_fast |
| BIOUSDT | IDLE | 2.95 | 7.36 | 1.26 | 0.06 | 201434.13 | 2.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 1.04 | 0.12 | 537942.24 | 44.09 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.55 | 0.09 | 58580.75 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.56 | 0.2 | 158126.89 | 8.75 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 4.07 | 2.17 | -0.02 | 80170.38 | 55.52 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.28 | 0.14 | 67998.08 | 11.49 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 8.56 | 4.46 | 0.1 | 182393.44 | 63.68 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.48 | 0.01 | 9348.0 | 65.22 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.59 | 0.1 | 182259.65 | 19.86 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.16 | 0.06 | 56616.19 | 16.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
