# Hulk DIGEST — 2026-09-06T17:32:30Z

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
| XRPUSDT | IDLE | 1.1 | 2.0 | 1.28 | -0.01 | 25679761.35 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.91 | 1.72 | 0.66 | 0.0 | 246937251.2 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.02 | 0.4 | -0.0 | 374073700.84 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.63 | 4.73 | 3.52 | -0.01 | 509093.23 | 1.84 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 5.94 | 2.39 | 0.01 | 427077.9 | 1.72 | skipped_fast |
| WUSDT | IDLE | 2.29 | 4.42 | 1.12 | 0.05 | 263183.07 | 13.48 | skipped_fast |
| EDELUSDT | IDLE | 2.95 | 5.34 | 3.69 | -0.01 | 62911.11 | 19.18 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 13.25 | 8.96 | -0.18 | 75231.82 | 41.68 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 2.2 | 1.76 | -0.01 | 324353.06 | 7.34 | skipped_fast |
| BIOUSDT | IDLE | 1.97 | 3.71 | 1.54 | -0.01 | 93301.98 | 3.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 2.41 | 2.0 | -0.02 | 197496.63 | 22.08 | skipped_fast |
| RWAINCUSDT | IDLE | 2.08 | 4.5 | 2.6 | 0.05 | 6431.19 | 35.89 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.94 | 1.62 | 0.02 | 63823.97 | 12.55 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 1.73 | 1.52 | -0.0 | 429233.93 | 1.25 | skipped_fast |
| KITEUSDT | IDLE | 0.79 | 1.41 | 1.16 | -0.0 | 60215.3 | 11.1 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.44 | 1.28 | -0.03 | 54174.81 | 14.38 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 1.59 | 0.45 | 0.02 | 37231.96 | 7.61 | skipped_fast |
| TELUSDT | IDLE | 0.78 | 1.53 | 0.23 | 0.0 | 66183.11 | 23.27 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.36 | 0.17 | 0.02 | 41503.62 | 14.78 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.63 | 0.63 | 0.02 | 194.56 | 22.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
