# Hulk DIGEST — 2026-10-26T17:27:50Z

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
| ETHUSDT | IDLE | 1.11 | 2.11 | 0.7 | -0.01 | 138350965.31 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.05 | 2.01 | 0.61 | -0.01 | 24355571.84 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.89 | 1.69 | 0.55 | -0.0 | 346802080.79 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.92 | 7.97 | 7.16 | 0.09 | 1509850.85 | 12.51 | skipped_fast |
| PYTHUSDT | IDLE | 2.05 | 3.76 | 2.21 | 0.03 | 941718.1 | 3.99 | skipped_fast |
| WUSDT | IDLE | 3.2 | 6.6 | 1.47 | 0.02 | 601005.28 | 43.52 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 13.37 | 9.95 | -0.14 | 62852.2 | 19.13 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.23 | 15.42 | 1.87 | 0.2 | 266086.76 | 18.65 | skipped_fast |
| EDELUSDT | IDLE | 2.21 | 4.44 | 1.57 | 0.07 | 122733.12 | 33.59 | skipped_fast |
| RIZEUSDT | IDLE | 2.48 | 4.69 | 1.84 | -0.0 | 29073.94 | 27.76 | skipped_fast |
| BIOUSDT | IDLE | 1.75 | 3.28 | 1.5 | -0.01 | 60231.39 | 8.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.26 | 2.63 | 1.78 | -0.08 | 204604.15 | 29.77 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.98 | 1.35 | 0.01 | 63033.01 | 14.95 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 1.7 | 1.19 | -0.02 | 190203.82 | 9.97 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.22 | 1.26 | 0.0 | 53694.09 | 13.22 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 1.97 | 1.28 | -0.01 | 243404.15 | 7.79 | skipped_fast |
| WAXLUSDT | IDLE | 2.06 | 4.01 | 0.77 | -0.01 | 53691.71 | 36.89 | skipped_fast |
| LAUSDT | IDLE | 1.69 | 3.41 | 1.88 | 0.01 | 66983.73 | 41.1 | skipped_fast |
| IOTAUSDT | IDLE | 1.31 | 2.44 | 1.2 | -0.01 | 79912.09 | 2.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.35 | 2.0 | -0.04 | 1388.64 | 21.58 | skipped_fast |
| RWAUSDT | IDLE | 0.76 | 1.44 | 0.55 | -0.0 | 54495.62 | 31.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.09 | -0.01 | 42855.61 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
