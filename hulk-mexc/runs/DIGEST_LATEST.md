# Hulk DIGEST — 2026-10-29T17:21:54Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 10.02 | 6.78 | 0.01 | 1024608.09 | 2.82 | skipped_fast |
| ETHUSDT | IDLE | 1.51 | 2.84 | 1.16 | 0.01 | 274038780.36 | 0.21 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 2.5 | 1.59 | -0.01 | 26240413.61 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 1.34 | 2.53 | 1.05 | 0.01 | 395881905.52 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.75 | 6.2 | 2.8 | 0.02 | 387639.65 | 10.77 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 9.68 | 5.24 | 0.03 | 135612.6 | 10.03 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.6 | 2.11 | -0.02 | 401200.68 | 14.58 | skipped_fast |
| BIOUSDT | IDLE | 2.82 | 5.58 | 1.53 | 0.03 | 72939.04 | 8.65 | skipped_fast |
| QNTUSDT | IDLE | 2.1 | 3.87 | 2.26 | 0.0 | 483237.0 | 1.53 | skipped_fast |
| EDELUSDT | IDLE | 1.38 | 2.62 | 0.98 | -0.03 | 327891.05 | 3.19 | skipped_fast |
| HBARUSDT | IDLE | 1.84 | 3.38 | 2.02 | -0.01 | 468414.88 | 4.04 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.33 | 0.84 | 0.0 | 230111.76 | 23.69 | skipped_fast |
| REDUSDT | IDLE | 1.6 | 3.05 | 1.06 | 0.0 | 63346.86 | 7.27 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.29 | 1.28 | -0.0 | 59086.4 | 11.37 | skipped_fast |
| LAUSDT | IDLE | 2.37 | 4.49 | 1.61 | 0.01 | 59426.78 | 22.44 | skipped_fast |
| RWAINCUSDT | IDLE | 1.1 | 2.21 | 0.0 | -0.02 | 31984.16 | 6.97 | skipped_fast |
| IOTAUSDT | IDLE | 1.78 | 3.44 | 1.37 | -0.0 | 95870.28 | 14.64 | skipped_fast |
| RIZEUSDT | IDLE | 0.88 | 1.55 | 1.34 | -0.02 | 67267.69 | 51.66 | skipped_fast |
| WAXLUSDT | IDLE | 1.75 | 4.25 | 1.31 | -0.02 | 53406.4 | 27.39 | skipped_fast |
| FLUIDUSDT | IDLE | 1.74 | 3.62 | 3.06 | -0.05 | 7756.37 | 21.51 | skipped_fast |
| RWAUSDT | IDLE | 0.9 | 1.78 | 0.08 | 0.01 | 55374.82 | 7.97 | skipped_fast |
| MNSRYUSDT | IDLE | 1.06 | 2.04 | 0.57 | -0.0 | 37589.18 | 23.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
