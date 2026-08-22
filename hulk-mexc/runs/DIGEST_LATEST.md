# Hulk DIGEST — 2026-08-22T03:12:16Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 10.96 | 0.65 | 0.18 | 7604367.64 | 3.75 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 11.43 | 0.71 | 0.2 | 160801745.41 | 2.59 | skipped_fast |
| HBARUSDT | IDLE | 2.17 | 5.29 | 0.55 | 0.1 | 997247.89 | 1.22 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 8.96 | 0.62 | 0.19 | 671378.97 | 5.9 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.43 | 0.06 | 195696.38 | 3.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 4.28 | 0.27 | -0.01 | 449073.59 | 5.97 | skipped_fast |
| WUSDT | IDLE | 1.79 | 5.61 | 0.51 | 0.12 | 418076.35 | 7.91 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 5.16 | 2.69 | 0.13 | 541104.9 | 45.92 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.46 | 0.1 | 59508.97 | 28.89 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 3.83 | 3.15 | -0.03 | 80070.94 | 22.4 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.03 | 0.2 | 158026.49 | 17.42 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9452.18 | 16.21 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 4.4 | 0.24 | 0.12 | 67677.22 | 10.72 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3813.17 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 3.97 | 0.25 | 0.08 | 174155.4 | 1.49 | skipped_fast |
| RWAUSDT | IDLE | 1.18 | 2.31 | 0.32 | 0.05 | 56179.66 | 8.09 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 2.19 | 0.31 | 0.07 | 173267.52 | 56.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 19.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
