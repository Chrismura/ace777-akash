# Hulk DIGEST — 2026-10-26T16:26:42Z

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
| ETHUSDT | IDLE | 1.13 | 2.11 | 1.01 | -0.01 | 137020852.16 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 2.01 | 1.09 | -0.0 | 23747392.06 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.91 | 1.69 | 0.8 | -0.0 | 332987711.14 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.76 | 7.44 | 6.6 | 0.12 | 1475447.36 | 3.35 | skipped_fast |
| PYTHUSDT | IDLE | 2.0 | 3.76 | 1.61 | 0.06 | 936880.79 | 3.96 | skipped_fast |
| WUSDT | IDLE | 3.01 | 5.96 | 0.41 | 0.02 | 581273.02 | 37.35 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.36 | 13.6 | 1.58 | 0.17 | 225546.86 | 25.18 | skipped_fast |
| RWAINCUSDT | IDLE | 2.3 | 5.08 | 4.83 | -0.09 | 61409.51 | 18.14 | skipped_fast |
| BIOUSDT | IDLE | 1.77 | 3.28 | 1.72 | -0.0 | 59737.96 | 8.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.05 | 1.47 | -0.03 | 215188.69 | 37.21 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 2.98 | 1.71 | 0.02 | 62909.15 | 15.02 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.74 | 1.18 | -0.02 | 188531.5 | 9.96 | skipped_fast |
| EDELUSDT | IDLE | 1.26 | 3.4 | 0.34 | 0.09 | 131427.45 | 21.36 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 2.63 | 1.59 | 0.01 | 53496.56 | 13.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.71 | 3.33 | 0.57 | 0.02 | 34431.94 | 64.04 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.61 | 1.38 | -0.0 | 233143.89 | 6.5 | skipped_fast |
| LAUSDT | IDLE | 1.8 | 3.75 | 1.18 | 0.03 | 66778.93 | 39.25 | skipped_fast |
| WAXLUSDT | IDLE | 2.02 | 4.01 | 0.26 | -0.01 | 53271.58 | 56.92 | skipped_fast |
| IOTAUSDT | IDLE | 1.34 | 2.44 | 1.6 | -0.01 | 74045.03 | 18.81 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.99 | 0.34 | -0.02 | 1706.2 | 21.29 | skipped_fast |
| RWAUSDT | IDLE | 0.78 | 1.44 | 0.79 | 0.0 | 54770.53 | 31.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.62 | -0.02 | 42701.41 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
