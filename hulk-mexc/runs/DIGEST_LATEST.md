# Hulk DIGEST — 2026-09-28T08:20:15Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 2.35 | 8.07 | 6.42 | -0.06 | 4483237.26 | 12.68 | skipped_fast |
| PYTHUSDT | IDLE | 2.17 | 5.78 | 4.01 | -0.09 | 1814177.56 | 3.74 | skipped_fast |
| QNTUSDT | IDLE | 0.55 | 17.68 | 8.94 | 0.52 | 17068814.37 | 11.68 | skipped_fast |
| XRPUSDT | IDLE | 1.22 | 2.22 | 1.5 | -0.04 | 50258702.55 | 2.7 | skipped_fast |
| HBARUSDT | IDLE | 2.95 | 5.8 | 0.65 | 0.03 | 1565540.23 | 7.08 | skipped_fast |
| CCUSDT | IDLE | 3.88 | 9.05 | 4.83 | 0.02 | 938582.21 | 5.78 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.04 | 0.71 | -0.02 | 609069577.57 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.49 | 0.91 | 0.41 | -0.02 | 296873970.07 | 0.04 | skipped_fast |
| KITEUSDT | IDLE | 2.15 | 5.23 | 4.15 | -0.09 | 106057.36 | 7.83 | skipped_fast |
| BIOUSDT | IDLE | 2.16 | 4.78 | 3.65 | -0.07 | 102625.08 | 6.71 | skipped_fast |
| TELUSDT | IDLE | 2.87 | 5.74 | 3.97 | 0.02 | 177360.14 | 27.94 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 3.57 | 2.51 | -0.09 | 64231.28 | 7.41 | skipped_fast |
| EDELUSDT | IDLE | 1.08 | 5.76 | 3.55 | -0.14 | 185159.95 | 28.04 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 3.73 | 3.02 | -0.1 | 89272.33 | 15.82 | skipped_fast |
| ZBCNUSDT | IDLE | 0.85 | 1.52 | 1.24 | -0.05 | 218864.82 | 28.25 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 5.39 | 5.11 | -0.05 | 3627.16 | 27.24 | skipped_fast |
| RWAINCUSDT | IDLE | 0.66 | 6.09 | 5.74 | 0.14 | 32169.32 | 65.6 | skipped_fast |
| RIZEUSDT | IDLE | 0.32 | 1.99 | 0.57 | -0.15 | 59351.4 | 54.46 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.3 | 0.93 | -0.02 | 59414.7 | 35.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.75 | 0.13 | -0.01 | 36834.97 | 25.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
