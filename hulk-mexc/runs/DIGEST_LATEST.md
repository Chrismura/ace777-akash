# Hulk DIGEST — 2026-09-19T20:02:38Z

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
| XRPUSDT | IDLE | 0.95 | 1.71 | 1.22 | 0.02 | 58979632.15 | 1.4 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.42 | 1.24 | 0.0 | 284025918.33 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.75 | 0.64 | 0.0 | 457742584.77 | 0.0 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 12.48 | 5.07 | 0.09 | 225699.05 | 39.25 | skipped_fast |
| PYTHUSDT | IDLE | 1.35 | 2.61 | 0.64 | 0.01 | 679865.81 | 1.64 | skipped_fast |
| WUSDT | IDLE | 1.23 | 2.26 | 1.4 | -0.0 | 579376.69 | 6.34 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 2.57 | 2.29 | 0.01 | 330951.02 | 10.8 | skipped_fast |
| RWAINCUSDT | IDLE | 3.18 | 7.86 | 0.0 | 0.01 | 5418.92 | 51.8 | skipped_fast |
| EDELUSDT | IDLE | 1.82 | 7.26 | 3.29 | -0.1 | 155103.36 | 33.69 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 2.22 | 0.15 | 0.04 | 602438.58 | 1.22 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 2.95 | 1.61 | 0.02 | 83016.76 | 7.11 | skipped_fast |
| CHIPUSDT | IDLE | 0.97 | 2.23 | 2.09 | -0.0 | 131728.36 | 16.24 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 1.77 | 1.54 | 0.04 | 73860.36 | 11.31 | skipped_fast |
| REDUSDT | IDLE | 0.33 | 1.51 | 0.38 | 0.02 | 136158.55 | 14.84 | skipped_fast |
| RIZEUSDT | IDLE | 1.42 | 5.75 | 4.7 | 0.03 | 37794.79 | 136.63 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 3.32 | 2.89 | -0.02 | 126758.83 | 19.87 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.02 | 1.9 | 0.07 | 9472.77 | 21.75 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 0.94 | 0.52 | 0.03 | 57150.11 | 7.66 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.03 | 0.66 | 0.01 | 53993.33 | 29.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.71 | 0.17 | -0.01 | 35753.23 | 63.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
