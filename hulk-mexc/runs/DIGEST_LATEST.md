# Hulk DIGEST — 2026-10-02T18:44:39Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 6.71 | 5.77 | -0.03 | 59717976.14 | 2.05 | skipped_fast |
| ETHUSDT | IDLE | 2.51 | 4.42 | 4.05 | -0.02 | 531414904.36 | 0.75 | skipped_fast |
| QNTUSDT | IDLE | 1.93 | 7.68 | 6.59 | -0.11 | 5176712.27 | 5.52 | skipped_fast |
| BTCUSDT | IDLE | 2.18 | 3.82 | 3.55 | -0.01 | 869370636.83 | 0.1 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 30.27 | 6.59 | 0.13 | 632312.64 | 39.53 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.54 | 9.49 | 8.39 | -0.03 | 533473.46 | 14.65 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.53 | 10.88 | 9.68 | -0.05 | 499893.01 | 17.0 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 10.26 | 7.31 | -0.05 | 875592.09 | 13.18 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.99 | 8.65 | 7.83 | -0.0 | 526937.01 | 20.11 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.54 | 10.1 | 9.17 | -0.03 | 97189.94 | 20.35 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.05 | 7.69 | 6.99 | -0.01 | 90829.25 | 25.71 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.69 | 17.55 | 7.38 | -0.09 | 44357.59 | 56.52 | skipped_fast |
| KITEUSDT | IDLE | 3.22 | 5.71 | 4.83 | -0.04 | 80543.26 | 21.45 | skipped_fast |
| ZBCNUSDT | IDLE | 2.43 | 5.91 | 4.57 | -0.02 | 283458.9 | 46.4 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 9.7 | 8.51 | -0.09 | 148532.71 | 35.42 | skipped_fast |
| REDUSDT | IDLE | 2.15 | 8.4 | 7.5 | -0.07 | 117308.92 | 22.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.73 | 4.63 | 4.42 | -0.06 | 5342.71 | 30.51 | skipped_fast |
| FLUIDUSDT | IDLE | 2.03 | 5.14 | 4.56 | 0.06 | 6471.37 | 38.6 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.53 | 1.37 | -0.0 | 54662.8 | 14.59 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.8 | 0.27 | 0.01 | 39807.63 | 55.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
