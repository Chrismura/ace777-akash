# Hulk DIGEST — 2026-08-22T05:53:30Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.05 | 0.08 | 17493326.11 | 3.94 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 23.87 | 9.49 | 0.18 | 205878848.0 | 5.2 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 15.8 | 8.91 | 0.06 | 1368749.32 | 7.58 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.91 | -0.09 | 710756.67 | 13.36 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.16 | 0.07 | 605053.27 | 12.35 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.04 | -0.03 | 245321.43 | 16.42 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.9 | 0.1 | 164936.44 | 41.57 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.87 | 0.18 | 766685.38 | 10.83 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 8.47 | 6.09 | 0.04 | 547506.61 | 22.99 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 13.91 | 8.72 | 0.04 | 197087.52 | 9.27 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 9.68 | 6.25 | 0.07 | 74180.99 | 9.29 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.0 | 11600.95 | 64.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.2 | 0.06 | 59005.61 | 47.31 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.65 | 0.06 | 5383.27 | 21.8 | skipped_fast |
| EDELUSDT | IDLE | 2.18 | 4.52 | 2.05 | -0.01 | 88051.07 | 76.88 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3293.96 | 7.99 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.52 | 2.86 | 0.07 | 196661.57 | 50.68 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.05 | 57893.25 | 8.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
