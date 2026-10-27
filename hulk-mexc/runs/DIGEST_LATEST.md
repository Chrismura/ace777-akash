# Hulk DIGEST — 2026-10-27T17:26:26Z

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
| XRPUSDT | IDLE | 1.09 | 2.12 | 0.44 | 0.02 | 19457102.34 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.98 | 1.94 | 0.13 | 0.01 | 193321012.65 | 0.47 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.17 | 0.01 | 0.0 | 313696245.88 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.39 | 7.64 | 4.01 | 0.03 | 691956.2 | 18.7 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 3.51 | 1.67 | -0.04 | 822436.05 | 2.99 | skipped_fast |
| KITEUSDT | IDLE | 3.27 | 6.38 | 2.16 | 0.04 | 57774.57 | 9.29 | skipped_fast |
| REDUSDT | IDLE | 3.12 | 6.21 | 0.17 | 0.05 | 59549.43 | 14.22 | skipped_fast |
| PYTHUSDT | IDLE | 1.37 | 2.56 | 1.16 | -0.04 | 431566.66 | 2.76 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.64 | 1.36 | -0.0 | 463426.5 | 27.62 | skipped_fast |
| CHIPUSDT | IDLE | 2.01 | 5.97 | 1.44 | 0.01 | 184207.83 | 14.81 | skipped_fast |
| CCUSDT | IDLE | 1.83 | 3.51 | 1.03 | -0.01 | 237999.72 | 7.06 | skipped_fast |
| LAUSDT | IDLE | 3.84 | 7.92 | 0.16 | 0.05 | 58976.1 | 34.25 | skipped_fast |
| BIOUSDT | IDLE | 1.54 | 3.06 | 0.13 | 0.01 | 58894.88 | 8.88 | skipped_fast |
| ZBCNUSDT | IDLE | 0.83 | 2.49 | 0.09 | 0.03 | 257206.41 | 32.99 | skipped_fast |
| RWAINCUSDT | IDLE | 0.61 | 2.26 | 0.27 | -0.05 | 61942.52 | 26.83 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.79 | 0.39 | -0.01 | 220705.02 | 10.48 | skipped_fast |
| WAXLUSDT | IDLE | 1.74 | 3.28 | 1.29 | -0.0 | 54033.31 | 36.69 | skipped_fast |
| RIZEUSDT | IDLE | 0.69 | 1.34 | 0.26 | -0.01 | 39006.07 | 65.34 | skipped_fast |
| RWAUSDT | IDLE | 1.45 | 2.87 | 0.24 | -0.0 | 56775.47 | 23.91 | skipped_fast |
| IOTAUSDT | IDLE | 1.1 | 2.01 | 1.22 | -0.02 | 86103.45 | 26.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.76 | 0.0 | 0.05 | 3234.8 | 21.63 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.77 | 0.03 | 0.0 | 37243.23 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
