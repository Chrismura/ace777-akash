# Hulk DIGEST — 2026-10-23T20:52:50Z

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
| XRPUSDT | IDLE | 0.68 | 1.28 | 0.52 | 0.01 | 23969283.5 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.84 | 0.43 | 0.01 | 177224033.51 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.73 | 0.5 | 0.0 | 287599264.47 | 0.01 | skipped_fast |
| PYTHUSDT | IDLE | 2.66 | 4.77 | 3.66 | -0.03 | 775055.53 | 4.23 | skipped_fast |
| WUSDT | IDLE | 2.52 | 4.47 | 3.78 | -0.0 | 820900.57 | 16.82 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 3.73 | 1.08 | -0.02 | 1186043.9 | 2.18 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 4.57 | 3.16 | 0.01 | 527605.33 | 21.95 | skipped_fast |
| CHIPUSDT | IDLE | 3.2 | 5.76 | 4.33 | 0.01 | 85810.39 | 16.03 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 10.22 | 7.75 | -0.0 | 67330.69 | 49.64 | skipped_fast |
| ZBCNUSDT | IDLE | 2.22 | 4.19 | 2.34 | 0.02 | 204529.83 | 22.81 | skipped_fast |
| CCUSDT | IDLE | 1.81 | 3.26 | 2.45 | 0.01 | 184198.16 | 6.8 | skipped_fast |
| REDUSDT | IDLE | 2.0 | 3.65 | 2.39 | 0.01 | 57486.72 | 10.63 | skipped_fast |
| RWAINCUSDT | IDLE | 1.89 | 3.78 | 0.0 | 0.05 | 47983.84 | 5.35 | skipped_fast |
| KITEUSDT | IDLE | 1.75 | 3.31 | 1.29 | 0.01 | 57170.68 | 10.82 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 2.89 | 2.1 | 0.02 | 74281.62 | 8.43 | skipped_fast |
| FLUIDUSDT | IDLE | 3.2 | 6.04 | 2.34 | 0.03 | 4571.01 | 21.05 | skipped_fast |
| LAUSDT | IDLE | 2.99 | 11.41 | 2.36 | 0.13 | 64080.14 | 109.79 | skipped_fast |
| WAXLUSDT | IDLE | 2.25 | 4.04 | 3.01 | -0.0 | 57173.29 | 37.74 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 1.93 | 1.55 | -0.01 | 239803.08 | 6.4 | skipped_fast |
| IOTAUSDT | IDLE | 1.62 | 2.94 | 2.04 | 0.02 | 71348.77 | 15.69 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.63 | 0.47 | 0.01 | 51528.5 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.72 | 0.01 | 0.0 | 36357.95 | 74.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
