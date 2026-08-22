# Hulk DIGEST — 2026-08-22T00:28:51Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.19 | 0.1 | 6373581.33 | 2.04 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.01 | 8.23 | 1.11 | 0.15 | 144141663.5 | 3.43 | skipped_fast |
| HBARUSDT | IDLE | 2.8 | 6.36 | 1.68 | 0.07 | 932676.28 | 3.77 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 11.25 | 1.9 | 0.11 | 533390.97 | 64.27 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 7.42 | 1.29 | 0.13 | 648436.68 | 5.34 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.91 | 0.66 | 0.08 | 384701.49 | 12.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.0 | 0.04 | 552909.95 | 6.13 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.58 | 0.02 | 185867.2 | 3.09 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.74 | -0.02 | 79834.0 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.65 | 0.13 | 59812.45 | 21.69 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.31 | 0.06 | 170961.9 | 6.05 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.46 | 0.06 | 188877.47 | 51.39 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 4.91 | 0.78 | 0.22 | 157851.69 | 17.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.04 | 9718.83 | 59.19 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.16 | 0.1 | 61059.79 | 11.0 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54668.05 | 16.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
