# Hulk DIGEST — 2026-10-19T08:51:55Z

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
| XRPUSDT | IDLE | 0.56 | 1.02 | 0.66 | 0.02 | 31626469.7 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 1.03 | 0.43 | 0.01 | 141322167.12 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.81 | 0.41 | 0.01 | 324014725.55 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 3.02 | 1.69 | -0.04 | 1017531.33 | 1.33 | skipped_fast |
| ZBCNUSDT | IDLE | 3.18 | 11.35 | 4.99 | 0.02 | 315838.65 | 14.47 | skipped_fast |
| QNTUSDT | IDLE | 2.03 | 5.46 | 1.4 | 0.02 | 686050.0 | 2.01 | skipped_fast |
| WUSDT | IDLE | 1.36 | 2.45 | 2.38 | -0.04 | 529905.69 | 14.86 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.69 | 0.59 | -0.04 | 818457.27 | 5.9 | skipped_fast |
| EDELUSDT | IDLE | 1.87 | 3.73 | 2.87 | 0.02 | 236110.97 | 22.21 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.62 | 0.88 | 0.02 | 318639.15 | 5.85 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 5.06 | 2.49 | -0.02 | 80022.05 | 5.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.0 | 2.54 | 2.31 | -0.0 | 78280.17 | 14.19 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 1.83 | 1.19 | 0.01 | 64249.31 | 9.54 | skipped_fast |
| REDUSDT | IDLE | 0.78 | 1.43 | 0.92 | 0.0 | 94094.21 | 16.78 | skipped_fast |
| BIOUSDT | IDLE | 0.74 | 1.45 | 0.21 | 0.0 | 80553.35 | 8.41 | skipped_fast |
| FLUIDUSDT | IDLE | 2.24 | 6.06 | 1.87 | 0.02 | 7651.86 | 19.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.35 | 1.85 | 0.82 | -0.04 | 58368.86 | 63.44 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 1.91 | 1.48 | 0.01 | 54878.04 | 15.89 | skipped_fast |
| LAUSDT | IDLE | 0.94 | 1.79 | 0.65 | -0.01 | 58629.39 | 24.47 | skipped_fast |
| IOTAUSDT | IDLE | 0.98 | 1.88 | 0.51 | -0.0 | 64904.03 | 46.48 | skipped_fast |
| WAXLUSDT | IDLE | 0.81 | 3.7 | 1.66 | -0.02 | 85633.4 | 60.14 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.51 | 0.14 | -0.0 | 38729.96 | 25.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
