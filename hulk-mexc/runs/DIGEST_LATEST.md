# Hulk DIGEST — 2026-08-22T05:46:57Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.91 | 0.07 | 17100441.34 | 9.94 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 11.01 | 0.16 | 204503148.26 | 5.96 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.57 | 0.05 | 1367225.15 | 8.91 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.59 | -0.1 | 712405.14 | 13.44 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.41 | 0.06 | 601760.67 | 14.56 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 29.98 | 13.51 | -0.05 | 244477.04 | 3.34 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 45.06 | 14.26 | 0.09 | 164856.36 | 10.63 | skipped_fast |
| CCUSDT | IDLE | 2.21 | 11.56 | 3.52 | 0.17 | 764909.8 | 11.7 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 8.47 | 6.21 | 0.04 | 547490.39 | 25.98 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 13.91 | 9.41 | 0.04 | 197029.36 | 10.87 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 9.68 | 6.66 | 0.07 | 74444.87 | 12.11 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 4.52 | 1.08 | -0.03 | 88519.93 | 43.81 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.16 | 0.06 | 58974.72 | 47.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.0 | 11498.71 | 70.06 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5400.55 | 21.93 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.07 | 5.52 | 2.67 | 0.07 | 195480.32 | 40.67 | skipped_fast |
| RWAUSDT | IDLE | 1.84 | 3.38 | 1.99 | 0.05 | 57957.82 | 8.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
