# Hulk DIGEST — 2026-10-14T13:18:16Z

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
| PYTHUSDT | IDLE | 2.54 | 6.19 | 2.3 | 0.01 | 2017740.4 | 3.59 | skipped_fast |
| WUSDT | IDLE | 1.97 | 8.89 | 7.66 | -0.17 | 3385980.36 | 8.42 | skipped_fast |
| XRPUSDT | IDLE | 1.54 | 2.73 | 2.39 | -0.01 | 33237227.59 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 1.5 | 2.65 | 2.37 | -0.01 | 133504413.89 | 0.53 | skipped_fast |
| BTCUSDT | IDLE | 1.18 | 2.08 | 1.85 | -0.01 | 347199147.24 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.63 | 6.2 | 4.81 | -0.0 | 1616979.25 | 0.49 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 5.13 | 4.53 | -0.08 | 497686.83 | 6.8 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 17.46 | 11.41 | 0.01 | 49434.04 | 55.05 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 6.77 | 6.22 | -0.07 | 76090.22 | 11.01 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 8.39 | 7.39 | 0.04 | 81006.56 | 9.11 | skipped_fast |
| REDUSDT | IDLE | 2.57 | 4.5 | 4.25 | -0.0 | 63109.72 | 9.85 | skipped_fast |
| BIOUSDT | IDLE | 2.33 | 4.08 | 3.88 | -0.02 | 67249.68 | 7.48 | skipped_fast |
| ZBCNUSDT | IDLE | 1.72 | 3.02 | 2.77 | -0.01 | 197909.96 | 12.36 | skipped_fast |
| HBARUSDT | IDLE | 1.98 | 3.46 | 3.34 | -0.03 | 307888.23 | 5.9 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.49 | 2.4 | -0.02 | 171225.05 | 29.52 | skipped_fast |
| RWAINCUSDT | IDLE | 1.05 | 2.52 | 1.64 | -0.05 | 33296.76 | 5.19 | skipped_fast |
| FLUIDUSDT | IDLE | 1.98 | 5.82 | 3.8 | 0.06 | 22616.8 | 21.23 | skipped_fast |
| TELUSDT | IDLE | 0.71 | 1.29 | 0.83 | 0.03 | 107435.96 | 27.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 1.0 | 0.59 | -0.01 | 39216.87 | 40.69 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.55 | 0.39 | -0.01 | 55904.59 | 23.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
