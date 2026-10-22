# Hulk DIGEST — 2026-10-22T11:29:17Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 1.08 | 4.69 | 4.02 | -0.05 | 3271197.86 | 19.14 | skipped_fast |
| ETHUSDT | IDLE | 1.09 | 1.94 | 1.63 | -0.03 | 229035916.53 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.01 | 1.79 | 1.48 | -0.02 | 32794345.08 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.48 | 1.21 | -0.02 | 523361069.56 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.0 | 1.49 | -0.05 | 1374630.38 | 4.96 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 2.17 | 2.12 | -0.03 | 1285340.04 | 3.61 | skipped_fast |
| PYTHUSDT | IDLE | 1.21 | 3.41 | 1.39 | -0.07 | 628412.85 | 2.66 | skipped_fast |
| EDELUSDT | IDLE | 1.56 | 2.73 | 2.66 | -0.03 | 563423.39 | 26.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.3 | 5.36 | 3.41 | -0.04 | 341933.47 | 15.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.8 | 5.15 | 0.59 | -0.05 | 228332.67 | 18.61 | skipped_fast |
| CCUSDT | IDLE | 0.78 | 2.33 | 1.68 | -0.04 | 392196.88 | 6.76 | skipped_fast |
| RWAINCUSDT | IDLE | 1.92 | 3.57 | 1.84 | -0.02 | 62902.19 | 11.34 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 2.28 | 1.24 | -0.04 | 78551.51 | 4.17 | skipped_fast |
| REDUSDT | IDLE | 1.03 | 1.96 | 1.72 | -0.02 | 80780.73 | 16.27 | skipped_fast |
| KITEUSDT | IDLE | 1.04 | 1.83 | 1.65 | -0.04 | 60382.94 | 9.25 | skipped_fast |
| RIZEUSDT | IDLE | 1.22 | 2.72 | 0.21 | 0.05 | 43977.08 | 56.42 | skipped_fast |
| IOTAUSDT | IDLE | 1.16 | 2.25 | 1.59 | -0.04 | 78415.27 | 24.37 | skipped_fast |
| WAXLUSDT | IDLE | 1.12 | 3.91 | 2.16 | -0.08 | 58876.13 | 32.75 | skipped_fast |
| LAUSDT | IDLE | 0.94 | 2.44 | 1.67 | -0.04 | 58750.94 | 19.91 | skipped_fast |
| FLUIDUSDT | IDLE | 0.66 | 3.41 | 3.3 | -0.04 | 19567.52 | 21.74 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.95 | 0.55 | -0.01 | 52649.24 | 15.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.63 | 0.51 | -0.0 | 40029.52 | 55.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
