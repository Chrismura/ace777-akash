# Hulk DIGEST — 2026-10-26T20:31:46Z

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
| ETHUSDT | IDLE | 0.87 | 1.53 | 1.41 | -0.02 | 146427763.2 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.87 | 1.57 | 1.07 | -0.01 | 24575726.87 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.3 | 1.18 | -0.01 | 358889870.03 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.51 | 6.28 | 5.76 | 0.04 | 1440252.13 | 3.47 | skipped_fast |
| PYTHUSDT | IDLE | 2.56 | 4.48 | 4.25 | -0.02 | 861880.42 | 5.43 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.87 | 1.86 | 0.03 | 665338.94 | 45.34 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 13.24 | 8.24 | -0.12 | 56999.5 | 6.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.66 | 12.74 | 8.05 | 0.17 | 323357.32 | 19.12 | skipped_fast |
| EDELUSDT | IDLE | 2.29 | 4.11 | 3.13 | 0.01 | 92641.26 | 24.92 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.49 | 2.4 | -0.03 | 206355.43 | 5.04 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 3.08 | 2.22 | -0.06 | 215332.89 | 43.58 | skipped_fast |
| RIZEUSDT | IDLE | 2.32 | 4.4 | 1.55 | 0.0 | 45444.86 | 64.9 | skipped_fast |
| REDUSDT | IDLE | 1.63 | 2.86 | 2.63 | -0.0 | 63300.32 | 7.57 | skipped_fast |
| BIOUSDT | IDLE | 1.63 | 2.86 | 2.69 | -0.01 | 59021.85 | 9.06 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.17 | 0.9 | 0.01 | 53528.5 | 11.41 | skipped_fast |
| FLUIDUSDT | IDLE | 2.65 | 5.19 | 0.74 | -0.01 | 1850.79 | 21.46 | skipped_fast |
| WAXLUSDT | IDLE | 2.58 | 4.54 | 4.16 | -0.04 | 53620.82 | 69.83 | skipped_fast |
| HBARUSDT | IDLE | 1.16 | 2.07 | 1.68 | -0.01 | 255855.9 | 9.12 | skipped_fast |
| IOTAUSDT | IDLE | 1.59 | 2.83 | 2.36 | -0.02 | 85052.51 | 21.31 | skipped_fast |
| LAUSDT | IDLE | 1.41 | 2.76 | 2.1 | 0.02 | 64669.41 | 25.75 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.88 | 0.4 | -0.0 | 53942.62 | 15.92 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.74 | 0.0 | -0.0 | 41911.83 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
