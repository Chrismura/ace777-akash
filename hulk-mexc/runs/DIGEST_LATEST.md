# Hulk DIGEST — 2026-08-21T23:47:44Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.61 | 0.1 | 6181107.17 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.96 | 8.23 | 1.13 | 0.15 | 141782229.22 | 2.74 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 11.25 | 1.95 | 0.13 | 514178.49 | 13.44 | skipped_fast |
| HBARUSDT | IDLE | 2.61 | 6.36 | 0.97 | 0.09 | 906843.49 | 2.5 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.01 | 0.13 | 644499.41 | 8.89 | skipped_fast |
| WUSDT | IDLE | 2.78 | 6.91 | 1.95 | 0.08 | 378298.01 | 14.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.43 | 0.03 | 546923.86 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.05 | 0.02 | 186598.26 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | 0.0 | 80153.49 | 11.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.83 | 0.12 | 58832.82 | 46.13 | skipped_fast |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.36 | 0.07 | 190341.19 | 25.66 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.68 | 0.19 | 157865.51 | 17.83 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.04 | 0.08 | 148434.88 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10306.4 | 69.69 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 1.04 | 0.1 | 61337.31 | 11.1 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54552.15 | 8.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 21.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
