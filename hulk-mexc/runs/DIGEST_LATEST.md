# Hulk DIGEST — 2026-09-02T15:47:22Z

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
| XRPUSDT | IDLE | 1.44 | 2.79 | 0.65 | -0.03 | 39657036.5 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 1.4 | 2.63 | 1.1 | -0.02 | 411990590.04 | 0.04 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 11.79 | 9.82 | -0.07 | 1031385.21 | 2.45 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.59 | 0.21 | -0.01 | 518733008.99 | 0.01 | skipped_fast |
| PYTHUSDT | IDLE | 1.94 | 8.5 | 0.19 | 0.14 | 1182724.05 | 10.37 | skipped_fast |
| CCUSDT | IDLE | 2.14 | 3.77 | 3.36 | -0.05 | 363764.89 | 10.9 | skipped_fast |
| REDUSDT | IDLE | 2.74 | 5.41 | 0.52 | 0.02 | 159685.01 | 8.65 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.78 | 0.87 | -0.02 | 389044.75 | 12.61 | skipped_fast |
| KITEUSDT | IDLE | 1.66 | 6.19 | 2.26 | 0.12 | 94440.61 | 11.0 | skipped_fast |
| RWAINCUSDT | IDLE | 1.93 | 5.69 | 2.85 | 0.08 | 10542.18 | 5.43 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 7.8 | 1.08 | -0.06 | 37290.16 | 77.43 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 2.07 | 1.55 | -0.06 | 182937.19 | 13.33 | skipped_fast |
| BIOUSDT | IDLE | 1.14 | 2.2 | 0.51 | -0.03 | 71171.03 | 3.94 | skipped_fast |
| EDELUSDT | IDLE | 0.68 | 3.7 | 2.03 | 0.07 | 170316.47 | 41.31 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.84 | 0.94 | -0.02 | 211703.21 | 2.72 | skipped_fast |
| FLUIDUSDT | IDLE | 2.0 | 3.74 | 2.33 | -0.06 | 1836.1 | 21.82 | skipped_fast |
| TELUSDT | IDLE | 1.69 | 3.25 | 0.87 | -0.0 | 74413.02 | 35.27 | skipped_fast |
| QNTUSDT | IDLE | 1.29 | 2.48 | 0.68 | 0.02 | 69849.4 | 7.78 | skipped_fast |
| RWAUSDT | IDLE | 1.27 | 2.47 | 0.45 | 0.02 | 51633.03 | 7.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.52 | 0.27 | -0.01 | 33799.43 | 39.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
