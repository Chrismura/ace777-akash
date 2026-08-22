# Hulk DIGEST — 2026-08-22T10:30:57Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 16.77 | 11.64 | 0.0 | 51639574.63 | 6.21 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 23.87 | 13.53 | 0.07 | 217005565.62 | 5.45 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.44 | 15.8 | 11.62 | 0.01 | 1246839.21 | 6.53 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 22.93 | 12.37 | -0.11 | 666648.22 | 3.4 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 16.84 | 10.28 | 0.0 | 598669.41 | 11.76 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 11.98 | -0.06 | 238566.84 | 3.27 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.53 | 0.12 | 811776.31 | 9.51 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.26 | 0.04 | 154823.0 | 12.62 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 9.72 | 8.33 | -0.03 | 426281.2 | 22.65 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 9.28 | 5.57 | 0.03 | 73218.69 | 11.12 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 5.96 | 5.41 | -0.05 | 78842.6 | 68.42 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 9.75 | 7.23 | -0.01 | 189350.9 | 6.31 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 9.12 | 8.21 | -0.05 | 168610.52 | 48.45 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5710.05 | 23.21 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3242.83 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.26 | 0.0 | 49252.19 | 46.66 | skipped_fast |
| RWAUSDT | IDLE | 1.8 | 3.29 | 2.07 | 0.01 | 57358.15 | 24.44 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11327.59 | 97.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
