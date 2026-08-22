# Hulk DIGEST — 2026-08-22T04:51:54Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.97 | 15.45 | 0.79 | 0.2 | 12382517.49 | 16.25 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 16.94 | 0.12 | 0.27 | 178406800.15 | 5.41 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.46 | 9.11 | 0.17 | 0.14 | 1074149.67 | 4.66 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.2 | 0.2 | 737798.89 | 9.01 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 5.36 | 1.44 | 0.02 | 454108.72 | 8.97 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 8.62 | 0.71 | 0.15 | 436291.23 | 9.6 | skipped_fast |
| BIOUSDT | IDLE | 2.93 | 7.36 | 1.0 | 0.06 | 200540.75 | 5.93 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 1.08 | 0.11 | 537951.64 | 25.64 | skipped_fast |
| EDELUSDT | IDLE | 1.97 | 4.07 | 1.95 | -0.02 | 80219.99 | 11.08 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 8.56 | 4.1 | 0.1 | 182378.44 | 10.3 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.54 | 0.09 | 58589.98 | 37.4 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.05 | 0.21 | 158092.46 | 18.27 | skipped_fast |
| KITEUSDT | IDLE | 1.63 | 5.91 | 0.0 | 0.14 | 67922.56 | 14.05 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.01 | 9540.48 | 92.27 | skipped_fast |
| TELUSDT | IDLE | 1.98 | 5.52 | 0.89 | 0.1 | 183337.78 | 39.76 | skipped_fast |
| RWAUSDT | IDLE | 1.58 | 3.13 | 0.24 | 0.06 | 56574.2 | 32.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
