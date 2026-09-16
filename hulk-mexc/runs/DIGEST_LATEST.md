# Hulk DIGEST — 2026-09-16T10:12:33Z

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
| ETHUSDT | IDLE | 0.64 | 1.23 | 0.33 | -0.03 | 487326623.4 | 0.12 | skipped_fast |
| XRPUSDT | IDLE | 0.53 | 1.91 | 1.02 | -0.08 | 94988219.15 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.97 | 0.12 | -0.01 | 601116971.49 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.51 | 2.68 | 2.29 | -0.03 | 669478.1 | 1.91 | skipped_fast |
| EDELUSDT | IDLE | 1.28 | 19.06 | 8.52 | 0.5 | 433515.17 | 22.08 | skipped_fast |
| REDUSDT | IDLE | 2.66 | 4.76 | 3.68 | -0.06 | 68421.59 | 16.91 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.64 | 1.2 | -0.04 | 379314.37 | 7.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.6 | 17.64 | 0.42 | 0.36 | 43737.19 | 73.65 | skipped_fast |
| WUSDT | IDLE | 1.19 | 2.67 | 1.8 | -0.07 | 209593.31 | 16.84 | skipped_fast |
| KITEUSDT | IDLE | 1.74 | 3.09 | 2.67 | -0.06 | 60440.76 | 15.05 | skipped_fast |
| CHIPUSDT | IDLE | 1.21 | 3.75 | 3.12 | -0.1 | 118296.99 | 10.89 | skipped_fast |
| ZBCNUSDT | IDLE | 0.73 | 2.49 | 0.52 | -0.07 | 202929.29 | 32.06 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.22 | 0.68 | -0.04 | 445683.89 | 1.35 | skipped_fast |
| RWAINCUSDT | IDLE | 1.32 | 2.39 | 1.71 | -0.04 | 14498.21 | 23.22 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.63 | 0.4 | -0.02 | 80688.14 | 12.1 | skipped_fast |
| QNTUSDT | IDLE | 1.62 | 2.9 | 2.28 | -0.06 | 44158.18 | 6.71 | skipped_fast |
| TELUSDT | IDLE | 1.46 | 2.75 | 2.61 | -0.07 | 110896.81 | 48.13 | skipped_fast |
| RWAUSDT | IDLE | 0.75 | 1.38 | 0.76 | -0.02 | 52339.39 | 15.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.62 | 1.59 | -0.06 | 1537.92 | 20.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.48 | 0.07 | -0.02 | 31570.53 | 1.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
