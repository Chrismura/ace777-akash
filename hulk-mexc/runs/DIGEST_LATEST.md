# Hulk DIGEST — 2026-10-22T18:36:12Z

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
| ETHUSDT | IDLE | 1.31 | 2.39 | 1.57 | -0.05 | 194614556.7 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.29 | 2.29 | 2.0 | -0.06 | 29813627.1 | 1.53 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.4 | 1.04 | -0.04 | 503249945.86 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.63 | 2.51 | 0.92 | -0.12 | 1522667.77 | 16.49 | skipped_fast |
| HBARUSDT | IDLE | 1.62 | 3.3 | 2.41 | -0.08 | 1305405.62 | 5.04 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 7.74 | 6.79 | -0.1 | 217959.66 | 13.85 | skipped_fast |
| PYTHUSDT | IDLE | 1.75 | 4.22 | 2.66 | -0.09 | 556208.24 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.63 | 4.71 | 3.82 | -0.11 | 847863.34 | 1.06 | skipped_fast |
| EDELUSDT | IDLE | 1.78 | 4.66 | 4.08 | -0.1 | 525497.44 | 9.53 | skipped_fast |
| RIZEUSDT | IDLE | 3.25 | 5.87 | 4.23 | 0.02 | 38804.55 | 57.97 | skipped_fast |
| RWAINCUSDT | IDLE | 2.71 | 4.92 | 3.36 | -0.04 | 56730.9 | 11.4 | skipped_fast |
| CHIPUSDT | IDLE | 0.81 | 3.56 | 1.26 | -0.11 | 255186.37 | 13.65 | skipped_fast |
| BIOUSDT | IDLE | 1.54 | 3.47 | 2.57 | -0.09 | 76931.34 | 8.51 | skipped_fast |
| CCUSDT | IDLE | 0.55 | 1.95 | 0.61 | -0.09 | 304363.17 | 4.87 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 2.76 | 2.18 | -0.06 | 100124.88 | 17.1 | skipped_fast |
| KITEUSDT | IDLE | 0.78 | 1.44 | 0.75 | -0.03 | 59723.57 | 10.86 | skipped_fast |
| LAUSDT | IDLE | 1.34 | 4.02 | 3.2 | -0.11 | 57993.16 | 25.99 | skipped_fast |
| IOTAUSDT | IDLE | 1.33 | 3.09 | 2.03 | -0.09 | 76649.11 | 22.5 | skipped_fast |
| FLUIDUSDT | IDLE | 0.84 | 6.23 | 2.82 | -0.09 | 23284.61 | 15.31 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.28 | 0.87 | -0.02 | 52632.39 | 7.97 | skipped_fast |
| WAXLUSDT | IDLE | 0.66 | 2.42 | 2.03 | -0.13 | 58530.59 | 62.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 0.92 | 0.64 | -0.01 | 39551.9 | 74.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
