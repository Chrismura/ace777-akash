# Hulk DIGEST — 2026-08-22T01:46:11Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 10.86 | 0.58 | 0.16 | 6825311.14 | 1.94 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 9.72 | 0.0 | 0.16 | 151984665.04 | 2.0 | skipped_fast |
| HBARUSDT | IDLE | 3.0 | 6.36 | 0.57 | 0.08 | 960616.01 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.73 | 0.08 | 550787.48 | 0.48 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.1 | 0.17 | 661466.74 | 7.85 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.31 | 0.09 | 391790.28 | 15.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.06 | 0.02 | 512418.46 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.57 | 0.12 | 0.05 | 186766.28 | 9.15 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79516.19 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.98 | 0.11 | 60939.99 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.84 | 0.18 | 158051.66 | 18.37 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.17 | 0.13 | 0.13 | 61450.93 | 8.96 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 6.19 | 1.59 | 0.05 | 182181.67 | 41.58 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 5.18 | 1.06 | 0.07 | 171705.51 | 10.57 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9235.4 | 90.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.26 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54673.66 | 24.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
