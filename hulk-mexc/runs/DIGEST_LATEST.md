# Hulk DIGEST — 2026-08-22T05:45:38Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.92 | 0.07 | 17036815.58 | 7.95 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 11.21 | 0.16 | 204149473.09 | 4.64 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.68 | 0.04 | 1366575.19 | 12.76 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 24.54 | 12.85 | -0.1 | 709784.74 | 13.5 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.82 | 0.05 | 601596.97 | 9.4 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 29.98 | 13.83 | -0.05 | 245391.82 | 16.72 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 45.06 | 14.4 | 0.09 | 164714.38 | 22.2 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 11.56 | 3.94 | 0.17 | 763661.4 | 5.06 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 8.47 | 6.06 | 0.05 | 547566.24 | 31.51 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 13.91 | 9.48 | 0.03 | 197011.15 | 9.34 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 9.68 | 6.59 | 0.07 | 74503.16 | 11.2 | skipped_fast |
| EDELUSDT | IDLE | 2.1 | 4.52 | 0.86 | -0.02 | 88518.88 | 32.84 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 6.91 | 6.23 | 0.06 | 58958.32 | 47.31 | skipped_fast |
| FLUIDUSDT | IDLE | 3.18 | 7.9 | 4.66 | 0.06 | 5400.55 | 21.97 | skipped_fast |
| RWAINCUSDT | IDLE | 2.5 | 4.48 | 3.4 | 0.0 | 11498.71 | 75.47 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3288.58 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 5.52 | 2.96 | 0.07 | 195065.0 | 45.74 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.75 | 0.05 | 57952.55 | 8.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
