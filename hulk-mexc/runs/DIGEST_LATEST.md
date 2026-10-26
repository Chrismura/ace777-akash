# Hulk DIGEST — 2026-10-26T08:18:36Z

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
| XRPUSDT | IDLE | 0.91 | 1.63 | 1.3 | -0.02 | 19250171.0 | 0.78 | skipped_fast |
| ETHUSDT | IDLE | 0.85 | 1.59 | 0.72 | -0.01 | 109543895.34 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.14 | 0.6 | -0.01 | 217006219.39 | 0.1 | skipped_fast |
| PYTHUSDT | IDLE | 1.3 | 2.73 | 2.22 | 0.03 | 804220.09 | 2.74 | skipped_fast |
| CHIPUSDT | IDLE | 4.03 | 9.75 | 4.51 | 0.02 | 107120.78 | 24.43 | skipped_fast |
| WUSDT | IDLE | 1.38 | 2.51 | 1.6 | -0.03 | 509160.73 | 15.36 | skipped_fast |
| QNTUSDT | IDLE | 1.22 | 3.69 | 0.27 | 0.07 | 748699.71 | 3.07 | skipped_fast |
| LAUSDT | IDLE | 3.9 | 7.91 | 3.9 | 0.0 | 63382.86 | 24.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 3.14 | 2.85 | 0.0 | 181879.74 | 22.15 | skipped_fast |
| REDUSDT | IDLE | 2.03 | 3.63 | 2.88 | -0.02 | 61075.38 | 7.68 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 2.83 | 2.24 | -0.0 | 54430.35 | 8.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.41 | 2.7 | 1.95 | -0.05 | 67805.04 | 5.84 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.52 | 1.83 | -0.02 | 60994.69 | 18.17 | skipped_fast |
| CCUSDT | IDLE | 0.84 | 1.49 | 1.32 | 0.0 | 162546.86 | 10.93 | skipped_fast |
| EDELUSDT | IDLE | 0.82 | 2.0 | 1.18 | 0.06 | 140868.98 | 31.43 | skipped_fast |
| WAXLUSDT | IDLE | 2.19 | 3.86 | 3.43 | -0.01 | 52447.27 | 63.72 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.57 | 1.15 | -0.01 | 170412.08 | 5.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.48 | 0.93 | 0.23 | 0.0 | 33112.33 | 59.87 | skipped_fast |
| IOTAUSDT | IDLE | 1.13 | 2.06 | 1.29 | -0.02 | 62344.97 | 30.85 | skipped_fast |
| FLUIDUSDT | IDLE | 0.28 | 1.49 | 0.0 | -0.02 | 19116.06 | 19.98 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.01 | 52771.48 | 23.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.57 | 0.0 | -0.01 | 38427.33 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
