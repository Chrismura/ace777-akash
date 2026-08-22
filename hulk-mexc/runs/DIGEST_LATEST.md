# Hulk DIGEST — 2026-08-22T04:34:42Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 13.61 | 0.31 | 0.2 | 11298939.48 | 14.61 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.22 | 13.83 | 0.07 | 0.24 | 170990767.07 | 8.03 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.53 | 0.19 | 732742.91 | 9.06 | skipped_fast |
| HBARUSDT | IDLE | 2.25 | 7.14 | 0.3 | 0.12 | 1033991.18 | 1.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.74 | 5.36 | 0.79 | 0.02 | 449556.33 | 5.93 | skipped_fast |
| BIOUSDT | IDLE | 2.98 | 7.36 | 1.76 | 0.07 | 200433.13 | 2.98 | skipped_fast |
| WUSDT | IDLE | 1.96 | 7.29 | 0.05 | 0.14 | 435066.96 | 10.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 0.96 | 0.13 | 535309.38 | 25.06 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.47 | -0.04 | 79996.24 | 33.69 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 8.56 | 4.06 | 0.15 | 181886.22 | 10.34 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.04 | 0.09 | 58552.67 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.87 | 0.2 | 158350.55 | 17.53 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.52 | 0.13 | 67994.88 | 10.62 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.27 | -0.0 | 9264.44 | 48.95 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 3.39 | 0.15 | 0.09 | 176807.4 | 25.26 | skipped_fast |
| RWAUSDT | IDLE | 1.56 | 3.05 | 0.48 | 0.06 | 56359.05 | 8.03 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 20.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
