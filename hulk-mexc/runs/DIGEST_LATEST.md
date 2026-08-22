# Hulk DIGEST — 2026-08-22T07:46:01Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.81 | 0.02 | 23168739.88 | 15.71 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 23.87 | 6.23 | 0.21 | 222478442.89 | 6.91 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.3 | 0.04 | 1349082.91 | 3.81 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.82 | -0.09 | 695077.8 | 3.34 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.17 | 0.05 | 617034.16 | 13.46 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.5 | -0.04 | 247780.99 | 3.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.94 | 0.07 | 160770.02 | 11.31 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 11.25 | 2.92 | 0.2 | 806128.05 | 4.11 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 8.47 | 5.6 | 0.04 | 538488.22 | 14.93 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.74 | 0.03 | 195655.25 | 9.28 | skipped_fast |
| KITEUSDT | IDLE | 3.43 | 9.68 | 3.54 | 0.08 | 74349.25 | 11.76 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.35 | -0.04 | 87138.32 | 55.83 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 19.71 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.36 | 3.9 | -0.01 | 177294.47 | 30.82 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3225.39 | 59.7 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.25 | -0.04 | 52667.17 | 41.01 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.04 | 58315.93 | 8.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
