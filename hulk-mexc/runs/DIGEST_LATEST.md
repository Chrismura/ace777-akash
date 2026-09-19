# Hulk DIGEST — 2026-09-19T12:58:06Z

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
| XRPUSDT | IDLE | 0.97 | 2.09 | 0.56 | 0.08 | 69668918.53 | 1.4 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.39 | 0.68 | 0.06 | 545095089.36 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.31 | 0.58 | 0.22 | 0.04 | 621614183.08 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.32 | 3.83 | 0.04 | 0.09 | 1008463.12 | 8.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 3.02 | 0.67 | 0.03 | 697078.93 | 6.59 | skipped_fast |
| BIOUSDT | IDLE | 3.61 | 7.38 | 2.6 | 0.05 | 84601.73 | 14.25 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 5.68 | 5.38 | -0.0 | 5876.29 | 23.95 | skipped_fast |
| EDELUSDT | IDLE | 1.91 | 11.15 | 5.17 | -0.1 | 196413.24 | 28.42 | skipped_fast |
| HBARUSDT | IDLE | 1.78 | 3.5 | 0.4 | 0.05 | 574863.87 | 2.48 | skipped_fast |
| CCUSDT | IDLE | 1.08 | 2.07 | 0.56 | 0.03 | 405550.2 | 5.4 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 4.38 | 3.96 | 0.03 | 144179.17 | 11.39 | skipped_fast |
| KITEUSDT | IDLE | 1.64 | 3.02 | 1.71 | 0.04 | 71544.98 | 9.51 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 5.18 | 2.41 | 0.07 | 132885.74 | 15.98 | skipped_fast |
| ZBCNUSDT | IDLE | 0.85 | 1.67 | 0.16 | 0.02 | 174705.59 | 29.27 | skipped_fast |
| QNTUSDT | IDLE | 1.96 | 3.85 | 0.41 | 0.04 | 75564.03 | 1.53 | skipped_fast |
| TELUSDT | IDLE | 1.61 | 4.69 | 3.79 | 0.01 | 126535.97 | 52.67 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 4.72 | 0.0 | 0.16 | 11299.61 | 21.64 | skipped_fast |
| RIZEUSDT | IDLE | 0.26 | 2.11 | 1.77 | -0.08 | 38987.04 | 138.49 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.18 | 0.22 | 0.01 | 55643.19 | 29.28 | skipped_fast |
| MNSRYUSDT | IDLE | 0.24 | 0.47 | 0.05 | 0.04 | 38796.29 | 6.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
