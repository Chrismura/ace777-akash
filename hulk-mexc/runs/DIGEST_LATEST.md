# Hulk DIGEST — 2026-10-28T17:41:33Z

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
| ETHUSDT | IDLE | 0.91 | 1.66 | 1.07 | -0.01 | 179045884.36 | 0.09 | skipped_fast |
| XRPUSDT | IDLE | 0.7 | 1.28 | 0.74 | -0.0 | 19247240.8 | 1.52 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.16 | 0.87 | -0.0 | 276339407.57 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 10.25 | 9.3 | -0.02 | 36606.68 | 27.3 | skipped_fast |
| CCUSDT | IDLE | 2.82 | 6.57 | 1.71 | 0.01 | 389215.88 | 9.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 10.65 | 9.36 | -0.11 | 217234.06 | 10.4 | skipped_fast |
| PYTHUSDT | IDLE | 1.46 | 2.57 | 2.3 | -0.02 | 380315.7 | 1.42 | skipped_fast |
| WUSDT | IDLE | 1.32 | 2.42 | 1.48 | -0.01 | 424276.16 | 15.0 | skipped_fast |
| QNTUSDT | IDLE | 2.24 | 4.03 | 3.05 | -0.02 | 401642.48 | 2.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.66 | 3.18 | 1.8 | -0.06 | 259459.9 | 25.24 | skipped_fast |
| EDELUSDT | IDLE | 1.55 | 2.77 | 2.21 | -0.01 | 186288.98 | 21.63 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.07 | 1.85 | -0.02 | 496429.96 | 8.01 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 2.75 | 1.71 | -0.0 | 84229.73 | 8.92 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.08 | 1.36 | -0.03 | 58422.72 | 11.31 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.71 | 1.15 | -0.02 | 54672.45 | 15.26 | skipped_fast |
| RIZEUSDT | IDLE | 1.08 | 1.91 | 1.69 | 0.02 | 37783.55 | 61.98 | skipped_fast |
| LAUSDT | IDLE | 1.88 | 3.32 | 2.99 | -0.06 | 57720.77 | 20.93 | skipped_fast |
| IOTAUSDT | IDLE | 1.73 | 3.05 | 2.7 | -0.02 | 73849.09 | 24.31 | skipped_fast |
| FLUIDUSDT | IDLE | 1.16 | 3.48 | 2.76 | -0.01 | 6687.12 | 21.18 | skipped_fast |
| WAXLUSDT | IDLE | 1.34 | 2.38 | 2.06 | -0.02 | 55862.8 | 72.89 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.12 | 0.95 | -0.01 | 55468.24 | 48.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.51 | 0.44 | 0.0 | 35497.16 | 54.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
