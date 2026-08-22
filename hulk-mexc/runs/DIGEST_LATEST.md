# Hulk DIGEST — 2026-08-22T14:53:53Z

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
| PYTHUSDT | IDLE | 1.6 | 7.62 | 2.04 | 0.04 | 51453257.19 | 1.99 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.58 | 5.52 | 0.03 | 213328826.56 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 6.16 | 3.14 | 0.11 | 795934.8 | 6.0 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 3.34 | 3.08 | -0.02 | 1174878.15 | 5.25 | skipped_fast |
| WUSDT | IDLE | 1.13 | 4.43 | 3.5 | -0.02 | 563497.64 | 10.75 | skipped_fast |
| CHIPUSDT | IDLE | 0.65 | 3.51 | 3.02 | -0.11 | 614088.27 | 3.42 | skipped_fast |
| KITEUSDT | IDLE | 2.72 | 6.37 | 1.38 | 0.04 | 84421.35 | 11.59 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 4.21 | 1.92 | -0.07 | 324151.93 | 14.31 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 6.58 | 5.89 | -0.06 | 226030.12 | 6.69 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.63 | 1.56 | -0.04 | 78916.32 | 22.7 | skipped_fast |
| QAITUSDT | IDLE | 2.01 | 3.76 | 1.79 | -0.01 | 2374.33 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.42 | 5.06 | 4.8 | -0.04 | 150746.44 | 21.16 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 3.28 | 0.0 | 0.03 | 46772.01 | 45.5 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.4 | 0.85 | 0.01 | 9946.26 | 75.23 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.3 | -0.01 | 188443.31 | 6.31 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 3.24 | 1.83 | 0.01 | 140088.01 | 53.28 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.55 | 0.72 | 0.02 | 57271.05 | 16.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 21.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
