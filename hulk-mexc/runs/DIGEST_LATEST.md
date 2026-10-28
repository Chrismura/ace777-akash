# Hulk DIGEST — 2026-10-28T15:38:31Z

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
| ETHUSDT | IDLE | 1.24 | 2.21 | 1.82 | -0.0 | 223401195.8 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.0 | 1.76 | 1.56 | -0.01 | 19219147.35 | 1.52 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.46 | 1.25 | 0.0 | 295186923.63 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 4.27 | 9.68 | 4.4 | 0.0 | 375770.7 | 7.99 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 13.96 | 10.57 | -0.05 | 185571.28 | 15.62 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 7.89 | 7.32 | 0.01 | 41048.24 | 6.7 | skipped_fast |
| QNTUSDT | IDLE | 2.9 | 5.16 | 4.28 | -0.02 | 422939.36 | 0.51 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.74 | 1.09 | -0.03 | 508151.22 | 15.7 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 2.78 | 1.88 | -0.02 | 399747.33 | 4.2 | skipped_fast |
| ZBCNUSDT | IDLE | 2.09 | 3.94 | 2.69 | -0.04 | 225492.95 | 29.68 | skipped_fast |
| HBARUSDT | IDLE | 1.27 | 2.32 | 1.45 | -0.0 | 516996.61 | 6.61 | skipped_fast |
| EDELUSDT | IDLE | 1.54 | 2.83 | 1.6 | 0.0 | 215022.37 | 40.03 | skipped_fast |
| BIOUSDT | IDLE | 1.79 | 3.29 | 1.87 | 0.01 | 87945.74 | 8.88 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 2.24 | 1.52 | -0.04 | 58870.31 | 11.31 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.13 | 0.99 | -0.02 | 53654.31 | 15.17 | skipped_fast |
| IOTAUSDT | IDLE | 1.91 | 3.45 | 2.47 | -0.02 | 75181.4 | 26.49 | skipped_fast |
| WAXLUSDT | IDLE | 1.81 | 3.26 | 2.37 | -0.02 | 56095.83 | 20.74 | skipped_fast |
| RIZEUSDT | IDLE | 0.97 | 1.79 | 0.99 | 0.03 | 37091.38 | 61.57 | skipped_fast |
| LAUSDT | IDLE | 1.67 | 3.08 | 1.78 | -0.02 | 57925.15 | 15.4 | skipped_fast |
| FLUIDUSDT | IDLE | 1.16 | 3.48 | 2.88 | -0.0 | 6664.52 | 21.7 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.12 | 1.03 | -0.0 | 55091.61 | 24.01 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.51 | 0.36 | 0.0 | 36552.63 | 52.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
