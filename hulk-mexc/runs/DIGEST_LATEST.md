# Hulk DIGEST — 2026-08-22T04:48:27Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.96 | 15.45 | 0.41 | 0.21 | 12073760.61 | 8.99 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.38 | 16.63 | 0.14 | 0.27 | 177120211.11 | 6.03 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 8.85 | 0.23 | 0.14 | 1074016.27 | 1.17 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.51 | 0.2 | 737713.33 | 10.68 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 5.36 | 1.47 | 0.01 | 451041.95 | 2.98 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 8.34 | 0.0 | 0.15 | 433982.54 | 18.14 | skipped_fast |
| BIOUSDT | IDLE | 2.94 | 7.36 | 1.14 | 0.06 | 200973.62 | 2.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 0.94 | 0.12 | 537934.38 | 23.21 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 4.07 | 2.5 | -0.02 | 80195.44 | 22.17 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 8.56 | 4.53 | 0.1 | 182320.83 | 20.67 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.54 | 0.09 | 58574.97 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.46 | 0.21 | 158110.93 | 18.31 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.69 | 0.0 | 0.14 | 67967.26 | 21.12 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.59 | 0.1 | 182254.44 | 24.83 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.01 | 9540.48 | 97.61 | skipped_fast |
| RWAUSDT | IDLE | 1.53 | 3.05 | 0.08 | 0.06 | 56602.98 | 16.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 20.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
