# Hulk DIGEST — 2026-10-13T05:56:07Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.28 | 13.1 | 1.85 | 0.09 | 3792296.29 | 4.61 | skipped_fast |
| WUSDT | IDLE | 0.68 | 11.65 | 5.55 | -0.31 | 11149614.51 | 12.93 | skipped_fast |
| ETHUSDT | IDLE | 2.68 | 5.31 | 0.33 | -0.02 | 265449950.03 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.4 | 4.9 | 0.08 | -0.03 | 35609207.76 | 0.73 | skipped_fast |
| BTCUSDT | IDLE | 1.77 | 3.49 | 0.27 | -0.01 | 366181245.67 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.21 | 5.95 | 0.17 | -0.03 | 915646.58 | 3.03 | skipped_fast |
| CCUSDT | IDLE | 3.11 | 7.38 | 0.22 | -0.02 | 423316.42 | 11.24 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 9.09 | 0.63 | -0.06 | 75252.74 | 7.08 | skipped_fast |
| KITEUSDT | IDLE | 2.66 | 7.74 | 0.07 | -0.01 | 67202.45 | 12.48 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 5.31 | 0.7 | -0.07 | 575373.5 | 9.08 | skipped_fast |
| ZBCNUSDT | IDLE | 2.13 | 4.18 | 0.6 | -0.02 | 214473.99 | 16.24 | skipped_fast |
| REDUSDT | IDLE | 1.2 | 8.72 | 1.08 | 0.03 | 312473.82 | 13.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.83 | 8.57 | 0.5 | -0.09 | 153410.03 | 11.64 | skipped_fast |
| EDELUSDT | IDLE | 0.92 | 3.88 | 1.7 | -0.13 | 284993.43 | 18.22 | skipped_fast |
| FLUIDUSDT | IDLE | 3.43 | 6.8 | 0.34 | 0.04 | 13027.01 | 21.79 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 4.81 | 0.34 | 0.04 | 40370.57 | 14.54 | skipped_fast |
| TELUSDT | IDLE | 2.43 | 4.81 | 0.39 | 0.03 | 112826.43 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 3.02 | 0.39 | -0.11 | 67288.39 | 60.49 | skipped_fast |
| RWAUSDT | IDLE | 0.95 | 1.88 | 0.08 | 0.0 | 53536.77 | 7.71 | skipped_fast |
| MNSRYUSDT | IDLE | 1.24 | 2.36 | 0.78 | -0.01 | 39814.62 | 42.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
