# Hulk DIGEST — 2026-10-26T04:44:01Z

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
| ETHUSDT | IDLE | 1.15 | 2.13 | 1.16 | -0.02 | 105655663.57 | 0.22 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 2.13 | 1.11 | -0.02 | 16742782.76 | 1.56 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.37 | 0.6 | -0.01 | 198736809.0 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.9 | 2.55 | 0.03 | 753072.44 | 2.71 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.61 | 1.9 | -0.04 | 582261.73 | 18.79 | skipped_fast |
| CHIPUSDT | IDLE | 3.47 | 7.27 | 0.09 | 0.01 | 99593.72 | 15.32 | skipped_fast |
| ZBCNUSDT | IDLE | 1.88 | 3.44 | 2.47 | 0.02 | 187493.1 | 9.61 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 2.4 | 0.85 | 0.03 | 715400.31 | 2.62 | skipped_fast |
| KITEUSDT | IDLE | 1.63 | 3.13 | 0.83 | -0.0 | 54474.36 | 11.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 3.01 | 2.59 | -0.06 | 65056.3 | 34.58 | skipped_fast |
| BIOUSDT | IDLE | 1.47 | 2.75 | 1.25 | -0.03 | 61083.69 | 4.52 | skipped_fast |
| REDUSDT | IDLE | 1.48 | 2.76 | 1.35 | -0.03 | 61038.72 | 15.98 | skipped_fast |
| EDELUSDT | IDLE | 0.86 | 2.13 | 1.06 | 0.05 | 206397.42 | 28.31 | skipped_fast |
| CCUSDT | IDLE | 0.8 | 1.5 | 0.64 | -0.0 | 173392.41 | 10.89 | skipped_fast |
| LAUSDT | IDLE | 2.19 | 6.15 | 0.1 | -0.04 | 60613.95 | 25.75 | skipped_fast |
| WAXLUSDT | IDLE | 2.38 | 4.3 | 3.05 | -0.03 | 54077.18 | 68.99 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.18 | 1.37 | -0.02 | 180691.48 | 6.5 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 1.25 | 0.64 | 0.0 | 33018.04 | 23.05 | skipped_fast |
| IOTAUSDT | IDLE | 1.72 | 3.13 | 2.11 | -0.03 | 61195.98 | 30.77 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 3.99 | 3.84 | -0.04 | 19225.79 | 21.75 | skipped_fast |
| RWAUSDT | IDLE | 0.18 | 0.32 | 0.24 | -0.0 | 53280.24 | 23.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.57 | 0.23 | -0.01 | 38283.64 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
