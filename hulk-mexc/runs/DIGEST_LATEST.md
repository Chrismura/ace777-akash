# Hulk DIGEST — 2026-08-22T00:36:36Z

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
| PYTHUSDT | IDLE | 1.77 | 6.5 | 0.85 | 0.11 | 6415735.5 | 2.03 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 8.72 | 1.19 | 0.16 | 145753209.45 | 4.78 | skipped_fast |
| HBARUSDT | IDLE | 2.79 | 6.36 | 1.54 | 0.08 | 939270.67 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.93 | 0.11 | 542397.61 | 22.31 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.65 | 0.14 | 639526.38 | 9.75 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.91 | 0.94 | 0.08 | 388092.23 | 10.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.13 | 0.02 | 554619.24 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.24 | 5.04 | 0.34 | 0.02 | 186063.49 | 6.17 | skipped_fast |
| EDELUSDT | IDLE | 2.6 | 5.5 | 1.63 | -0.02 | 79678.14 | 22.1 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.88 | 0.13 | 59938.68 | 45.4 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.56 | 0.05 | 186233.48 | 36.04 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.33 | 0.06 | 170455.67 | 4.54 | skipped_fast |
| REDUSDT | IDLE | 0.71 | 6.54 | 0.0 | 0.24 | 157971.52 | 48.34 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.2 | 0.1 | 61020.43 | 11.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.04 | 9678.68 | 59.19 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54639.55 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
