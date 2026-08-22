# Hulk DIGEST — 2026-08-22T08:19:59Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.1 | 0.03 | 27009336.2 | 5.91 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 23.87 | 9.04 | 0.14 | 223406150.12 | 1.94 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.32 | 0.03 | 1351659.09 | 5.08 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.68 | -0.1 | 684665.99 | 3.33 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.41 | 0.04 | 604851.5 | 12.35 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.24 | -0.03 | 248277.48 | 15.89 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.28 | 0.07 | 154518.28 | 14.0 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 11.25 | 2.28 | 0.2 | 823275.9 | 6.54 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 8.47 | 6.3 | 0.03 | 537544.32 | 17.04 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.36 | 0.03 | 194178.62 | 9.25 | skipped_fast |
| KITEUSDT | IDLE | 3.79 | 9.68 | 3.71 | 0.07 | 72772.83 | 9.96 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 36.21 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 4.52 | 3.46 | -0.03 | 86841.62 | 66.96 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11182.34 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.95 | -0.01 | 174170.65 | 20.57 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.73 | 0.01 | 52284.26 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 1.04 | 0.04 | 58170.25 | 16.1 | skipped_fast |
| QAITUSDT | IDLE | 1.46 | 2.91 | 0.0 | 0.02 | 3202.73 | 132.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
