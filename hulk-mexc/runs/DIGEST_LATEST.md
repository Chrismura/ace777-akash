# Hulk DIGEST — 2026-08-22T00:24:28Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.25 | 0.1 | 6349386.92 | 2.04 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.03 | 8.23 | 1.58 | 0.14 | 143813110.41 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.81 | 0.07 | 931015.6 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.77 | 0.11 | 518836.57 | 15.48 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 7.42 | 1.9 | 0.12 | 646514.21 | 8.97 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.91 | 0.76 | 0.08 | 384688.31 | 14.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 3.56 | 0.58 | 0.04 | 545182.02 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.68 | 0.02 | 185793.03 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.01 | 79841.23 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 2.23 | 9.82 | 2.94 | 0.14 | 59823.48 | 43.62 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.51 | 0.06 | 170957.99 | 3.03 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.51 | 0.06 | 188818.83 | 46.31 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 3.12 | 0.56 | 0.09 | 61302.95 | 11.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.03 | 9727.87 | 59.19 | skipped_fast |
| REDUSDT | IDLE | 0.54 | 4.91 | 0.42 | 0.22 | 157812.71 | 37.06 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 54760.65 | 16.41 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
