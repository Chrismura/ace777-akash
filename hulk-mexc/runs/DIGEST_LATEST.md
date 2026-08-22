# Hulk DIGEST — 2026-08-22T06:11:27Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.94 | 0.07 | 18858889.03 | 5.9 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 23.87 | 9.88 | 0.16 | 208966084.93 | 3.27 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.31 | 0.05 | 1377426.78 | 2.54 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.26 | -0.09 | 699334.45 | 3.31 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.25 | 0.06 | 614626.61 | 13.46 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.82 | -0.04 | 245836.82 | 6.62 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 42.58 | 12.56 | 0.08 | 165863.18 | 11.47 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 8.47 | 5.72 | 0.04 | 547617.24 | 29.3 | skipped_fast |
| CCUSDT | IDLE | 1.84 | 9.8 | 1.81 | 0.18 | 765391.67 | 8.25 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.04 | 0.04 | 198260.49 | 1.55 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 9.68 | 5.97 | 0.08 | 74858.24 | 12.04 | skipped_fast |
| EDELUSDT | IDLE | 2.21 | 4.52 | 2.38 | -0.02 | 88103.12 | 44.25 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.01 | 11531.83 | 64.66 | skipped_fast |
| FLUIDUSDT | IDLE | 3.24 | 7.9 | 4.42 | 0.06 | 5356.23 | 37.9 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.52 | 2.86 | 0.07 | 195642.74 | 35.6 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 3.99 | 2.64 | 0.08 | 59306.97 | 45.14 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.05 | 58021.69 | 16.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
