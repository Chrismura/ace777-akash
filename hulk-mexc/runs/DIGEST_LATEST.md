# Hulk DIGEST — 2026-10-28T11:33:14Z

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
| ETHUSDT | IDLE | 0.86 | 1.57 | 1.0 | 0.02 | 240177472.76 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.69 | 1.24 | 0.93 | 0.02 | 20206417.83 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.15 | 0.48 | 0.02 | 307132934.76 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.24 | 6.2 | 2.99 | 0.05 | 292675.2 | 7.88 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 7.64 | 5.51 | 0.02 | 156617.25 | 16.62 | skipped_fast |
| RWAINCUSDT | IDLE | 3.42 | 6.85 | 0.0 | 0.05 | 51801.99 | 6.41 | skipped_fast |
| WUSDT | IDLE | 0.73 | 1.36 | 0.73 | 0.04 | 629968.86 | 15.59 | skipped_fast |
| ZBCNUSDT | IDLE | 1.61 | 3.17 | 1.14 | -0.04 | 216127.42 | 11.01 | skipped_fast |
| PYTHUSDT | IDLE | 0.72 | 1.38 | 0.38 | 0.0 | 399596.25 | 2.76 | skipped_fast |
| EDELUSDT | IDLE | 1.22 | 2.26 | 1.24 | 0.01 | 285676.95 | 30.61 | skipped_fast |
| QNTUSDT | IDLE | 1.49 | 2.75 | 1.5 | -0.01 | 462487.57 | 2.0 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.32 | 0.88 | 0.0 | 407561.08 | 6.56 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 1.77 | 1.47 | 0.04 | 54601.48 | 15.06 | skipped_fast |
| KITEUSDT | IDLE | 0.89 | 1.6 | 1.24 | 0.02 | 60592.86 | 9.45 | skipped_fast |
| BIOUSDT | IDLE | 0.8 | 1.5 | 0.65 | 0.03 | 83356.74 | 8.77 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 1.33 | 0.32 | 0.03 | 36353.83 | 38.46 | skipped_fast |
| WAXLUSDT | IDLE | 1.15 | 2.15 | 0.95 | 0.02 | 55898.7 | 42.9 | skipped_fast |
| LAUSDT | IDLE | 0.72 | 1.38 | 0.76 | 0.03 | 59792.25 | 20.29 | skipped_fast |
| IOTAUSDT | IDLE | 0.71 | 1.31 | 0.77 | 0.0 | 75135.02 | 33.13 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.37 | 0.16 | 0.01 | 55056.21 | 39.76 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 1.76 | 0.0 | 0.01 | 6667.15 | 21.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.64 | 1.25 | 0.2 | 0.01 | 36037.92 | 54.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
