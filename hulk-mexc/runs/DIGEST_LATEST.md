# Hulk DIGEST — 2026-08-22T02:19:07Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 8.42 | 0.95 | 0.14 | 6939442.74 | 9.74 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 10.26 | 0.05 | 0.17 | 154076117.19 | 4.63 | skipped_fast |
| HBARUSDT | IDLE | 2.28 | 4.9 | 0.01 | 0.08 | 961620.79 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.75 | 0.09 | 544660.52 | 13.55 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.16 | 0.01 | 0.15 | 654343.96 | 9.58 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 5.07 | 0.42 | -0.0 | 514715.13 | 6.02 | skipped_fast |
| BIOUSDT | IDLE | 3.05 | 7.64 | 0.03 | 0.1 | 192528.18 | 5.9 | skipped_fast |
| WUSDT | IDLE | 1.81 | 4.9 | 0.0 | 0.1 | 401110.2 | 4.01 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.77 | 0.11 | 61266.03 | 32.15 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 8.27 | 7.37 | 0.17 | 156983.19 | 18.81 | skipped_fast |
| EDELUSDT | IDLE | 2.4 | 5.02 | 1.85 | -0.02 | 79723.92 | 77.73 | skipped_fast |
| QNTUSDT | IDLE | 2.26 | 4.89 | 0.54 | 0.08 | 171170.67 | 4.5 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.66 | 0.12 | 61613.1 | 12.61 | skipped_fast |
| QAITUSDT | IDLE | 1.86 | 3.57 | 0.94 | 0.0 | 3916.13 | 39.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.01 | 9406.34 | 43.38 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.13 | 0.05 | 179441.28 | 36.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 16.88 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54795.03 | 16.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
