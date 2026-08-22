# Hulk DIGEST — 2026-08-22T00:15:02Z

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
| PYTHUSDT | IDLE | 1.78 | 6.39 | 1.81 | 0.1 | 6310991.15 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 2.07 | 8.23 | 2.95 | 0.13 | 143683997.6 | 2.1 | skipped_fast |
| HBARUSDT | IDLE | 2.85 | 6.36 | 2.4 | 0.07 | 929436.73 | 1.27 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.4 | 0.11 | 516061.78 | 43.85 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 7.42 | 1.91 | 0.12 | 645485.75 | 6.28 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.18 | 0.08 | 381430.17 | 8.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.49 | 0.05 | 544967.58 | 6.11 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.26 | 0.02 | 187101.47 | 3.12 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.41 | -0.01 | 79841.44 | 22.05 | skipped_fast |
| RIZEUSDT | IDLE | 2.23 | 9.82 | 3.22 | 0.13 | 59456.17 | 45.4 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.85 | 6.89 | 0.77 | 0.05 | 190045.25 | 46.38 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.42 | 1.82 | 0.05 | 167500.68 | 13.7 | skipped_fast |
| REDUSDT | IDLE | 0.58 | 4.91 | 2.77 | 0.19 | 157494.86 | 10.51 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.78 | 0.09 | 61416.32 | 12.0 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.01 | 10306.29 | 80.8 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54665.51 | 32.81 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 35.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
