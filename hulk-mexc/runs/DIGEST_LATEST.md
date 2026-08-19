# Hulk DIGEST — 2026-08-19T06:51:18Z

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
| XRPUSDT | IDLE | 0.43 | 0.83 | 0.14 | 0.01 | 10009502.69 | 1.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 5.54 | 4.32 | -0.08 | 184968.67 | 3.89 | skipped_fast |
| PYTHUSDT | IDLE | 1.7 | 3.14 | 1.7 | 0.02 | 167442.03 | 5.17 | skipped_fast |
| REDUSDT | IDLE | 1.29 | 5.99 | 3.82 | -0.16 | 154965.46 | 27.21 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 1.77 | 1.17 | -0.01 | 215327.14 | 10.01 | skipped_fast |
| EDELUSDT | IDLE | 1.52 | 2.71 | 2.24 | -0.04 | 59214.04 | 13.49 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 2.3 | 1.75 | -0.03 | 65521.73 | 16.62 | skipped_fast |
| ZBCNUSDT | IDLE | 0.81 | 1.57 | 0.27 | 0.0 | 156971.59 | 3.18 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 2.07 | 0.08 | 0.03 | 61740.88 | 3.99 | skipped_fast |
| WUSDT | IDLE | 0.81 | 1.58 | 0.21 | -0.01 | 118615.75 | 14.82 | skipped_fast |
| RWAINCUSDT | IDLE | 0.68 | 1.49 | 0.12 | 0.01 | 10568.94 | 29.58 | skipped_fast |
| QAITUSDT | IDLE | 0.56 | 3.72 | 0.62 | -0.14 | 9517.2 | 50.53 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.18 | 0.22 | 0.03 | 120593.78 | 1.47 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.63 | 0.0 | 0.01 | 38117.84 | 3.53 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.5 | 1.13 | -0.01 | 51658.38 | 17.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.56 | 4.17 | 4.0 | -0.05 | 27498.26 | 269.02 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.68 | 0.58 | -0.01 | 187.92 | 23.89 | skipped_fast |
| TELUSDT | IDLE | 0.67 | 1.25 | 0.62 | 0.04 | 87752.23 | 48.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
