# Hulk DIGEST — 2026-10-20T12:15:11Z

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
| ETHUSDT | IDLE | 0.52 | 0.94 | 0.65 | -0.02 | 123292819.75 | 0.13 | skipped_fast |
| XRPUSDT | IDLE | 0.53 | 0.98 | 0.51 | -0.01 | 18993097.59 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.63 | 0.55 | -0.01 | 291933214.0 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 11.61 | 10.4 | -0.06 | 83418.1 | 5.3 | skipped_fast |
| WUSDT | IDLE | 1.82 | 3.24 | 2.71 | 0.01 | 698884.79 | 15.56 | skipped_fast |
| PYTHUSDT | IDLE | 0.76 | 1.39 | 0.81 | -0.01 | 905832.75 | 1.38 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 9.76 | 6.33 | -0.05 | 67919.44 | 41.76 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 1.9 | 0.46 | 0.01 | 445938.89 | 5.76 | skipped_fast |
| EDELUSDT | IDLE | 1.3 | 7.37 | 0.4 | 0.19 | 296537.03 | 9.32 | skipped_fast |
| ZBCNUSDT | IDLE | 1.67 | 3.02 | 2.07 | -0.03 | 185151.06 | 16.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.73 | 4.18 | 3.74 | 0.03 | 93152.73 | 13.9 | skipped_fast |
| KITEUSDT | IDLE | 1.71 | 3.1 | 2.12 | 0.02 | 90333.53 | 12.52 | skipped_fast |
| QNTUSDT | IDLE | 1.25 | 2.43 | 0.51 | -0.03 | 484738.78 | 1.55 | skipped_fast |
| HBARUSDT | IDLE | 1.32 | 2.34 | 1.98 | -0.01 | 353532.7 | 4.86 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 1.97 | 1.86 | -0.01 | 57723.5 | 9.59 | skipped_fast |
| BIOUSDT | IDLE | 0.64 | 1.2 | 0.55 | 0.0 | 65894.8 | 8.5 | skipped_fast |
| WAXLUSDT | IDLE | 1.93 | 4.21 | 3.34 | -0.08 | 57367.62 | 46.98 | skipped_fast |
| IOTAUSDT | IDLE | 1.05 | 1.91 | 1.27 | 0.01 | 84627.99 | 24.31 | skipped_fast |
| LAUSDT | IDLE | 1.17 | 2.12 | 1.47 | -0.02 | 56657.99 | 25.12 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.31 | 0.01 | 51142.86 | 7.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.1 | 0.0 | 39265.29 | 5.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.35 | 0.65 | 0.27 | 0.01 | 4452.44 | 21.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
