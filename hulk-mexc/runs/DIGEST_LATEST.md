# Hulk DIGEST — 2026-08-22T10:42:11Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.72 | 16.77 | 10.87 | 0.02 | 51653385.95 | 2.05 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.85 | 23.87 | 11.59 | 0.09 | 217861673.33 | 2.66 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 15.8 | 10.89 | 0.01 | 1250475.77 | 9.04 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.74 | -0.09 | 661907.72 | 3.38 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 16.84 | 9.3 | 0.02 | 597794.7 | 13.75 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 29.98 | 11.2 | -0.05 | 239353.33 | 6.5 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.52 | 0.13 | 810582.12 | 3.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.17 | 0.03 | 154363.4 | 13.51 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 9.72 | 7.43 | -0.02 | 423954.06 | 21.45 | skipped_fast |
| KITEUSDT | IDLE | 4.13 | 9.28 | 4.75 | 0.04 | 73474.26 | 9.19 | skipped_fast |
| EDELUSDT | IDLE | 3.33 | 5.96 | 4.65 | -0.04 | 78963.97 | 11.34 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 9.12 | 7.96 | -0.05 | 168588.35 | 37.56 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 9.75 | 6.24 | 0.0 | 189340.35 | 9.37 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5710.05 | 21.51 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3241.83 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 59.77 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.38 | 0.0 | 49225.36 | 46.66 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.23 | 0.01 | 57512.46 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
