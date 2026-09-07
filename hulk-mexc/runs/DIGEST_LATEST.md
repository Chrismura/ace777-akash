# Hulk DIGEST — 2026-09-07T15:36:11Z

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
| XRPUSDT | IDLE | 1.2 | 2.12 | 1.81 | -0.01 | 35097604.34 | 1.44 | skipped_fast |
| ETHUSDT | IDLE | 0.93 | 1.65 | 1.41 | -0.0 | 325138876.63 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.03 | 0.93 | -0.01 | 432150997.51 | 0.51 | skipped_fast |
| PYTHUSDT | IDLE | 2.28 | 4.03 | 3.59 | 0.01 | 553290.08 | 3.65 | skipped_fast |
| CHIPUSDT | IDLE | 2.1 | 7.24 | 6.64 | -0.09 | 290105.33 | 7.74 | skipped_fast |
| WUSDT | IDLE | 1.87 | 3.32 | 2.76 | -0.02 | 407319.21 | 12.78 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 2.73 | 2.6 | -0.03 | 419386.27 | 9.43 | skipped_fast |
| HBARUSDT | IDLE | 1.91 | 3.44 | 2.51 | 0.01 | 511931.07 | 4.93 | skipped_fast |
| RIZEUSDT | IDLE | 2.17 | 9.74 | 8.36 | -0.09 | 60167.8 | 66.55 | skipped_fast |
| REDUSDT | IDLE | 2.2 | 4.1 | 1.94 | 0.04 | 63828.39 | 11.31 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 2.81 | 1.84 | -0.0 | 194136.7 | 29.51 | skipped_fast |
| BIOUSDT | IDLE | 1.69 | 2.97 | 2.78 | -0.01 | 69527.9 | 7.41 | skipped_fast |
| EDELUSDT | IDLE | 1.67 | 4.55 | 4.06 | -0.04 | 79027.04 | 50.38 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.19 | 1.92 | -0.04 | 59562.22 | 10.77 | skipped_fast |
| MNSRYUSDT | IDLE | 2.8 | 5.35 | 1.72 | -0.02 | 38206.08 | 66.8 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 3.75 | 0.81 | 0.08 | 5369.45 | 91.5 | skipped_fast |
| QNTUSDT | IDLE | 1.17 | 2.12 | 1.44 | 0.0 | 46856.09 | 1.53 | skipped_fast |
| TELUSDT | IDLE | 1.06 | 1.89 | 1.56 | -0.0 | 110850.5 | 23.53 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.73 | 0.43 | -0.0 | 52022.64 | 21.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 1152.45 | 21.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
