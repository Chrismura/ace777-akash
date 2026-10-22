# Hulk DIGEST — 2026-10-22T09:26:55Z

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
| WUSDT | IDLE | 1.51 | 6.56 | 5.66 | -0.04 | 3483274.09 | 15.46 | skipped_fast |
| ETHUSDT | IDLE | 1.25 | 2.2 | 2.01 | -0.03 | 258794035.19 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 2.02 | 1.88 | -0.02 | 34823819.71 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 0.92 | 1.62 | 1.46 | -0.02 | 517564009.26 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.09 | 2.44 | -0.05 | 1382005.58 | 7.43 | skipped_fast |
| QNTUSDT | IDLE | 1.75 | 4.13 | 3.6 | -0.02 | 1265437.14 | 1.03 | skipped_fast |
| CHIPUSDT | IDLE | 2.38 | 9.12 | 8.33 | -0.03 | 345435.41 | 13.84 | skipped_fast |
| PYTHUSDT | IDLE | 1.44 | 3.74 | 3.25 | -0.07 | 635344.36 | 2.7 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 2.68 | 2.0 | -0.02 | 542879.72 | 11.86 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 3.07 | 2.42 | -0.03 | 393186.89 | 7.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.2 | 3.33 | 2.53 | -0.05 | 248949.89 | 13.92 | skipped_fast |
| BIOUSDT | IDLE | 1.61 | 3.25 | 3.02 | -0.05 | 78675.57 | 8.43 | skipped_fast |
| REDUSDT | IDLE | 1.6 | 2.96 | 2.68 | -0.02 | 80651.74 | 7.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.81 | 1.11 | -0.06 | 60768.34 | 61.92 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.82 | 0.93 | -0.02 | 59591.47 | 10.86 | skipped_fast |
| IOTAUSDT | IDLE | 2.02 | 3.84 | 3.18 | -0.05 | 78611.39 | 31.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.17 | 2.32 | 0.4 | 0.04 | 44959.24 | 56.93 | skipped_fast |
| LAUSDT | IDLE | 1.81 | 4.63 | 3.69 | -0.06 | 62691.5 | 19.91 | skipped_fast |
| WAXLUSDT | IDLE | 1.8 | 6.13 | 4.7 | -0.09 | 57841.02 | 41.12 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 2.22 | 1.49 | -0.0 | 19847.24 | 21.42 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.63 | 0.47 | -0.01 | 52865.18 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.88 | 0.57 | 0.0 | 40061.38 | 55.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
