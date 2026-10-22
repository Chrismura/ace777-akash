# Hulk DIGEST — 2026-10-22T13:32:01Z

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
| WUSDT | IDLE | 0.82 | 4.01 | 3.18 | -0.1 | 2998922.14 | 17.22 | skipped_fast |
| XRPUSDT | IDLE | 0.88 | 1.58 | 1.23 | -0.02 | 32349589.52 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.82 | 1.46 | 1.23 | -0.03 | 216675009.96 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.81 | 0.63 | -0.02 | 531175542.05 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 3.0 | 5.49 | 4.85 | -0.05 | 546933.93 | 9.22 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.44 | 0.48 | -0.05 | 1374975.91 | 7.41 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.08 | 1.19 | -0.0 | 1258138.86 | 4.11 | skipped_fast |
| PYTHUSDT | IDLE | 0.8 | 2.34 | 0.31 | -0.06 | 643603.24 | 2.66 | skipped_fast |
| ZBCNUSDT | IDLE | 2.25 | 6.18 | 2.5 | -0.05 | 225408.04 | 27.97 | skipped_fast |
| RWAINCUSDT | IDLE | 2.44 | 4.49 | 2.65 | -0.01 | 66018.68 | 11.33 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 2.48 | 2.04 | -0.04 | 390446.16 | 6.8 | skipped_fast |
| CHIPUSDT | IDLE | 0.83 | 3.43 | 2.09 | -0.04 | 337627.31 | 16.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.63 | 4.3 | 0.41 | 0.06 | 43706.21 | 55.6 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 1.83 | 0.7 | -0.02 | 59724.64 | 12.52 | skipped_fast |
| REDUSDT | IDLE | 0.86 | 1.72 | 0.92 | -0.03 | 85923.39 | 16.86 | skipped_fast |
| BIOUSDT | IDLE | 0.62 | 1.39 | 0.17 | -0.04 | 77666.83 | 4.17 | skipped_fast |
| WAXLUSDT | IDLE | 0.94 | 3.18 | 2.56 | -0.09 | 58799.26 | 39.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.77 | 4.14 | 3.97 | -0.03 | 19552.58 | 22.33 | skipped_fast |
| LAUSDT | IDLE | 0.73 | 1.91 | 1.16 | -0.03 | 57752.35 | 18.1 | skipped_fast |
| IOTAUSDT | IDLE | 0.67 | 1.36 | 0.64 | -0.05 | 79970.14 | 19.95 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.11 | 0.78 | -0.01 | 52485.07 | 23.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.53 | 0.5 | -0.0 | 39931.17 | 55.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
