# Hulk DIGEST — 2026-09-22T13:10:09Z

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
| XRPUSDT | IDLE | 1.4 | 2.67 | 0.8 | 0.04 | 109987844.96 | 1.95 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.52 | 0.2 | 0.01 | 553558242.97 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.23 | 0.27 | 0.01 | 981589397.01 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.49 | 5.11 | 2.26 | 0.04 | 1143229.72 | 1.05 | skipped_fast |
| PYTHUSDT | IDLE | 1.84 | 3.73 | 0.35 | -0.02 | 751457.09 | 1.57 | skipped_fast |
| CHIPUSDT | IDLE | 3.67 | 6.86 | 3.19 | -0.01 | 165646.28 | 17.0 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.56 | 1.73 | 0.02 | 566985.55 | 6.79 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.48 | 10.74 | 1.02 | 0.09 | 171195.98 | 9.54 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.89 | 0.53 | -0.01 | 373232.47 | 5.85 | skipped_fast |
| EDELUSDT | IDLE | 1.84 | 8.39 | 3.61 | 0.13 | 243918.41 | 39.12 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 8.12 | 0.93 | 0.11 | 116579.59 | 8.91 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 2.87 | 1.74 | -0.03 | 265496.63 | 29.65 | skipped_fast |
| REDUSDT | IDLE | 2.35 | 4.35 | 2.38 | 0.02 | 67188.44 | 42.97 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.78 | 0.14 | -0.0 | 124753.99 | 6.87 | skipped_fast |
| TELUSDT | IDLE | 2.34 | 4.65 | 0.24 | 0.02 | 107339.95 | 18.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 2.18 | 1.04 | 0.06 | 27309.74 | 27.68 | skipped_fast |
| RIZEUSDT | IDLE | 0.35 | 3.26 | 1.65 | -0.14 | 46101.57 | 71.86 | skipped_fast |
| FLUIDUSDT | IDLE | 1.11 | 2.07 | 1.04 | 0.02 | 8571.82 | 21.17 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.36 | 0.0 | 55317.97 | 36.43 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.4 | 0.04 | 0.01 | 40329.57 | 7.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
