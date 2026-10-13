# Hulk DIGEST — 2026-10-13T21:09:07Z

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
| WUSDT | IDLE | 1.47 | 10.22 | 1.19 | -0.14 | 4776798.55 | 16.63 | skipped_fast |
| PYTHUSDT | IDLE | 1.1 | 3.46 | 2.5 | -0.07 | 2212470.85 | 1.28 | skipped_fast |
| QNTUSDT | IDLE | 2.89 | 10.52 | 2.88 | -0.06 | 1684073.19 | 1.85 | skipped_fast |
| XRPUSDT | IDLE | 0.62 | 1.15 | 0.55 | 0.0 | 37375205.65 | 0.73 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.1 | 0.52 | -0.0 | 235000418.41 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.76 | 0.24 | 0.01 | 395053047.78 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.1 | 3.33 | 1.88 | 0.05 | 617913.5 | 6.26 | skipped_fast |
| RIZEUSDT | IDLE | 2.73 | 8.99 | 4.32 | 0.01 | 52760.7 | 61.51 | skipped_fast |
| RWAINCUSDT | IDLE | 2.46 | 4.56 | 2.37 | 0.02 | 31304.2 | 19.42 | skipped_fast |
| EDELUSDT | IDLE | 1.35 | 2.81 | 1.27 | 0.01 | 246501.02 | 11.67 | skipped_fast |
| REDUSDT | IDLE | 1.71 | 3.7 | 0.12 | -0.01 | 132663.02 | 15.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 1.98 | 1.8 | -0.02 | 220941.13 | 18.1 | skipped_fast |
| CHIPUSDT | IDLE | 1.1 | 2.56 | 0.6 | -0.01 | 105822.51 | 12.15 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 2.2 | 0.79 | -0.02 | 75602.38 | 7.24 | skipped_fast |
| KITEUSDT | IDLE | 0.75 | 1.64 | 0.15 | 0.01 | 60407.37 | 12.48 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.59 | 0.44 | -0.02 | 323627.12 | 3.42 | skipped_fast |
| TELUSDT | IDLE | 1.98 | 3.74 | 1.44 | 0.01 | 116662.29 | 39.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.62 | 3.66 | 0.0 | 0.04 | 23327.31 | 21.34 | skipped_fast |
| RWAUSDT | IDLE | 0.21 | 0.39 | 0.23 | -0.0 | 52436.78 | 15.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.24 | 0.45 | 0.17 | -0.02 | 38458.89 | 13.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
