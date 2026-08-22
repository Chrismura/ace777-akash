# Hulk DIGEST — 2026-08-22T16:29:28Z

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
| PYTHUSDT | IDLE | 1.46 | 7.24 | 0.06 | 0.07 | 51438494.6 | 3.89 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.8 | 0.05 | 215625684.69 | 2.04 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.09 | -0.0 | 1127094.08 | 5.17 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 4.14 | 2.3 | 0.09 | 764417.61 | 8.55 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.96 | -0.1 | 627576.75 | 3.36 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 0.9 | -0.01 | 544154.17 | 20.15 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.32 | -0.04 | 316210.08 | 25.54 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.29 | -0.06 | 219809.01 | 3.29 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.46 | 0.03 | 85233.23 | 10.68 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.52 | 1.9 | -0.03 | 74831.18 | 22.83 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.09 | -0.13 | 132930.2 | 11.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.22 | 0.03 | 56593.92 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.1 | -0.02 | 183792.96 | 3.15 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.03 | 8171.79 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 2.37 | 1.21 | 0.01 | 137751.37 | 47.83 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.32 | 0.02 | 56330.47 | 24.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 22.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
