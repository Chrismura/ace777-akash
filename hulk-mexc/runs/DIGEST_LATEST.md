# Hulk DIGEST — 2026-08-22T15:12:48Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.6 | 0.04 | 51474177.43 | 11.87 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.49 | 6.05 | 0.02 | 214428573.7 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.68 | 0.11 | 800896.62 | 6.86 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 2.85 | 2.3 | -0.01 | 1172956.35 | 3.93 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.59 | -0.11 | 614019.67 | 3.42 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 1.86 | -0.02 | 562193.9 | 4.28 | skipped_fast |
| KITEUSDT | IDLE | 2.79 | 6.37 | 2.51 | 0.02 | 85080.51 | 4.5 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.42 | -0.07 | 324818.65 | 16.9 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.29 | -0.07 | 226357.74 | 3.33 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.12 | -0.04 | 79080.42 | 22.81 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 5.19 | 4.94 | -0.04 | 150590.4 | 11.98 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.37 | 0.03 | 46042.15 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 2.69 | 2.51 | -0.02 | 188475.14 | 9.49 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9931.39 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.75 | 1.1 | 0.01 | 141045.19 | 53.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 21.74 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.23 | 0.32 | 0.02 | 57327.67 | 8.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
