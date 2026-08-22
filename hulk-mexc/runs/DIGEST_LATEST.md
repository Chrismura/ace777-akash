# Hulk DIGEST — 2026-08-22T01:30:14Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 10.86 | 0.04 | 0.16 | 6737106.75 | 1.93 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.18 | 8.56 | 0.1 | 0.15 | 150260722.27 | 3.37 | skipped_fast |
| HBARUSDT | IDLE | 3.0 | 6.36 | 0.59 | 0.08 | 951694.49 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.75 | 0.1 | 544899.73 | 2.42 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.28 | 0.34 | 0.16 | 660445.25 | 9.62 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.65 | 1.07 | 0.08 | 392141.0 | 12.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 3.56 | 1.61 | -0.01 | 513538.18 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.57 | 1.07 | 0.04 | 186069.31 | 6.17 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79570.19 | 11.08 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.13 | 0.11 | 60676.01 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.5 | 0.18 | 158508.11 | 7.96 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 6.19 | 1.23 | 0.05 | 181064.84 | 20.74 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.9 | 0.07 | 170114.84 | 6.03 | skipped_fast |
| KITEUSDT | IDLE | 1.49 | 4.63 | 0.08 | 0.12 | 60942.53 | 10.8 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.3 | 2.45 | 1.01 | 0.04 | 9587.29 | 69.69 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54928.51 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
