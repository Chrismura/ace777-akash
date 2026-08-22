# Hulk DIGEST — 2026-08-22T00:26:45Z

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
| PYTHUSDT | IDLE | 1.75 | 6.39 | 1.13 | 0.1 | 6361954.72 | 2.04 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.01 | 8.23 | 1.06 | 0.15 | 143951855.43 | 1.37 | skipped_fast |
| HBARUSDT | IDLE | 2.8 | 6.36 | 1.7 | 0.07 | 933166.52 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.51 | 0.13 | 648459.3 | 6.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.87 | 11.25 | 2.17 | 0.11 | 533556.44 | 78.65 | skipped_fast |
| WUSDT | IDLE | 2.71 | 6.91 | 0.59 | 0.08 | 384683.84 | 9.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.7 | 0.04 | 545093.02 | 6.13 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.65 | 0.02 | 185907.87 | 6.19 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79866.23 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 2.23 | 9.82 | 3.11 | 0.12 | 59739.05 | 43.62 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| QNTUSDT | IDLE | 2.56 | 5.42 | 1.36 | 0.06 | 170967.41 | 3.03 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.51 | 0.06 | 188907.09 | 46.26 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 3.12 | 0.48 | 0.1 | 61103.86 | 9.19 | skipped_fast |
| REDUSDT | IDLE | 0.54 | 4.91 | 0.6 | 0.23 | 157831.72 | 19.84 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.03 | 9718.83 | 59.19 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54706.25 | 8.21 | skipped_fast |
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
