# Hulk DIGEST — 2026-08-21T23:44:49Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.55 | 0.1 | 6165619.31 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.95 | 8.23 | 0.87 | 0.15 | 141640099.7 | 1.37 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 11.25 | 1.74 | 0.13 | 514124.01 | 2.39 | skipped_fast |
| HBARUSDT | IDLE | 2.61 | 6.36 | 0.92 | 0.09 | 909831.92 | 1.25 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 0.99 | 0.13 | 646049.9 | 8.89 | skipped_fast |
| WUSDT | IDLE | 2.77 | 6.91 | 1.69 | 0.08 | 379987.36 | 11.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.46 | 0.03 | 547353.11 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.8 | 0.02 | 186459.26 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 2.57 | 5.5 | 1.19 | -0.04 | 82659.51 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.2 | 9.82 | 4.5 | 0.13 | 58854.29 | 46.02 | skipped_fast |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.26 | 0.07 | 190301.9 | 25.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10299.86 | 21.39 | skipped_fast |
| REDUSDT | IDLE | 0.86 | 7.3 | 4.29 | 0.19 | 157787.6 | 11.26 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.04 | 0.08 | 147095.45 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 1.0 | 0.1 | 61415.69 | 12.93 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54563.5 | 24.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 21.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
