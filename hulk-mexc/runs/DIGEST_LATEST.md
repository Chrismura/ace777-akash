# Hulk DIGEST — 2026-10-23T10:18:58Z

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
| XRPUSDT | IDLE | 0.57 | 1.04 | 0.6 | -0.01 | 25758030.03 | 2.27 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.89 | 0.42 | -0.0 | 228916330.55 | 0.17 | skipped_fast |
| BTCUSDT | IDLE | 0.26 | 0.5 | 0.18 | -0.0 | 342595437.55 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.57 | 4.54 | 4.05 | -0.02 | 635959.57 | 16.45 | skipped_fast |
| PYTHUSDT | IDLE | 1.95 | 3.51 | 2.65 | -0.04 | 669792.9 | 2.79 | skipped_fast |
| QNTUSDT | IDLE | 2.84 | 5.94 | 4.36 | -0.07 | 652935.41 | 14.27 | skipped_fast |
| ZBCNUSDT | IDLE | 3.58 | 8.19 | 3.2 | -0.02 | 174881.03 | 14.73 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 3.48 | 2.44 | -0.06 | 398855.82 | 25.26 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.72 | 11.83 | 8.49 | -0.1 | 45133.12 | 65.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 3.57 | 2.59 | 0.04 | 125284.51 | 15.49 | skipped_fast |
| HBARUSDT | IDLE | 1.93 | 3.44 | 2.83 | -0.02 | 326642.23 | 10.08 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 1.65 | 0.88 | -0.02 | 212267.0 | 9.71 | skipped_fast |
| RWAINCUSDT | IDLE | 1.24 | 2.3 | 1.21 | 0.01 | 51174.05 | 5.55 | skipped_fast |
| REDUSDT | IDLE | 1.03 | 1.82 | 1.61 | -0.02 | 82440.07 | 8.57 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 1.39 | 1.0 | -0.0 | 59349.12 | 8.37 | skipped_fast |
| KITEUSDT | IDLE | 0.63 | 1.22 | 0.28 | 0.01 | 58043.76 | 10.78 | skipped_fast |
| WAXLUSDT | IDLE | 1.75 | 3.15 | 2.38 | -0.03 | 56312.98 | 44.09 | skipped_fast |
| LAUSDT | IDLE | 1.1 | 2.19 | 0.11 | 0.0 | 53705.15 | 25.06 | skipped_fast |
| FLUIDUSDT | IDLE | 1.12 | 1.95 | 1.91 | -0.04 | 9535.91 | 21.63 | skipped_fast |
| RWAUSDT | IDLE | 0.76 | 1.43 | 0.63 | 0.0 | 51903.73 | 15.75 | skipped_fast |
| IOTAUSDT | IDLE | 0.65 | 1.23 | 0.51 | -0.0 | 66201.0 | 22.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.63 | 0.61 | -0.01 | 38216.17 | 65.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
