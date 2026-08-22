# Hulk DIGEST — 2026-08-22T06:20:46Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.11 | 19.14 | 8.02 | 0.07 | 19468021.09 | 3.89 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 23.87 | 9.67 | 0.17 | 209478479.61 | 2.61 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.57 | 0.04 | 1384681.04 | 3.82 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.26 | -0.09 | 691491.97 | 6.63 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.87 | 0.06 | 615264.31 | 15.5 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 13.28 | -0.04 | 244758.88 | 16.56 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.65 | 0.09 | 166103.76 | 12.24 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 11.25 | 1.97 | 0.2 | 768864.3 | 10.59 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 8.47 | 5.7 | 0.03 | 545856.41 | 27.87 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.04 | 0.04 | 199146.38 | 1.55 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 9.68 | 5.31 | 0.08 | 74894.35 | 11.93 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.02 | 6441.01 | 22.73 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.01 | 11505.67 | 64.66 | skipped_fast |
| EDELUSDT | IDLE | 2.32 | 4.52 | 4.0 | -0.03 | 88150.45 | 89.69 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.52 | 4.1 | 0.05 | 196780.49 | 41.17 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.97 | 3.99 | 2.86 | 0.08 | 59422.73 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.67 | 0.05 | 58088.45 | 8.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
