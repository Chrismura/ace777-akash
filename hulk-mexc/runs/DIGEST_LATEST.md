# Hulk DIGEST — 2026-10-28T13:36:42Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 1.28 | 2.25 | 2.02 | 0.0 | 236525418.69 | 0.47 | skipped_fast |
| XRPUSDT | IDLE | 1.14 | 2.04 | 1.62 | 0.0 | 19944748.91 | 0.76 | skipped_fast |
| BTCUSDT | IDLE | 0.85 | 1.51 | 1.33 | 0.01 | 311694827.6 | 0.0 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.53 | 9.68 | 8.61 | -0.03 | 355480.11 | 5.23 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.5 | 11.76 | 9.86 | -0.02 | 179087.1 | 17.43 | skipped_fast |
| RWAINCUSDT | IDLE | 4.14 | 10.56 | 2.42 | 0.05 | 47158.19 | 6.36 | skipped_fast |
| WUSDT | IDLE | 1.41 | 2.52 | 2.06 | -0.01 | 577611.43 | 18.93 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.52 | 1.89 | -0.02 | 426708.37 | 1.4 | skipped_fast |
| QNTUSDT | IDLE | 2.46 | 4.45 | 3.13 | -0.02 | 455991.92 | 7.11 | skipped_fast |
| ZBCNUSDT | IDLE | 2.08 | 3.94 | 2.64 | -0.04 | 229179.72 | 5.35 | skipped_fast |
| EDELUSDT | IDLE | 1.47 | 2.58 | 2.39 | -0.01 | 255484.19 | 21.69 | skipped_fast |
| HBARUSDT | IDLE | 1.27 | 2.26 | 1.91 | -0.01 | 461507.12 | 7.96 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 2.5 | 2.27 | 0.01 | 87059.09 | 8.91 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.72 | 1.57 | -0.03 | 59900.93 | 12.16 | skipped_fast |
| REDUSDT | IDLE | 0.83 | 1.44 | 1.42 | 0.0 | 52963.77 | 15.89 | skipped_fast |
| RIZEUSDT | IDLE | 1.0 | 1.79 | 1.35 | 0.02 | 36391.37 | 66.34 | skipped_fast |
| IOTAUSDT | IDLE | 1.56 | 2.78 | 2.21 | -0.01 | 76334.81 | 23.96 | skipped_fast |
| LAUSDT | IDLE | 1.36 | 2.41 | 2.13 | 0.01 | 59854.37 | 24.03 | skipped_fast |
| WAXLUSDT | IDLE | 1.37 | 2.45 | 1.96 | -0.02 | 56073.16 | 47.51 | skipped_fast |
| FLUIDUSDT | IDLE | 0.67 | 1.84 | 1.81 | 0.01 | 6424.69 | 21.42 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.29 | 0.24 | 0.02 | 54408.08 | 39.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.64 | 1.25 | 0.19 | 0.01 | 36376.84 | 54.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
