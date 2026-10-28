# Hulk DIGEST — 2026-10-28T05:26:33Z

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
| XRPUSDT | IDLE | 0.79 | 1.4 | 1.17 | 0.02 | 19441714.92 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.21 | 0.57 | 0.02 | 247460250.73 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.74 | 0.31 | 0.01 | 310779242.45 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.89 | 1.86 | 0.55 | 0.05 | 647075.96 | 21.79 | skipped_fast |
| EDELUSDT | IDLE | 1.8 | 3.34 | 1.76 | 0.02 | 376167.89 | 24.38 | skipped_fast |
| ZBCNUSDT | IDLE | 2.43 | 4.8 | 2.57 | -0.04 | 202043.39 | 34.01 | skipped_fast |
| RWAINCUSDT | IDLE | 2.67 | 5.68 | 4.66 | -0.06 | 57676.94 | 6.79 | skipped_fast |
| PYTHUSDT | IDLE | 0.99 | 1.75 | 1.57 | -0.0 | 364776.29 | 2.75 | skipped_fast |
| QNTUSDT | IDLE | 0.98 | 1.89 | 0.49 | 0.01 | 655249.31 | 4.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 3.29 | 2.22 | 0.05 | 129307.61 | 18.43 | skipped_fast |
| CCUSDT | IDLE | 0.71 | 1.35 | 0.52 | 0.02 | 225603.39 | 9.03 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 1.83 | 1.27 | 0.05 | 59663.38 | 11.02 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.07 | 0.98 | 0.0 | 329358.4 | 10.45 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 1.82 | 0.87 | 0.03 | 58513.46 | 13.2 | skipped_fast |
| REDUSDT | IDLE | 0.63 | 1.37 | 0.3 | 0.06 | 58567.62 | 15.52 | skipped_fast |
| RIZEUSDT | IDLE | 0.41 | 0.79 | 0.21 | 0.01 | 34854.75 | 52.98 | skipped_fast |
| LAUSDT | IDLE | 1.04 | 2.01 | 1.71 | 0.03 | 59137.13 | 20.29 | skipped_fast |
| IOTAUSDT | IDLE | 0.91 | 1.61 | 1.4 | 0.01 | 74260.63 | 47.29 | skipped_fast |
| FLUIDUSDT | IDLE | 0.46 | 1.38 | 0.72 | 0.01 | 7457.67 | 18.94 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.64 | 0.32 | -0.0 | 55773.63 | 24.09 | skipped_fast |
| WAXLUSDT | IDLE | 0.67 | 1.25 | 0.59 | 0.01 | 56275.55 | 71.44 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.77 | 0.01 | 0.01 | 36378.62 | 66.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
