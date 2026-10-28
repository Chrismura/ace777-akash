# Hulk DIGEST — 2026-10-28T02:23:16Z

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
| XRPUSDT | IDLE | 1.02 | 2.0 | 0.3 | 0.03 | 19106566.69 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.24 | 0.36 | 0.02 | 246452928.17 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.81 | 0.32 | 0.01 | 322880091.38 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.14 | 3.95 | 2.15 | 0.01 | 417214.53 | 21.36 | skipped_fast |
| WUSDT | IDLE | 0.9 | 2.02 | 1.14 | 0.04 | 671338.12 | 17.98 | skipped_fast |
| QNTUSDT | IDLE | 1.41 | 2.62 | 1.27 | -0.02 | 666700.09 | 1.5 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 11.2 | 8.86 | 0.01 | 7290.81 | 21.51 | skipped_fast |
| PYTHUSDT | IDLE | 1.0 | 1.9 | 0.66 | 0.0 | 403731.08 | 2.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.63 | 5.83 | 3.08 | -0.02 | 260122.09 | 36.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.93 | 4.11 | 3.17 | -0.04 | 57688.27 | 20.09 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 2.17 | 0.74 | 0.01 | 232840.12 | 10.06 | skipped_fast |
| CHIPUSDT | IDLE | 1.1 | 2.92 | 0.4 | 0.07 | 126585.96 | 23.6 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 2.09 | 0.35 | 0.03 | 59486.53 | 8.77 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 1.83 | 1.0 | 0.04 | 58297.32 | 12.68 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 1.91 | 1.46 | 0.06 | 59657.15 | 16.92 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.69 | 0.19 | 0.0 | 323531.25 | 10.42 | skipped_fast |
| LAUSDT | IDLE | 1.5 | 2.93 | 2.18 | 0.03 | 58761.25 | 21.76 | skipped_fast |
| RIZEUSDT | IDLE | 0.55 | 1.07 | 0.25 | 0.0 | 34613.45 | 62.38 | skipped_fast |
| IOTAUSDT | IDLE | 1.29 | 2.49 | 0.56 | 0.01 | 74707.81 | 35.17 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.21 | 0.8 | -0.01 | 57153.85 | 16.05 | skipped_fast |
| WAXLUSDT | IDLE | 0.71 | 1.38 | 0.26 | 0.05 | 56966.31 | 44.72 | skipped_fast |
| MNSRYUSDT | IDLE | 0.45 | 0.8 | 0.6 | -0.0 | 36447.06 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
