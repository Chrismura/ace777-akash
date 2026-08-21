# Hulk DIGEST — 2026-08-21T22:00:11Z

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
| PYTHUSDT | IDLE | 1.22 | 4.74 | 0.39 | 0.1 | 5689875.77 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.59 | 0.12 | 129653847.91 | 2.85 | skipped_fast |
| HBARUSDT | IDLE | 2.09 | 4.71 | 0.38 | 0.08 | 833706.13 | 1.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.52 | 0.04 | 527084.32 | 6.18 | skipped_fast |
| ZBCNUSDT | IDLE | 1.9 | 8.19 | 2.14 | 0.11 | 493687.37 | 28.66 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 3.92 | 0.02 | 0.11 | 635833.32 | 8.2 | skipped_fast |
| WUSDT | IDLE | 2.11 | 4.19 | 0.17 | 0.07 | 367602.51 | 11.43 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 5.2 | 1.14 | 0.03 | 186133.49 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.51 | 0.18 | 153867.38 | 13.0 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.24 | 11.42 | 1.54 | 0.05 | 56596.96 | 45.14 | skipped_fast |
| EDELUSDT | IDLE | 1.88 | 4.12 | 0.22 | -0.03 | 83195.0 | 22.3 | skipped_fast |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.23 | 0.05 | 191563.58 | 25.99 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.9 | 0.03 | 10238.87 | 53.39 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 1.12 | 0.11 | 61229.06 | 9.19 | skipped_fast |
| QNTUSDT | IDLE | 1.25 | 2.49 | 0.08 | 0.05 | 62402.33 | 3.08 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.33 | 0.08 | 0.04 | 54125.39 | 16.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
