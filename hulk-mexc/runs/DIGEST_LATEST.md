# Hulk DIGEST — 2026-10-13T03:55:06Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.79 | 11.21 | 1.22 | 0.05 | 3711803.12 | 3.5 | skipped_fast |
| WUSDT | IDLE | 0.69 | 11.65 | 6.67 | -0.32 | 12451378.58 | 7.83 | skipped_fast |
| XRPUSDT | IDLE | 2.38 | 4.89 | 0.52 | -0.03 | 37061010.18 | 2.19 | skipped_fast |
| ETHUSDT | IDLE | 2.15 | 4.27 | 0.17 | -0.01 | 287480372.77 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 1.56 | 3.09 | 0.26 | -0.0 | 361917101.06 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.8 | 5.06 | 0.37 | -0.04 | 871039.17 | 0.88 | skipped_fast |
| CCUSDT | IDLE | 2.36 | 5.58 | 0.29 | -0.03 | 420065.64 | 8.18 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 5.4 | 1.35 | -0.07 | 633949.58 | 5.71 | skipped_fast |
| EDELUSDT | IDLE | 1.53 | 6.64 | 4.13 | -0.14 | 294689.53 | 18.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.98 | 3.89 | 0.53 | -0.02 | 233360.47 | 25.67 | skipped_fast |
| CHIPUSDT | IDLE | 1.73 | 8.57 | 2.9 | -0.08 | 162504.65 | 11.96 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 7.82 | 0.3 | 0.04 | 297615.17 | 12.67 | skipped_fast |
| BIOUSDT | IDLE | 2.02 | 7.56 | 1.64 | -0.08 | 75522.57 | 7.25 | skipped_fast |
| KITEUSDT | IDLE | 2.2 | 6.28 | 0.86 | -0.02 | 66849.83 | 10.36 | skipped_fast |
| FLUIDUSDT | IDLE | 2.93 | 5.82 | 0.22 | 0.05 | 13531.83 | 21.27 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.9 | 1.65 | 0.02 | 37945.72 | 4.94 | skipped_fast |
| TELUSDT | IDLE | 2.05 | 4.0 | 0.62 | 0.02 | 117008.03 | 34.21 | skipped_fast |
| MNSRYUSDT | IDLE | 1.47 | 2.66 | 1.81 | -0.02 | 40006.54 | 2.79 | skipped_fast |
| RIZEUSDT | IDLE | 0.41 | 2.83 | 0.08 | -0.05 | 71057.12 | 83.35 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.81 | 0.08 | 0.0 | 53234.9 | 15.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
