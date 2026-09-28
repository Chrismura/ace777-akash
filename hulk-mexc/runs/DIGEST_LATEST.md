# Hulk DIGEST — 2026-09-28T04:17:23Z

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
| QNTUSDT | IDLE | 1.43 | 45.68 | 24.86 | 0.49 | 15279463.36 | 12.05 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 10.77 | 7.39 | 0.05 | 5199911.72 | 8.79 | skipped_fast |
| PYTHUSDT | IDLE | 2.23 | 4.69 | 3.27 | -0.0 | 2027148.31 | 4.87 | skipped_fast |
| XRPUSDT | IDLE | 1.89 | 3.38 | 2.71 | -0.02 | 49741147.41 | 2.68 | skipped_fast |
| ETHUSDT | IDLE | 1.3 | 2.32 | 1.81 | -0.02 | 257696128.65 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.19 | 2.11 | 1.84 | -0.01 | 506797515.91 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.23 | 7.73 | 2.81 | 0.04 | 763154.48 | 7.08 | skipped_fast |
| HBARUSDT | IDLE | 2.06 | 3.76 | 2.46 | 0.02 | 998647.37 | 2.1 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.11 | 7.74 | 5.96 | -0.05 | 105213.19 | 7.59 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.1 | 7.32 | 5.83 | -0.04 | 89990.66 | 6.56 | skipped_fast |
| REDUSDT | IDLE | 2.53 | 5.3 | 4.46 | -0.06 | 66528.37 | 13.44 | skipped_fast |
| CHIPUSDT | IDLE | 2.32 | 6.25 | 5.02 | -0.07 | 92712.98 | 17.84 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 2.76 | 2.13 | -0.04 | 246312.27 | 13.29 | skipped_fast |
| RIZEUSDT | IDLE | 1.4 | 13.55 | 6.37 | -0.2 | 64997.15 | 60.72 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 5.92 | 5.59 | -0.01 | 3571.59 | 21.53 | skipped_fast |
| EDELUSDT | IDLE | 1.2 | 6.39 | 4.27 | -0.13 | 164632.98 | 36.4 | skipped_fast |
| RWAINCUSDT | IDLE | 0.61 | 5.95 | 3.56 | 0.21 | 31548.8 | 43.92 | skipped_fast |
| TELUSDT | IDLE | 0.81 | 1.79 | 1.55 | 0.03 | 170182.71 | 21.7 | skipped_fast |
| MNSRYUSDT | IDLE | 1.09 | 1.97 | 1.4 | -0.01 | 39242.85 | 52.67 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.14 | 0.71 | 0.01 | 59425.38 | 64.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
