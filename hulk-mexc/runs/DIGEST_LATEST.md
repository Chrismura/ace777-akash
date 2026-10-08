# Hulk DIGEST — 2026-10-08T22:19:38Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.06 | 14.97 | 0.45 | 0.16 | 2678232.21 | 3.57 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 8.66 | 1.84 | -0.06 | 1986480.61 | 1.7 | skipped_fast |
| WUSDT | IDLE | 0.88 | 5.24 | 2.49 | -0.02 | 5124035.81 | 14.54 | skipped_fast |
| XRPUSDT | IDLE | 2.38 | 4.97 | 0.13 | -0.02 | 52565251.07 | 2.17 | skipped_fast |
| ETHUSDT | IDLE | 1.6 | 3.17 | 0.21 | -0.03 | 533433401.42 | 0.24 | skipped_fast |
| BTCUSDT | IDLE | 0.93 | 1.86 | 0.05 | -0.02 | 501030462.51 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.1 | 5.21 | 1.73 | -0.02 | 940365.14 | 3.3 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 3.94 | 0.25 | -0.02 | 545904.1 | 6.78 | skipped_fast |
| EDELUSDT | IDLE | 1.78 | 11.3 | 2.29 | -0.15 | 430471.63 | 2.93 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 8.65 | 1.69 | -0.0 | 251056.41 | 16.41 | skipped_fast |
| RWAINCUSDT | IDLE | 2.99 | 11.77 | 3.53 | 0.08 | 29978.82 | 79.31 | skipped_fast |
| RIZEUSDT | IDLE | 2.09 | 13.27 | 11.23 | 0.04 | 64885.68 | 59.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 6.84 | 0.45 | -0.04 | 163164.32 | 12.25 | skipped_fast |
| REDUSDT | IDLE | 1.77 | 4.52 | 1.28 | -0.04 | 62510.46 | 9.03 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 5.52 | 0.21 | -0.04 | 81903.96 | 3.55 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.67 | 1.51 | -0.06 | 68321.88 | 8.75 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 5.75 | 2.96 | -0.09 | 187147.39 | 32.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.54 | 6.38 | 0.0 | -0.07 | 13989.01 | 21.7 | skipped_fast |
| RWAUSDT | IDLE | 0.94 | 1.84 | 0.24 | -0.04 | 52474.09 | 15.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.99 | 1.83 | 0.98 | -0.04 | 32484.63 | 44.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
