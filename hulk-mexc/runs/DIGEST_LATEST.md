# Hulk DIGEST — 2026-09-05T11:40:03Z

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
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 57.48 | 33.0 | -0.03 | 220753.87 | 18.67 | skipped_fast |
| XRPUSDT | IDLE | 0.49 | 0.89 | 0.55 | -0.04 | 37399898.59 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.22 | 0.4 | 0.26 | -0.03 | 356478552.74 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.25 | 0.14 | -0.02 | 491844538.9 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 6.84 | 5.63 | 0.0 | 451132.56 | 1.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.94 | 25.72 | 17.7 | -0.11 | 154928.61 | 157.96 | skipped_fast |
| PYTHUSDT | IDLE | 0.86 | 1.7 | 0.17 | -0.02 | 418891.32 | 3.69 | skipped_fast |
| CCUSDT | IDLE | 0.5 | 0.99 | 0.09 | -0.02 | 319946.72 | 6.43 | skipped_fast |
| WUSDT | IDLE | 0.75 | 1.4 | 0.72 | 0.01 | 204766.93 | 10.08 | skipped_fast |
| REDUSDT | IDLE | 1.26 | 2.32 | 2.1 | 0.04 | 65143.58 | 11.92 | skipped_fast |
| ZBCNUSDT | IDLE | 0.65 | 1.42 | 0.16 | -0.06 | 195919.51 | 2.12 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 2.11 | 0.37 | -0.02 | 63176.94 | 8.3 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 1.5 | 1.12 | -0.01 | 85505.43 | 7.31 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 1.6 | 0.61 | 0.01 | 289975.7 | 1.25 | skipped_fast |
| RWAUSDT | IDLE | 1.73 | 3.38 | 0.5 | 0.01 | 52839.22 | 14.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.81 | 1.52 | 0.64 | -0.01 | 5301.11 | 101.9 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.9 | 1.05 | -0.04 | 74768.83 | 65.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.96 | 1.92 | 0.0 | -0.0 | 1030.12 | 22.43 | skipped_fast |
| QNTUSDT | IDLE | 0.5 | 0.91 | 0.59 | -0.05 | 44158.24 | 6.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.17 | 0.31 | 0.25 | -0.01 | 36544.96 | 28.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
