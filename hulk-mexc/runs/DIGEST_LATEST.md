# Hulk DIGEST — 2026-08-22T04:59:36Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.0 | 15.45 | 1.88 | 0.19 | 13173985.79 | 23.72 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 17.46 | 0.64 | 0.26 | 180568379.02 | 9.03 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.54 | 9.87 | 0.43 | 0.14 | 1097573.66 | 6.97 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.24 | 0.2 | 742420.06 | 8.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 5.36 | 1.47 | 0.01 | 446616.99 | 2.99 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 8.62 | 1.09 | 0.15 | 448769.94 | 14.44 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 4.29 | 1.25 | 0.11 | 537326.58 | 24.24 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.0 | 8.75 | 0.09 | 0.09 | 203370.77 | 58.11 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 9.16 | 3.96 | 0.1 | 187012.49 | 4.4 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10345.47 | 21.57 | skipped_fast |
| KITEUSDT | IDLE | 1.76 | 6.71 | 0.1 | 0.15 | 68375.36 | 12.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.68 | 0.09 | 58606.36 | 46.02 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 4.07 | 2.17 | -0.03 | 80195.04 | 33.28 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.54 | 0.21 | 157897.04 | 18.37 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.49 | 0.1 | 183538.81 | 14.88 | skipped_fast |
| RWAUSDT | IDLE | 1.56 | 3.13 | 0.0 | 0.07 | 56536.69 | 7.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3692.42 | 22.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
