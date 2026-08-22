# Hulk DIGEST — 2026-08-22T08:00:42Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.1 | -0.0 | 24512495.43 | 35.5 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.41 | 23.87 | 7.93 | 0.19 | 224155707.93 | 5.76 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.64 | 0.04 | 1352413.88 | 2.55 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.97 | -0.09 | 683515.48 | 6.68 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.35 | 0.04 | 615216.36 | 15.58 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.76 | -0.04 | 247642.98 | 9.59 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.51 | 0.06 | 158066.07 | 11.41 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 11.25 | 2.43 | 0.2 | 811622.25 | 9.83 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.16 | 0.03 | 537553.29 | 15.51 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.7 | 0.03 | 194454.09 | 9.25 | skipped_fast |
| KITEUSDT | IDLE | 3.81 | 9.68 | 4.01 | 0.07 | 72995.53 | 11.8 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 20.45 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.81 | -0.03 | 87034.42 | 44.4 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11250.14 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 1.87 | 4.7 | 4.24 | -0.01 | 174905.3 | 41.15 | skipped_fast |
| QAITUSDT | IDLE | 1.69 | 3.32 | 0.35 | 0.01 | 3170.95 | 67.05 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.68 | 0.01 | 52397.73 | 44.42 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 1.04 | 0.05 | 58398.36 | 8.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
