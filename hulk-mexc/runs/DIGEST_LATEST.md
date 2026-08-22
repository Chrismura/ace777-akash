# Hulk DIGEST — 2026-08-22T04:50:52Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 15.45 | 1.25 | 0.2 | 12292843.96 | 10.88 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.38 | 16.63 | 0.52 | 0.25 | 177975859.9 | 4.84 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.46 | 9.11 | 0.13 | 0.14 | 1077399.33 | 1.16 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.25 | 0.2 | 737772.65 | 9.83 | skipped_fast |
| CHIPUSDT | IDLE | 2.76 | 5.36 | 1.03 | 0.02 | 453624.28 | 2.98 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 8.62 | 0.41 | 0.16 | 435552.47 | 7.66 | skipped_fast |
| BIOUSDT | IDLE | 2.92 | 7.36 | 0.85 | 0.06 | 200049.81 | 2.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 4.29 | 0.88 | 0.11 | 537923.03 | 24.15 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 8.56 | 4.15 | 0.1 | 182354.64 | 2.94 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.54 | 0.1 | 58594.34 | 46.02 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.07 | 2.39 | -0.02 | 80170.56 | 44.4 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.73 | 0.2 | 157868.17 | 19.94 | skipped_fast |
| KITEUSDT | IDLE | 1.63 | 5.84 | 0.09 | 0.14 | 67877.31 | 9.68 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.54 | 0.1 | 182660.6 | 24.82 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.01 | 9540.48 | 103.06 | skipped_fast |
| RWAUSDT | IDLE | 1.52 | 3.05 | 0.0 | 0.07 | 56614.55 | 7.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 20.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
