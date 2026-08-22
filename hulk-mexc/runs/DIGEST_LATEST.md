# Hulk DIGEST — 2026-08-22T07:58:13Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.7 | 0.01 | 24323921.14 | 11.79 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 23.87 | 7.48 | 0.2 | 223949195.27 | 1.91 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.53 | 0.04 | 1349881.46 | 5.09 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.88 | -0.09 | 688178.66 | 6.67 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.18 | 0.04 | 616115.1 | 14.53 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.61 | -0.04 | 247456.26 | 9.58 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.45 | 0.06 | 160150.01 | 9.64 | skipped_fast |
| CCUSDT | IDLE | 2.03 | 11.25 | 2.6 | 0.2 | 811455.02 | 5.74 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.06 | 0.04 | 537755.11 | 17.5 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.64 | 0.04 | 194445.44 | 7.72 | skipped_fast |
| KITEUSDT | IDLE | 3.44 | 9.68 | 3.9 | 0.07 | 74121.66 | 13.6 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.03 | 87111.31 | 22.3 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 20.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 5.36 | 4.15 | -0.01 | 175230.83 | 25.75 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.32 | 0.67 | 0.01 | 3157.72 | 63.29 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.01 | 0.01 | 52396.44 | 41.01 | skipped_fast |
| RWAUSDT | IDLE | 1.73 | 3.29 | 1.12 | 0.05 | 58413.52 | 8.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
