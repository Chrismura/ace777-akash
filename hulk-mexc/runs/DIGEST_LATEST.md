# Hulk DIGEST — 2026-09-25T13:44:40Z

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
| XRPUSDT | IDLE | 2.9 | 6.47 | 2.69 | 0.06 | 108156410.57 | 3.15 | skipped_fast |
| ETHUSDT | IDLE | 1.46 | 2.65 | 1.83 | 0.01 | 382748811.95 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.92 | 1.6 | 1.58 | 0.0 | 750534637.87 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.17 | 5.73 | 1.95 | 0.09 | 1205957.79 | 7.0 | skipped_fast |
| HBARUSDT | IDLE | 2.67 | 5.04 | 1.98 | 0.04 | 1046860.15 | 1.06 | skipped_fast |
| CCUSDT | IDLE | 2.0 | 7.21 | 2.79 | 0.12 | 723422.74 | 10.69 | skipped_fast |
| ZBCNUSDT | IDLE | 4.08 | 9.62 | 4.61 | 0.04 | 201820.05 | 18.83 | skipped_fast |
| RIZEUSDT | IDLE | 1.43 | 32.62 | 22.86 | 0.49 | 127323.41 | 40.03 | skipped_fast |
| WUSDT | IDLE | 2.34 | 4.38 | 1.96 | 0.04 | 378407.9 | 7.55 | skipped_fast |
| BIOUSDT | IDLE | 2.76 | 10.37 | 2.94 | 0.13 | 112217.9 | 9.08 | skipped_fast |
| QNTUSDT | IDLE | 1.26 | 9.11 | 7.45 | 0.24 | 601062.89 | 7.39 | skipped_fast |
| KITEUSDT | IDLE | 2.71 | 5.09 | 2.14 | -0.01 | 73770.22 | 10.05 | skipped_fast |
| REDUSDT | IDLE | 2.32 | 6.13 | 0.87 | 0.1 | 136063.94 | 13.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.8 | 8.67 | 3.4 | 0.17 | 122061.17 | 16.5 | skipped_fast |
| RWAINCUSDT | IDLE | 2.01 | 9.11 | 7.22 | 0.06 | 23877.7 | 96.42 | skipped_fast |
| EDELUSDT | IDLE | 0.49 | 5.36 | 2.15 | 0.09 | 225198.17 | 43.81 | skipped_fast |
| TELUSDT | IDLE | 2.45 | 4.71 | 1.3 | -0.02 | 121111.96 | 41.95 | skipped_fast |
| MNSRYUSDT | IDLE | 1.27 | 2.42 | 0.76 | 0.03 | 43371.58 | 7.65 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.98 | 1.06 | 0.08 | 451.8 | 16.71 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.8 | 0.01 | 58378.22 | 7.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
