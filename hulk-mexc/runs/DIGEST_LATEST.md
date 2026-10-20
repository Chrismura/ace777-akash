# Hulk DIGEST — 2026-10-20T14:16:41Z

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
| ETHUSDT | IDLE | 2.01 | 3.97 | 0.34 | 0.03 | 129294223.63 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.88 | 3.73 | 0.2 | 0.03 | 19371301.76 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 1.22 | 2.43 | 0.08 | 0.01 | 306428910.57 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.15 | 6.26 | 0.2 | 0.05 | 889772.2 | 2.62 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.48 | 12.27 | 9.98 | 0.0 | 79796.76 | 5.28 | skipped_fast |
| WUSDT | IDLE | 2.3 | 4.59 | 0.11 | 0.03 | 696670.79 | 15.06 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 17.37 | 10.82 | -0.02 | 73080.17 | 59.1 | skipped_fast |
| QNTUSDT | IDLE | 2.74 | 5.39 | 0.63 | 0.03 | 586567.56 | 9.98 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.82 | 0.0 | -0.0 | 437058.46 | 4.73 | skipped_fast |
| BIOUSDT | IDLE | 2.86 | 5.72 | 0.0 | 0.06 | 62114.37 | 12.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.17 | 7.08 | 0.3 | 0.13 | 94469.31 | 15.23 | skipped_fast |
| KITEUSDT | IDLE | 2.08 | 4.13 | 0.18 | 0.04 | 90323.22 | 11.35 | skipped_fast |
| EDELUSDT | IDLE | 0.76 | 4.43 | 1.62 | 0.2 | 303432.99 | 9.31 | skipped_fast |
| REDUSDT | IDLE | 2.06 | 4.13 | 0.0 | 0.03 | 58829.54 | 9.29 | skipped_fast |
| HBARUSDT | IDLE | 1.84 | 3.67 | 0.04 | 0.02 | 372410.61 | 8.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 2.54 | 0.0 | -0.01 | 193564.8 | 16.17 | skipped_fast |
| IOTAUSDT | IDLE | 2.72 | 5.39 | 0.34 | 0.06 | 84126.86 | 21.21 | skipped_fast |
| WAXLUSDT | IDLE | 2.43 | 4.82 | 0.22 | -0.03 | 56633.92 | 18.12 | skipped_fast |
| LAUSDT | IDLE | 2.45 | 4.86 | 0.33 | 0.02 | 56749.61 | 24.18 | skipped_fast |
| RWAUSDT | IDLE | 0.73 | 1.42 | 0.31 | 0.01 | 51043.78 | 23.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.8 | 1.52 | 0.48 | 0.0 | 39395.06 | 32.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.56 | 0.98 | 0.97 | 0.02 | 4457.88 | 41.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
