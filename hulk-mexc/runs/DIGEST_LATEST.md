# Hulk DIGEST — 2026-08-22T05:49:43Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.54 | 0.08 | 17261180.94 | 17.62 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 23.87 | 9.72 | 0.17 | 204971353.5 | 9.79 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 15.8 | 8.89 | 0.06 | 1367739.8 | 7.58 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.76 | -0.09 | 710406.05 | 13.25 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.16 | 0.07 | 603812.05 | 13.34 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.07 | -0.03 | 244468.59 | 22.99 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.73 | 0.09 | 164914.92 | 21.09 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.79 | 0.18 | 765876.06 | 12.48 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 8.47 | 5.33 | 0.05 | 547441.65 | 23.3 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 13.91 | 8.64 | 0.04 | 197065.85 | 4.63 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.87 | 9.68 | 5.72 | 0.08 | 74344.41 | 12.01 | skipped_fast |
| EDELUSDT | IDLE | 2.15 | 4.52 | 1.51 | -0.02 | 88503.22 | 43.81 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.0 | 11600.95 | 64.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.28 | 0.06 | 58983.1 | 47.31 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.65 | 0.06 | 5443.31 | 21.79 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3293.96 | 7.99 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 5.52 | 3.01 | 0.07 | 196207.87 | 35.6 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.75 | 0.05 | 57989.26 | 16.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
