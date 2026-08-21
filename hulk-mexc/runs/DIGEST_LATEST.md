# Hulk DIGEST — 2026-08-21T07:29:40Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.6 | 10.37 | 0.0 | 0.16 | 2605443.36 | 2.02 | skipped_fast |
| XRPUSDT | IDLE | 0.61 | 3.1 | 0.59 | 0.18 | 122320947.52 | 2.28 | skipped_fast |
| CCUSDT | IDLE | 2.08 | 4.04 | 0.76 | 0.01 | 489599.1 | 7.86 | skipped_fast |
| CHIPUSDT | IDLE | 1.37 | 7.93 | 4.73 | 0.15 | 477931.74 | 3.03 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.46 | 15.17 | 0.0 | 0.03 | 44663.05 | 38.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 7.31 | 2.92 | 0.06 | 296891.29 | 28.76 | skipped_fast |
| BIOUSDT | IDLE | 1.84 | 5.44 | 0.34 | 0.06 | 224009.62 | 3.14 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 6.07 | 1.66 | -0.06 | 120280.51 | 20.47 | skipped_fast |
| WUSDT | IDLE | 0.94 | 1.82 | 0.37 | 0.06 | 272284.53 | 13.13 | skipped_fast |
| EDELUSDT | IDLE | 1.89 | 3.61 | 1.16 | 0.03 | 75737.92 | 42.83 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.57 | 0.42 | 0.06 | 532032.49 | 1.33 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.8 | 0.28 | 0.06 | 61293.94 | 14.78 | skipped_fast |
| QAITUSDT | IDLE | 1.17 | 2.95 | 0.78 | -0.03 | 5370.76 | 62.72 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 1.77 | 1.57 | 0.03 | 8505.35 | 54.7 | skipped_fast |
| TELUSDT | IDLE | 0.66 | 3.52 | 0.0 | 0.16 | 203031.9 | 48.01 | skipped_fast |
| QNTUSDT | IDLE | 0.97 | 1.87 | 0.41 | 0.05 | 69930.76 | 9.61 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.62 | 0.25 | 0.03 | 54982.72 | 16.85 | skipped_fast |
| FLUIDUSDT | IDLE | 0.85 | 1.71 | 0.0 | 0.08 | 2738.45 | 21.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
