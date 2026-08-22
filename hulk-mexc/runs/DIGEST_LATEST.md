# Hulk DIGEST — 2026-08-22T01:21:36Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 10.28 | 0.04 | 0.15 | 6673083.6 | 15.55 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.18 | 8.4 | 0.47 | 0.15 | 149965825.4 | 4.75 | skipped_fast |
| HBARUSDT | IDLE | 3.02 | 6.36 | 0.83 | 0.08 | 955225.55 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.91 | 0.1 | 546433.69 | 28.09 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 7.28 | 0.12 | 0.16 | 659510.4 | 9.6 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.65 | 0.97 | 0.08 | 392205.35 | 10.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.09 | -0.0 | 519328.68 | 6.15 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.57 | 0.88 | 0.04 | 186526.56 | 6.15 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79560.25 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.16 | 0.11 | 60559.46 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.4 | 0.18 | 159148.91 | 9.54 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.85 | 0.07 | 170353.37 | 4.52 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 4.63 | 0.24 | 0.12 | 60848.13 | 10.82 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.66 | 0.05 | 181068.07 | 46.38 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.02 | 9586.1 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.7 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 55104.39 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
