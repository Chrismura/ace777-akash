# Hulk DIGEST — 2026-10-26T18:28:17Z

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
| ETHUSDT | IDLE | 1.12 | 2.11 | 0.9 | -0.01 | 141580609.33 | 0.39 | skipped_fast |
| XRPUSDT | IDLE | 1.06 | 2.01 | 0.67 | -0.0 | 24385008.19 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.9 | 1.69 | 0.76 | -0.01 | 346930774.26 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.85 | 7.77 | 6.5 | 0.06 | 1432246.49 | 2.44 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 3.76 | 2.9 | 0.01 | 927399.68 | 2.68 | skipped_fast |
| WUSDT | IDLE | 3.24 | 6.6 | 1.99 | 0.02 | 596922.13 | 79.9 | skipped_fast |
| CHIPUSDT | IDLE | 2.27 | 18.78 | 2.3 | 0.23 | 303352.82 | 12.55 | skipped_fast |
| RWAINCUSDT | IDLE | 3.0 | 13.37 | 3.28 | -0.07 | 61193.66 | 5.95 | skipped_fast |
| EDELUSDT | IDLE | 2.44 | 4.44 | 2.92 | 0.03 | 104425.59 | 37.17 | skipped_fast |
| BIOUSDT | IDLE | 1.79 | 3.28 | 2.03 | -0.01 | 59827.87 | 4.5 | skipped_fast |
| ZBCNUSDT | IDLE | 1.26 | 2.46 | 2.17 | -0.06 | 197119.85 | 17.07 | skipped_fast |
| CCUSDT | IDLE | 1.19 | 2.11 | 1.86 | -0.03 | 195215.97 | 7.02 | skipped_fast |
| RIZEUSDT | IDLE | 2.3 | 4.4 | 1.28 | 0.0 | 28862.29 | 50.86 | skipped_fast |
| REDUSDT | IDLE | 1.65 | 2.98 | 2.13 | -0.0 | 63075.04 | 16.44 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 2.22 | 1.49 | 0.0 | 53880.66 | 9.71 | skipped_fast |
| HBARUSDT | IDLE | 1.1 | 1.97 | 1.54 | -0.01 | 249624.11 | 10.42 | skipped_fast |
| WAXLUSDT | IDLE | 2.16 | 4.01 | 2.05 | -0.01 | 53926.27 | 41.42 | skipped_fast |
| LAUSDT | IDLE | 1.73 | 3.41 | 2.39 | 0.0 | 65602.7 | 18.95 | skipped_fast |
| IOTAUSDT | IDLE | 1.39 | 2.44 | 2.2 | -0.02 | 84443.61 | 30.71 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.35 | 2.0 | -0.05 | 1378.64 | 21.27 | skipped_fast |
| RWAUSDT | IDLE | 0.75 | 1.44 | 0.4 | 0.0 | 54190.61 | 7.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.62 | -0.01 | 42430.44 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
