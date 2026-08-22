# Hulk DIGEST — 2026-08-22T03:25:50Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 11.15 | 0.17 | 0.18 | 7743950.21 | 1.86 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.36 | 0.21 | 163814117.12 | 4.44 | skipped_fast |
| HBARUSDT | IDLE | 2.3 | 6.29 | 0.17 | 0.11 | 1014643.61 | 1.21 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 8.96 | 1.8 | 0.17 | 681638.98 | 5.11 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 7.36 | 1.99 | 0.08 | 198083.69 | 2.99 | skipped_fast |
| CHIPUSDT | IDLE | 2.02 | 4.43 | 0.62 | -0.02 | 452417.5 | 5.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 5.16 | 1.58 | 0.13 | 538764.1 | 4.78 | skipped_fast |
| WUSDT | IDLE | 1.77 | 5.63 | 0.02 | 0.13 | 421487.26 | 5.9 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 3.83 | 3.15 | -0.03 | 79971.07 | 22.45 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.42 | 0.1 | 59531.96 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.19 | 0.21 | 157964.31 | 10.21 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9338.84 | 37.87 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 4.4 | 0.14 | 0.12 | 67699.41 | 9.82 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.75 | 4.26 | 0.0 | 0.09 | 174205.65 | 10.37 | skipped_fast |
| RWAUSDT | IDLE | 1.29 | 2.56 | 0.08 | 0.05 | 56241.09 | 8.06 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 2.19 | 0.51 | 0.07 | 173257.83 | 51.23 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 16.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
