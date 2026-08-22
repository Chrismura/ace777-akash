# Hulk DIGEST — 2026-08-22T03:40:31Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 11.15 | 0.17 | 0.18 | 8032619.62 | 1.86 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 14.16 | 1.38 | 0.2 | 164737666.5 | 5.71 | skipped_fast |
| HBARUSDT | IDLE | 2.42 | 6.93 | 0.77 | 0.11 | 1033481.58 | 1.21 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 9.22 | 0.02 | 0.19 | 692221.4 | 5.84 | skipped_fast |
| CHIPUSDT | IDLE | 2.5 | 5.36 | 1.56 | -0.02 | 451989.0 | 5.97 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.2 | 0.08 | 198628.97 | 3.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.4 | 5.16 | 1.26 | 0.13 | 536576.45 | 21.87 | skipped_fast |
| WUSDT | IDLE | 1.81 | 5.83 | 0.21 | 0.12 | 424064.28 | 9.84 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.42 | 0.1 | 59542.92 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.54 | 0.21 | 157902.18 | 19.87 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 3.95 | 2.06 | -0.03 | 80379.13 | 55.59 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 4.61 | 0.0 | 0.12 | 67724.0 | 13.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.06 | 3.6 | 3.48 | 0.0 | 9369.97 | 70.75 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.43 | 0.09 | 174996.39 | 62.24 | skipped_fast |
| RWAUSDT | IDLE | 1.49 | 2.97 | 0.0 | 0.06 | 56298.01 | 8.02 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.45 | 0.51 | 0.07 | 173579.55 | 35.8 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 21.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
