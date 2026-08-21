# Hulk DIGEST — 2026-08-21T07:42:32Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.67 | 11.44 | 0.02 | 0.17 | 2657092.1 | 6.0 | skipped_fast |
| XRPUSDT | IDLE | 0.61 | 3.1 | 0.49 | 0.18 | 122875717.58 | 1.52 | skipped_fast |
| RIZEUSDT | IDLE | 3.6 | 18.43 | 2.12 | 0.04 | 44098.17 | 42.76 | skipped_fast |
| CCUSDT | IDLE | 2.09 | 4.04 | 0.99 | -0.0 | 494145.55 | 11.84 | skipped_fast |
| CHIPUSDT | IDLE | 1.36 | 7.93 | 4.27 | 0.16 | 478495.19 | 9.03 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 7.31 | 1.47 | 0.08 | 304055.65 | 23.71 | skipped_fast |
| BIOUSDT | IDLE | 2.13 | 6.36 | 0.0 | 0.05 | 222447.65 | 6.19 | skipped_fast |
| REDUSDT | IDLE | 1.98 | 6.07 | 1.32 | -0.06 | 118301.65 | 22.26 | skipped_fast |
| WUSDT | IDLE | 1.08 | 2.16 | 0.01 | 0.07 | 276128.29 | 8.71 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 3.61 | 1.58 | 0.02 | 75794.67 | 21.48 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.57 | 0.33 | 0.06 | 531452.73 | 2.66 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 2.8 | 0.04 | 0.06 | 60911.23 | 10.82 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 8.98 | 1.31 | 0.2 | 218013.27 | 30.77 | skipped_fast |
| QAITUSDT | IDLE | 1.17 | 2.95 | 0.78 | -0.03 | 5370.76 | 62.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.94 | 1.77 | 0.76 | 0.04 | 8572.64 | 60.46 | skipped_fast |
| QNTUSDT | IDLE | 0.94 | 1.87 | 0.13 | 0.06 | 72992.77 | 7.99 | skipped_fast |
| RWAUSDT | IDLE | 0.84 | 1.62 | 0.42 | 0.02 | 54857.51 | 16.86 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.71 | 0.32 | 0.07 | 2740.65 | 21.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
