# Hulk DIGEST — 2026-10-28T03:23:56Z

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
| XRPUSDT | IDLE | 0.88 | 1.65 | 0.68 | 0.03 | 19182408.38 | 2.25 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.21 | 0.35 | 0.02 | 246365828.19 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.64 | 0.17 | 0.02 | 312136249.07 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 3.4 | 2.63 | 0.01 | 409379.56 | 24.52 | skipped_fast |
| WUSDT | IDLE | 0.61 | 1.37 | 0.6 | 0.04 | 664458.93 | 24.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.12 | 5.49 | 2.53 | -0.0 | 256264.27 | 36.89 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 11.23 | 9.73 | 0.0 | 7467.51 | 22.18 | skipped_fast |
| PYTHUSDT | IDLE | 0.96 | 1.75 | 1.18 | 0.01 | 390947.18 | 4.1 | skipped_fast |
| QNTUSDT | IDLE | 0.9 | 1.6 | 1.3 | -0.02 | 662946.96 | 1.01 | skipped_fast |
| RWAINCUSDT | IDLE | 2.26 | 4.75 | 4.14 | -0.04 | 58230.72 | 26.99 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 2.02 | 0.7 | 0.02 | 214560.91 | 7.03 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 3.29 | 1.22 | 0.08 | 127090.0 | 12.77 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.83 | 1.21 | 0.05 | 59373.39 | 9.32 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.73 | 0.65 | 0.03 | 59608.46 | 4.39 | skipped_fast |
| REDUSDT | IDLE | 0.82 | 1.62 | 1.36 | 0.06 | 59594.12 | 8.46 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.69 | 0.34 | 0.01 | 325745.85 | 11.72 | skipped_fast |
| LAUSDT | IDLE | 1.33 | 2.53 | 2.39 | 0.03 | 58495.1 | 23.59 | skipped_fast |
| IOTAUSDT | IDLE | 1.18 | 2.27 | 0.58 | 0.02 | 75385.95 | 23.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.35 | 0.65 | 0.28 | 0.01 | 34896.41 | 64.68 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.05 | 0.64 | -0.01 | 56428.18 | 16.05 | skipped_fast |
| WAXLUSDT | IDLE | 0.7 | 1.25 | 1.06 | 0.05 | 57003.13 | 47.19 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.77 | 0.54 | -0.0 | 36013.66 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
