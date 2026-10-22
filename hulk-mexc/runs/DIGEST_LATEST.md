# Hulk DIGEST — 2026-10-22T22:37:26Z

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
| XRPUSDT | IDLE | 0.94 | 1.77 | 0.73 | -0.05 | 30514655.98 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.61 | 1.13 | 0.62 | -0.04 | 237543122.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.63 | 0.15 | -0.04 | 464330531.87 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.08 | 2.99 | 1.75 | -0.1 | 1284197.73 | 16.66 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 1.59 | 0.13 | -0.06 | 1264275.9 | 6.27 | skipped_fast |
| PYTHUSDT | IDLE | 1.54 | 3.53 | 3.17 | -0.09 | 566458.43 | 2.77 | skipped_fast |
| EDELUSDT | IDLE | 1.35 | 3.64 | 0.86 | -0.07 | 517140.07 | 15.57 | skipped_fast |
| RIZEUSDT | IDLE | 2.74 | 7.42 | 4.83 | -0.04 | 40316.07 | 35.95 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 2.13 | 1.36 | -0.1 | 693789.67 | 2.66 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 5.03 | 1.42 | -0.09 | 223334.74 | 11.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 3.47 | 1.01 | 0.01 | 49674.73 | 5.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.09 | 2.3 | 0.66 | -0.04 | 196975.59 | 19.63 | skipped_fast |
| CCUSDT | IDLE | 0.56 | 1.63 | 0.29 | -0.1 | 259194.18 | 7.79 | skipped_fast |
| REDUSDT | IDLE | 1.22 | 2.28 | 1.19 | -0.06 | 86282.42 | 7.85 | skipped_fast |
| BIOUSDT | IDLE | 0.82 | 1.72 | 0.8 | -0.07 | 62326.86 | 4.27 | skipped_fast |
| KITEUSDT | IDLE | 0.8 | 1.49 | 0.8 | -0.03 | 60096.59 | 12.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.47 | 4.16 | 1.23 | -0.08 | 22596.85 | 21.52 | skipped_fast |
| IOTAUSDT | IDLE | 0.91 | 1.94 | 1.12 | -0.08 | 79873.67 | 22.64 | skipped_fast |
| LAUSDT | IDLE | 0.72 | 1.98 | 0.88 | -0.09 | 55229.48 | 22.16 | skipped_fast |
| WAXLUSDT | IDLE | 0.7 | 2.42 | 1.03 | -0.12 | 58538.78 | 66.4 | skipped_fast |
| RWAUSDT | IDLE | 0.21 | 0.4 | 0.16 | -0.02 | 52496.99 | 15.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.64 | 1.16 | 0.77 | -0.01 | 37739.29 | 65.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
