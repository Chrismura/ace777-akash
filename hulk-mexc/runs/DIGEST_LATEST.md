# Hulk DIGEST — 2026-10-22T17:34:41Z

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
| ETHUSDT | IDLE | 1.31 | 2.39 | 1.5 | -0.05 | 194165016.05 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 1.98 | 1.38 | -0.05 | 29459395.15 | 1.52 | skipped_fast |
| BTCUSDT | IDLE | 0.77 | 1.4 | 0.93 | -0.04 | 505671455.38 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.71 | 2.86 | 1.3 | -0.13 | 1673839.7 | 16.51 | skipped_fast |
| HBARUSDT | IDLE | 1.52 | 3.3 | 2.46 | -0.08 | 1297079.54 | 6.29 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 4.71 | 3.65 | -0.06 | 1101852.31 | 1.06 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 5.38 | 4.39 | -0.09 | 532600.6 | 22.02 | skipped_fast |
| PYTHUSDT | IDLE | 1.54 | 4.22 | 2.7 | -0.1 | 561922.19 | 2.71 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.83 | 7.31 | 6.69 | -0.09 | 222592.44 | 32.04 | skipped_fast |
| RIZEUSDT | IDLE | 3.28 | 5.87 | 4.66 | 0.04 | 39278.52 | 58.15 | skipped_fast |
| RWAINCUSDT | IDLE | 2.46 | 4.37 | 3.69 | -0.03 | 57971.53 | 5.75 | skipped_fast |
| CCUSDT | IDLE | 0.61 | 2.06 | 1.48 | -0.06 | 329984.32 | 4.91 | skipped_fast |
| CHIPUSDT | IDLE | 0.76 | 3.4 | 0.77 | -0.09 | 312546.29 | 18.12 | skipped_fast |
| REDUSDT | IDLE | 1.49 | 2.76 | 1.43 | -0.06 | 100066.23 | 15.55 | skipped_fast |
| BIOUSDT | IDLE | 1.38 | 3.47 | 2.24 | -0.08 | 77359.67 | 8.47 | skipped_fast |
| KITEUSDT | IDLE | 0.77 | 1.44 | 0.62 | -0.03 | 60574.74 | 9.16 | skipped_fast |
| LAUSDT | IDLE | 1.3 | 4.02 | 2.77 | -0.09 | 58150.13 | 11.09 | skipped_fast |
| IOTAUSDT | IDLE | 1.26 | 3.09 | 1.81 | -0.08 | 77524.07 | 29.18 | skipped_fast |
| WAXLUSDT | IDLE | 1.0 | 3.87 | 1.62 | -0.1 | 58601.03 | 51.41 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.6 | 1.18 | -0.02 | 51800.05 | 23.93 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 3.35 | 2.59 | -0.07 | 18549.43 | 15.31 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.92 | 0.28 | -0.01 | 40141.32 | 74.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
