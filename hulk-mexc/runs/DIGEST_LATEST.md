# Hulk DIGEST — 2026-08-22T05:47:54Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.46 | 0.07 | 17107115.79 | 13.85 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 23.87 | 10.48 | 0.16 | 204681002.98 | 3.94 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.28 | 0.05 | 1367340.32 | 8.88 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.97 | -0.1 | 711717.87 | 13.36 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.13 | 0.06 | 601837.0 | 19.65 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 29.98 | 13.51 | -0.05 | 244497.6 | 16.53 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 45.06 | 14.26 | 0.09 | 164856.36 | 10.6 | skipped_fast |
| CCUSDT | IDLE | 2.2 | 11.56 | 3.21 | 0.18 | 765868.68 | 6.68 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 8.47 | 5.98 | 0.05 | 547535.0 | 21.94 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 13.91 | 8.83 | 0.04 | 197049.69 | 9.28 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 9.68 | 6.16 | 0.08 | 74406.12 | 12.99 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.28 | 0.06 | 58974.72 | 47.31 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.65 | 0.06 | 5443.31 | 21.1 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.0 | 11498.71 | 75.47 | skipped_fast |
| EDELUSDT | IDLE | 2.17 | 4.52 | 1.84 | -0.03 | 88500.98 | 76.88 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3293.96 | 7.99 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.52 | 2.81 | 0.07 | 195479.52 | 45.65 | skipped_fast |
| RWAUSDT | IDLE | 1.84 | 3.38 | 1.99 | 0.05 | 57966.44 | 8.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
