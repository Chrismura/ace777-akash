# Hulk DIGEST — 2026-09-17T00:14:36Z

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
| XRPUSDT | IDLE | 1.83 | 3.44 | 1.45 | 0.01 | 57950990.86 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 1.0 | 1.98 | 0.2 | 0.01 | 369234770.52 | 0.37 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.58 | 0.18 | 0.01 | 506357750.5 | 0.0 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.69 | 10.49 | 0.64 | 0.13 | 516278.19 | 13.7 | skipped_fast |
| RWAINCUSDT | IDLE | 4.18 | 7.81 | 3.71 | -0.03 | 20636.35 | 35.11 | skipped_fast |
| WUSDT | IDLE | 2.8 | 5.55 | 0.27 | 0.0 | 208985.31 | 10.86 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.09 | 0.41 | -0.0 | 412621.81 | 1.89 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 5.13 | 1.6 | -0.02 | 80595.11 | 13.77 | skipped_fast |
| KITEUSDT | IDLE | 2.02 | 7.47 | 0.76 | 0.07 | 67803.82 | 13.96 | skipped_fast |
| BIOUSDT | IDLE | 1.94 | 3.79 | 0.6 | 0.0 | 79247.67 | 11.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.16 | 2.17 | 0.99 | 0.02 | 181187.35 | 18.43 | skipped_fast |
| REDUSDT | IDLE | 1.57 | 3.24 | 0.98 | -0.02 | 65075.11 | 21.67 | skipped_fast |
| EDELUSDT | IDLE | 0.52 | 3.15 | 1.79 | 0.12 | 297156.88 | 83.08 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.15 | 0.42 | -0.01 | 283840.41 | 1.36 | skipped_fast |
| RWAUSDT | IDLE | 1.96 | 3.87 | 0.37 | 0.01 | 55143.97 | 14.97 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 9.65 | 6.35 | 0.24 | 60676.43 | 124.88 | skipped_fast |
| QNTUSDT | IDLE | 1.51 | 2.99 | 0.16 | 0.0 | 37141.21 | 8.17 | skipped_fast |
| TELUSDT | IDLE | 1.26 | 2.38 | 0.89 | -0.03 | 114747.1 | 41.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 1.07 | 0.0 | -0.02 | 1573.23 | 44.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.47 | 0.93 | 0.0 | 0.0 | 31713.07 | 70.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
