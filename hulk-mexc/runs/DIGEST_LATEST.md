# Hulk DIGEST — 2026-08-21T23:23:24Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.58 | 0.12 | 6053660.84 | 4.06 | skipped_fast |
| XRPUSDT | IDLE | 1.86 | 7.72 | 0.12 | 0.16 | 139699696.01 | 6.14 | skipped_fast |
| HBARUSDT | IDLE | 2.56 | 6.29 | 0.19 | 0.1 | 899978.57 | 1.24 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.82 | 11.25 | 0.88 | 0.15 | 512759.19 | 44.22 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.14 | 0.13 | 643706.97 | 8.02 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.23 | 0.08 | 377666.97 | 11.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.37 | 0.05 | 548041.45 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.03 | 187677.16 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82511.67 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.17 | 9.82 | 3.53 | 0.1 | 59648.74 | 45.4 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 26.99 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.68 | 0.19 | 157447.5 | 10.49 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.21 | 0.07 | 185068.16 | 41.11 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 2.54 | 5.4 | 0.01 | 0.07 | 119154.66 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.15 | 0.09 | 61502.47 | 10.2 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54451.83 | 16.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 21.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
