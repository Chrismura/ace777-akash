# Hulk DIGEST — 2026-08-22T05:13:17Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 19.14 | 12.39 | 0.05 | 14854090.74 | 69.57 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 23.87 | 10.85 | 0.14 | 189126634.75 | 24.4 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 10.28 | 0.03 | 1304385.3 | 52.62 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 24.54 | 14.44 | -0.13 | 579532.7 | 24.05 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 17.58 | 10.54 | 0.03 | 537368.28 | 43.71 | skipped_fast |
| CCUSDT | IDLE | 2.31 | 11.56 | 7.04 | 0.12 | 757889.0 | 46.74 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.44 | 45.06 | 18.23 | 0.04 | 161832.07 | 224.39 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.03 | 7.86 | 6.6 | 0.05 | 541750.29 | 54.12 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.61 | -0.05 | 208360.22 | 496.41 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.99 | 9.68 | 8.66 | 0.05 | 72334.39 | 69.87 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 13.91 | 8.66 | 0.06 | 189096.47 | 196.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11016.11 | 21.61 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 7.9 | 5.26 | 0.06 | 5158.18 | 65.43 | skipped_fast |
| EDELUSDT | IDLE | 1.56 | 3.39 | 0.33 | -0.01 | 83839.36 | 32.84 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.98 | 5.52 | 0.99 | 0.09 | 188409.33 | 39.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 4.03 | 0.09 | 58678.52 | 44.52 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.05 | 57225.95 | 16.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
