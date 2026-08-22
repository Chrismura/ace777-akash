# Hulk DIGEST — 2026-08-22T05:42:55Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.83 | 0.07 | 16941556.7 | 11.92 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 11.21 | 0.16 | 203539745.98 | 8.62 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.83 | 0.04 | 1364300.25 | 26.89 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 24.54 | 13.24 | -0.1 | 709480.61 | 16.98 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.54 | 0.06 | 600716.49 | 6.26 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 29.98 | 13.94 | -0.05 | 233182.81 | 3.36 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.95 | 0.09 | 164573.4 | 22.08 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.56 | 4.1 | 0.17 | 763523.75 | 7.61 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 8.47 | 6.29 | 0.04 | 547294.11 | 43.09 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 13.91 | 9.67 | 0.04 | 197005.24 | 7.81 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 9.68 | 6.57 | 0.07 | 73360.49 | 10.26 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 4.52 | 1.08 | -0.02 | 88466.91 | 32.73 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.0 | 11498.71 | 53.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.15 | 0.06 | 58992.04 | 47.31 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5400.55 | 21.21 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.52 | 2.91 | 0.07 | 195134.29 | 15.26 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.05 | 58010.31 | 32.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
