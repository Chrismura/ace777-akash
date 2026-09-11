# Hulk DIGEST — 2026-09-11T08:17:48Z

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
| XRPUSDT | IDLE | 0.89 | 1.67 | 0.68 | -0.02 | 39844384.63 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.33 | 0.24 | -0.0 | 456104288.42 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.93 | 0.27 | -0.01 | 540493996.47 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.4 | 35.33 | 23.23 | 0.13 | 143738.68 | 171.43 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 6.92 | 4.28 | -0.07 | 124322.08 | 13.18 | skipped_fast |
| CCUSDT | IDLE | 1.11 | 2.1 | 0.78 | -0.05 | 449041.3 | 8.1 | skipped_fast |
| PYTHUSDT | IDLE | 1.17 | 2.27 | 0.5 | -0.0 | 342419.45 | 1.94 | skipped_fast |
| WUSDT | IDLE | 1.49 | 2.72 | 1.7 | -0.01 | 144009.62 | 14.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.54 | 0.2 | -0.04 | 200261.88 | 15.94 | skipped_fast |
| EDELUSDT | IDLE | 0.82 | 3.53 | 2.95 | -0.07 | 199232.03 | 18.98 | skipped_fast |
| REDUSDT | IDLE | 1.17 | 2.19 | 1.03 | -0.01 | 59651.25 | 10.68 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.57 | 0.95 | -0.02 | 72647.88 | 4.0 | skipped_fast |
| KITEUSDT | IDLE | 0.95 | 1.71 | 1.32 | -0.04 | 58937.27 | 12.99 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 1.85 | 0.44 | 0.02 | 3171.51 | 16.6 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.79 | 1.48 | -0.02 | 186478.66 | 2.68 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 2.26 | 1.47 | -0.04 | 96052.17 | 34.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 2.26 | 2.04 | -0.03 | 2138.71 | 21.83 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 1.46 | 0.69 | -0.03 | 36106.12 | 3.09 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.77 | 0.08 | -0.02 | 49994.95 | 15.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.6 | 0.01 | -0.01 | 35786.06 | 4.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
