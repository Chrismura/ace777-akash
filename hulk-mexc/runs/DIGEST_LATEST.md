# Hulk DIGEST — 2026-08-22T02:37:36Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.59 | 10.52 | 0.85 | 0.16 | 7133781.94 | 11.47 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 12.02 | 0.24 | 0.18 | 156348687.09 | 1.96 | skipped_fast |
| HBARUSDT | IDLE | 2.43 | 5.62 | 0.43 | 0.08 | 977191.58 | 2.47 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 9.63 | 1.63 | 0.1 | 542941.45 | 17.69 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 6.75 | 0.1 | 0.15 | 653770.28 | 6.06 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 5.26 | 0.57 | -0.01 | 459188.1 | 3.01 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.17 | 8.18 | 1.47 | 0.09 | 193658.68 | 2.97 | skipped_fast |
| WUSDT | IDLE | 1.94 | 5.62 | 0.08 | 0.1 | 410722.14 | 13.96 | skipped_fast |
| EDELUSDT | IDLE | 2.42 | 5.02 | 2.17 | -0.03 | 79742.34 | 55.52 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.26 | 0.1 | 61502.68 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.78 | 0.17 | 157849.27 | 21.76 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.24 | 0.08 | 172652.44 | 8.93 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.23 | 0.12 | 62482.43 | 9.85 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9324.96 | 43.38 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.33 | 0.06 | 176322.24 | 51.76 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.83 | skipped_fast |
| RWAUSDT | IDLE | 1.15 | 2.25 | 0.33 | 0.04 | 55277.96 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
