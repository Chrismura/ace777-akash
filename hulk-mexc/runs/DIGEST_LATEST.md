# Hulk DIGEST — 2026-08-22T15:12:14Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.6 | 0.03 | 51474124.5 | 11.86 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.49 | 5.72 | 0.02 | 214586412.5 | 4.16 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.66 | 0.11 | 800898.72 | 7.71 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 2.85 | 2.31 | -0.02 | 1172945.96 | 5.23 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.49 | -0.1 | 614270.78 | 3.41 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 1.87 | -0.02 | 562151.35 | 13.91 | skipped_fast |
| KITEUSDT | IDLE | 2.77 | 6.37 | 2.3 | 0.03 | 85075.71 | 10.78 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.43 | -0.07 | 324818.54 | 18.94 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.01 | -0.06 | 225640.72 | 3.32 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.12 | -0.05 | 79105.4 | 34.19 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 5.19 | 4.85 | -0.05 | 150614.46 | 11.04 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.37 | 0.04 | 46230.85 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.24 | -0.01 | 188475.14 | 9.47 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9931.39 | 59.06 | skipped_fast |
| TELUSDT | IDLE | 1.12 | 2.75 | 1.79 | 0.01 | 141125.02 | 58.5 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 22.44 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.23 | 0.32 | 0.02 | 57420.75 | 16.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
