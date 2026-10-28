# Hulk DIGEST — 2026-10-28T21:43:19Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 1.47 | 2.74 | 1.27 | 0.0 | 199749411.43 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.43 | 2.71 | 1.03 | 0.0 | 22878387.36 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 0.9 | 1.7 | 0.7 | 0.0 | 321892253.09 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.05 | 5.96 | 0.94 | 0.0 | 445255.35 | 2.7 | skipped_fast |
| CCUSDT | IDLE | 1.66 | 3.76 | 1.65 | 0.02 | 432113.06 | 10.93 | skipped_fast |
| WUSDT | IDLE | 1.8 | 3.26 | 2.28 | -0.01 | 413734.08 | 15.71 | skipped_fast |
| QNTUSDT | IDLE | 2.56 | 4.89 | 1.49 | -0.01 | 398754.56 | 1.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.86 | 5.05 | 4.47 | -0.02 | 39741.53 | 35.53 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.13 | 1.99 | -0.01 | 565666.84 | 7.94 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 4.39 | 1.42 | 0.01 | 89181.73 | 8.7 | skipped_fast |
| CHIPUSDT | IDLE | 1.39 | 6.39 | 2.28 | -0.09 | 234934.59 | 14.05 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 2.82 | 2.16 | -0.02 | 185417.42 | 21.74 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.42 | 0.33 | -0.02 | 272305.52 | 41.7 | skipped_fast |
| KITEUSDT | IDLE | 1.57 | 3.01 | 0.87 | -0.02 | 62224.84 | 9.41 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.65 | 1.95 | -0.03 | 54010.66 | 14.54 | skipped_fast |
| IOTAUSDT | IDLE | 2.65 | 4.9 | 2.6 | -0.01 | 78007.51 | 28.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 2.83 | 2.69 | -0.03 | 33820.9 | 13.84 | skipped_fast |
| LAUSDT | IDLE | 2.06 | 3.83 | 1.87 | -0.04 | 56851.72 | 22.29 | skipped_fast |
| WAXLUSDT | IDLE | 2.01 | 3.82 | 1.27 | -0.01 | 54605.14 | 46.9 | skipped_fast |
| FLUIDUSDT | IDLE | 1.02 | 3.18 | 1.6 | -0.0 | 8076.79 | 21.32 | skipped_fast |
| RWAUSDT | IDLE | 0.76 | 1.37 | 1.03 | -0.0 | 55007.18 | 48.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.12 | 0.01 | 35569.61 | 40.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
