# Hulk DIGEST — 2026-10-21T04:31:24Z

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
| ETHUSDT | IDLE | 0.52 | 0.91 | 0.82 | 0.01 | 170875237.87 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.48 | 0.85 | 0.77 | 0.02 | 24040517.93 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.59 | 0.48 | 0.01 | 317160053.31 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.95 | 3.02 | 1.06 | 0.1 | 936793.41 | 2.48 | skipped_fast |
| ZBCNUSDT | IDLE | 3.24 | 14.69 | 2.19 | 0.15 | 222746.22 | 26.46 | skipped_fast |
| WUSDT | IDLE | 1.41 | 2.73 | 0.63 | 0.03 | 628403.86 | 17.7 | skipped_fast |
| QNTUSDT | IDLE | 1.3 | 2.46 | 0.94 | -0.0 | 800093.8 | 2.54 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 3.53 | 2.24 | 0.03 | 447335.98 | 11.33 | skipped_fast |
| EDELUSDT | IDLE | 0.83 | 5.28 | 4.16 | 0.21 | 343060.49 | 22.91 | skipped_fast |
| RWAINCUSDT | IDLE | 1.66 | 7.84 | 4.56 | -0.07 | 79624.55 | 5.56 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 1.76 | 0.58 | -0.02 | 322157.87 | 7.56 | skipped_fast |
| REDUSDT | IDLE | 1.84 | 3.58 | 0.63 | 0.04 | 57552.22 | 16.64 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.64 | 1.28 | -0.01 | 332588.13 | 4.79 | skipped_fast |
| BIOUSDT | IDLE | 0.7 | 1.23 | 1.09 | 0.03 | 61837.57 | 8.16 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 3.01 | 2.05 | 0.06 | 61143.05 | 35.51 | skipped_fast |
| LAUSDT | IDLE | 2.03 | 4.98 | 1.71 | 0.05 | 55854.14 | 23.32 | skipped_fast |
| KITEUSDT | IDLE | 0.62 | 1.23 | 0.12 | -0.01 | 70898.08 | 8.98 | skipped_fast |
| WAXLUSDT | IDLE | 1.79 | 3.28 | 2.05 | -0.04 | 57212.28 | 35.77 | skipped_fast |
| IOTAUSDT | IDLE | 0.79 | 1.38 | 1.32 | 0.01 | 75209.81 | 19.44 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.55 | 0.31 | 0.0 | 53141.41 | 15.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.38 | 1.42 | 1.12 | 0.04 | 17687.46 | 21.2 | skipped_fast |
| MNSRYUSDT | IDLE | 0.17 | 0.34 | 0.06 | -0.0 | 40010.7 | 5.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
