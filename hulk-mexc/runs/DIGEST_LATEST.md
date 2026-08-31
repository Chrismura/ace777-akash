# Hulk DIGEST — 2026-08-31T07:16:20Z

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
| XRPUSDT | IDLE | 1.07 | 2.14 | 0.05 | -0.02 | 37272167.58 | 0.73 | skipped_fast |
| ETHUSDT | IDLE | 0.91 | 1.81 | 0.13 | -0.01 | 406401619.76 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.97 | 0.02 | -0.0 | 453039894.84 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.08 | 26.17 | 18.99 | 0.02 | 121177.38 | 24.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 6.44 | 0.1 | 0.0 | 508402.55 | 2.49 | skipped_fast |
| PYTHUSDT | IDLE | 1.55 | 3.99 | 0.0 | -0.01 | 560687.49 | 2.11 | skipped_fast |
| WUSDT | IDLE | 2.4 | 4.75 | 0.93 | 0.02 | 225004.97 | 13.84 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 3.81 | 0.35 | 0.01 | 215789.8 | 9.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.72 | 5.3 | 3.14 | -0.07 | 227911.32 | 27.59 | skipped_fast |
| REDUSDT | IDLE | 1.86 | 3.6 | 0.79 | 0.02 | 69799.51 | 3.6 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 2.92 | 0.11 | -0.03 | 87993.7 | 3.73 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 3.79 | 1.29 | -0.06 | 90610.52 | 18.87 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.97 | 2.89 | -0.02 | 2197.33 | 91.06 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 4.18 | 0.92 | 0.02 | 93191.45 | 52.1 | skipped_fast |
| RIZEUSDT | IDLE | 1.07 | 2.01 | 0.92 | -0.02 | 36965.81 | 60.19 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.74 | 0.04 | -0.01 | 215850.68 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.27 | 0.31 | -0.01 | 41214.14 | 4.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.41 | 2.81 | 0.0 | 0.01 | 3789.76 | 21.67 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.06 | 0.4 | 0.01 | 53081.86 | 40.47 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.67 | 0.4 | -0.01 | 29876.79 | 13.55 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
