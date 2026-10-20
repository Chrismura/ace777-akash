# Hulk DIGEST — 2026-10-20T14:17:57Z

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
| ETHUSDT | IDLE | 2.03 | 3.97 | 0.65 | 0.02 | 129074444.1 | 0.77 | skipped_fast |
| XRPUSDT | IDLE | 1.92 | 3.73 | 0.67 | 0.02 | 19483137.14 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 1.25 | 2.43 | 0.45 | 0.01 | 305715657.45 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 3.17 | 6.26 | 0.55 | 0.04 | 887773.51 | 1.31 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.48 | 12.27 | 9.98 | -0.0 | 79484.18 | 5.28 | skipped_fast |
| WUSDT | IDLE | 2.34 | 4.59 | 0.54 | 0.02 | 696466.08 | 15.84 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 17.37 | 10.62 | -0.02 | 73079.2 | 63.64 | skipped_fast |
| QNTUSDT | IDLE | 2.77 | 5.39 | 0.95 | 0.02 | 596871.53 | 10.49 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 2.82 | 0.14 | -0.0 | 436431.23 | 9.47 | skipped_fast |
| BIOUSDT | IDLE | 2.89 | 5.72 | 0.4 | 0.05 | 62318.18 | 12.15 | skipped_fast |
| CHIPUSDT | IDLE | 2.17 | 7.08 | 0.41 | 0.13 | 94428.16 | 15.21 | skipped_fast |
| KITEUSDT | IDLE | 2.09 | 4.13 | 0.38 | 0.03 | 90189.15 | 8.92 | skipped_fast |
| REDUSDT | IDLE | 2.1 | 4.13 | 0.43 | 0.02 | 58825.99 | 15.75 | skipped_fast |
| HBARUSDT | IDLE | 1.86 | 3.67 | 0.38 | 0.02 | 372303.06 | 2.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.54 | 0.08 | -0.01 | 193503.94 | 8.09 | skipped_fast |
| EDELUSDT | IDLE | 0.74 | 4.43 | 0.61 | 0.21 | 303652.16 | 30.85 | skipped_fast |
| IOTAUSDT | IDLE | 2.71 | 5.39 | 0.25 | 0.06 | 84111.15 | 23.28 | skipped_fast |
| LAUSDT | IDLE | 2.44 | 4.86 | 0.15 | 0.03 | 56782.15 | 25.99 | skipped_fast |
| WAXLUSDT | IDLE | 2.44 | 4.82 | 0.41 | -0.03 | 56611.06 | 57.76 | skipped_fast |
| RWAUSDT | IDLE | 0.74 | 1.42 | 0.39 | 0.01 | 51145.51 | 23.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.79 | 1.52 | 0.4 | 0.0 | 39412.37 | 32.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.56 | 0.98 | 0.97 | 0.02 | 4457.88 | 21.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
