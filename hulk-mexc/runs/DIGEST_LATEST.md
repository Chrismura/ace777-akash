# Hulk DIGEST — 2026-09-06T04:30:33Z

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
| XRPUSDT | IDLE | 1.13 | 2.12 | 0.89 | 0.02 | 24449622.81 | 0.7 | skipped_fast |
| ETHUSDT | IDLE | 0.76 | 1.46 | 0.44 | 0.02 | 202249650.35 | 0.28 | skipped_fast |
| BTCUSDT | IDLE | 0.26 | 0.49 | 0.23 | 0.0 | 375077500.78 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.79 | 5.29 | 1.92 | 0.04 | 441424.56 | 1.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.55 | 5.64 | 3.03 | 0.05 | 423895.96 | 1.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.76 | 5.37 | 0.94 | 0.03 | 8962.63 | 5.25 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.52 | 1.62 | 0.01 | 291717.98 | 6.39 | skipped_fast |
| WUSDT | IDLE | 1.77 | 3.22 | 2.16 | 0.03 | 175218.44 | 0.99 | skipped_fast |
| KITEUSDT | IDLE | 2.13 | 4.06 | 1.28 | -0.03 | 65308.14 | 8.51 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 2.68 | 0.19 | 0.0 | 208124.41 | 18.66 | skipped_fast |
| HBARUSDT | IDLE | 1.5 | 2.85 | 1.01 | 0.03 | 416342.37 | 1.23 | skipped_fast |
| RIZEUSDT | IDLE | 1.28 | 8.56 | 1.55 | 0.07 | 119408.22 | 56.22 | skipped_fast |
| REDUSDT | IDLE | 1.48 | 2.67 | 1.88 | 0.01 | 59311.94 | 8.7 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 1.73 | 0.96 | 0.03 | 96009.03 | 7.15 | skipped_fast |
| EDELUSDT | IDLE | 0.23 | 3.05 | 1.76 | 0.01 | 113440.07 | 28.24 | skipped_fast |
| RWAUSDT | IDLE | 1.52 | 2.7 | 2.28 | 0.04 | 53303.32 | 21.27 | skipped_fast |
| MNSRYUSDT | IDLE | 1.38 | 2.64 | 0.83 | 0.02 | 39656.67 | 4.03 | skipped_fast |
| QNTUSDT | IDLE | 1.29 | 2.33 | 1.66 | 0.03 | 37281.13 | 4.6 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 2.68 | 0.52 | 0.0 | 72782.65 | 29.18 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.82 | 0.0 | 0.03 | 390.92 | 22.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
