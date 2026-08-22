# Hulk DIGEST — 2026-08-22T08:14:54Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.11 | 19.14 | 8.15 | 0.04 | 26532623.5 | 1.95 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 23.87 | 8.69 | 0.15 | 224457760.62 | 3.22 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.21 | 0.04 | 1357441.3 | 2.54 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.18 | -0.09 | 684679.11 | 6.62 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.24 | 0.05 | 611068.12 | 11.31 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 29.98 | 8.2 | -0.02 | 247144.46 | 6.29 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 11.11 | 0.07 | 154511.3 | 21.81 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 11.25 | 2.1 | 0.2 | 821932.7 | 8.16 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.01 | 0.03 | 537480.43 | 37.89 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.11 | 0.04 | 194173.23 | 10.75 | skipped_fast |
| KITEUSDT | IDLE | 3.78 | 9.68 | 3.54 | 0.07 | 72898.98 | 12.65 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 22.36 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 4.52 | 3.46 | -0.02 | 86974.07 | 111.48 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11216.08 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 4.7 | 3.8 | -0.01 | 173692.48 | 35.93 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.78 | 0.0 | 52296.99 | 29.07 | skipped_fast |
| RWAUSDT | IDLE | 1.71 | 3.29 | 0.88 | 0.05 | 58168.29 | 24.14 | skipped_fast |
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
