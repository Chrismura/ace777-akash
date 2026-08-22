# Hulk DIGEST — 2026-08-22T05:17:48Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 19.14 | 11.39 | 0.06 | 15456329.58 | 54.54 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 23.87 | 11.68 | 0.14 | 192567084.68 | 16.01 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 10.07 | 0.04 | 1330267.11 | 47.44 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.82 | -0.1 | 625069.07 | 16.73 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.9 | 0.05 | 565853.67 | 27.24 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 29.98 | 13.6 | -0.05 | 210066.97 | 56.73 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 11.56 | 5.07 | 0.15 | 759093.8 | 18.76 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.08 | 0.1 | 163236.12 | 142.22 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 8.47 | 7.47 | 0.03 | 543687.65 | 90.89 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 13.91 | 10.0 | 0.03 | 193228.88 | 38.81 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.92 | 9.68 | 6.84 | 0.07 | 73283.05 | 75.35 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 4.29 | 0.0 | -0.0 | 86925.42 | 10.84 | skipped_fast |
| RWAINCUSDT | IDLE | 2.51 | 4.48 | 3.55 | 0.01 | 11335.16 | 96.72 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 7.9 | 5.99 | 0.04 | 5406.56 | 56.26 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.01 | 5.52 | 1.43 | 0.09 | 191817.49 | 44.97 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 3.99 | 0.09 | 58694.34 | 44.52 | skipped_fast |
| RWAUSDT | IDLE | 1.86 | 3.38 | 2.31 | 0.04 | 57445.27 | 24.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
