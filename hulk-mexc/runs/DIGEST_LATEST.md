# Hulk DIGEST — 2026-09-13T09:33:50Z

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
| ETHUSDT | IDLE | 1.13 | 1.98 | 1.88 | -0.02 | 206085817.73 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.13 | 1.97 | 1.89 | -0.02 | 13498102.8 | 1.49 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 0.93 | 0.92 | -0.01 | 297476444.79 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.82 | 13.41 | 11.09 | 0.07 | 203515.64 | 8.21 | skipped_fast |
| PYTHUSDT | IDLE | 2.21 | 3.88 | 3.59 | 0.01 | 457155.63 | 1.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.89 | 30.17 | 11.24 | 0.18 | 101302.95 | 39.36 | skipped_fast |
| CCUSDT | IDLE | 2.39 | 4.21 | 3.83 | -0.04 | 280529.15 | 5.25 | skipped_fast |
| WUSDT | IDLE | 1.53 | 2.7 | 2.41 | 0.01 | 241976.1 | 3.05 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 3.5 | 3.22 | 0.02 | 55438.04 | 18.46 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 3.67 | 2.85 | -0.02 | 77479.57 | 15.01 | skipped_fast |
| KITEUSDT | IDLE | 1.69 | 3.01 | 2.45 | 0.02 | 62067.12 | 12.02 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 2.54 | 2.13 | -0.01 | 70920.25 | 7.92 | skipped_fast |
| ZBCNUSDT | IDLE | 0.7 | 1.97 | 1.62 | -0.03 | 214119.81 | 18.04 | skipped_fast |
| TELUSDT | IDLE | 2.65 | 4.86 | 2.93 | -0.06 | 88292.29 | 37.71 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.35 | -0.06 | 9319.3 | 5.59 | skipped_fast |
| FLUIDUSDT | IDLE | 1.99 | 3.57 | 2.71 | 0.01 | 1217.06 | 56.74 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 1.57 | 1.31 | 0.0 | 152813.65 | 2.68 | skipped_fast |
| QNTUSDT | IDLE | 0.74 | 1.29 | 1.28 | -0.01 | 36945.87 | 6.3 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.05 | 1.04 | -0.01 | 55948.93 | 22.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.36 | 0.24 | -0.0 | 33527.08 | 29.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
