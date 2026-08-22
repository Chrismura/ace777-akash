# Hulk DIGEST — 2026-08-22T00:41:01Z

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
| PYTHUSDT | IDLE | 1.9 | 7.1 | 0.06 | 0.13 | 6444797.53 | 8.02 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.09 | 8.72 | 1.95 | 0.15 | 146506930.0 | 1.38 | skipped_fast |
| HBARUSDT | IDLE | 2.79 | 6.36 | 1.49 | 0.08 | 939647.48 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.75 | 0.12 | 543805.22 | 11.13 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 7.42 | 0.87 | 0.15 | 640376.82 | 7.1 | skipped_fast |
| WUSDT | IDLE | 2.7 | 6.91 | 0.44 | 0.09 | 388096.43 | 12.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 3.56 | 0.55 | 0.03 | 553221.0 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 5.36 | 0.18 | 0.03 | 186089.09 | 3.06 | skipped_fast |
| EDELUSDT | IDLE | 2.56 | 5.5 | 1.09 | -0.01 | 79897.68 | 21.93 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 9.82 | 3.32 | 0.12 | 59995.73 | 45.4 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.56 | 0.06 | 186306.26 | 36.04 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.34 | 0.06 | 170518.95 | 1.51 | skipped_fast |
| REDUSDT | IDLE | 0.74 | 6.54 | 1.61 | 0.23 | 158088.0 | 17.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.04 | 9787.93 | 48.56 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.17 | 0.1 | 61151.25 | 11.93 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54731.82 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
