# Hulk DIGEST — 2026-08-19T09:47:42Z

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
| XRPUSDT | IDLE | 0.55 | 1.01 | 0.54 | 0.01 | 10368027.17 | 1.99 | skipped_fast |
| PYTHUSDT | IDLE | 1.11 | 1.94 | 1.83 | 0.02 | 164765.82 | 2.59 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 4.43 | 2.82 | -0.15 | 146002.93 | 14.8 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.63 | 1.22 | 0.03 | 64620.6 | 3.99 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 1.89 | 0.16 | 0.01 | 154513.09 | 5.05 | skipped_fast |
| CHIPUSDT | IDLE | 0.78 | 2.44 | 1.69 | -0.12 | 164474.35 | 3.9 | skipped_fast |
| CCUSDT | IDLE | 0.57 | 1.07 | 0.5 | -0.02 | 213202.19 | 8.89 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.19 | 1.54 | -0.0 | 64925.47 | 16.6 | skipped_fast |
| WUSDT | IDLE | 0.92 | 1.73 | 0.74 | -0.01 | 102623.28 | 17.36 | skipped_fast |
| RIZEUSDT | IDLE | 1.34 | 3.86 | 1.54 | -0.05 | 28416.25 | 51.39 | skipped_fast |
| QAITUSDT | IDLE | 0.76 | 4.96 | 1.59 | -0.17 | 12068.34 | 62.72 | skipped_fast |
| EDELUSDT | IDLE | 1.24 | 2.44 | 0.26 | -0.02 | 59245.65 | 120.24 | skipped_fast |
| RWAINCUSDT | IDLE | 0.83 | 1.49 | 1.12 | -0.03 | 10032.44 | 130.25 | skipped_fast |
| HBARUSDT | IDLE | 0.5 | 0.91 | 0.57 | 0.03 | 125642.96 | 1.48 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 1.42 | 1.07 | 0.01 | 38402.64 | 8.86 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.41 | 1.22 | -0.01 | 52777.82 | 17.61 | skipped_fast |
| TELUSDT | IDLE | 0.65 | 1.25 | 0.27 | 0.04 | 87085.78 | 41.29 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 1.66 | 0.0 | -0.01 | 1163.31 | 22.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
