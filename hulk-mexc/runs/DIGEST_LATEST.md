# Hulk DIGEST — 2026-08-22T05:21:21Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.71 | 0.08 | 15851165.4 | 11.9 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 11.25 | 0.14 | 195187223.16 | 13.28 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.32 | 0.05 | 1332384.6 | 47.04 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.29 | -0.09 | 673587.49 | 23.24 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.51 | 0.06 | 574925.79 | 23.94 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 45.06 | 12.15 | 0.11 | 164092.94 | 11.23 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 29.98 | 11.37 | -0.03 | 213780.34 | 26.03 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 11.56 | 4.4 | 0.16 | 759784.53 | 12.66 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 8.47 | 6.72 | 0.04 | 544090.21 | 50.31 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 13.91 | 9.24 | 0.04 | 193214.77 | 21.77 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 9.68 | 6.3 | 0.08 | 73343.61 | 12.98 | skipped_fast |
| EDELUSDT | IDLE | 2.1 | 4.52 | 0.86 | -0.01 | 88091.89 | 32.7 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 7.9 | 5.99 | 0.04 | 5406.56 | 39.17 | skipped_fast |
| RWAINCUSDT | IDLE | 2.51 | 4.48 | 3.55 | 0.01 | 11281.01 | 102.07 | skipped_fast |
| TELUSDT | IDLE | 2.04 | 5.52 | 2.02 | 0.08 | 192494.34 | 25.18 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 4.41 | 3.86 | 0.09 | 58700.98 | 42.81 | skipped_fast |
| RWAUSDT | IDLE | 1.86 | 3.38 | 2.31 | 0.04 | 57599.75 | 32.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
