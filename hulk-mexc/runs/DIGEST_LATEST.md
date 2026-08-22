# Hulk DIGEST — 2026-08-22T01:33:57Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 10.86 | 0.79 | 0.15 | 6758970.22 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.22 | 8.84 | 0.14 | 0.15 | 150579027.67 | 2.69 | skipped_fast |
| HBARUSDT | IDLE | 2.98 | 6.36 | 0.38 | 0.08 | 950545.67 | 2.49 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.79 | 0.1 | 547084.77 | 13.06 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.35 | 0.0 | 0.16 | 660894.1 | 7.84 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.65 | 0.92 | 0.09 | 391312.99 | 11.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 3.56 | 1.46 | -0.01 | 513231.52 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.57 | 1.19 | 0.03 | 186099.09 | 3.09 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79541.24 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.18 | 0.11 | 60731.72 | 20.39 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.86 | 0.17 | 158642.49 | 10.39 | skipped_fast |
| QNTUSDT | IDLE | 2.4 | 5.18 | 0.72 | 0.07 | 170073.92 | 4.51 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 6.19 | 1.23 | 0.05 | 181929.81 | 41.39 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 4.93 | 0.16 | 0.12 | 61021.66 | 13.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.3 | 2.45 | 1.01 | 0.04 | 9587.29 | 37.46 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 125.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 20.41 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 54865.15 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
