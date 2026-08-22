# Hulk DIGEST — 2026-08-22T10:48:31Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 16.77 | 11.49 | 0.01 | 51652160.76 | 2.06 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 23.87 | 12.39 | 0.08 | 218258683.05 | 0.67 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 15.8 | 11.14 | 0.0 | 1250407.03 | 2.59 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.53 | -0.09 | 663283.09 | 3.37 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.67 | 0.01 | 596155.91 | 11.68 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.52 | -0.05 | 240518.54 | 3.26 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 11.25 | 7.93 | 0.12 | 817484.78 | 6.08 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.26 | 0.03 | 154297.41 | 19.84 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 9.72 | 7.88 | -0.03 | 424156.52 | 25.62 | skipped_fast |
| KITEUSDT | IDLE | 4.12 | 9.28 | 4.68 | 0.04 | 73390.65 | 12.89 | skipped_fast |
| EDELUSDT | IDLE | 3.35 | 5.96 | 4.97 | -0.04 | 78951.57 | 34.03 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 9.75 | 6.44 | -0.01 | 189244.96 | 7.82 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.6 | 9.12 | 7.81 | -0.04 | 168806.52 | 53.59 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.38 | 5.33 | -0.01 | 5711.25 | 21.64 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.0 | 3237.82 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 59.77 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.23 | 0.01 | 57374.76 | 8.15 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 3.18 | 1.48 | -0.0 | 49199.02 | 46.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
