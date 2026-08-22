# Hulk DIGEST — 2026-08-22T04:06:05Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.78 | 12.16 | 0.13 | 0.19 | 9782853.21 | 5.54 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.16 | 12.22 | 1.92 | 0.18 | 166621660.28 | 3.19 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 10.63 | 0.49 | 0.2 | 713806.61 | 13.12 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 6.03 | 0.56 | 0.1 | 1011316.46 | 1.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.91 | 5.36 | 3.0 | -0.02 | 457523.23 | 6.07 | skipped_fast |
| BIOUSDT | IDLE | 3.05 | 7.36 | 3.05 | 0.06 | 199579.91 | 12.08 | skipped_fast |
| WUSDT | IDLE | 1.98 | 7.18 | 1.02 | 0.13 | 428637.68 | 13.65 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 4.29 | 1.74 | 0.13 | 537132.66 | 18.62 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.04 | 80481.03 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.04 | 0.1 | 59143.69 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.86 | 0.21 | 157779.73 | 22.15 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.38 | 0.13 | 67560.15 | 12.38 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 3.8 | 0.77 | 0.09 | 178576.85 | 10.41 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56318.26 | 8.02 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.4 | 0.41 | 0.07 | 174290.63 | 15.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
