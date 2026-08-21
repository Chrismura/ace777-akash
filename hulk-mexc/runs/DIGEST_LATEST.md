# Hulk DIGEST — 2026-08-21T21:42:26Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.16 | 4.51 | 0.43 | 0.1 | 5653835.36 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.6 | 0.11 | 129218282.38 | 1.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.43 | 0.05 | 516841.42 | 9.28 | skipped_fast |
| ZBCNUSDT | IDLE | 1.95 | 8.19 | 3.74 | 0.1 | 490428.13 | 43.29 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 3.75 | 0.32 | 0.1 | 651391.38 | 7.31 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.24 | 0.14 | 0.07 | 818374.28 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.94 | 3.83 | 0.27 | 0.06 | 369156.21 | 14.6 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.9 | 0.02 | 187817.7 | 6.26 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.21 | 0.17 | 154238.34 | 19.67 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.11 | 0.04 | 55808.06 | 28.08 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 4.12 | 0.77 | -0.04 | 83608.84 | 22.2 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.43 | 0.11 | 61095.29 | 10.14 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 95.92 | skipped_fast |
| TELUSDT | IDLE | 1.89 | 4.81 | 0.78 | 0.03 | 183062.23 | 31.51 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 2.65 | 0.55 | 0.04 | 62603.61 | 3.09 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.41 | 0.03 | 53975.1 | 33.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
