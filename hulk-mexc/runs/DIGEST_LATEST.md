# Hulk DIGEST — 2026-09-27T01:04:53Z

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
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.32 | 38.65 | 1.32 | 0.65 | 2378578.73 | 14.2 | skipped_fast |
| XRPUSDT | IDLE | 1.02 | 1.9 | 0.94 | -0.03 | 40409180.84 | 1.32 | skipped_fast |
| PYTHUSDT | IDLE | 2.37 | 9.47 | 3.04 | 0.12 | 1286924.15 | 7.31 | skipped_fast |
| ETHUSDT | IDLE | 0.61 | 1.2 | 0.15 | 0.0 | 115243020.43 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.76 | 0.2 | 0.0 | 340794479.81 | 0.0 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.0 | 9.79 | 1.26 | 0.11 | 627076.49 | 23.47 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 3.73 | 1.17 | 0.03 | 801631.29 | 5.16 | skipped_fast |
| EDELUSDT | IDLE | 2.85 | 5.04 | 4.37 | 0.0 | 168576.75 | 6.78 | skipped_fast |
| KITEUSDT | IDLE | 1.86 | 6.5 | 2.66 | 0.11 | 145498.56 | 7.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 4.88 | 1.25 | -0.01 | 103539.84 | 14.28 | skipped_fast |
| ZBCNUSDT | IDLE | 1.56 | 2.74 | 2.55 | -0.03 | 192228.38 | 16.4 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 2.02 | 1.13 | -0.02 | 538661.4 | 1.08 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.67 | 1.05 | -0.02 | 109510.13 | 6.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.95 | 4.93 | 0.38 | 0.1 | 46074.64 | 61.89 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 2.12 | 0.78 | -0.03 | 58734.74 | 7.14 | skipped_fast |
| TELUSDT | IDLE | 1.97 | 3.91 | 0.24 | 0.02 | 125627.92 | 35.91 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.29 | 1.89 | -0.0 | 973.55 | 21.69 | skipped_fast |
| RWAINCUSDT | IDLE | 0.29 | 1.08 | 0.24 | 0.04 | 10100.65 | 78.05 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 1.01 | 0.14 | 0.03 | 56385.91 | 7.14 | skipped_fast |
| MNSRYUSDT | IDLE | 0.5 | 0.95 | 0.34 | -0.0 | 38825.09 | 38.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
