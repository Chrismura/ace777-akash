# Hulk DIGEST — 2026-08-21T21:38:49Z

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
| PYTHUSDT | IDLE | 1.16 | 4.51 | 0.45 | 0.1 | 5648157.33 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.11 | 3.73 | 1.0 | 0.11 | 129379921.24 | 2.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 5.61 | 3.82 | 0.05 | 517097.52 | 6.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.95 | 8.19 | 3.59 | 0.11 | 489403.99 | 29.1 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 3.75 | 0.09 | 0.1 | 650964.66 | 7.3 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.24 | 0.08 | 0.07 | 817651.56 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.83 | 0.4 | 0.06 | 368992.3 | 14.62 | skipped_fast |
| BIOUSDT | IDLE | 2.41 | 5.2 | 1.81 | 0.02 | 187894.4 | 3.13 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.2 | 0.17 | 154178.55 | 19.64 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.06 | 0.02 | 56007.32 | 28.08 | skipped_fast |
| EDELUSDT | IDLE | 1.91 | 4.12 | 0.66 | -0.04 | 83583.77 | 33.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.03 | 10249.04 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.48 | 0.11 | 61020.73 | 9.22 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 119.76 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 4.81 | 1.46 | 0.03 | 182884.13 | 58.37 | skipped_fast |
| QNTUSDT | IDLE | 1.39 | 2.65 | 0.8 | 0.04 | 62881.15 | 4.65 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.17 | 0.58 | 0.03 | 53972.63 | 24.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
