# Hulk DIGEST — 2026-08-21T21:24:03Z

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
| PYTHUSDT | IDLE | 1.19 | 4.51 | 1.03 | 0.09 | 5620322.47 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.13 | 3.73 | 1.61 | 0.11 | 128786410.99 | 0.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.92 | 5.61 | 4.65 | 0.05 | 517065.39 | 6.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.96 | 8.19 | 4.08 | 0.1 | 484530.7 | 23.22 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.3 | 0.1 | 644391.92 | 8.28 | skipped_fast |
| HBARUSDT | IDLE | 1.57 | 3.04 | 0.72 | 0.07 | 809511.56 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.83 | 0.58 | 0.06 | 366593.73 | 9.42 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.2 | 2.58 | 0.01 | 186789.97 | 6.3 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.54 | 0.17 | 153657.6 | 18.08 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10270.17 | 5.38 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 4.12 | 2.31 | -0.05 | 82616.59 | 33.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.41 | 0.02 | 56202.43 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 4.0 | 1.89 | 0.11 | 61038.89 | 10.18 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3754.88 | 155.41 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 3.39 | 0.69 | 0.02 | 178965.46 | 37.28 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60689.07 | 1.56 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.17 | 0.74 | 0.03 | 53873.41 | 33.17 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.08 | 4161.15 | 41.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
