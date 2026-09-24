# Hulk DIGEST — 2026-09-24T18:38:56Z

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
| XRPUSDT | IDLE | 2.24 | 4.37 | 0.68 | 0.03 | 69405296.42 | 2.61 | skipped_fast |
| PYTHUSDT | IDLE | 3.19 | 11.6 | 4.81 | 0.08 | 1281552.02 | 2.96 | skipped_fast |
| ETHUSDT | IDLE | 1.18 | 2.24 | 0.84 | 0.01 | 333443954.9 | 0.82 | skipped_fast |
| BTCUSDT | IDLE | 1.09 | 2.04 | 0.9 | 0.0 | 708022104.95 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.2 | 6.06 | 2.31 | 0.04 | 471422.59 | 9.86 | skipped_fast |
| HBARUSDT | IDLE | 2.52 | 4.67 | 2.43 | 0.03 | 875938.05 | 1.08 | skipped_fast |
| CHIPUSDT | IDLE | 3.57 | 11.66 | 2.57 | 0.08 | 73566.07 | 17.64 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.2 | 10.36 | 1.74 | 0.1 | 85534.54 | 9.65 | skipped_fast |
| WUSDT | IDLE | 2.46 | 4.66 | 1.67 | 0.04 | 233229.4 | 5.97 | skipped_fast |
| ZBCNUSDT | IDLE | 2.65 | 5.08 | 1.5 | 0.03 | 215677.09 | 31.1 | skipped_fast |
| EDELUSDT | IDLE | 2.32 | 6.17 | 1.59 | 0.01 | 154509.17 | 14.3 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.57 | 14.51 | 0.7 | 0.15 | 10332.38 | 130.96 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 15.06 | 0.79 | 0.21 | 204494.62 | 17.56 | skipped_fast |
| REDUSDT | IDLE | 2.01 | 5.36 | 1.47 | 0.05 | 100202.59 | 14.39 | skipped_fast |
| RIZEUSDT | IDLE | 2.16 | 11.1 | 4.22 | 0.16 | 54015.24 | 93.81 | skipped_fast |
| TELUSDT | IDLE | 2.94 | 5.45 | 2.82 | -0.03 | 107740.17 | 24.14 | skipped_fast |
| KITEUSDT | IDLE | 1.63 | 3.06 | 1.33 | 0.0 | 69374.51 | 11.31 | skipped_fast |
| FLUIDUSDT | IDLE | 2.41 | 4.77 | 0.28 | 0.05 | 2637.47 | 14.9 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.92 | 0.22 | 0.02 | 56180.02 | 7.28 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.23 | 0.14 | 0.0 | 37271.18 | 3.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
