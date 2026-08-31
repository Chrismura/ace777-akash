# Hulk DIGEST — 2026-08-31T09:16:14Z

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
| XRPUSDT | IDLE | 1.33 | 2.56 | 0.62 | -0.01 | 39191819.18 | 2.19 | skipped_fast |
| BTCUSDT | IDLE | 0.87 | 1.7 | 0.25 | 0.01 | 496784725.96 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.69 | 0.33 | -0.0 | 422950218.69 | 0.37 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 25.32 | 19.06 | 0.01 | 120371.05 | 41.61 | skipped_fast |
| CHIPUSDT | IDLE | 2.14 | 7.01 | 0.81 | 0.02 | 554879.07 | 2.48 | skipped_fast |
| PYTHUSDT | IDLE | 1.39 | 3.48 | 0.67 | -0.01 | 546803.49 | 2.11 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 3.21 | 2.04 | -0.0 | 228390.79 | 7.6 | skipped_fast |
| ZBCNUSDT | IDLE | 1.5 | 4.71 | 2.08 | -0.08 | 225188.42 | 11.78 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.54 | 2.07 | 0.01 | 239092.89 | 19.4 | skipped_fast |
| REDUSDT | IDLE | 1.95 | 3.58 | 2.09 | 0.0 | 70034.93 | 11.87 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 2.63 | 2.44 | -0.06 | 97922.45 | 8.3 | skipped_fast |
| BIOUSDT | IDLE | 1.01 | 1.94 | 0.63 | -0.02 | 86101.39 | 3.75 | skipped_fast |
| FLUIDUSDT | IDLE | 2.51 | 5.02 | 0.0 | 0.02 | 2183.51 | 21.73 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 4.12 | 1.43 | 0.02 | 94638.77 | 40.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.04 | 2.01 | 0.53 | -0.02 | 34858.81 | 62.31 | skipped_fast |
| HBARUSDT | IDLE | 0.71 | 1.35 | 0.44 | -0.01 | 226682.55 | 1.35 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 1.37 | 0.0 | 0.01 | 2256.88 | 102.04 | skipped_fast |
| QNTUSDT | IDLE | 0.99 | 1.88 | 0.65 | -0.01 | 35518.32 | 8.23 | skipped_fast |
| RWAUSDT | IDLE | 0.79 | 1.55 | 0.16 | 0.02 | 53382.68 | 24.13 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.67 | 0.4 | -0.01 | 29285.71 | 18.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
