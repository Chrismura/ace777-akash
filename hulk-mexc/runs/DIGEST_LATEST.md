# Hulk DIGEST — 2026-10-22T20:36:55Z

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
| ETHUSDT | IDLE | 1.24 | 2.29 | 1.33 | -0.05 | 197904377.54 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.21 | 2.12 | 2.05 | -0.07 | 30676180.04 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.17 | 0.69 | -0.04 | 478246350.55 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.94 | 2.87 | 2.77 | -0.12 | 1346011.54 | 14.51 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.24 | 2.08 | -0.08 | 1293224.31 | 8.9 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 11.34 | 8.7 | -0.03 | 41147.14 | 63.23 | skipped_fast |
| EDELUSDT | IDLE | 1.78 | 4.46 | 3.79 | -0.09 | 521203.51 | 12.7 | skipped_fast |
| ZBCNUSDT | IDLE | 2.87 | 5.72 | 3.92 | -0.06 | 199216.75 | 20.54 | skipped_fast |
| PYTHUSDT | IDLE | 1.18 | 2.67 | 2.2 | -0.09 | 541848.33 | 2.74 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 3.61 | 3.09 | -0.11 | 729606.42 | 0.53 | skipped_fast |
| CHIPUSDT | IDLE | 1.25 | 4.64 | 3.56 | -0.12 | 245947.15 | 16.17 | skipped_fast |
| RWAINCUSDT | IDLE | 2.21 | 4.16 | 1.72 | -0.04 | 54264.84 | 11.3 | skipped_fast |
| CCUSDT | IDLE | 0.55 | 1.76 | 1.64 | -0.12 | 266426.08 | 5.92 | skipped_fast |
| REDUSDT | IDLE | 1.28 | 2.25 | 2.07 | -0.06 | 100417.15 | 7.9 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 2.06 | 1.97 | -0.09 | 76875.13 | 8.57 | skipped_fast |
| KITEUSDT | IDLE | 0.82 | 1.44 | 1.36 | -0.03 | 60314.97 | 13.44 | skipped_fast |
| IOTAUSDT | IDLE | 1.06 | 2.37 | 2.29 | -0.09 | 76838.43 | 22.77 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 6.13 | 3.14 | -0.09 | 22524.29 | 19.81 | skipped_fast |
| LAUSDT | IDLE | 0.96 | 2.71 | 2.18 | -0.11 | 55186.18 | 24.19 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.04 | 0.63 | -0.02 | 52448.83 | 7.97 | skipped_fast |
| WAXLUSDT | IDLE | 0.66 | 2.42 | 2.01 | -0.13 | 58530.05 | 58.5 | skipped_fast |
| MNSRYUSDT | IDLE | 0.56 | 1.03 | 0.61 | -0.01 | 39257.58 | 65.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
