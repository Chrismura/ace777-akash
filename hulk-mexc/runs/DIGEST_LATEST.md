# Hulk DIGEST — 2026-10-29T17:19:32Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 10.02 | 7.01 | 0.0 | 1024907.55 | 5.64 | skipped_fast |
| ETHUSDT | IDLE | 1.51 | 2.84 | 1.23 | 0.01 | 273440521.84 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.38 | 2.5 | 1.7 | -0.01 | 26265321.37 | 2.32 | skipped_fast |
| BTCUSDT | IDLE | 1.35 | 2.53 | 1.15 | 0.01 | 395342094.69 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.75 | 6.2 | 2.86 | 0.02 | 387729.78 | 11.76 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 9.68 | 5.12 | 0.04 | 135668.19 | 6.0 | skipped_fast |
| BIOUSDT | IDLE | 2.84 | 5.58 | 1.83 | 0.03 | 72882.6 | 8.68 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.6 | 2.1 | -0.03 | 400406.41 | 15.39 | skipped_fast |
| QNTUSDT | IDLE | 2.12 | 3.87 | 2.41 | 0.0 | 483234.79 | 5.12 | skipped_fast |
| EDELUSDT | IDLE | 1.37 | 2.62 | 0.82 | -0.03 | 327073.42 | 3.19 | skipped_fast |
| HBARUSDT | IDLE | 1.85 | 3.38 | 2.09 | -0.01 | 468084.93 | 5.39 | skipped_fast |
| ZBCNUSDT | IDLE | 1.22 | 2.33 | 0.79 | 0.01 | 230321.99 | 16.43 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 3.05 | 1.17 | 0.0 | 63300.25 | 9.93 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.29 | 1.3 | -0.0 | 59003.87 | 14.0 | skipped_fast |
| LAUSDT | IDLE | 2.37 | 4.49 | 1.68 | 0.01 | 59456.85 | 24.2 | skipped_fast |
| RWAINCUSDT | IDLE | 1.07 | 2.14 | 0.0 | -0.03 | 31934.1 | 6.97 | skipped_fast |
| IOTAUSDT | IDLE | 1.78 | 3.44 | 1.42 | -0.01 | 95905.58 | 14.65 | skipped_fast |
| RIZEUSDT | IDLE | 0.88 | 1.55 | 1.34 | -0.02 | 67257.87 | 51.66 | skipped_fast |
| WAXLUSDT | IDLE | 1.75 | 4.25 | 1.31 | -0.02 | 53336.51 | 27.39 | skipped_fast |
| FLUIDUSDT | IDLE | 1.74 | 3.62 | 3.06 | -0.05 | 7756.37 | 21.02 | skipped_fast |
| MNSRYUSDT | IDLE | 1.06 | 2.04 | 0.58 | -0.0 | 37521.18 | 23.46 | skipped_fast |
| RWAUSDT | IDLE | 0.85 | 1.7 | 0.0 | 0.01 | 55363.25 | 23.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
