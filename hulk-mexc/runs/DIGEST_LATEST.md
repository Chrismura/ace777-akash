# Hulk DIGEST — 2026-09-07T06:33:26Z

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
| XRPUSDT | IDLE | 1.17 | 2.12 | 1.45 | -0.01 | 29648873.34 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.95 | 1.71 | 1.24 | -0.0 | 290286663.73 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.09 | 0.86 | -0.0 | 399726337.35 | 0.24 | skipped_fast |
| PYTHUSDT | IDLE | 2.51 | 4.54 | 3.23 | 0.01 | 587260.94 | 3.6 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 6.85 | 5.72 | -0.03 | 438417.54 | 3.57 | skipped_fast |
| EDELUSDT | IDLE | 3.97 | 7.34 | 3.96 | -0.01 | 63974.18 | 28.13 | skipped_fast |
| WUSDT | IDLE | 1.54 | 2.87 | 1.45 | 0.04 | 410307.98 | 14.33 | skipped_fast |
| CCUSDT | IDLE | 1.0 | 1.86 | 0.9 | 0.0 | 386919.14 | 9.08 | skipped_fast |
| RIZEUSDT | IDLE | 1.24 | 8.69 | 1.97 | -0.16 | 70657.92 | 62.31 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.89 | 1.3 | -0.0 | 390131.82 | 1.23 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 2.24 | 1.7 | -0.03 | 55913.01 | 11.17 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 1.99 | 1.27 | -0.02 | 74495.07 | 3.67 | skipped_fast |
| RWAINCUSDT | IDLE | 1.68 | 5.5 | 5.08 | 0.09 | 6826.08 | 78.97 | skipped_fast |
| ZBCNUSDT | IDLE | 0.7 | 1.27 | 0.86 | -0.01 | 131105.28 | 10.79 | skipped_fast |
| REDUSDT | IDLE | 0.67 | 1.28 | 0.43 | -0.0 | 66739.06 | 11.81 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.21 | 1.31 | 0.01 | 97772.4 | 11.53 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.76 | 1.73 | -0.01 | 1096.83 | 16.5 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.22 | 0.86 | 0.01 | 36898.53 | 6.01 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.87 | 0.79 | -0.02 | 53752.72 | 14.44 | skipped_fast |
| MNSRYUSDT | IDLE | 0.1 | 0.19 | 0.05 | -0.0 | 38921.83 | 4.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
