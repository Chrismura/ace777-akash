# Hulk DIGEST — 2026-10-18T22:05:32Z

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
| XRPUSDT | IDLE | 1.51 | 3.02 | 0.02 | 0.0 | 26817049.07 | 2.32 | skipped_fast |
| ETHUSDT | IDLE | 1.44 | 2.87 | 0.09 | 0.0 | 114327948.07 | 0.54 | skipped_fast |
| PYTHUSDT | IDLE | 2.04 | 5.76 | 2.33 | -0.1 | 1488042.84 | 2.71 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.21 | 0.0 | 0.0 | 226577955.65 | 0.64 | skipped_fast |
| WUSDT | IDLE | 1.56 | 4.1 | 0.91 | -0.06 | 876995.63 | 13.89 | skipped_fast |
| HBARUSDT | IDLE | 2.37 | 5.75 | 1.62 | 0.01 | 803756.04 | 8.25 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 9.75 | 7.79 | -0.04 | 61468.41 | 54.0 | skipped_fast |
| QNTUSDT | IDLE | 2.02 | 4.8 | 0.99 | -0.03 | 576947.51 | 8.48 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 14.68 | 7.52 | 0.02 | 80422.14 | 38.3 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 3.11 | 0.59 | -0.04 | 234965.36 | 10.09 | skipped_fast |
| EDELUSDT | IDLE | 1.84 | 4.42 | 2.1 | -0.07 | 248113.76 | 61.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.37 | 2.53 | 1.43 | -0.05 | 217113.14 | 19.7 | skipped_fast |
| REDUSDT | IDLE | 1.74 | 3.48 | 0.01 | -0.01 | 95661.23 | 16.84 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 3.05 | 0.0 | -0.03 | 81565.27 | 8.6 | skipped_fast |
| CHIPUSDT | IDLE | 1.3 | 4.12 | 0.42 | -0.06 | 76787.99 | 14.91 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.42 | 0.0 | -0.01 | 65250.55 | 11.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 4.56 | 3.96 | -0.04 | 58505.38 | 61.82 | skipped_fast |
| FLUIDUSDT | IDLE | 2.1 | 3.87 | 3.58 | -0.07 | 4269.88 | 49.07 | skipped_fast |
| IOTAUSDT | IDLE | 1.54 | 3.61 | 0.54 | -0.04 | 68062.37 | 27.31 | skipped_fast |
| LAUSDT | IDLE | 1.3 | 3.4 | 0.23 | -0.05 | 58853.47 | 23.01 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.7 | 0.65 | -0.01 | 34770.71 | 19.98 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.72 | 0.48 | -0.0 | 48112.41 | 40.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
