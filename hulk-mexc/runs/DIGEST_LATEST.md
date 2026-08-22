# Hulk DIGEST — 2026-08-22T07:03:55Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.13 | 0.04 | 20974037.23 | 1.97 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 23.87 | 6.85 | 0.21 | 216060533.21 | 6.32 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.08 | 0.05 | 1390594.98 | 6.33 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.21 | -0.1 | 704400.54 | 6.62 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 17.58 | 6.92 | 0.07 | 619766.74 | 12.3 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 11.92 | -0.03 | 247483.25 | 3.28 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.83 | 0.06 | 160605.22 | 20.87 | skipped_fast |
| CCUSDT | IDLE | 2.03 | 11.25 | 2.82 | 0.19 | 790620.05 | 7.4 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 8.47 | 5.04 | 0.05 | 544157.22 | 16.3 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.17 | 0.04 | 200289.7 | 10.73 | skipped_fast |
| KITEUSDT | IDLE | 3.4 | 9.68 | 2.93 | 0.11 | 74406.13 | 11.67 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.92 | -0.03 | 87561.88 | 22.27 | skipped_fast |
| FLUIDUSDT | IDLE | 3.34 | 7.38 | 4.29 | 0.05 | 6989.9 | 21.79 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.0 | 11258.23 | 91.72 | skipped_fast |
| TELUSDT | IDLE | 2.05 | 5.36 | 3.41 | 0.06 | 196660.48 | 51.2 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3304.43 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.5 | 0.06 | 57827.24 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.78 | 3.29 | 1.75 | 0.04 | 57928.47 | 24.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
