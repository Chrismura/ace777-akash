# Hulk DIGEST — 2026-10-29T04:49:06Z

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
| XRPUSDT | IDLE | 1.79 | 3.23 | 2.35 | -0.03 | 24073660.89 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 1.62 | 2.99 | 1.71 | -0.02 | 232018399.06 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.14 | 2.06 | 1.41 | -0.01 | 336715843.87 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.74 | 6.74 | 4.87 | -0.03 | 468833.34 | 2.83 | skipped_fast |
| WUSDT | IDLE | 2.82 | 5.15 | 3.31 | -0.04 | 471300.96 | 16.96 | skipped_fast |
| CCUSDT | IDLE | 2.65 | 5.7 | 4.73 | -0.03 | 447729.52 | 7.24 | skipped_fast |
| QNTUSDT | IDLE | 3.59 | 6.45 | 4.85 | -0.03 | 459300.48 | 3.11 | skipped_fast |
| BIOUSDT | IDLE | 3.13 | 5.72 | 3.58 | -0.03 | 93217.22 | 9.05 | skipped_fast |
| HBARUSDT | IDLE | 1.98 | 3.61 | 2.33 | -0.04 | 615122.94 | 10.85 | skipped_fast |
| KITEUSDT | IDLE | 2.53 | 4.53 | 3.53 | -0.05 | 60587.96 | 9.78 | skipped_fast |
| EDELUSDT | IDLE | 2.1 | 3.68 | 3.46 | -0.05 | 164576.0 | 19.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 2.99 | 1.64 | -0.01 | 269211.34 | 22.26 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.53 | 6.23 | 5.47 | -0.06 | 53048.83 | 58.3 | skipped_fast |
| CHIPUSDT | IDLE | 0.96 | 4.6 | 2.75 | -0.11 | 233018.04 | 16.61 | skipped_fast |
| REDUSDT | IDLE | 1.77 | 3.19 | 2.33 | -0.03 | 63283.71 | 14.81 | skipped_fast |
| IOTAUSDT | IDLE | 2.57 | 4.6 | 3.63 | -0.05 | 104143.37 | 27.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.19 | 4.49 | 3.47 | -0.05 | 31022.88 | 21.61 | skipped_fast |
| FLUIDUSDT | IDLE | 2.72 | 4.79 | 4.29 | -0.04 | 5972.11 | 19.67 | skipped_fast |
| LAUSDT | IDLE | 2.26 | 4.37 | 0.99 | -0.02 | 55277.08 | 24.08 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 1.53 | 0.38 | -0.02 | 38976.98 | 66.43 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.53 | 1.35 | 0.0 | 54966.35 | 32.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.9 | 1.58 | 1.53 | -0.01 | 36637.45 | 56.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
