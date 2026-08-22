# Hulk DIGEST — 2026-08-22T08:01:40Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.31 | 0.0 | 24612529.78 | 23.7 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 23.87 | 7.9 | 0.19 | 224268366.17 | 5.11 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.52 | 0.04 | 1352282.18 | 2.54 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.85 | -0.09 | 683526.76 | 6.67 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.24 | 0.04 | 616167.59 | 12.46 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.76 | -0.04 | 247648.11 | 9.6 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.41 | 0.06 | 157458.4 | 19.28 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 11.25 | 2.0 | 0.2 | 812329.36 | 8.15 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.07 | 0.04 | 537591.61 | 17.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.55 | 0.04 | 194463.16 | 6.16 | skipped_fast |
| KITEUSDT | IDLE | 3.81 | 9.68 | 3.97 | 0.07 | 73014.19 | 12.71 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.16 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.81 | -0.04 | 87034.34 | 33.28 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11250.14 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.95 | -0.0 | 174933.31 | 46.26 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.66 | 0.01 | 52399.08 | 44.42 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 1.04 | 0.05 | 58342.8 | 8.05 | skipped_fast |
| QAITUSDT | IDLE | 0.99 | 1.92 | 0.35 | 0.01 | 3170.95 | 67.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
