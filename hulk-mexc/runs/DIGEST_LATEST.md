# Hulk DIGEST — 2026-09-15T06:45:03Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.25 | 2.19 | 2.08 | 0.01 | 75402426.3 | 2.14 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 49.04 | 18.62 | 0.3 | 453252.88 | 43.96 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.66 | 1.24 | -0.01 | 463219496.64 | 0.32 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 0.97 | 0.82 | -0.0 | 516909620.9 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 40.02 | 18.68 | -0.17 | 51544.01 | 30.47 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.49 | 21.64 | 17.69 | -0.01 | 169732.86 | 16.48 | skipped_fast |
| PYTHUSDT | IDLE | 2.43 | 4.32 | 3.55 | -0.04 | 313337.14 | 3.63 | skipped_fast |
| CHIPUSDT | IDLE | 2.52 | 4.47 | 3.76 | -0.04 | 67247.82 | 14.66 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.54 | 3.42 | -0.04 | 168387.32 | 12.3 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 1.61 | 1.56 | -0.01 | 326106.91 | 4.21 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 2.51 | 1.67 | 0.01 | 200277.36 | 10.57 | skipped_fast |
| HBARUSDT | IDLE | 1.56 | 2.74 | 2.48 | 0.0 | 384662.44 | 1.3 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.89 | 1.08 | -0.01 | 97204.7 | 15.66 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 2.13 | 0.05 | -0.0 | 62844.93 | 13.96 | skipped_fast |
| TELUSDT | IDLE | 1.83 | 4.08 | 3.86 | 0.01 | 101852.71 | 31.38 | skipped_fast |
| RWAINCUSDT | IDLE | 0.62 | 1.11 | 0.82 | -0.0 | 4936.12 | 16.61 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 2.13 | 1.92 | -0.0 | 46500.38 | 6.27 | skipped_fast |
| FLUIDUSDT | IDLE | 1.46 | 2.57 | 2.39 | -0.0 | 2014.36 | 21.21 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.45 | -0.01 | 53929.32 | 14.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.55 | 0.21 | 0.0 | 34588.58 | 38.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
