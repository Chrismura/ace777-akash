# Hulk DIGEST — 2026-10-10T15:52:50Z

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
| WUSDT | IDLE | 3.84 | 12.87 | 3.49 | 0.04 | 1213614.24 | 18.04 | skipped_fast |
| ETHUSDT | IDLE | 0.49 | 0.95 | 0.23 | 0.01 | 85858508.44 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.39 | 0.73 | 0.27 | 0.02 | 16012968.22 | 2.13 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.36 | 0.02 | 0.0 | 187381933.71 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.45 | 4.39 | 3.37 | -0.02 | 1114881.19 | 2.44 | skipped_fast |
| PYTHUSDT | IDLE | 0.56 | 1.31 | 0.8 | -0.09 | 998860.97 | 2.56 | skipped_fast |
| EDELUSDT | IDLE | 3.18 | 6.53 | 4.16 | -0.03 | 218865.5 | 5.2 | skipped_fast |
| KITEUSDT | IDLE | 2.4 | 6.81 | 0.61 | 0.09 | 73108.85 | 9.91 | skipped_fast |
| CCUSDT | IDLE | 0.7 | 1.36 | 0.29 | -0.01 | 369233.24 | 4.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.05 | 1.96 | 0.93 | -0.01 | 204336.75 | 18.33 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.16 | 1.02 | 0.03 | 54311.92 | 9.32 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 1.93 | 0.28 | 0.03 | 82771.19 | 6.92 | skipped_fast |
| CHIPUSDT | IDLE | 0.89 | 2.11 | 1.69 | 0.06 | 90105.01 | 15.45 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.69 | 0.82 | 0.02 | 348868.99 | 3.23 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 3.81 | 3.4 | -0.03 | 112997.98 | 39.16 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.78 | 0.29 | -0.0 | 9624.54 | 43.85 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 1.44 | 1.1 | -0.0 | 44864.69 | 57.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.94 | 0.77 | 0.0 | 15074.48 | 21.28 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.71 | 0.47 | -0.01 | 54294.28 | 7.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.67 | 0.27 | 0.0 | 39137.95 | 14.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
