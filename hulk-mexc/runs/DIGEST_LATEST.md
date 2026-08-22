# Hulk DIGEST — 2026-08-22T01:47:40Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.88 | 10.86 | 1.01 | 0.15 | 6830616.34 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.32 | 9.99 | 0.12 | 0.17 | 152502415.08 | 6.66 | skipped_fast |
| HBARUSDT | IDLE | 2.99 | 6.36 | 0.42 | 0.08 | 960661.11 | 3.73 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.73 | 0.09 | 554995.59 | 0.48 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.02 | 0.17 | 661386.22 | 6.97 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.39 | 0.09 | 392299.96 | 11.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.19 | 0.02 | 512320.83 | 6.15 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.57 | 0.09 | 0.06 | 186315.22 | 6.09 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79491.15 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.0 | 0.11 | 60953.4 | 21.98 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.87 | 0.18 | 158105.77 | 16.79 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.17 | 0.13 | 0.13 | 61405.57 | 8.96 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 5.18 | 1.11 | 0.07 | 171667.33 | 4.53 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 6.19 | 1.59 | 0.04 | 182146.93 | 41.58 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9235.4 | 90.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 19.83 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54619.15 | 8.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
