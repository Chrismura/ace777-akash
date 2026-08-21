# Hulk DIGEST — 2026-08-21T21:55:54Z

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
| PYTHUSDT | IDLE | 1.21 | 4.74 | 0.04 | 0.1 | 5679516.06 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 3.73 | 0.4 | 0.12 | 129951702.76 | 1.42 | skipped_fast |
| HBARUSDT | IDLE | 2.08 | 4.71 | 0.24 | 0.08 | 833869.32 | 1.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.86 | 5.61 | 3.34 | 0.05 | 526904.86 | 3.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 8.19 | 2.65 | 0.11 | 492108.46 | 18.38 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 3.89 | 0.05 | 0.11 | 635629.5 | 6.38 | skipped_fast |
| WUSDT | IDLE | 2.11 | 4.19 | 0.25 | 0.06 | 367580.5 | 14.54 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 5.2 | 1.14 | 0.04 | 186099.78 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.44 | 0.19 | 153759.28 | 18.65 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.01 | 10.4 | 0.62 | 0.05 | 56177.77 | 46.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.03 | 10221.48 | 10.66 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.18 | 0.04 | 191865.91 | 57.07 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 4.12 | 2.09 | -0.04 | 83609.24 | 89.49 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 1.07 | 0.11 | 61317.22 | 11.01 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.65 | 0.17 | 0.05 | 62561.58 | 3.08 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.17 | 0.0 | 0.04 | 54132.83 | 32.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
