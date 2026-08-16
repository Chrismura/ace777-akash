# Hulk DIGEST — 2026-08-16T10:04:44Z

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
| XRPUSDT | IDLE | 0.19 | 0.34 | 0.26 | -0.0 | 4626487.1 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 9.89 | 1.4 | 0.2 | 187547.23 | 17.36 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 1.71 | 1.53 | 0.0 | 315614.81 | 7.3 | skipped_fast |
| ZBCNUSDT | IDLE | 0.9 | 1.59 | 1.45 | -0.01 | 210158.53 | 14.8 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 3.85 | 3.17 | -0.03 | 67650.89 | 135.87 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.68 | 0.81 | -0.01 | 66923.64 | 4.06 | skipped_fast |
| WUSDT | IDLE | 0.66 | 1.28 | 0.23 | -0.0 | 113816.06 | 13.15 | skipped_fast |
| QAITUSDT | IDLE | 1.18 | 2.07 | 1.94 | -0.04 | 972.61 | 34.69 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 3.31 | 0.88 | 0.09 | 8461.76 | 44.72 | skipped_fast |
| PYTHUSDT | IDLE | 0.51 | 0.97 | 0.38 | -0.01 | 81534.05 | 2.54 | skipped_fast |
| KITEUSDT | IDLE | 0.67 | 1.29 | 0.31 | -0.02 | 58760.6 | 15.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.07 | 2.06 | 0.57 | -0.01 | 38623.98 | 61.81 | skipped_fast |
| REDUSDT | IDLE | 0.27 | 2.31 | 1.68 | 0.01 | 91048.17 | 17.05 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.15 | 1.42 | -0.03 | 95792.41 | 41.24 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.14 | 0.14 | -0.01 | 32471.99 | 6.95 | skipped_fast |
| HBARUSDT | IDLE | 0.25 | 0.45 | 0.38 | -0.01 | 77209.71 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.61 | 0.0 | -0.0 | 52365.86 | 8.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.59 | 1.18 | 0.0 | 0.04 | 102.3 | 20.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
