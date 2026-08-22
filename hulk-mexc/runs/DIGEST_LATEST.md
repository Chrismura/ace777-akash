# Hulk DIGEST — 2026-08-22T04:22:22Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.88 | 13.61 | 0.6 | 0.2 | 10686422.35 | 3.66 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 12.22 | 0.73 | 0.21 | 168838146.01 | 3.78 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 11.56 | 0.76 | 0.21 | 728468.89 | 9.79 | skipped_fast |
| HBARUSDT | IDLE | 2.27 | 7.14 | 0.66 | 0.12 | 1019461.6 | 1.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.77 | 5.36 | 1.15 | 0.01 | 442647.3 | 5.96 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.26 | 0.08 | 199950.12 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.95 | 7.18 | 0.27 | 0.14 | 434402.69 | 9.68 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 4.29 | 1.35 | 0.11 | 535585.54 | 16.17 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 4.07 | 3.37 | -0.04 | 80150.46 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.06 | 0.1 | 59177.13 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.9 | 0.21 | 159774.68 | 10.39 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.53 | 0.13 | 67741.07 | 9.75 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.27 | 0.0 | 9427.75 | 70.63 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 3.8 | 0.43 | 0.09 | 178594.43 | 8.89 | skipped_fast |
| TELUSDT | IDLE | 1.33 | 3.12 | 0.71 | 0.08 | 175318.05 | 45.65 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.4 | 0.06 | 56290.99 | 16.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
