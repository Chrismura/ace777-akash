# Hulk DIGEST — 2026-09-22T05:05:17Z

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
| XRPUSDT | IDLE | 1.05 | 2.45 | 1.86 | 0.07 | 118508197.35 | 2.64 | skipped_fast |
| ETHUSDT | IDLE | 1.07 | 1.87 | 1.79 | 0.02 | 712499123.69 | 0.7 | skipped_fast |
| BTCUSDT | IDLE | 0.88 | 1.55 | 1.42 | 0.05 | 1122079638.04 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.9 | 4.44 | 2.83 | 0.07 | 1217394.86 | 1.08 | skipped_fast |
| PYTHUSDT | IDLE | 1.47 | 3.13 | 2.32 | 0.04 | 792988.2 | 4.73 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 3.01 | 1.64 | 0.06 | 646400.3 | 7.64 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 27.81 | 12.24 | -0.17 | 53231.4 | 88.24 | skipped_fast |
| WUSDT | IDLE | 1.33 | 2.37 | 1.96 | -0.02 | 485132.58 | 7.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.74 | 3.76 | 1.34 | 0.03 | 269827.45 | 55.45 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 8.42 | 0.74 | 0.11 | 236193.33 | 34.22 | skipped_fast |
| KITEUSDT | IDLE | 2.09 | 4.02 | 1.02 | 0.06 | 83190.93 | 15.56 | skipped_fast |
| CHIPUSDT | IDLE | 1.36 | 5.12 | 3.21 | 0.1 | 171132.34 | 12.86 | skipped_fast |
| REDUSDT | IDLE | 1.84 | 3.48 | 1.27 | 0.03 | 98464.89 | 16.09 | skipped_fast |
| BIOUSDT | IDLE | 1.47 | 2.69 | 1.63 | 0.03 | 127979.08 | 6.92 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 2.29 | 0.82 | 0.02 | 121653.53 | 4.49 | skipped_fast |
| RWAINCUSDT | IDLE | 0.82 | 1.94 | 1.69 | 0.06 | 22540.78 | 77.56 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 2.86 | 1.57 | 0.06 | 118433.33 | 24.59 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.37 | 0.83 | 0.02 | 41036.73 | 9.02 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.17 | 0.86 | 0.0 | 57886.36 | 21.83 | skipped_fast |
| FLUIDUSDT | IDLE | 0.68 | 1.33 | 0.18 | 0.09 | 13282.37 | 21.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
