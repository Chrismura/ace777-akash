# Hulk DIGEST — 2026-10-12T21:49:50Z

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
| WUSDT | IDLE | 1.84 | 26.81 | 20.23 | -0.07 | 15512891.83 | 6.68 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 10.47 | 7.6 | 0.07 | 3367772.88 | 13.29 | skipped_fast |
| XRPUSDT | IDLE | 1.67 | 2.97 | 2.5 | -0.04 | 29252895.32 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 1.14 | 2.03 | 1.71 | -0.01 | 216103778.44 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 0.99 | 0.7 | -0.01 | 290427948.72 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.76 | 3.36 | 2.18 | -0.05 | 834346.76 | 10.57 | skipped_fast |
| HBARUSDT | IDLE | 1.95 | 3.64 | 3.1 | -0.06 | 591831.25 | 12.46 | skipped_fast |
| EDELUSDT | IDLE | 1.54 | 6.93 | 2.05 | -0.11 | 282601.86 | 2.96 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 14.0 | 8.08 | -0.06 | 70942.47 | 50.55 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.83 | 1.57 | -0.02 | 399773.66 | 7.42 | skipped_fast |
| KITEUSDT | IDLE | 2.23 | 4.06 | 2.7 | -0.01 | 66424.9 | 34.31 | skipped_fast |
| BIOUSDT | IDLE | 1.89 | 3.69 | 3.31 | -0.07 | 81396.71 | 10.82 | skipped_fast |
| ZBCNUSDT | IDLE | 1.11 | 1.98 | 1.62 | 0.01 | 273841.49 | 14.75 | skipped_fast |
| REDUSDT | IDLE | 0.69 | 4.24 | 3.64 | 0.02 | 265717.32 | 14.3 | skipped_fast |
| CHIPUSDT | IDLE | 0.79 | 3.58 | 3.07 | -0.14 | 160600.12 | 12.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.11 | 2.9 | 1.94 | -0.01 | 31495.49 | 4.95 | skipped_fast |
| TELUSDT | IDLE | 2.07 | 3.89 | 1.68 | 0.03 | 118118.15 | 28.42 | skipped_fast |
| FLUIDUSDT | IDLE | 2.03 | 3.8 | 1.73 | 0.01 | 15836.79 | 21.29 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 0.98 | 0.62 | -0.01 | 41469.24 | 31.67 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.62 | 0.46 | 0.0 | 52577.81 | 23.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
