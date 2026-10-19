# Hulk DIGEST — 2026-10-19T10:58:34Z

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
| XRPUSDT | IDLE | 0.96 | 1.74 | 1.23 | 0.01 | 32446110.23 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.68 | 1.24 | 0.84 | 0.0 | 330130252.38 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.22 | 0.77 | 0.0 | 146526000.48 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.21 | 3.16 | 2.71 | -0.06 | 982109.56 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.74 | 5.25 | 1.5 | 0.02 | 770623.7 | 2.98 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.59 | 2.02 | -0.04 | 527055.41 | 15.71 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.46 | 2.28 | -0.06 | 773608.19 | 4.8 | skipped_fast |
| EDELUSDT | IDLE | 2.2 | 4.47 | 2.69 | 0.02 | 239061.85 | 36.83 | skipped_fast |
| CCUSDT | IDLE | 0.85 | 1.62 | 0.59 | 0.01 | 326835.55 | 8.75 | skipped_fast |
| RWAINCUSDT | IDLE | 1.62 | 5.06 | 0.93 | -0.0 | 86017.65 | 5.23 | skipped_fast |
| KITEUSDT | IDLE | 1.98 | 3.95 | 0.08 | 0.03 | 62927.7 | 21.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.51 | 4.0 | 2.52 | 0.0 | 79308.38 | 16.63 | skipped_fast |
| ZBCNUSDT | IDLE | 0.65 | 2.33 | 1.07 | 0.01 | 284641.81 | 14.08 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.14 | 1.47 | -0.01 | 79681.73 | 4.26 | skipped_fast |
| REDUSDT | IDLE | 1.04 | 1.9 | 1.25 | -0.01 | 76700.77 | 8.81 | skipped_fast |
| RIZEUSDT | IDLE | 0.9 | 4.84 | 3.09 | -0.04 | 61377.82 | 30.77 | skipped_fast |
| IOTAUSDT | IDLE | 1.41 | 2.51 | 2.09 | -0.02 | 75555.68 | 18.0 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.83 | 1.56 | 0.0 | 55179.39 | 15.89 | skipped_fast |
| FLUIDUSDT | IDLE | 1.08 | 2.67 | 2.6 | 0.0 | 6400.69 | 21.4 | skipped_fast |
| WAXLUSDT | IDLE | 0.85 | 3.3 | 2.2 | 0.03 | 78708.95 | 50.06 | skipped_fast |
| LAUSDT | IDLE | 0.82 | 1.55 | 0.6 | -0.01 | 59715.88 | 22.49 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.53 | 0.14 | -0.0 | 40139.74 | 14.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
