# Hulk DIGEST — 2026-10-27T11:24:28Z

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
| XRPUSDT | IDLE | 0.71 | 1.37 | 0.34 | 0.01 | 21234526.62 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.61 | 1.17 | 0.4 | -0.0 | 144431365.29 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.8 | 0.29 | -0.0 | 354284929.75 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.2 | 6.93 | 4.05 | -0.05 | 1147519.56 | 2.46 | skipped_fast |
| PYTHUSDT | IDLE | 1.43 | 2.6 | 1.69 | -0.03 | 560823.77 | 2.75 | skipped_fast |
| WUSDT | IDLE | 1.37 | 2.42 | 2.1 | 0.05 | 514094.39 | 21.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.46 | 7.23 | 1.23 | 0.13 | 319830.54 | 17.07 | skipped_fast |
| RWAINCUSDT | IDLE | 2.17 | 8.54 | 7.18 | -0.13 | 54052.16 | 40.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.19 | 3.29 | 2.08 | 0.02 | 260542.6 | 14.83 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.42 | 1.61 | -0.04 | 231406.15 | 6.21 | skipped_fast |
| EDELUSDT | IDLE | 0.74 | 1.38 | 0.71 | 0.01 | 339260.82 | 21.74 | skipped_fast |
| REDUSDT | IDLE | 1.53 | 2.85 | 1.46 | -0.01 | 62591.06 | 8.91 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.62 | 1.34 | -0.0 | 56554.68 | 9.08 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 2.1 | 0.1 | 0.02 | 53742.51 | 11.37 | skipped_fast |
| HBARUSDT | IDLE | 1.05 | 1.89 | 1.38 | -0.02 | 201726.89 | 7.91 | skipped_fast |
| WAXLUSDT | IDLE | 1.83 | 3.31 | 2.31 | 0.01 | 54950.3 | 33.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.61 | 1.1 | 0.81 | -0.02 | 42871.01 | 65.56 | skipped_fast |
| LAUSDT | IDLE | 1.35 | 2.49 | 1.46 | -0.01 | 61161.87 | 19.21 | skipped_fast |
| IOTAUSDT | IDLE | 1.03 | 2.0 | 0.4 | -0.01 | 94861.93 | 16.62 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.16 | 1.38 | 0.04 | 3147.46 | 21.47 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.22 | 0.32 | -0.01 | 56045.57 | 8.04 | skipped_fast |
| MNSRYUSDT | IDLE | 0.44 | 0.77 | 0.7 | -0.0 | 37356.26 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
