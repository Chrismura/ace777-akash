# Hulk DIGEST — 2026-09-21T20:06:48Z

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
| XRPUSDT | IDLE | 1.09 | 2.32 | 0.53 | 0.07 | 89302611.5 | 1.33 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.75 | 0.23 | 0.05 | 704782760.05 | 0.29 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.46 | 0.2 | 0.07 | 996707204.68 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.37 | 5.49 | 4.43 | 0.04 | 672031.93 | 6.29 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 3.42 | 2.03 | 0.07 | 1141248.54 | 1.09 | skipped_fast |
| WUSDT | IDLE | 1.54 | 3.46 | 1.82 | 0.03 | 595576.9 | 2.56 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 2.76 | 1.23 | 0.07 | 575997.37 | 2.58 | skipped_fast |
| ZBCNUSDT | IDLE | 2.25 | 6.77 | 3.53 | 0.08 | 249680.99 | 28.2 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.87 | 2.02 | -0.0 | 104805.81 | 8.61 | skipped_fast |
| BIOUSDT | IDLE | 1.56 | 2.88 | 1.61 | 0.04 | 100770.43 | 3.47 | skipped_fast |
| CHIPUSDT | IDLE | 1.13 | 5.87 | 1.34 | 0.12 | 141816.01 | 19.09 | skipped_fast |
| EDELUSDT | IDLE | 0.72 | 4.58 | 2.16 | 0.25 | 236674.96 | 29.24 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 2.49 | 1.84 | 0.03 | 76850.45 | 10.16 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 5.24 | 0.36 | 0.09 | 100114.23 | 18.06 | skipped_fast |
| RWAINCUSDT | IDLE | 0.87 | 1.56 | 1.2 | 0.04 | 12320.51 | 11.53 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.53 | 1.23 | 0.03 | 107911.17 | 7.48 | skipped_fast |
| RIZEUSDT | IDLE | 0.77 | 6.2 | 0.47 | -0.1 | 48411.03 | 94.94 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.24 | 0.72 | 0.01 | 56413.37 | 7.25 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.81 | 0.71 | 0.08 | 9962.76 | 49.61 | skipped_fast |
| MNSRYUSDT | IDLE | 0.17 | 0.32 | 0.09 | 0.03 | 42725.71 | 23.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
