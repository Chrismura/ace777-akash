# Hulk DIGEST — 2026-08-22T10:27:06Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 16.77 | 12.39 | -0.01 | 51637063.16 | 2.09 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.93 | 23.87 | 15.09 | 0.05 | 216667910.0 | 2.08 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 15.8 | 12.21 | -0.0 | 1250340.89 | 1.31 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.05 | 22.93 | 12.75 | -0.12 | 664452.45 | 13.68 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 16.84 | 11.13 | -0.01 | 599109.45 | 15.1 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.82 | -0.06 | 237996.6 | 3.31 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.26 | 0.11 | 811796.03 | 7.84 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 37.92 | 11.99 | 0.02 | 155377.66 | 10.0 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 9.65 | 8.78 | -0.03 | 428575.73 | 26.91 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 9.28 | 6.21 | 0.02 | 73182.95 | 26.16 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 8.94 | 8.21 | -0.05 | 168602.98 | 16.19 | skipped_fast |
| EDELUSDT | IDLE | 2.9 | 5.11 | 4.65 | -0.04 | 78867.87 | 22.7 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 9.75 | 7.55 | -0.01 | 189348.66 | 6.33 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5825.49 | 21.07 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.36 | 0.0 | 49248.15 | 46.66 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.23 | 0.01 | 57538.07 | 16.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11368.82 | 75.88 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.03 | 3218.01 | 146.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
