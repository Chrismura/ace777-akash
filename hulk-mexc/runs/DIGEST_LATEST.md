# Hulk DIGEST — 2026-08-22T00:59:52Z

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
| PYTHUSDT | IDLE | 1.99 | 7.38 | 0.42 | 0.13 | 6542741.72 | 2.01 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 8.72 | 1.37 | 0.15 | 147916574.62 | 2.05 | skipped_fast |
| HBARUSDT | IDLE | 2.79 | 6.36 | 1.5 | 0.08 | 951087.64 | 3.77 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.89 | 0.11 | 543485.54 | 25.19 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.62 | 0.15 | 651435.68 | 8.86 | skipped_fast |
| WUSDT | IDLE | 2.71 | 6.91 | 0.48 | 0.1 | 391599.09 | 11.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.55 | 3.56 | 0.21 | 0.02 | 539769.59 | 6.09 | skipped_fast |
| BIOUSDT | IDLE | 2.5 | 5.62 | 0.31 | 0.04 | 186671.6 | 3.07 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.28 | -0.02 | 79753.12 | 22.17 | skipped_fast |
| RIZEUSDT | IDLE | 2.26 | 9.82 | 3.95 | 0.11 | 60273.55 | 45.71 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.72 | 0.06 | 183784.03 | 5.16 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.58 | 2.8 | 0.2 | 159362.61 | 18.81 | skipped_fast |
| QNTUSDT | IDLE | 2.52 | 5.42 | 0.79 | 0.07 | 170539.12 | 3.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.02 | 9620.44 | 16.16 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.22 | 1.21 | 0.01 | 3850.39 | 67.05 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 4.3 | 0.06 | 0.11 | 60908.52 | 19.95 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54913.39 | 8.22 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 0.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
