# Hulk DIGEST — 2026-10-25T18:07:28Z

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
| ETHUSDT | IDLE | 0.83 | 1.62 | 0.32 | 0.01 | 86811219.37 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.77 | 1.46 | 0.58 | 0.02 | 14723776.89 | 2.3 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.85 | 0.17 | 0.01 | 146954742.83 | 0.0 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.79 | 8.12 | 1.42 | 0.06 | 206798.33 | 26.83 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.99 | 0.41 | -0.01 | 603304.81 | 15.6 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.06 | 9.92 | 1.55 | 0.11 | 548929.92 | 8.12 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.27 | 0.0 | 0.03 | 403293.04 | 9.69 | skipped_fast |
| PYTHUSDT | IDLE | 2.34 | 4.65 | 0.26 | 0.07 | 433322.84 | 2.71 | skipped_fast |
| CHIPUSDT | IDLE | 2.97 | 5.84 | 0.71 | 0.09 | 92264.39 | 26.42 | skipped_fast |
| KITEUSDT | IDLE | 2.74 | 5.12 | 2.43 | 0.0 | 53390.76 | 11.51 | skipped_fast |
| REDUSDT | IDLE | 2.14 | 4.24 | 0.25 | -0.01 | 63441.54 | 15.68 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.64 | 0.42 | 0.02 | 180129.82 | 8.76 | skipped_fast |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.69 | 14.14 | 0.0 | 0.04 | 18749.01 | 21.72 | skipped_fast |
| BIOUSDT | IDLE | 1.17 | 2.26 | 0.57 | 0.0 | 59397.41 | 4.44 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 1.72 | 1.36 | -0.03 | 59644.6 | 16.64 | skipped_fast |
| RIZEUSDT | IDLE | 1.28 | 2.61 | 1.42 | -0.01 | 44863.99 | 48.71 | skipped_fast |
| WAXLUSDT | IDLE | 1.87 | 3.56 | 1.2 | 0.02 | 53667.12 | 48.63 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 2.14 | 0.14 | 0.02 | 141521.14 | 5.13 | skipped_fast |
| LAUSDT | IDLE | 1.1 | 4.35 | 0.87 | -0.11 | 71461.03 | 22.44 | skipped_fast |
| IOTAUSDT | IDLE | 1.13 | 2.19 | 0.44 | 0.0 | 61920.39 | 32.3 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.2 | 0.32 | 0.01 | 51362.63 | 15.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.74 | 0.41 | 0.0 | 36927.94 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
