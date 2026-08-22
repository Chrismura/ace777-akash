# Hulk DIGEST — 2026-08-22T04:51:24Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 15.45 | 1.18 | 0.2 | 12350711.73 | 12.69 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.38 | 16.63 | 0.42 | 0.26 | 178109112.68 | 0.61 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.46 | 9.11 | 0.22 | 0.14 | 1076761.32 | 1.17 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.25 | 0.2 | 737805.59 | 7.37 | skipped_fast |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.35 | 0.02 | 453624.28 | 2.98 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 8.62 | 0.65 | 0.15 | 436260.43 | 9.59 | skipped_fast |
| BIOUSDT | IDLE | 2.92 | 7.36 | 0.85 | 0.06 | 200075.41 | 2.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 4.29 | 0.86 | 0.11 | 537960.4 | 19.95 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 8.56 | 4.1 | 0.1 | 182354.64 | 7.36 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.54 | 0.1 | 58594.34 | 46.02 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.07 | 2.39 | -0.03 | 80195.52 | 44.4 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.05 | 0.21 | 158145.03 | 18.27 | skipped_fast |
| KITEUSDT | IDLE | 1.63 | 5.84 | 0.07 | 0.14 | 67935.11 | 14.05 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.54 | 0.1 | 182660.6 | 24.82 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.01 | 9540.48 | 103.06 | skipped_fast |
| RWAUSDT | IDLE | 1.58 | 3.13 | 0.16 | 0.07 | 56546.32 | 8.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
