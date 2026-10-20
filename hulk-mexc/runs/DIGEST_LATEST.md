# Hulk DIGEST — 2026-10-20T02:58:27Z

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
| ETHUSDT | IDLE | 0.98 | 1.85 | 0.68 | -0.01 | 122526679.76 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.99 | 1.9 | 0.55 | -0.01 | 20338068.59 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.31 | 0.55 | -0.01 | 307358658.45 | 0.05 | skipped_fast |
| PYTHUSDT | IDLE | 2.03 | 3.71 | 2.34 | -0.03 | 1064804.57 | 2.75 | skipped_fast |
| WUSDT | IDLE | 2.98 | 5.57 | 2.64 | 0.01 | 714440.51 | 12.16 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 13.3 | 10.82 | -0.07 | 66630.28 | 34.95 | skipped_fast |
| EDELUSDT | IDLE | 3.05 | 6.01 | 0.65 | 0.03 | 165140.94 | 28.79 | skipped_fast |
| QNTUSDT | IDLE | 1.57 | 3.09 | 0.32 | 0.02 | 696520.78 | 5.6 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.84 | 0.11 | 0.04 | 385479.21 | 5.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 3.33 | 0.73 | -0.01 | 76623.65 | 14.21 | skipped_fast |
| REDUSDT | IDLE | 1.58 | 3.0 | 1.04 | -0.01 | 58274.46 | 10.91 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 2.86 | 1.66 | 0.06 | 76709.47 | 10.64 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 2.56 | 0.26 | 0.02 | 196643.37 | 14.24 | skipped_fast |
| BIOUSDT | IDLE | 1.25 | 2.46 | 0.25 | -0.01 | 67278.38 | 8.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.25 | 2.61 | 1.37 | 0.03 | 68846.86 | 20.66 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.73 | 0.29 | -0.02 | 401967.23 | 6.01 | skipped_fast |
| WAXLUSDT | IDLE | 1.85 | 4.28 | 2.25 | -0.05 | 57238.92 | 54.76 | skipped_fast |
| LAUSDT | IDLE | 1.52 | 2.95 | 0.59 | -0.0 | 55464.66 | 26.59 | skipped_fast |
| IOTAUSDT | IDLE | 1.17 | 2.31 | 0.15 | 0.01 | 90244.42 | 26.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.25 | 0.28 | 0.02 | 4732.18 | 21.54 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.63 | 0.39 | 0.0 | 52741.82 | 23.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.09 | 0.0 | 40075.87 | 8.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
