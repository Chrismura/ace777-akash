# Hulk DIGEST — 2026-08-22T05:56:44Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.96 | 0.08 | 17691825.82 | 11.8 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 23.87 | 9.79 | 0.17 | 206333012.46 | 5.22 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 15.8 | 8.76 | 0.05 | 1368555.63 | 29.06 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.12 | -0.09 | 710187.39 | 6.69 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.39 | 0.07 | 610156.75 | 6.18 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.01 | -0.03 | 246207.31 | 9.88 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.76 | 0.09 | 164920.21 | 11.49 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.96 | 0.17 | 762990.09 | 10.01 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 8.47 | 6.2 | 0.04 | 547529.38 | 15.5 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 13.91 | 8.94 | 0.04 | 197119.1 | 7.74 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 6.01 | 0.08 | 74167.21 | 11.14 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 4.52 | 1.41 | -0.01 | 88078.58 | 32.84 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.0 | 11566.79 | 64.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.08 | 0.06 | 59012.67 | 45.57 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.65 | 0.06 | 5383.27 | 18.91 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3293.96 | 7.99 | skipped_fast |
| TELUSDT | IDLE | 2.04 | 5.52 | 2.17 | 0.08 | 196328.21 | 55.65 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.67 | 0.05 | 57905.0 | 24.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
