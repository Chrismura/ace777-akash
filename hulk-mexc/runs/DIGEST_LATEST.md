# Hulk DIGEST — 2026-08-29T12:11:16Z

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
| XRPUSDT | IDLE | 0.43 | 0.78 | 0.58 | -0.03 | 39456188.22 | 1.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 7.78 | 6.82 | -0.08 | 1144471.91 | 4.94 | skipped_fast |
| PYTHUSDT | IDLE | 0.62 | 1.22 | 0.19 | -0.02 | 423508.27 | 2.12 | skipped_fast |
| WUSDT | IDLE | 1.33 | 2.33 | 2.22 | -0.05 | 215975.58 | 12.22 | skipped_fast |
| CCUSDT | IDLE | 1.39 | 2.72 | 0.34 | -0.0 | 196525.2 | 8.82 | skipped_fast |
| REDUSDT | IDLE | 1.73 | 5.17 | 1.57 | 0.07 | 74481.49 | 15.98 | skipped_fast |
| ZBCNUSDT | IDLE | 0.87 | 2.04 | 1.59 | -0.08 | 185361.4 | 9.23 | skipped_fast |
| EDELUSDT | IDLE | 1.07 | 4.15 | 1.99 | -0.1 | 92798.89 | 19.36 | skipped_fast |
| BIOUSDT | IDLE | 0.69 | 1.21 | 1.19 | -0.04 | 83385.85 | 3.65 | skipped_fast |
| KITEUSDT | IDLE | 0.87 | 1.64 | 0.64 | 0.01 | 62682.69 | 11.73 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.05 | 0.86 | -0.04 | 371950.12 | 1.34 | skipped_fast |
| QAITUSDT | IDLE | 0.4 | 3.44 | 2.81 | -0.03 | 86285.96 | 52.06 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 1.59 | 1.01 | -0.02 | 26849.83 | 47.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.92 | 1.61 | 1.59 | -0.03 | 3674.22 | 99.45 | skipped_fast |
| QNTUSDT | IDLE | 0.75 | 1.32 | 1.14 | -0.03 | 39424.9 | 1.64 | skipped_fast |
| TELUSDT | IDLE | 0.73 | 1.33 | 0.86 | -0.05 | 78817.71 | 34.56 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.66 | 0.41 | 0.01 | 57251.5 | 24.72 | skipped_fast |
| FLUIDUSDT | IDLE | 0.35 | 0.66 | 0.3 | -0.03 | 1864.7 | 21.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
