# Hulk DIGEST — 2026-08-21T21:36:52Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.6 | 0.1 | 5647324.14 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.11 | 3.73 | 1.09 | 0.11 | 129338759.43 | 3.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.64 | 0.06 | 517146.7 | 6.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.96 | 8.19 | 3.84 | 0.1 | 488804.09 | 36.14 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 3.52 | 0.03 | 0.1 | 647350.16 | 7.31 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.24 | 0.28 | 0.07 | 816681.54 | 5.12 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.83 | 0.46 | 0.06 | 369058.57 | 13.58 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.97 | 0.02 | 187966.13 | 3.13 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.96 | 0.17 | 154154.59 | 10.63 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.23 | 0.02 | 56013.11 | 28.08 | skipped_fast |
| RWAINCUSDT | IDLE | 2.24 | 4.3 | 1.22 | 0.03 | 10157.2 | 5.41 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 4.12 | 1.32 | -0.04 | 83608.62 | 66.74 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.42 | 0.11 | 61020.72 | 13.86 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 4.81 | 1.1 | 0.03 | 182957.64 | 52.77 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 190.93 | skipped_fast |
| QNTUSDT | IDLE | 1.39 | 2.65 | 0.91 | 0.04 | 62892.84 | 10.85 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.49 | 0.03 | 53968.37 | 24.84 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
