# Hulk DIGEST — 2026-10-29T01:45:36Z

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
| XRPUSDT | IDLE | 1.55 | 2.73 | 2.51 | -0.02 | 22568162.61 | 2.29 | skipped_fast |
| ETHUSDT | IDLE | 1.5 | 2.64 | 2.46 | -0.01 | 207613986.95 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.92 | 1.61 | 1.49 | -0.0 | 319972215.64 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.13 | 3.92 | 2.25 | -0.01 | 443139.63 | 19.19 | skipped_fast |
| CCUSDT | IDLE | 1.8 | 3.81 | 3.57 | -0.01 | 439217.58 | 9.12 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.46 | 3.13 | -0.01 | 409900.53 | 19.03 | skipped_fast |
| HBARUSDT | IDLE | 2.18 | 3.83 | 3.48 | -0.03 | 561872.73 | 9.42 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 4.02 | 3.69 | -0.01 | 87714.16 | 8.92 | skipped_fast |
| IOTAUSDT | WATCH_PULLBACK — tension haute + reflux | 3.59 | 6.3 | 5.93 | -0.05 | 77102.15 | 17.3 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 3.5 | 2.43 | -0.04 | 174920.0 | 31.56 | skipped_fast |
| QNTUSDT | IDLE | 1.79 | 3.13 | 2.94 | -0.01 | 416224.38 | 4.58 | skipped_fast |
| KITEUSDT | IDLE | 1.82 | 3.2 | 2.92 | -0.03 | 60995.05 | 9.61 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 1.71 | 1.44 | 0.0 | 285461.98 | 33.16 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 3.1 | 2.65 | -0.1 | 234011.08 | 16.36 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 2.73 | 2.42 | -0.03 | 56200.77 | 14.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.36 | 5.58 | 1.17 | -0.05 | 34854.56 | 6.96 | skipped_fast |
| RIZEUSDT | IDLE | 1.79 | 3.31 | 2.2 | -0.03 | 39326.26 | 49.71 | skipped_fast |
| WAXLUSDT | IDLE | 2.88 | 5.05 | 4.79 | -0.04 | 53446.65 | 46.49 | skipped_fast |
| LAUSDT | IDLE | 1.95 | 3.41 | 3.23 | -0.04 | 54211.93 | 26.11 | skipped_fast |
| FLUIDUSDT | IDLE | 1.96 | 3.43 | 3.31 | -0.02 | 5216.08 | 21.23 | skipped_fast |
| RWAUSDT | IDLE | 0.73 | 1.37 | 0.56 | 0.01 | 54440.74 | 31.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.07 | 0.01 | 36399.08 | 40.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
