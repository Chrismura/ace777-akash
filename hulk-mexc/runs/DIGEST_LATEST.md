# Hulk DIGEST — 2026-10-23T18:51:41Z

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
| XRPUSDT | IDLE | 0.93 | 1.69 | 1.15 | 0.0 | 25426515.82 | 2.29 | skipped_fast |
| ETHUSDT | IDLE | 0.85 | 1.6 | 0.64 | 0.01 | 208570478.87 | 0.25 | skipped_fast |
| BTCUSDT | IDLE | 0.63 | 1.15 | 0.72 | 0.0 | 290611570.42 | 0.11 | skipped_fast |
| QNTUSDT | IDLE | 2.16 | 4.16 | 1.11 | -0.03 | 1190482.95 | 1.63 | skipped_fast |
| PYTHUSDT | IDLE | 2.21 | 4.23 | 1.27 | -0.02 | 720147.55 | 1.38 | skipped_fast |
| WUSDT | IDLE | 1.84 | 3.45 | 1.47 | -0.0 | 737094.75 | 7.46 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 4.93 | 3.76 | 0.0 | 508831.33 | 15.76 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 10.14 | 5.33 | -0.03 | 67405.29 | 46.33 | skipped_fast |
| CHIPUSDT | IDLE | 2.53 | 5.06 | 2.06 | 0.01 | 111727.76 | 17.87 | skipped_fast |
| REDUSDT | IDLE | 2.44 | 4.7 | 1.15 | 0.02 | 59917.44 | 14.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.83 | 3.66 | 0.66 | 0.05 | 198097.87 | 16.71 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 3.07 | 2.1 | 0.01 | 179527.52 | 7.74 | skipped_fast |
| RWAINCUSDT | IDLE | 2.07 | 3.93 | 1.46 | 0.04 | 48953.56 | 5.48 | skipped_fast |
| KITEUSDT | IDLE | 1.66 | 2.92 | 2.69 | -0.01 | 57159.44 | 9.29 | skipped_fast |
| BIOUSDT | IDLE | 1.44 | 2.71 | 1.15 | 0.02 | 72444.62 | 4.17 | skipped_fast |
| LAUSDT | IDLE | 2.8 | 7.87 | 0.47 | 0.11 | 57426.08 | 21.91 | skipped_fast |
| HBARUSDT | IDLE | 1.36 | 2.39 | 2.26 | -0.01 | 238715.66 | 5.09 | skipped_fast |
| WAXLUSDT | IDLE | 1.97 | 3.69 | 1.67 | 0.01 | 56963.96 | 26.88 | skipped_fast |
| FLUIDUSDT | IDLE | 2.02 | 4.03 | 0.13 | 0.01 | 3936.19 | 21.49 | skipped_fast |
| IOTAUSDT | IDLE | 1.62 | 3.01 | 1.54 | 0.01 | 71017.4 | 24.52 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.55 | 0.24 | 0.01 | 51274.62 | 15.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.72 | 0.47 | -0.0 | 35737.37 | 74.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
