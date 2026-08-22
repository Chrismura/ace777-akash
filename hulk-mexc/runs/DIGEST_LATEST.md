# Hulk DIGEST — 2026-08-22T10:33:34Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 16.77 | 11.48 | 0.01 | 51644649.26 | 4.13 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 23.87 | 12.65 | 0.07 | 217208423.4 | 6.74 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.44 | 0.01 | 1246418.31 | 5.2 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 22.93 | 12.4 | -0.11 | 666634.85 | 3.4 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.87 | 0.01 | 598468.5 | 14.9 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.01 | -0.06 | 239113.7 | 26.33 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.6 | 0.13 | 811607.57 | 9.52 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.23 | 0.03 | 154730.94 | 17.13 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 9.72 | 8.17 | -0.03 | 426347.53 | 22.62 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 9.28 | 5.35 | 0.03 | 73173.68 | 12.07 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 5.96 | 5.08 | -0.04 | 78893.93 | 56.85 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 9.75 | 7.0 | -0.0 | 189422.4 | 11.03 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 9.12 | 8.01 | -0.05 | 168550.16 | 59.19 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5710.05 | 19.53 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3242.83 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.38 | 0.0 | 49262.24 | 46.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11327.59 | 70.48 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.29 | 2.31 | 0.01 | 57341.57 | 32.55 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
