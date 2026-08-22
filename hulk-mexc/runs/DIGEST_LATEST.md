# Hulk DIGEST — 2026-08-22T09:48:32Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 19.14 | 11.43 | 0.01 | 46298142.39 | 18.19 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 23.87 | 12.07 | 0.07 | 218303737.71 | 4.02 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 15.8 | 10.66 | 0.02 | 1267426.85 | 1.29 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 23.96 | 12.53 | -0.1 | 665265.05 | 16.88 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 17.58 | 9.61 | 0.02 | 591545.96 | 18.98 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.62 | -0.04 | 237676.96 | 16.12 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.46 | 0.11 | 805923.37 | 8.72 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 12.16 | 0.05 | 154259.06 | 20.44 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 8.0 | 7.34 | -0.02 | 438441.53 | 35.01 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 9.68 | 5.0 | 0.04 | 73135.89 | 11.01 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.28 | 0.0 | 192868.2 | 4.66 | skipped_fast |
| EDELUSDT | IDLE | 2.5 | 4.52 | 3.24 | -0.02 | 79232.51 | 33.58 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 21.39 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.78 | 7.03 | 6.12 | -0.02 | 170949.66 | 47.41 | skipped_fast |
| RWAINCUSDT | IDLE | 2.42 | 4.36 | 3.14 | 0.01 | 11436.39 | 91.42 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.82 | -0.01 | 49340.43 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.03 | 57576.54 | 16.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
