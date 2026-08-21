# Hulk DIGEST — 2026-08-21T21:41:42Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.6 | 0.1 | 5652351.31 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.1 | 3.73 | 0.77 | 0.11 | 129394993.5 | 2.85 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 5.61 | 3.88 | 0.04 | 516826.18 | 3.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.95 | 8.19 | 3.7 | 0.1 | 490155.82 | 39.69 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 3.75 | 0.32 | 0.1 | 651816.12 | 9.15 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.24 | 0.14 | 0.07 | 818387.87 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.83 | 0.46 | 0.06 | 369156.22 | 13.58 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.97 | 0.02 | 187812.92 | 3.13 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.49 | 0.17 | 154271.03 | 20.49 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.11 | 0.03 | 55836.45 | 28.08 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 4.12 | 1.21 | -0.04 | 83608.84 | 33.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.03 | 10249.04 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.44 | 0.11 | 61046.98 | 11.05 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 107.85 | skipped_fast |
| TELUSDT | IDLE | 1.89 | 4.81 | 0.73 | 0.03 | 182954.13 | 52.58 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 2.65 | 0.68 | 0.04 | 62618.47 | 3.09 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.41 | 0.03 | 53983.82 | 16.53 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
