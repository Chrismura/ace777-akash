# Hulk DIGEST — 2026-10-19T02:13:56Z

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
| XRPUSDT | IDLE | 2.02 | 4.03 | 0.13 | 0.01 | 29527445.15 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 1.67 | 3.33 | 0.1 | 0.01 | 127653445.17 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.04 | 2.06 | 0.07 | 0.01 | 270515883.89 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.94 | 5.75 | 0.55 | -0.04 | 1278815.72 | 3.98 | skipped_fast |
| WUSDT | IDLE | 1.99 | 5.13 | 0.36 | -0.04 | 772750.42 | 15.18 | skipped_fast |
| CCUSDT | IDLE | 3.27 | 6.48 | 0.44 | 0.0 | 289559.06 | 10.71 | skipped_fast |
| ZBCNUSDT | IDLE | 3.15 | 6.7 | 0.44 | -0.01 | 271862.69 | 18.29 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 6.17 | 0.85 | -0.01 | 594707.61 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 1.69 | 4.05 | 1.55 | -0.01 | 792235.12 | 3.55 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 8.93 | 6.55 | -0.02 | 64897.31 | 5.34 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.27 | 10.54 | 0.0 | 0.01 | 80106.09 | 13.9 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 6.13 | 0.96 | 0.02 | 257820.19 | 22.25 | skipped_fast |
| BIOUSDT | IDLE | 2.74 | 5.46 | 0.13 | -0.01 | 83831.33 | 4.18 | skipped_fast |
| REDUSDT | IDLE | 2.72 | 5.29 | 0.94 | 0.0 | 95567.1 | 17.34 | skipped_fast |
| KITEUSDT | IDLE | 2.12 | 4.2 | 0.21 | 0.0 | 67296.55 | 11.25 | skipped_fast |
| IOTAUSDT | IDLE | 2.73 | 5.92 | 0.53 | -0.02 | 67808.57 | 30.95 | skipped_fast |
| WAXLUSDT | IDLE | 1.93 | 8.62 | 5.57 | 0.03 | 84919.82 | 51.83 | skipped_fast |
| LAUSDT | IDLE | 2.15 | 5.22 | 0.47 | -0.03 | 58642.21 | 22.58 | skipped_fast |
| FLUIDUSDT | IDLE | 2.29 | 4.8 | 0.0 | -0.02 | 4322.47 | 21.59 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 3.1 | 2.51 | -0.05 | 58791.74 | 48.39 | skipped_fast |
| RWAUSDT | IDLE | 1.42 | 2.73 | 0.7 | 0.02 | 51283.5 | 15.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 1.03 | 0.17 | -0.01 | 36392.77 | 31.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
