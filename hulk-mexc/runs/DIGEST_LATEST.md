# Hulk DIGEST — 2026-08-22T05:40:16Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.37 | 0.08 | 16881846.84 | 13.84 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 11.08 | 0.16 | 203083908.89 | 6.63 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.53 | 0.05 | 1361149.13 | 31.89 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.41 | -0.1 | 706209.46 | 3.35 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.18 | 0.06 | 599367.86 | 19.73 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 12.9 | -0.04 | 228245.14 | 6.63 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 45.06 | 13.57 | 0.1 | 164300.59 | 11.45 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 11.56 | 4.06 | 0.17 | 762940.66 | 2.53 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 8.47 | 5.66 | 0.05 | 547261.69 | 33.84 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 13.91 | 9.19 | 0.04 | 197010.02 | 74.33 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 6.03 | 0.08 | 73331.14 | 13.91 | skipped_fast |
| EDELUSDT | IDLE | 2.13 | 4.52 | 1.19 | -0.02 | 88466.99 | 32.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.33 | 0.06 | 58933.32 | 28.08 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.0 | 11498.71 | 75.47 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5410.56 | 34.92 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.1 | 5.52 | 3.26 | 0.07 | 195464.83 | 40.82 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.75 | 0.05 | 57936.63 | 24.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
