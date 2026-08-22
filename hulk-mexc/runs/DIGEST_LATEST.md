# Hulk DIGEST — 2026-08-22T11:00:14Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 16.77 | 11.84 | -0.0 | 51655220.25 | 4.15 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 23.87 | 12.61 | 0.07 | 218111624.62 | 4.72 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.25 | -0.0 | 1248874.19 | 3.88 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.01 | 22.93 | 11.44 | -0.1 | 645999.85 | 6.72 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 16.84 | 9.43 | 0.01 | 595791.83 | 9.52 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.58 | -0.06 | 240681.01 | 3.27 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.55 | 0.12 | 817882.42 | 6.04 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 9.72 | 8.15 | -0.03 | 424408.92 | 20.56 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.84 | 37.92 | 10.49 | 0.03 | 154120.6 | 11.61 | skipped_fast |
| KITEUSDT | IDLE | 4.1 | 9.28 | 4.24 | 0.03 | 73308.5 | 13.71 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 9.12 | 7.47 | -0.04 | 169051.57 | 48.09 | skipped_fast |
| EDELUSDT | IDLE | 2.76 | 4.93 | 3.93 | -0.04 | 78999.55 | 34.07 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.01 | 2418.23 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | 0.0 | 11326.93 | 59.83 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.33 | -0.0 | 49217.23 | 46.66 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.97 | -0.01 | 189130.25 | 6.25 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.6 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.01 | 57415.25 | 16.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
