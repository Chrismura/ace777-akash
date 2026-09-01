# Hulk DIGEST — 2026-09-01T14:24:06Z

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
| XRPUSDT | IDLE | 1.1 | 2.1 | 0.73 | 0.01 | 30794313.29 | 0.73 | skipped_fast |
| ETHUSDT | IDLE | 0.82 | 1.54 | 0.68 | 0.0 | 306101118.24 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.13 | 0.32 | 0.0 | 554230648.7 | 0.07 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.49 | 14.27 | 0.75 | 0.11 | 453887.6 | 18.17 | skipped_fast |
| PYTHUSDT | IDLE | 2.14 | 4.8 | 2.11 | 0.06 | 594936.59 | 2.0 | skipped_fast |
| CCUSDT | IDLE | 2.3 | 4.08 | 3.43 | -0.0 | 395927.97 | 8.55 | skipped_fast |
| WUSDT | IDLE | 2.06 | 4.07 | 0.36 | 0.06 | 251636.21 | 12.35 | skipped_fast |
| KITEUSDT | IDLE | 2.83 | 5.58 | 0.5 | 0.04 | 60859.84 | 8.95 | skipped_fast |
| ZBCNUSDT | IDLE | 2.1 | 3.87 | 2.23 | 0.03 | 215355.86 | 13.5 | skipped_fast |
| EDELUSDT | IDLE | 0.84 | 5.64 | 3.17 | -0.05 | 173975.94 | 8.62 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 2.57 | 1.02 | 0.03 | 64643.48 | 13.67 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 2.26 | 0.84 | -0.0 | 64857.0 | 3.84 | skipped_fast |
| RIZEUSDT | IDLE | 1.65 | 4.79 | 1.22 | -0.07 | 39377.03 | 69.65 | skipped_fast |
| HBARUSDT | IDLE | 1.28 | 2.41 | 1.01 | 0.02 | 252060.6 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 2.0 | 3.99 | 0.05 | 0.04 | 39750.49 | 3.16 | skipped_fast |
| RWAINCUSDT | IDLE | 0.99 | 1.95 | 0.23 | -0.01 | 4856.09 | 40.78 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.57 | 1.14 | 0.01 | 62954.39 | 23.05 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 1.76 | 1.15 | 0.02 | 97172.99 | 40.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.56 | 0.45 | -0.0 | 33027.32 | 2.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 859.4 | 20.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
