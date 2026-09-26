# Hulk DIGEST — 2026-09-26T16:01:54Z

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
| XRPUSDT | IDLE | 0.57 | 1.12 | 0.19 | -0.02 | 45683811.59 | 2.58 | skipped_fast |
| ETHUSDT | IDLE | 0.27 | 0.52 | 0.15 | 0.0 | 141772131.06 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.4 | 0.05 | 0.0 | 358498629.32 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.73 | 15.78 | 3.31 | 0.22 | 1190875.44 | 11.23 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 4.56 | 1.84 | 0.07 | 1079759.86 | 3.85 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 5.28 | 1.73 | 0.11 | 952066.15 | 10.85 | skipped_fast |
| CHIPUSDT | IDLE | 3.49 | 7.71 | 0.54 | 0.06 | 111149.85 | 27.05 | skipped_fast |
| WUSDT | IDLE | 1.6 | 3.23 | 1.58 | 0.07 | 447742.66 | 7.82 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 10.66 | 8.51 | -0.05 | 7697.56 | 79.39 | skipped_fast |
| EDELUSDT | IDLE | 2.29 | 4.13 | 3.04 | 0.01 | 162356.84 | 9.89 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.42 | 0.14 | 0.02 | 572992.61 | 1.05 | skipped_fast |
| KITEUSDT | IDLE | 2.05 | 4.91 | 0.44 | 0.08 | 76098.89 | 8.49 | skipped_fast |
| ZBCNUSDT | IDLE | 1.39 | 2.74 | 0.22 | -0.01 | 233516.64 | 11.46 | skipped_fast |
| BIOUSDT | IDLE | 1.62 | 3.04 | 1.27 | 0.02 | 105481.0 | 3.05 | skipped_fast |
| REDUSDT | IDLE | 0.83 | 1.56 | 0.65 | -0.02 | 58112.02 | 13.02 | skipped_fast |
| RWAUSDT | IDLE | 1.8 | 3.54 | 0.43 | 0.02 | 55471.31 | 7.16 | skipped_fast |
| RIZEUSDT | IDLE | 0.53 | 2.36 | 0.79 | -0.1 | 42165.54 | 52.01 | skipped_fast |
| TELUSDT | IDLE | 1.14 | 2.15 | 0.93 | -0.03 | 125095.33 | 43.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.72 | 0.28 | 0.03 | 770.46 | 21.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.52 | 0.13 | 0.0 | 39644.25 | 30.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
