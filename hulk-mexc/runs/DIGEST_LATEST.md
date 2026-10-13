# Hulk DIGEST — 2026-10-13T04:54:46Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.27 | 13.1 | 1.66 | 0.08 | 3772024.53 | 3.46 | skipped_fast |
| WUSDT | IDLE | 0.69 | 11.65 | 6.0 | -0.33 | 11589448.86 | 6.75 | skipped_fast |
| XRPUSDT | IDLE | 2.38 | 4.89 | 0.58 | -0.04 | 35935655.78 | 2.19 | skipped_fast |
| ETHUSDT | IDLE | 2.26 | 4.51 | 0.06 | -0.02 | 284804349.4 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.55 | 3.09 | 0.13 | -0.01 | 362722766.25 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.94 | 6.94 | 0.39 | -0.03 | 417670.51 | 11.31 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 5.15 | 0.63 | -0.06 | 911837.83 | 1.75 | skipped_fast |
| ZBCNUSDT | IDLE | 2.14 | 4.18 | 0.62 | -0.03 | 225568.33 | 26.08 | skipped_fast |
| KITEUSDT | IDLE | 2.52 | 7.34 | 0.02 | -0.01 | 67376.47 | 11.73 | skipped_fast |
| HBARUSDT | IDLE | 1.42 | 4.58 | 0.18 | -0.07 | 594501.51 | 3.41 | skipped_fast |
| REDUSDT | IDLE | 1.07 | 7.82 | 0.73 | 0.03 | 300298.75 | 7.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.68 | 8.57 | 1.37 | -0.08 | 160695.32 | 18.45 | skipped_fast |
| EDELUSDT | IDLE | 1.18 | 5.03 | 2.6 | -0.13 | 288420.5 | 24.24 | skipped_fast |
| BIOUSDT | IDLE | 1.84 | 7.13 | 0.04 | -0.07 | 76300.57 | 3.58 | skipped_fast |
| FLUIDUSDT | IDLE | 3.43 | 6.8 | 0.34 | 0.04 | 13341.67 | 21.14 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 4.15 | 1.12 | 0.01 | 39541.46 | 49.14 | skipped_fast |
| TELUSDT | IDLE | 2.24 | 4.41 | 0.45 | 0.02 | 115576.42 | 34.01 | skipped_fast |
| MNSRYUSDT | IDLE | 1.43 | 2.59 | 1.82 | -0.02 | 39873.87 | 18.15 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 3.0 | 0.62 | -0.08 | 67329.35 | 87.88 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.81 | 0.08 | 0.0 | 53243.49 | 15.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
