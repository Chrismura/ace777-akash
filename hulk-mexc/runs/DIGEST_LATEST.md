# Hulk DIGEST — 2026-10-29T12:22:01Z

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
| ETHUSDT | IDLE | 0.56 | 1.08 | 0.26 | -0.01 | 233744505.52 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.41 | 0.74 | 0.56 | -0.02 | 23186059.93 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.31 | -0.01 | 339885270.76 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.42 | 4.83 | 0.0 | 0.01 | 416460.79 | 9.95 | skipped_fast |
| WUSDT | IDLE | 1.54 | 2.87 | 1.43 | -0.03 | 483859.98 | 17.83 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 2.41 | 2.31 | -0.03 | 445608.06 | 2.88 | skipped_fast |
| EDELUSDT | IDLE | 1.51 | 2.73 | 1.96 | -0.04 | 232373.81 | 3.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 4.1 | 1.11 | -0.08 | 191616.37 | 12.46 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 2.9 | 0.4 | -0.01 | 66808.57 | 4.48 | skipped_fast |
| HBARUSDT | IDLE | 0.61 | 1.13 | 0.65 | -0.02 | 559032.81 | 4.08 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 2.02 | 0.7 | -0.02 | 425193.7 | 0.52 | skipped_fast |
| RWAINCUSDT | IDLE | 1.36 | 4.82 | 1.74 | -0.1 | 34244.32 | 21.28 | skipped_fast |
| ZBCNUSDT | IDLE | 0.61 | 1.1 | 0.85 | -0.01 | 249546.38 | 26.91 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.26 | 0.23 | -0.02 | 64607.48 | 10.76 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.19 | 0.14 | -0.02 | 60170.02 | 9.68 | skipped_fast |
| LAUSDT | IDLE | 2.06 | 3.7 | 2.78 | -0.03 | 57814.51 | 22.91 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 0.89 | 0.56 | -0.02 | 39640.06 | 49.3 | skipped_fast |
| IOTAUSDT | IDLE | 1.07 | 2.04 | 0.99 | -0.04 | 94264.88 | 22.41 | skipped_fast |
| RWAUSDT | IDLE | 1.14 | 2.01 | 1.82 | -0.01 | 55985.37 | 16.09 | skipped_fast |
| WAXLUSDT | IDLE | 1.32 | 3.33 | 0.15 | -0.04 | 54205.48 | 36.54 | skipped_fast |
| FLUIDUSDT | IDLE | 1.39 | 2.79 | 0.99 | -0.06 | 6322.22 | 21.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.72 | 0.16 | -0.01 | 36409.19 | 5.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
