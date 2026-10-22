# Hulk DIGEST — 2026-10-22T18:35:20Z

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
| ETHUSDT | IDLE | 1.31 | 2.39 | 1.55 | -0.05 | 194628104.66 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.29 | 2.29 | 1.97 | -0.06 | 29768995.32 | 2.3 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.4 | 1.04 | -0.04 | 503426536.94 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.63 | 2.51 | 0.88 | -0.12 | 1525431.1 | 17.24 | skipped_fast |
| HBARUSDT | IDLE | 1.62 | 3.3 | 2.45 | -0.08 | 1305376.71 | 10.07 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 7.74 | 6.49 | -0.1 | 218228.97 | 17.06 | skipped_fast |
| PYTHUSDT | IDLE | 1.75 | 4.22 | 2.65 | -0.09 | 556303.1 | 2.71 | skipped_fast |
| QNTUSDT | IDLE | 1.63 | 4.71 | 3.9 | -0.11 | 847974.22 | 1.06 | skipped_fast |
| EDELUSDT | IDLE | 1.76 | 4.66 | 3.81 | -0.1 | 525603.49 | 3.17 | skipped_fast |
| RIZEUSDT | IDLE | 3.25 | 5.87 | 4.23 | 0.02 | 38799.56 | 57.97 | skipped_fast |
| RWAINCUSDT | IDLE | 2.74 | 4.92 | 3.69 | -0.04 | 56736.97 | 39.97 | skipped_fast |
| CCUSDT | IDLE | 0.55 | 1.95 | 0.6 | -0.09 | 304428.06 | 0.97 | skipped_fast |
| CHIPUSDT | IDLE | 0.8 | 3.56 | 1.03 | -0.11 | 255175.53 | 15.94 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 3.47 | 2.49 | -0.09 | 76944.69 | 8.5 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 2.76 | 2.08 | -0.06 | 100155.05 | 15.66 | skipped_fast |
| KITEUSDT | IDLE | 0.78 | 1.44 | 0.82 | -0.03 | 59741.96 | 9.19 | skipped_fast |
| LAUSDT | IDLE | 1.34 | 4.02 | 3.23 | -0.11 | 58006.35 | 26.0 | skipped_fast |
| IOTAUSDT | IDLE | 1.33 | 3.09 | 1.98 | -0.09 | 76593.09 | 22.5 | skipped_fast |
| FLUIDUSDT | IDLE | 0.84 | 6.23 | 2.82 | -0.09 | 23284.61 | 14.02 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.28 | 0.87 | -0.02 | 52599.09 | 7.97 | skipped_fast |
| WAXLUSDT | IDLE | 0.67 | 2.42 | 2.07 | -0.13 | 58530.59 | 62.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.5 | 0.92 | 0.58 | -0.01 | 39551.9 | 74.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
