# Hulk DIGEST — 2026-08-21T21:38:12Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.47 | 0.1 | 5648940.34 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.1 | 3.73 | 0.93 | 0.1 | 129350533.38 | 2.86 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 5.61 | 3.82 | 0.05 | 517102.04 | 3.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.95 | 8.19 | 3.56 | 0.11 | 489155.36 | 35.11 | skipped_fast |
| CCUSDT | IDLE | 1.25 | 3.67 | 0.0 | 0.1 | 650812.31 | 5.48 | skipped_fast |
| HBARUSDT | IDLE | 1.62 | 3.24 | 0.04 | 0.07 | 817437.29 | 3.83 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.83 | 0.42 | 0.06 | 368992.3 | 13.58 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.9 | 0.02 | 187975.34 | 3.13 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.95 | 0.17 | 154158.78 | 18.02 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.13 | 0.02 | 56007.32 | 28.08 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.03 | 10264.06 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.5 | 0.11 | 61046.15 | 9.22 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 4.12 | 1.32 | -0.04 | 83608.67 | 100.17 | skipped_fast |
| TELUSDT | IDLE | 1.92 | 4.81 | 1.25 | 0.03 | 182837.58 | 63.42 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 183.05 | skipped_fast |
| QNTUSDT | IDLE | 1.39 | 2.65 | 0.88 | 0.04 | 62898.79 | 6.2 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.17 | 0.58 | 0.03 | 53972.36 | 24.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
