# Hulk DIGEST — 2026-10-26T01:42:53Z

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
| ETHUSDT | IDLE | 1.05 | 1.86 | 1.64 | -0.02 | 94588173.47 | 0.95 | skipped_fast |
| BTCUSDT | IDLE | 0.77 | 1.34 | 1.27 | -0.01 | 167881289.06 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.74 | 1.32 | 1.04 | -0.01 | 15291354.95 | 1.55 | skipped_fast |
| PYTHUSDT | IDLE | 1.25 | 2.64 | 2.05 | 0.04 | 702616.95 | 2.69 | skipped_fast |
| WUSDT | IDLE | 1.81 | 3.28 | 2.31 | -0.04 | 604916.36 | 16.96 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 5.59 | 5.23 | -0.05 | 88657.0 | 16.28 | skipped_fast |
| QNTUSDT | IDLE | 1.49 | 4.02 | 3.59 | 0.04 | 672422.02 | 3.16 | skipped_fast |
| ZBCNUSDT | IDLE | 2.61 | 4.68 | 4.09 | 0.01 | 184253.31 | 33.4 | skipped_fast |
| EDELUSDT | IDLE | 1.11 | 2.75 | 1.4 | 0.05 | 269412.85 | 25.3 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 2.33 | 1.55 | -0.0 | 186517.1 | 9.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.91 | 3.49 | 2.21 | -0.04 | 61370.51 | 28.32 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 2.83 | 2.59 | -0.04 | 60216.75 | 9.11 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 1.91 | 1.52 | -0.03 | 59953.34 | 9.05 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 2.1 | 0.97 | -0.02 | 53816.38 | 13.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.41 | 2.81 | 0.0 | 0.01 | 32792.57 | 62.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.33 | 6.11 | 5.76 | -0.03 | 19007.27 | 13.18 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 1.68 | 1.65 | -0.02 | 179394.98 | 9.11 | skipped_fast |
| LAUSDT | IDLE | 1.49 | 3.41 | 2.84 | -0.05 | 65958.9 | 26.86 | skipped_fast |
| IOTAUSDT | IDLE | 1.29 | 2.29 | 1.87 | -0.03 | 59964.78 | 21.2 | skipped_fast |
| WAXLUSDT | IDLE | 1.17 | 2.11 | 1.58 | 0.0 | 54009.96 | 59.7 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.0 | 52649.19 | 15.92 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.59 | 0.13 | -0.01 | 38274.14 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
