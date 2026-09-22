# Hulk DIGEST — 2026-09-22T11:09:25Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.6 | 2.93 | 1.8 | 0.02 | 109893745.86 | 2.62 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.42 | 0.53 | 0.02 | 1039602912.64 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.19 | 0.52 | 0.01 | 586421206.72 | 0.04 | skipped_fast |
| HBARUSDT | IDLE | 2.87 | 5.69 | 4.69 | 0.04 | 1299461.52 | 1.07 | skipped_fast |
| PYTHUSDT | IDLE | 2.6 | 4.62 | 4.33 | -0.04 | 781919.6 | 1.62 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 2.65 | 2.03 | 0.01 | 611548.72 | 3.4 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 5.79 | 5.33 | -0.08 | 167496.31 | 17.39 | skipped_fast |
| KITEUSDT | IDLE | 2.85 | 9.99 | 2.77 | 0.1 | 113473.93 | 9.94 | skipped_fast |
| WUSDT | IDLE | 1.19 | 2.09 | 1.98 | -0.03 | 390702.6 | 4.27 | skipped_fast |
| REDUSDT | IDLE | 2.27 | 3.98 | 3.74 | 0.01 | 92001.49 | 15.6 | skipped_fast |
| ZBCNUSDT | IDLE | 1.68 | 3.01 | 2.29 | 0.0 | 273180.81 | 52.63 | skipped_fast |
| EDELUSDT | IDLE | 1.15 | 5.39 | 1.28 | 0.12 | 233214.62 | 27.71 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.29 | 2.1 | -0.02 | 128811.38 | 3.51 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 2.02 | 0.77 | 0.07 | 26525.72 | 5.51 | skipped_fast |
| QNTUSDT | IDLE | 1.73 | 3.42 | 0.27 | 0.03 | 123574.97 | 8.68 | skipped_fast |
| TELUSDT | IDLE | 1.68 | 3.15 | 1.34 | 0.0 | 110118.62 | 43.28 | skipped_fast |
| RIZEUSDT | IDLE | 0.45 | 4.48 | 1.23 | -0.17 | 50009.02 | 61.89 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.81 | 0.44 | 0.01 | 55392.76 | 7.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.27 | 0.0 | 0.05 | 8085.72 | 22.12 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.36 | 0.04 | 0.01 | 40310.42 | 2.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
