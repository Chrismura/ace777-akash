# Hulk DIGEST — 2026-10-20T11:12:39Z

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
| XRPUSDT | IDLE | 0.62 | 1.14 | 0.61 | -0.01 | 19460347.09 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 1.03 | 0.52 | -0.01 | 126003571.68 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.66 | 0.31 | -0.01 | 293072115.5 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.88 | 1.71 | 0.32 | -0.02 | 932854.29 | 2.75 | skipped_fast |
| WUSDT | IDLE | 1.64 | 2.99 | 1.96 | 0.02 | 708117.66 | 11.59 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.7 | 10.32 | 5.61 | 0.04 | 81271.05 | 5.03 | skipped_fast |
| EDELUSDT | IDLE | 1.63 | 9.33 | 0.19 | 0.19 | 301892.68 | 18.63 | skipped_fast |
| CCUSDT | IDLE | 1.1 | 2.07 | 0.81 | 0.01 | 444567.31 | 5.77 | skipped_fast |
| ZBCNUSDT | IDLE | 1.64 | 3.02 | 1.77 | -0.03 | 175053.46 | 5.78 | skipped_fast |
| KITEUSDT | IDLE | 1.93 | 3.47 | 2.58 | 0.01 | 88633.93 | 10.86 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.43 | 0.25 | -0.04 | 525391.89 | 1.03 | skipped_fast |
| CHIPUSDT | IDLE | 1.28 | 3.31 | 1.31 | 0.06 | 88185.18 | 13.57 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.19 | 1.63 | -0.0 | 352082.97 | 2.42 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 2.22 | 1.6 | 0.0 | 58748.59 | 17.62 | skipped_fast |
| BIOUSDT | IDLE | 0.59 | 1.15 | 0.17 | 0.01 | 65741.85 | 8.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 2.22 | 1.56 | -0.07 | 64472.3 | 61.47 | skipped_fast |
| IOTAUSDT | IDLE | 1.42 | 2.56 | 1.91 | 0.02 | 84500.47 | 28.74 | skipped_fast |
| WAXLUSDT | IDLE | 1.66 | 3.63 | 2.61 | -0.07 | 57963.69 | 67.03 | skipped_fast |
| LAUSDT | IDLE | 1.21 | 2.2 | 1.41 | -0.02 | 55686.69 | 28.93 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.31 | 0.01 | 51343.84 | 7.86 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 0.99 | 0.6 | -0.0 | 4463.59 | 21.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.24 | 0.06 | -0.0 | 39586.29 | 8.55 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
