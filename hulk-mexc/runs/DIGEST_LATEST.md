# Hulk DIGEST — 2026-08-22T10:36:27Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 16.77 | 11.22 | 0.01 | 51647629.22 | 2.06 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 23.87 | 12.48 | 0.08 | 217498486.84 | 9.42 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.44 | 15.8 | 11.59 | 0.01 | 1247052.02 | 1.3 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 22.93 | 11.77 | -0.1 | 661883.19 | 6.76 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.9 | 0.01 | 597478.06 | 14.9 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.15 | -0.06 | 239024.29 | 3.29 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.58 | 0.12 | 811318.33 | 11.25 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 9.72 | 8.24 | -0.03 | 426299.82 | 19.04 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.19 | 0.03 | 154691.38 | 13.51 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 9.28 | 5.24 | 0.03 | 73196.76 | 9.23 | skipped_fast |
| EDELUSDT | IDLE | 3.35 | 5.96 | 4.97 | -0.04 | 78943.93 | 34.07 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.62 | 9.12 | 8.21 | -0.05 | 168426.1 | 37.71 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 9.75 | 6.72 | -0.0 | 189461.2 | 7.85 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5710.05 | 21.72 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | -0.01 | 3242.83 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11275.22 | 43.43 | skipped_fast |
| RWAUSDT | IDLE | 1.81 | 3.29 | 2.23 | 0.01 | 57415.24 | 8.15 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.26 | 0.0 | 49259.38 | 46.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
