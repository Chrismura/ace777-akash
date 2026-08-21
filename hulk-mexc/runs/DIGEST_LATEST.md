# Hulk DIGEST — 2026-08-21T21:27:36Z

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
| PYTHUSDT | IDLE | 1.18 | 4.51 | 0.94 | 0.09 | 5628296.51 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.12 | 3.73 | 1.45 | 0.11 | 129036939.19 | 0.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.67 | 0.05 | 517629.65 | 3.1 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.34 | 0.09 | 484620.1 | 28.3 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 3.14 | 0.05 | 0.1 | 643991.19 | 2.75 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 3.04 | 0.26 | 0.07 | 813076.21 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.95 | 3.83 | 0.4 | 0.06 | 367477.33 | 10.45 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 2.03 | 0.02 | 186900.8 | 6.27 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.09 | 0.18 | 153875.42 | 11.46 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 4.12 | 2.31 | -0.05 | 82761.75 | 22.47 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10217.98 | 10.75 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.51 | 0.02 | 56011.29 | 45.77 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3754.88 | 56.07 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 4.0 | 1.76 | 0.11 | 61064.29 | 11.1 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 3.39 | 0.58 | 0.02 | 178757.33 | 37.24 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 2.65 | 0.69 | 0.04 | 62210.82 | 7.75 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.17 | 0.33 | 0.03 | 53831.71 | 24.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
