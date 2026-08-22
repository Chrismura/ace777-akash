# Hulk DIGEST — 2026-08-22T06:15:33Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.99 | 0.07 | 19103763.78 | 1.97 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 10.42 | 0.16 | 209090016.92 | 2.63 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.64 | 0.05 | 1382316.03 | 6.37 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.62 | -0.09 | 702980.37 | 3.32 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.3 | 0.06 | 615302.62 | 14.55 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 13.05 | -0.04 | 245816.58 | 3.32 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 42.58 | 12.29 | 0.09 | 165955.96 | 12.35 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 8.47 | 6.35 | 0.04 | 547545.2 | 41.1 | skipped_fast |
| CCUSDT | IDLE | 1.81 | 9.8 | 0.66 | 0.2 | 768142.13 | 4.07 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.28 | 0.03 | 198271.75 | 12.41 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 5.68 | 0.08 | 74838.34 | 11.1 | skipped_fast |
| EDELUSDT | IDLE | 2.21 | 4.52 | 2.38 | -0.02 | 88064.54 | 44.3 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.01 | 11531.83 | 64.66 | skipped_fast |
| FLUIDUSDT | IDLE | 3.24 | 7.9 | 4.42 | 0.06 | 5356.23 | 20.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.97 | 3.99 | 2.89 | 0.08 | 59413.62 | 22.59 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.52 | 4.29 | 0.07 | 195740.15 | 87.7 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.84 | 3.38 | 1.99 | 0.04 | 58142.32 | 16.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
