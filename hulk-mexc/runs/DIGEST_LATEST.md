# Hulk DIGEST — 2026-09-19T20:59:50Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.94 | 1.71 | 1.13 | 0.02 | 56882499.09 | 2.1 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.42 | 1.24 | 0.0 | 273140869.49 | 0.23 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.02 | 0.94 | 0.0 | 451543079.8 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.16 | 12.48 | 4.93 | 0.09 | 225497.78 | 35.1 | skipped_fast |
| PYTHUSDT | IDLE | 1.37 | 2.61 | 0.88 | 0.01 | 690502.06 | 1.64 | skipped_fast |
| WUSDT | IDLE | 1.28 | 2.26 | 1.94 | 0.01 | 533524.06 | 9.1 | skipped_fast |
| RWAINCUSDT | IDLE | 3.32 | 7.86 | 2.35 | -0.02 | 6711.34 | 58.72 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 2.57 | 2.16 | 0.0 | 325649.56 | 9.87 | skipped_fast |
| EDELUSDT | IDLE | 1.88 | 7.26 | 4.92 | -0.09 | 147012.62 | 39.01 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.22 | 1.42 | 0.02 | 606745.3 | 1.23 | skipped_fast |
| BIOUSDT | IDLE | 1.62 | 2.95 | 1.92 | 0.02 | 82938.23 | 7.13 | skipped_fast |
| RIZEUSDT | IDLE | 1.43 | 5.75 | 4.8 | 0.01 | 37666.82 | 10.51 | skipped_fast |
| CHIPUSDT | IDLE | 1.05 | 2.49 | 2.22 | -0.05 | 131023.56 | 18.59 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 2.08 | 1.97 | 0.03 | 77082.86 | 9.61 | skipped_fast |
| REDUSDT | IDLE | 0.34 | 1.56 | 0.34 | 0.02 | 136009.82 | 8.76 | skipped_fast |
| TELUSDT | IDLE | 1.23 | 3.67 | 3.22 | -0.03 | 123010.15 | 46.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.02 | 1.9 | 0.03 | 9401.27 | 21.83 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.61 | 0.0 | 0.04 | 58177.74 | 1.51 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.1 | 0.51 | 0.01 | 53839.4 | 29.24 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.71 | 0.28 | -0.01 | 35544.6 | 55.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
