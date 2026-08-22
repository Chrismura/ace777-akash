# Hulk DIGEST — 2026-08-22T01:42:20Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 10.86 | 0.7 | 0.16 | 6808579.04 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 9.48 | 0.07 | 0.16 | 151523166.92 | 2.01 | skipped_fast |
| HBARUSDT | IDLE | 2.98 | 6.36 | 0.33 | 0.09 | 959603.04 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.79 | 0.08 | 549815.65 | 18.88 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 7.36 | 0.24 | 0.16 | 663661.92 | 7.86 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.26 | 0.1 | 394042.26 | 16.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 3.56 | 0.97 | 0.02 | 511986.12 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.48 | 5.57 | 0.4 | 0.05 | 186595.83 | 15.27 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79516.15 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.16 | 0.11 | 60864.86 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.88 | 0.17 | 158595.3 | 18.37 | skipped_fast |
| TELUSDT | IDLE | 2.6 | 6.19 | 1.38 | 0.05 | 182256.82 | 31.17 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.17 | 0.04 | 0.13 | 61676.4 | 10.76 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| QNTUSDT | IDLE | 2.45 | 5.18 | 1.34 | 0.07 | 170714.92 | 21.14 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9242.23 | 85.56 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54672.73 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 50.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
