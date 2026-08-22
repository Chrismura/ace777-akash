# Hulk DIGEST — 2026-08-22T01:53:20Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.89 | 10.86 | 1.37 | 0.14 | 6840853.24 | 1.96 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 10.52 | 1.89 | 0.15 | 153358075.36 | 6.07 | skipped_fast |
| HBARUSDT | IDLE | 3.04 | 6.36 | 1.23 | 0.07 | 952191.63 | 5.02 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.77 | 0.08 | 552931.0 | 15.01 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 7.36 | 0.45 | 0.16 | 661311.29 | 7.88 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.28 | 0.08 | 391382.6 | 11.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.82 | 0.02 | 512126.61 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.61 | 5.86 | 0.43 | 0.05 | 185102.58 | 6.09 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79521.12 | 22.15 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.81 | 0.16 | 157167.74 | 0.81 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.97 | 0.11 | 61021.35 | 45.71 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.17 | 0.38 | 0.12 | 61338.62 | 13.46 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 5.18 | 1.18 | 0.06 | 171684.59 | 6.05 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 6.19 | 1.18 | 0.05 | 181471.01 | 57.07 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9181.85 | 74.83 | skipped_fast |
| FLUIDUSDT | IDLE | 1.46 | 3.74 | 2.03 | 0.08 | 4799.07 | 41.8 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54595.66 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
