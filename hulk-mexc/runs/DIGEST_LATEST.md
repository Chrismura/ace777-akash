# Hulk DIGEST — 2026-09-27T19:12:01Z

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
| WUSDT | IDLE | 1.61 | 10.64 | 0.15 | 0.2 | 4322183.7 | 9.52 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 4.99 | 0.7 | 0.1 | 2296750.66 | 5.81 | skipped_fast |
| QNTUSDT | IDLE | 1.25 | 19.39 | 3.64 | 0.53 | 6395501.06 | 10.17 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 2.11 | 0.5 | 0.01 | 42778623.54 | 1.3 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 1.03 | 0.54 | 0.0 | 199322005.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.82 | 0.29 | 0.01 | 437273856.81 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 42.2 | 16.29 | 0.12 | 26391.18 | 41.82 | skipped_fast |
| CCUSDT | IDLE | 2.68 | 5.22 | 0.93 | 0.03 | 601274.91 | 7.99 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.8 | 12.75 | 10.07 | -0.15 | 137358.15 | 42.2 | skipped_fast |
| HBARUSDT | IDLE | 1.2 | 2.35 | 0.28 | 0.01 | 680263.4 | 1.05 | skipped_fast |
| KITEUSDT | IDLE | 1.9 | 4.7 | 0.61 | 0.04 | 167891.39 | 9.8 | skipped_fast |
| RIZEUSDT | IDLE | 1.71 | 8.23 | 7.32 | -0.1 | 37474.65 | 44.35 | skipped_fast |
| CHIPUSDT | IDLE | 1.73 | 3.29 | 1.14 | -0.04 | 99272.0 | 14.74 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 3.22 | 0.02 | 0.03 | 65898.83 | 12.67 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 2.8 | 0.34 | -0.01 | 88957.72 | 9.41 | skipped_fast |
| ZBCNUSDT | IDLE | 0.85 | 1.69 | 0.09 | 0.01 | 201424.54 | 20.24 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 4.0 | 2.8 | 0.13 | 162092.63 | 5.43 | skipped_fast |
| FLUIDUSDT | IDLE | 1.27 | 2.5 | 0.27 | 0.03 | 2321.19 | 22.07 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.0 | 0.49 | 0.01 | 56929.38 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.23 | 0.43 | 0.14 | 0.01 | 39808.26 | 27.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
