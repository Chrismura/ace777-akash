# Hulk DIGEST — 2026-10-19T21:02:52Z

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
| XRPUSDT | IDLE | 0.45 | 0.85 | 0.33 | 0.03 | 23780981.58 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.43 | 0.82 | 0.26 | 0.02 | 141146478.51 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.25 | 0.48 | 0.14 | 0.01 | 348225697.08 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.49 | 4.45 | 3.58 | 0.01 | 851950.98 | 2.77 | skipped_fast |
| WUSDT | IDLE | 2.58 | 4.69 | 3.17 | 0.03 | 692726.61 | 15.3 | skipped_fast |
| QNTUSDT | IDLE | 0.92 | 2.32 | 1.34 | 0.05 | 730129.07 | 1.03 | skipped_fast |
| CCUSDT | IDLE | 0.75 | 1.53 | 0.62 | 0.06 | 416275.94 | 6.74 | skipped_fast |
| EDELUSDT | IDLE | 1.64 | 2.9 | 2.52 | 0.03 | 206965.28 | 18.74 | skipped_fast |
| ZBCNUSDT | IDLE | 0.69 | 2.29 | 2.23 | 0.01 | 251563.71 | 10.16 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 3.65 | 1.62 | 0.1 | 68313.95 | 10.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 3.3 | 1.68 | 0.06 | 78892.82 | 16.85 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.35 | 0.87 | -0.01 | 515611.94 | 7.31 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 2.43 | 1.38 | 0.02 | 58286.14 | 9.52 | skipped_fast |
| BIOUSDT | IDLE | 1.14 | 2.07 | 1.44 | 0.03 | 69470.12 | 4.28 | skipped_fast |
| RWAINCUSDT | IDLE | 0.99 | 1.96 | 1.92 | 0.04 | 78919.83 | 5.16 | skipped_fast |
| RIZEUSDT | IDLE | 1.03 | 3.65 | 0.76 | -0.05 | 53289.08 | 50.68 | skipped_fast |
| LAUSDT | IDLE | 0.96 | 1.76 | 1.06 | 0.02 | 56346.15 | 24.93 | skipped_fast |
| WAXLUSDT | IDLE | 1.12 | 2.67 | 1.77 | -0.01 | 64106.6 | 57.26 | skipped_fast |
| IOTAUSDT | IDLE | 0.86 | 1.63 | 0.58 | 0.03 | 90940.05 | 40.27 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.95 | 0.08 | 0.02 | 55702.36 | 15.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.27 | 0.03 | -0.0 | 40227.3 | 17.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.05 | 4749.48 | 20.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
