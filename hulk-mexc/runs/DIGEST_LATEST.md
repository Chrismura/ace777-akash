# Hulk DIGEST — 2026-09-25T12:44:13Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 2.91 | 7.27 | 0.96 | 0.1 | 98528352.97 | 1.86 | skipped_fast |
| ETHUSDT | IDLE | 1.49 | 2.83 | 1.05 | 0.03 | 384869590.97 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.97 | 1.79 | 0.97 | 0.01 | 726159850.15 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.07 | 7.16 | 0.59 | 0.14 | 1183993.16 | 4.16 | skipped_fast |
| HBARUSDT | IDLE | 2.92 | 5.65 | 1.25 | 0.06 | 1054540.36 | 1.05 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.38 | 1.67 | 0.15 | 674554.62 | 10.57 | skipped_fast |
| ZBCNUSDT | IDLE | 3.3 | 9.65 | 2.31 | 0.07 | 212251.61 | 34.88 | skipped_fast |
| RIZEUSDT | IDLE | 1.19 | 27.06 | 19.1 | 0.61 | 125419.39 | 23.39 | skipped_fast |
| WUSDT | IDLE | 2.38 | 4.71 | 0.31 | 0.07 | 352053.56 | 8.27 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 10.64 | 9.35 | 0.28 | 636075.19 | 9.49 | skipped_fast |
| KITEUSDT | IDLE | 2.86 | 5.66 | 0.4 | 0.01 | 72910.32 | 8.36 | skipped_fast |
| CHIPUSDT | IDLE | 1.86 | 9.28 | 3.06 | 0.17 | 114825.36 | 18.55 | skipped_fast |
| REDUSDT | IDLE | 1.97 | 5.52 | 0.72 | 0.1 | 136609.42 | 68.85 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 9.11 | 8.02 | 0.05 | 23848.74 | 86.49 | skipped_fast |
| BIOUSDT | IDLE | 1.54 | 4.07 | 0.09 | 0.11 | 93593.73 | 3.16 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 5.49 | 1.24 | -0.01 | 118596.85 | 47.96 | skipped_fast |
| EDELUSDT | IDLE | 0.39 | 4.31 | 2.08 | 0.11 | 201955.0 | 36.94 | skipped_fast |
| MNSRYUSDT | IDLE | 1.28 | 2.42 | 0.96 | 0.02 | 43823.66 | 14.06 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.98 | 1.07 | 0.08 | 443.55 | 22.17 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.66 | 0.58 | 0.01 | 58654.95 | 14.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
