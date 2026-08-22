# Hulk DIGEST — 2026-08-22T00:28:11Z

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
| PYTHUSDT | IDLE | 1.75 | 6.39 | 1.13 | 0.1 | 6368657.13 | 2.04 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.02 | 8.23 | 1.31 | 0.15 | 144054414.14 | 3.43 | skipped_fast |
| HBARUSDT | IDLE | 2.79 | 6.36 | 1.5 | 0.07 | 931382.19 | 2.51 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 11.25 | 1.87 | 0.12 | 533433.35 | 60.51 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 7.42 | 1.36 | 0.13 | 648455.01 | 8.03 | skipped_fast |
| WUSDT | IDLE | 2.71 | 6.91 | 0.63 | 0.08 | 384728.8 | 11.19 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.03 | 0.04 | 547629.34 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.65 | 0.03 | 185856.27 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79809.03 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.65 | 0.12 | 59752.7 | 43.33 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.51 | 0.06 | 188899.64 | 46.26 | skipped_fast |
| QNTUSDT | IDLE | 2.56 | 5.42 | 1.37 | 0.06 | 170968.3 | 4.54 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 4.91 | 0.83 | 0.22 | 157831.06 | 19.84 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.28 | 0.1 | 61085.14 | 10.11 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.03 | 9718.83 | 59.19 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54663.76 | 16.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 19.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
