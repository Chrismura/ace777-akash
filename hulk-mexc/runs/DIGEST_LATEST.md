# Hulk DIGEST — 2026-10-22T07:26:20Z

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
| WUSDT | IDLE | 1.57 | 6.27 | 5.78 | -0.01 | 3477324.29 | 17.51 | skipped_fast |
| BTCUSDT | IDLE | 0.86 | 1.5 | 1.45 | -0.01 | 515327278.52 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.68 | 1.23 | 0.86 | 0.0 | 35730851.18 | 2.24 | skipped_fast |
| ETHUSDT | IDLE | 0.64 | 1.13 | 0.99 | -0.01 | 255330573.72 | 0.41 | skipped_fast |
| QNTUSDT | IDLE | 2.25 | 5.42 | 3.85 | -0.01 | 1175272.4 | 0.51 | skipped_fast |
| PYTHUSDT | IDLE | 2.18 | 4.71 | 3.99 | -0.05 | 642619.62 | 2.65 | skipped_fast |
| HBARUSDT | IDLE | 1.85 | 3.34 | 2.36 | -0.03 | 1006989.27 | 1.22 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.71 | 8.4 | 7.09 | -0.01 | 369197.19 | 13.33 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.67 | 2.3 | -0.0 | 513525.61 | 20.62 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 5.19 | 4.54 | -0.01 | 416678.49 | 9.57 | skipped_fast |
| BIOUSDT | IDLE | 1.99 | 3.63 | 2.74 | -0.03 | 78461.58 | 4.15 | skipped_fast |
| REDUSDT | IDLE | 1.8 | 3.2 | 2.68 | -0.0 | 81859.29 | 9.06 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 2.99 | 2.06 | -0.02 | 59694.25 | 9.16 | skipped_fast |
| ZBCNUSDT | IDLE | 0.8 | 2.22 | 0.02 | -0.02 | 256098.14 | 21.02 | skipped_fast |
| WAXLUSDT | IDLE | 2.42 | 7.51 | 6.32 | -0.09 | 57894.1 | 53.13 | skipped_fast |
| RWAINCUSDT | IDLE | 0.92 | 3.81 | 1.94 | -0.03 | 66598.8 | 11.33 | skipped_fast |
| RIZEUSDT | IDLE | 1.16 | 2.32 | 0.29 | 0.05 | 44917.66 | 27.36 | skipped_fast |
| LAUSDT | IDLE | 1.97 | 4.52 | 4.06 | -0.03 | 63728.31 | 27.05 | skipped_fast |
| IOTAUSDT | IDLE | 1.94 | 3.41 | 3.15 | -0.03 | 80070.65 | 26.35 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.63 | 0.39 | -0.0 | 53272.95 | 31.45 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 0.96 | 0.76 | -0.0 | 39503.31 | 51.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 1.42 | 0.33 | 0.01 | 19811.38 | 21.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
