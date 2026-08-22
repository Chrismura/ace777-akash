# Hulk DIGEST — 2026-08-22T03:24:14Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.38 | 10.96 | 0.22 | 0.18 | 7724675.69 | 3.73 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 14.16 | 0.5 | 0.23 | 163222320.59 | 8.17 | skipped_fast |
| HBARUSDT | IDLE | 2.29 | 6.28 | 0.0 | 0.11 | 1007890.0 | 1.2 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 8.96 | 1.58 | 0.17 | 680899.95 | 6.8 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.14 | 0.07 | 197382.24 | 5.99 | skipped_fast |
| CHIPUSDT | IDLE | 2.0 | 4.43 | 0.36 | -0.01 | 452123.28 | 2.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 5.16 | 1.7 | 0.13 | 538844.95 | 20.56 | skipped_fast |
| WUSDT | IDLE | 1.76 | 5.63 | 0.0 | 0.13 | 421491.42 | 9.84 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 3.83 | 3.37 | -0.04 | 80021.08 | 22.45 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.34 | 0.1 | 59537.02 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 7.96 | 3.25 | 0.21 | 157947.87 | 10.21 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | 0.01 | 9365.24 | 21.62 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 4.4 | 0.44 | 0.12 | 67723.2 | 13.41 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 3808.79 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.72 | 4.14 | 0.0 | 0.09 | 174189.86 | 7.41 | skipped_fast |
| RWAUSDT | IDLE | 1.3 | 2.56 | 0.24 | 0.05 | 56315.27 | 16.12 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 2.19 | 0.41 | 0.06 | 173223.84 | 46.09 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 20.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
