# Hulk DIGEST — 2026-10-26T04:13:12Z

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
| ETHUSDT | IDLE | 1.16 | 2.13 | 1.31 | -0.02 | 104665614.62 | 0.13 | skipped_fast |
| XRPUSDT | IDLE | 1.16 | 2.13 | 1.26 | -0.02 | 16588883.86 | 3.11 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.37 | 0.76 | -0.01 | 194154286.07 | 0.24 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 2.9 | 2.33 | 0.03 | 748666.96 | 2.71 | skipped_fast |
| WUSDT | IDLE | 1.44 | 2.61 | 1.82 | -0.03 | 603510.94 | 20.48 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 3.44 | 3.05 | 0.01 | 181480.55 | 18.4 | skipped_fast |
| QNTUSDT | IDLE | 0.76 | 2.3 | 0.24 | 0.04 | 717064.45 | 9.38 | skipped_fast |
| CHIPUSDT | IDLE | 2.07 | 4.34 | 0.0 | -0.02 | 105567.81 | 17.95 | skipped_fast |
| RWAINCUSDT | IDLE | 1.68 | 3.01 | 2.31 | -0.07 | 63869.77 | 11.51 | skipped_fast |
| KITEUSDT | IDLE | 1.7 | 3.13 | 1.81 | -0.01 | 54322.86 | 9.82 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.75 | 1.78 | -0.03 | 61168.43 | 4.54 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 2.76 | 1.93 | -0.03 | 60413.93 | 15.37 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.5 | 0.98 | -0.01 | 173875.96 | 9.92 | skipped_fast |
| EDELUSDT | IDLE | 0.82 | 2.07 | 0.78 | 0.06 | 219644.78 | 40.71 | skipped_fast |
| WAXLUSDT | IDLE | 2.4 | 4.3 | 3.32 | -0.04 | 53973.22 | 20.94 | skipped_fast |
| LAUSDT | IDLE | 1.81 | 4.86 | 1.68 | -0.07 | 61711.48 | 24.58 | skipped_fast |
| HBARUSDT | IDLE | 1.2 | 2.18 | 1.44 | -0.02 | 180776.63 | 6.51 | skipped_fast |
| IOTAUSDT | IDLE | 1.72 | 3.13 | 2.13 | -0.04 | 60805.47 | 23.68 | skipped_fast |
| RIZEUSDT | IDLE | 0.68 | 1.25 | 0.76 | 0.0 | 33035.98 | 39.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 3.99 | 3.84 | -0.04 | 19225.79 | 20.38 | skipped_fast |
| RWAUSDT | IDLE | 0.18 | 0.32 | 0.24 | -0.01 | 53377.82 | 23.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.57 | 0.0 | -0.01 | 38284.0 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
