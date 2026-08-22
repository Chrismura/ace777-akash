# Hulk DIGEST — 2026-08-22T07:12:22Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.37 | 0.03 | 21453272.69 | 13.84 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 23.87 | 6.47 | 0.21 | 217501285.84 | 3.78 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.23 | 0.05 | 1368147.41 | 1.27 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.62 | -0.1 | 705843.79 | 3.32 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.63 | 0.06 | 620446.76 | 11.36 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.38 | -0.03 | 247546.64 | 3.29 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.78 | 0.07 | 160575.33 | 19.15 | skipped_fast |
| CCUSDT | IDLE | 2.07 | 11.25 | 4.06 | 0.18 | 796064.39 | 7.51 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 8.47 | 5.86 | 0.04 | 543178.48 | 62.92 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.28 | 0.04 | 199650.11 | 9.22 | skipped_fast |
| KITEUSDT | IDLE | 3.38 | 9.68 | 2.62 | 0.1 | 74317.22 | 10.74 | skipped_fast |
| EDELUSDT | IDLE | 2.26 | 4.52 | 3.14 | -0.03 | 87327.17 | 33.43 | skipped_fast |
| FLUIDUSDT | IDLE | 3.34 | 7.38 | 4.29 | 0.05 | 6989.9 | 21.9 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.03 | 11442.43 | 101.69 | skipped_fast |
| TELUSDT | IDLE | 2.07 | 5.36 | 3.65 | 0.06 | 196587.45 | 46.14 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3298.33 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.47 | 0.02 | 56848.51 | 46.34 | skipped_fast |
| RWAUSDT | IDLE | 1.77 | 3.29 | 1.67 | 0.04 | 58079.04 | 16.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
