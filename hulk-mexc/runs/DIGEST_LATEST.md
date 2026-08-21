# Hulk DIGEST — 2026-08-21T21:29:39Z

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
| PYTHUSDT | IDLE | 1.18 | 4.51 | 0.86 | 0.1 | 5631416.06 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.12 | 3.73 | 1.32 | 0.11 | 129135773.73 | 0.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.9 | 5.61 | 4.06 | 0.05 | 517554.25 | 9.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.19 | 0.1 | 485242.41 | 41.91 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 3.14 | 0.07 | 0.1 | 643946.2 | 7.34 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 3.04 | 0.26 | 0.07 | 813152.37 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.94 | 3.83 | 0.36 | 0.06 | 367564.54 | 4.18 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.93 | 0.02 | 187006.04 | 43.78 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.3 | 0.17 | 153899.6 | 12.29 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10169.83 | 16.1 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.47 | 0.02 | 56011.04 | 45.77 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 4.12 | 1.87 | -0.05 | 83316.58 | 33.65 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 1.53 | 0.12 | 61083.86 | 12.92 | skipped_fast |
| QAITUSDT | IDLE | 2.31 | 4.38 | 1.63 | -0.01 | 3782.1 | 135.62 | skipped_fast |
| TELUSDT | IDLE | 1.33 | 3.39 | 0.53 | 0.02 | 178687.16 | 53.25 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.65 | 0.42 | 0.05 | 63216.5 | 6.2 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.17 | 0.33 | 0.03 | 53848.32 | 24.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 23.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
