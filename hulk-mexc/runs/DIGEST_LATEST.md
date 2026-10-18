# Hulk DIGEST — 2026-10-18T21:09:25Z

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
| ETHUSDT | IDLE | 1.15 | 2.12 | 1.14 | -0.03 | 119069910.21 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 5.89 | 4.96 | -0.14 | 1473605.02 | 1.39 | skipped_fast |
| XRPUSDT | IDLE | 0.92 | 1.7 | 0.99 | -0.03 | 29360262.74 | 2.37 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.71 | 0.41 | -0.01 | 228663959.34 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.95 | 4.69 | 4.09 | -0.1 | 917865.27 | 16.65 | skipped_fast |
| HBARUSDT | IDLE | 2.74 | 6.26 | 4.47 | -0.03 | 772774.87 | 4.84 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 11.43 | 10.16 | -0.04 | 53596.58 | 91.23 | skipped_fast |
| QNTUSDT | IDLE | 2.17 | 4.8 | 3.43 | -0.08 | 627416.7 | 3.26 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 15.7 | 8.66 | -0.02 | 78413.37 | 51.04 | skipped_fast |
| EDELUSDT | IDLE | 1.84 | 4.42 | 3.03 | -0.09 | 246371.68 | 19.29 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 3.11 | 2.35 | -0.07 | 239360.69 | 9.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.73 | 3.3 | 1.06 | -0.06 | 205153.18 | 25.84 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 4.68 | 3.93 | -0.11 | 78856.21 | 7.68 | skipped_fast |
| REDUSDT | IDLE | 1.72 | 3.08 | 2.35 | -0.06 | 98689.31 | 9.79 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 2.97 | 2.19 | -0.07 | 84910.95 | 4.4 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 2.56 | 2.04 | -0.05 | 64575.85 | 9.89 | skipped_fast |
| RIZEUSDT | IDLE | 0.94 | 4.66 | 3.84 | -0.04 | 58567.11 | 61.44 | skipped_fast |
| FLUIDUSDT | IDLE | 2.1 | 3.87 | 3.58 | -0.08 | 4608.75 | 21.39 | skipped_fast |
| IOTAUSDT | IDLE | 1.75 | 3.77 | 2.91 | -0.08 | 73350.61 | 25.61 | skipped_fast |
| LAUSDT | IDLE | 1.19 | 2.81 | 2.35 | -0.1 | 58418.72 | 25.62 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.72 | 0.64 | -0.01 | 48663.24 | 16.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.73 | 0.68 | -0.01 | 34964.89 | 65.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
