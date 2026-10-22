# Hulk DIGEST — 2026-10-22T08:25:53Z

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
| WUSDT | IDLE | 1.68 | 7.06 | 6.31 | -0.03 | 3480988.14 | 15.42 | skipped_fast |
| XRPUSDT | IDLE | 0.9 | 1.58 | 1.48 | -0.01 | 35327420.74 | 2.25 | skipped_fast |
| ETHUSDT | IDLE | 0.85 | 1.48 | 1.42 | -0.02 | 255218633.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.22 | 1.18 | -0.01 | 518976975.55 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.01 | 4.78 | 3.96 | -0.02 | 1232774.41 | 2.56 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 4.9 | 4.46 | -0.06 | 635214.02 | 1.34 | skipped_fast |
| CHIPUSDT | IDLE | 2.42 | 8.08 | 7.48 | -0.03 | 356713.66 | 9.06 | skipped_fast |
| HBARUSDT | IDLE | 1.24 | 2.2 | 1.93 | -0.04 | 986253.12 | 4.93 | skipped_fast |
| EDELUSDT | IDLE | 1.47 | 2.68 | 1.68 | -0.01 | 525242.61 | 23.65 | skipped_fast |
| CCUSDT | IDLE | 1.55 | 4.08 | 3.61 | -0.02 | 393751.96 | 6.71 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 3.31 | 2.85 | -0.01 | 80783.17 | 9.13 | skipped_fast |
| ZBCNUSDT | IDLE | 1.16 | 3.07 | 2.83 | -0.06 | 249414.93 | 23.88 | skipped_fast |
| BIOUSDT | IDLE | 1.8 | 3.58 | 3.13 | -0.04 | 78541.45 | 8.4 | skipped_fast |
| RWAINCUSDT | IDLE | 0.94 | 3.81 | 2.0 | -0.04 | 67951.87 | 5.66 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.07 | 1.57 | -0.02 | 60315.73 | 9.19 | skipped_fast |
| RIZEUSDT | IDLE | 1.18 | 2.32 | 0.63 | 0.04 | 44965.61 | 42.33 | skipped_fast |
| IOTAUSDT | IDLE | 2.09 | 3.83 | 3.64 | -0.04 | 79133.78 | 28.92 | skipped_fast |
| WAXLUSDT | IDLE | 2.0 | 6.55 | 5.78 | -0.1 | 58061.53 | 51.67 | skipped_fast |
| LAUSDT | IDLE | 1.81 | 4.38 | 4.18 | -0.05 | 63084.15 | 25.43 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 1.7 | 1.5 | -0.0 | 19898.73 | 21.27 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.55 | 0.31 | -0.0 | 52173.2 | 23.59 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.88 | 0.66 | 0.0 | 39530.7 | 55.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
