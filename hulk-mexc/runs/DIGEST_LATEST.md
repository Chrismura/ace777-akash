# Hulk DIGEST — 2026-10-19T11:59:01Z

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
| XRPUSDT | IDLE | 1.01 | 1.83 | 1.32 | 0.01 | 33094925.16 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.39 | 1.02 | 0.0 | 150077757.18 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.24 | 0.92 | 0.0 | 334666890.88 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.67 | 4.32 | 3.91 | -0.07 | 1005219.03 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 4.09 | 3.08 | 0.0 | 796952.92 | 3.02 | skipped_fast |
| WUSDT | IDLE | 1.56 | 2.79 | 2.15 | -0.05 | 526405.48 | 17.33 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.55 | 2.95 | 0.02 | 238710.75 | 14.8 | skipped_fast |
| HBARUSDT | IDLE | 1.37 | 2.97 | 2.65 | -0.06 | 713508.81 | 4.82 | skipped_fast |
| KITEUSDT | IDLE | 2.29 | 4.38 | 1.39 | 0.02 | 63107.23 | 11.04 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.58 | 0.39 | 0.02 | 328289.92 | 6.79 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 4.1 | 3.17 | 0.0 | 87128.34 | 7.18 | skipped_fast |
| RWAINCUSDT | IDLE | 1.64 | 4.95 | 2.02 | -0.01 | 88833.53 | 31.71 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 2.54 | 2.1 | -0.02 | 72639.0 | 4.28 | skipped_fast |
| ZBCNUSDT | IDLE | 0.53 | 1.99 | 0.24 | 0.02 | 280123.76 | 19.1 | skipped_fast |
| REDUSDT | IDLE | 1.28 | 2.28 | 1.83 | -0.01 | 77054.1 | 10.34 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 4.84 | 3.7 | -0.05 | 60089.62 | 50.8 | skipped_fast |
| IOTAUSDT | IDLE | 1.75 | 3.11 | 2.62 | -0.02 | 76204.74 | 24.87 | skipped_fast |
| LAUSDT | IDLE | 1.48 | 2.58 | 2.52 | -0.03 | 59348.47 | 22.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.49 | 3.69 | 3.55 | 0.01 | 6404.42 | 21.53 | skipped_fast |
| WAXLUSDT | IDLE | 1.09 | 4.2 | 2.94 | 0.02 | 78786.04 | 64.6 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.8 | 0.16 | 0.01 | 55271.36 | 23.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.13 | -0.0 | 40147.96 | 4.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
