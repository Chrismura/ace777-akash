# Hulk DIGEST — 2026-08-22T08:03:20Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.96 | 0.0 | 24801217.05 | 15.74 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 23.87 | 8.17 | 0.18 | 224236970.7 | 6.41 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.53 | 0.04 | 1354561.82 | 6.36 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.91 | -0.09 | 683278.35 | 6.68 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.81 | 0.04 | 608726.62 | 19.62 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.47 | -0.04 | 247624.89 | 15.9 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 11.11 | 0.06 | 157445.17 | 19.21 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 11.25 | 1.93 | 0.2 | 813039.4 | 7.34 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.03 | 0.03 | 537488.29 | 16.99 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.11 | 0.04 | 194297.34 | 4.61 | skipped_fast |
| KITEUSDT | IDLE | 3.8 | 9.68 | 3.89 | 0.07 | 72863.9 | 11.8 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.12 | skipped_fast |
| EDELUSDT | IDLE | 2.18 | 4.52 | 1.95 | -0.04 | 87115.45 | 55.46 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11250.14 | 112.75 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.95 | -0.01 | 173882.38 | 46.28 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 3.73 | 0.9 | 0.0 | 52279.47 | 44.42 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 1.04 | 0.05 | 58307.9 | 8.05 | skipped_fast |
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
