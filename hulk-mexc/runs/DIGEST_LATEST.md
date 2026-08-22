# Hulk DIGEST — 2026-08-22T00:04:16Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.23 | 0.11 | 6252611.23 | 2.04 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.02 | 8.23 | 1.44 | 0.15 | 142362908.89 | 2.06 | skipped_fast |
| HBARUSDT | IDLE | 2.75 | 6.36 | 0.82 | 0.09 | 910473.55 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.78 | 0.13 | 515159.79 | 36.77 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.66 | 0.13 | 645363.45 | 7.97 | skipped_fast |
| WUSDT | IDLE | 2.76 | 6.91 | 1.4 | 0.08 | 379292.99 | 10.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.16 | 0.04 | 542154.03 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.48 | 0.03 | 187233.07 | 12.48 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | -0.01 | 80046.8 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.29 | 9.82 | 5.02 | 0.12 | 59051.17 | 45.5 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.41 | 0.06 | 189905.26 | 15.4 | skipped_fast |
| QNTUSDT | IDLE | 2.5 | 5.42 | 0.49 | 0.07 | 166721.34 | 1.5 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.57 | 4.91 | 2.49 | 0.19 | 157810.27 | 10.49 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 3.12 | 0.67 | 0.1 | 61516.85 | 12.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.08 | 0.04 | 54540.22 | 16.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.1 | 4934.79 | 29.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
