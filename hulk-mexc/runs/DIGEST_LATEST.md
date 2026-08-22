# Hulk DIGEST — 2026-08-22T00:16:36Z

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
| PYTHUSDT | IDLE | 1.78 | 6.39 | 1.77 | 0.1 | 6314689.46 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 2.07 | 8.23 | 2.81 | 0.13 | 143728630.52 | 1.4 | skipped_fast |
| HBARUSDT | IDLE | 2.84 | 6.36 | 2.36 | 0.07 | 929833.2 | 1.27 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.29 | 0.11 | 516293.31 | 5.84 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 7.42 | 2.11 | 0.12 | 644594.01 | 10.79 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.91 | 0.94 | 0.08 | 381474.16 | 10.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 3.56 | 0.24 | 0.05 | 544959.44 | 3.05 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.17 | 0.02 | 186644.64 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.6 | 5.5 | 1.63 | -0.01 | 79816.49 | 11.03 | skipped_fast |
| RIZEUSDT | IDLE | 2.23 | 9.82 | 3.2 | 0.13 | 59461.37 | 45.4 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.05 | 189987.4 | 41.22 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.42 | 1.7 | 0.06 | 169834.76 | 9.12 | skipped_fast |
| REDUSDT | IDLE | 0.58 | 4.91 | 2.85 | 0.19 | 157689.01 | 21.02 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.79 | 0.09 | 61360.13 | 9.22 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.02 | 10272.52 | 59.19 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54585.57 | 24.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 23.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
