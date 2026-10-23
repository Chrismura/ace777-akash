# Hulk DIGEST — 2026-10-23T21:52:39Z

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
| XRPUSDT | IDLE | 0.7 | 1.28 | 0.84 | -0.0 | 23383769.62 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.47 | 0.84 | 0.62 | 0.0 | 140302077.37 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.73 | 0.63 | -0.0 | 286815266.46 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.61 | 4.77 | 3.01 | -0.02 | 770461.67 | 4.21 | skipped_fast |
| WUSDT | IDLE | 2.31 | 4.1 | 3.45 | -0.01 | 856957.51 | 16.92 | skipped_fast |
| QNTUSDT | IDLE | 1.85 | 3.52 | 1.22 | -0.03 | 1204684.41 | 1.09 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 3.74 | 2.2 | 0.0 | 529376.17 | 9.39 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 11.45 | 8.21 | -0.01 | 69722.41 | 40.83 | skipped_fast |
| CHIPUSDT | IDLE | 3.19 | 5.76 | 4.16 | -0.0 | 84230.24 | 18.28 | skipped_fast |
| ZBCNUSDT | IDLE | 2.28 | 4.19 | 3.24 | 0.02 | 204055.83 | 26.61 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 2.79 | 2.24 | 0.01 | 184148.81 | 4.87 | skipped_fast |
| REDUSDT | IDLE | 2.07 | 3.65 | 3.31 | -0.0 | 57695.88 | 22.88 | skipped_fast |
| RWAINCUSDT | IDLE | 2.11 | 4.22 | 0.0 | 0.06 | 48033.52 | 16.01 | skipped_fast |
| BIOUSDT | IDLE | 1.73 | 3.02 | 2.93 | 0.0 | 74688.39 | 8.5 | skipped_fast |
| LAUSDT | IDLE | 2.49 | 9.26 | 2.04 | 0.12 | 63518.91 | 21.33 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 2.47 | 1.03 | -0.01 | 57208.83 | 11.71 | skipped_fast |
| FLUIDUSDT | IDLE | 2.68 | 5.01 | 2.34 | 0.02 | 4538.17 | 21.07 | skipped_fast |
| WAXLUSDT | IDLE | 2.22 | 4.04 | 2.7 | -0.01 | 59385.78 | 56.46 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.77 | 1.36 | -0.02 | 256666.28 | 8.96 | skipped_fast |
| IOTAUSDT | IDLE | 1.62 | 2.94 | 1.95 | 0.01 | 71251.36 | 15.67 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.63 | 0.47 | 0.01 | 51133.3 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.72 | 0.23 | 0.0 | 36595.89 | 72.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
