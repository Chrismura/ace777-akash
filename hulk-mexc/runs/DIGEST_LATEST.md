# Hulk DIGEST — 2026-09-22T21:15:18Z

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
| XRPUSDT | IDLE | 2.18 | 4.05 | 2.09 | 0.04 | 116406897.23 | 1.9 | skipped_fast |
| HBARUSDT | IDLE | 2.49 | 6.27 | 1.41 | 0.08 | 1682058.35 | 2.02 | skipped_fast |
| PYTHUSDT | IDLE | 0.71 | 3.25 | 1.95 | 0.04 | 1675970.16 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.66 | 1.24 | 0.57 | -0.01 | 411737852.94 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.67 | 0.47 | -0.0 | 921052198.18 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.86 | 3.41 | 2.06 | -0.03 | 478328.43 | 3.53 | skipped_fast |
| EDELUSDT | IDLE | 2.47 | 10.49 | 8.07 | -0.01 | 287022.28 | 56.81 | skipped_fast |
| ZBCNUSDT | IDLE | 2.54 | 4.6 | 3.24 | -0.02 | 215641.51 | 6.96 | skipped_fast |
| RWAINCUSDT | IDLE | 3.56 | 9.09 | 3.94 | 0.03 | 18864.36 | 94.89 | skipped_fast |
| WUSDT | IDLE | 1.55 | 2.81 | 1.87 | 0.02 | 335106.96 | 2.51 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 22.04 | 3.04 | -0.07 | 46883.43 | 111.73 | skipped_fast |
| CHIPUSDT | IDLE | 2.09 | 3.97 | 2.88 | -0.01 | 138669.06 | 17.68 | skipped_fast |
| BIOUSDT | IDLE | 1.69 | 3.19 | 1.31 | 0.02 | 136418.31 | 3.41 | skipped_fast |
| KITEUSDT | IDLE | 0.81 | 3.49 | 1.44 | 0.16 | 112808.92 | 10.88 | skipped_fast |
| REDUSDT | IDLE | 1.11 | 2.14 | 0.54 | 0.05 | 63676.59 | 14.56 | skipped_fast |
| TELUSDT | IDLE | 1.54 | 5.95 | 0.16 | 0.11 | 106676.08 | 21.86 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.86 | 0.0 | 0.09 | 172286.46 | 1.36 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.24 | 0.36 | -0.0 | 53588.19 | 7.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.18 | 0.12 | 0.01 | 7050.54 | 19.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.01 | -0.0 | 40265.79 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
