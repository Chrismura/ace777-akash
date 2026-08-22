# Hulk DIGEST — 2026-08-22T02:04:52Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 8.42 | 1.1 | 0.14 | 6885879.31 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.32 | 10.03 | 1.08 | 0.16 | 153928000.71 | 2.68 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.78 | 0.09 | 547459.11 | 13.06 | skipped_fast |
| HBARUSDT | IDLE | 2.31 | 4.9 | 0.5 | 0.08 | 952260.37 | 2.49 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.1 | 0.17 | 0.14 | 658234.29 | 6.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.69 | 0.15 | 0.02 | 516296.8 | 3.04 | skipped_fast |
| BIOUSDT | IDLE | 2.93 | 6.4 | 0.24 | 0.08 | 185063.75 | 17.93 | skipped_fast |
| WUSDT | IDLE | 1.72 | 4.41 | 0.24 | 0.09 | 400259.56 | 17.19 | skipped_fast |
| EDELUSDT | IDLE | 2.38 | 5.02 | 1.63 | -0.02 | 79621.15 | 22.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.0 | 0.11 | 61084.18 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.95 | 0.17 | 156735.89 | 16.98 | skipped_fast |
| QNTUSDT | IDLE | 2.28 | 4.89 | 0.85 | 0.07 | 171110.7 | 1.51 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 4.09 | 0.44 | 0.12 | 61316.74 | 10.78 | skipped_fast |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.05 | 178859.67 | 36.2 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.03 | 9241.73 | 64.41 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.2 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54584.05 | 8.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
