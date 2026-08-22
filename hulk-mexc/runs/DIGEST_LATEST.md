# Hulk DIGEST — 2026-08-22T04:50:11Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 15.45 | 1.18 | 0.21 | 12176566.79 | 29.0 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 16.63 | 0.68 | 0.26 | 177693191.58 | 1.21 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.46 | 9.11 | 0.19 | 0.14 | 1075506.09 | 1.17 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.11 | 0.2 | 737534.82 | 9.01 | skipped_fast |
| CHIPUSDT | IDLE | 2.78 | 5.36 | 1.29 | 0.01 | 451068.26 | 2.98 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 8.62 | 0.52 | 0.16 | 435375.13 | 20.08 | skipped_fast |
| BIOUSDT | IDLE | 2.93 | 7.36 | 0.94 | 0.06 | 200249.55 | 5.91 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 4.29 | 1.15 | 0.11 | 537878.34 | 25.58 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 8.56 | 4.15 | 0.1 | 182301.52 | 4.41 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.07 | 2.28 | -0.02 | 80170.53 | 22.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.54 | 0.1 | 58590.58 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.63 | 0.2 | 157870.2 | 19.14 | skipped_fast |
| KITEUSDT | IDLE | 1.63 | 5.84 | 0.1 | 0.14 | 67892.77 | 9.68 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.59 | 0.1 | 182684.43 | 24.82 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.01 | 9540.48 | 103.06 | skipped_fast |
| RWAUSDT | IDLE | 1.53 | 3.05 | 0.08 | 0.06 | 56637.56 | 16.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
