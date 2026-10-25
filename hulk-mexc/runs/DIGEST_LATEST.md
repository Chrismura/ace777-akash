# Hulk DIGEST — 2026-10-25T00:55:13Z

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
| XRPUSDT | IDLE | 0.82 | 1.63 | 0.09 | 0.01 | 25444980.92 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.23 | 0.06 | -0.01 | 121948307.15 | 0.13 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.77 | 0.03 | 0.0 | 248653490.13 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.19 | 2.79 | 0.38 | -0.03 | 775986.44 | 51.27 | skipped_fast |
| PYTHUSDT | IDLE | 1.77 | 3.48 | 0.44 | 0.03 | 529431.3 | 1.39 | skipped_fast |
| EDELUSDT | IDLE | 1.5 | 3.68 | 1.63 | -0.06 | 582244.32 | 13.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.8 | 6.23 | 4.56 | 0.02 | 227789.66 | 56.36 | skipped_fast |
| RIZEUSDT | IDLE | 3.12 | 8.8 | 2.43 | -0.02 | 42145.99 | 37.26 | skipped_fast |
| CHIPUSDT | IDLE | 2.32 | 7.24 | 1.19 | 0.07 | 87023.76 | 17.51 | skipped_fast |
| LAUSDT | IDLE | 2.07 | 11.14 | 9.38 | -0.03 | 104219.53 | 5.08 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 3.11 | 0.0 | 0.02 | 368142.36 | 0.55 | skipped_fast |
| KITEUSDT | IDLE | 1.53 | 3.05 | 0.11 | -0.02 | 61091.04 | 9.44 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 3.46 | 0.58 | 0.05 | 99944.91 | 15.92 | skipped_fast |
| CCUSDT | IDLE | 0.58 | 1.14 | 0.16 | 0.01 | 225688.12 | 7.87 | skipped_fast |
| BIOUSDT | IDLE | 1.25 | 2.43 | 0.52 | -0.01 | 67035.89 | 8.69 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 1.38 | 0.16 | 0.0 | 52444.24 | 5.44 | skipped_fast |
| WAXLUSDT | IDLE | 1.97 | 4.98 | 4.61 | 0.02 | 56250.55 | 49.32 | skipped_fast |
| FLUIDUSDT | IDLE | 1.78 | 3.67 | 1.39 | -0.04 | 13094.07 | 21.55 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.22 | 0.06 | 0.01 | 198408.92 | 7.69 | skipped_fast |
| IOTAUSDT | IDLE | 1.03 | 2.01 | 0.27 | -0.0 | 68545.12 | 29.44 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.88 | 0.32 | -0.0 | 54338.99 | 15.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.49 | -0.01 | 37596.96 | 65.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
