# Hulk DIGEST — 2026-08-22T01:41:26Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 10.86 | 0.81 | 0.16 | 6806287.61 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 9.48 | 0.25 | 0.16 | 151508619.3 | 3.35 | skipped_fast |
| HBARUSDT | IDLE | 2.98 | 6.36 | 0.31 | 0.08 | 959437.55 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.8 | 0.09 | 550384.32 | 14.04 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 7.36 | 0.3 | 0.16 | 663197.88 | 6.99 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.41 | 0.09 | 392784.74 | 11.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.82 | 0.02 | 511479.45 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.5 | 5.57 | 0.73 | 0.04 | 186418.38 | 6.14 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79516.13 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.13 | 0.11 | 60849.54 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.96 | 0.16 | 158594.67 | 11.2 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.17 | 0.41 | 0.13 | 61691.38 | 8.96 | skipped_fast |
| TELUSDT | IDLE | 2.63 | 6.19 | 1.79 | 0.05 | 182138.82 | 36.37 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.79 | 0.07 | 170726.43 | 7.52 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.48 | 0.03 | 9209.71 | 26.85 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 19.83 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54654.29 | 16.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
