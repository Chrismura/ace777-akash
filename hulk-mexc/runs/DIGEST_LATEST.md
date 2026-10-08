# Hulk DIGEST — 2026-10-08T19:18:55Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 17.67 | 7.04 | 0.1 | 2268112.44 | 1.25 | skipped_fast |
| WUSDT | IDLE | 2.2 | 14.41 | 10.62 | 0.05 | 5146906.12 | 15.25 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 14.03 | 7.29 | -0.08 | 1985064.96 | 6.87 | skipped_fast |
| XRPUSDT | IDLE | 3.45 | 6.79 | 3.1 | -0.04 | 52764117.87 | 2.2 | skipped_fast |
| ETHUSDT | IDLE | 2.91 | 5.33 | 3.26 | -0.04 | 525465080.86 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.59 | 2.96 | 1.45 | -0.02 | 511087323.92 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 3.27 | 8.13 | 2.77 | -0.0 | 948973.72 | 6.52 | skipped_fast |
| CCUSDT | IDLE | 3.79 | 6.96 | 4.15 | -0.03 | 539245.93 | 9.44 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 10.44 | 8.08 | -0.06 | 67822.95 | 11.1 | skipped_fast |
| EDELUSDT | IDLE | 1.88 | 12.8 | 8.75 | -0.2 | 374886.89 | 24.84 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 8.22 | 5.09 | -0.04 | 63304.88 | 7.68 | skipped_fast |
| ZBCNUSDT | IDLE | 2.51 | 7.24 | 3.69 | -0.07 | 256952.92 | 16.54 | skipped_fast |
| RIZEUSDT | IDLE | 2.12 | 19.01 | 15.59 | 0.02 | 61987.99 | 37.15 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 9.63 | 5.45 | -0.04 | 79816.04 | 7.21 | skipped_fast |
| CHIPUSDT | IDLE | 2.26 | 11.27 | 5.48 | -0.05 | 162486.02 | 16.54 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.06 | 11.77 | 5.61 | 0.06 | 34306.41 | 76.63 | skipped_fast |
| RWAUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 5.83 | 5.2 | -0.05 | 51116.5 | 15.91 | skipped_fast |
| TELUSDT | IDLE | 1.97 | 7.26 | 2.4 | -0.09 | 171766.68 | 26.7 | skipped_fast |
| FLUIDUSDT | IDLE | 2.36 | 8.87 | 5.81 | -0.08 | 15953.84 | 21.41 | skipped_fast |
| MNSRYUSDT | IDLE | 1.25 | 2.25 | 1.68 | -0.04 | 33449.16 | 55.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
