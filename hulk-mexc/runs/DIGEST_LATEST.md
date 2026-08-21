# Hulk DIGEST — 2026-08-21T21:54:40Z

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
| PYTHUSDT | IDLE | 1.15 | 4.51 | 0.1 | 0.1 | 5677327.69 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.53 | 0.11 | 130052139.67 | 2.85 | skipped_fast |
| HBARUSDT | IDLE | 2.07 | 4.71 | 0.09 | 0.08 | 830394.08 | 1.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.4 | 0.04 | 526813.39 | 6.18 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 8.19 | 2.66 | 0.11 | 491955.66 | 22.36 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 3.89 | 0.28 | 0.1 | 635602.38 | 10.04 | skipped_fast |
| WUSDT | IDLE | 2.13 | 4.19 | 0.43 | 0.07 | 369166.66 | 10.41 | skipped_fast |
| BIOUSDT | IDLE | 2.38 | 5.2 | 1.32 | 0.04 | 186569.24 | 6.22 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.49 | 0.18 | 154050.19 | 13.01 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.03 | 10222.59 | 10.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 0.92 | 0.04 | 55821.49 | 47.31 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| EDELUSDT | IDLE | 1.89 | 4.12 | 0.44 | -0.03 | 83584.2 | 44.15 | skipped_fast |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.18 | 0.05 | 189414.86 | 62.4 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 1.16 | 0.11 | 61265.82 | 9.19 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.65 | 0.15 | 0.05 | 62555.68 | 7.7 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.17 | 0.08 | 0.04 | 54068.79 | 8.24 | skipped_fast |
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
