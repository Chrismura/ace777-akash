# Hulk DIGEST — 2026-09-06T08:29:33Z

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
| XRPUSDT | IDLE | 0.91 | 1.65 | 1.08 | 0.01 | 25237631.98 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.61 | 1.11 | 0.02 | 225884221.57 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.38 | 0.0 | 391829990.5 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.71 | 4.86 | 3.76 | 0.03 | 429574.53 | 1.82 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 3.78 | 2.15 | 0.01 | 372881.88 | 13.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.84 | 3.64 | 0.27 | 0.01 | 228535.21 | 11.03 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 1.72 | 1.02 | 0.02 | 296512.86 | 7.28 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 4.06 | 0.94 | 0.02 | 9468.41 | 21.01 | skipped_fast |
| BIOUSDT | IDLE | 1.54 | 2.76 | 2.19 | 0.0 | 94821.94 | 7.24 | skipped_fast |
| RIZEUSDT | IDLE | 1.4 | 7.62 | 6.74 | 0.03 | 95175.73 | 65.04 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.1 | 1.54 | 0.02 | 441817.56 | 1.23 | skipped_fast |
| KITEUSDT | IDLE | 1.53 | 2.68 | 2.57 | -0.03 | 63931.84 | 10.19 | skipped_fast |
| WUSDT | IDLE | 1.12 | 2.13 | 0.75 | 0.02 | 174680.88 | 12.85 | skipped_fast |
| EDELUSDT | IDLE | 1.31 | 2.46 | 1.11 | 0.01 | 71477.12 | 18.64 | skipped_fast |
| REDUSDT | IDLE | 1.28 | 2.55 | 0.12 | 0.01 | 63672.43 | 11.7 | skipped_fast |
| QNTUSDT | IDLE | 1.72 | 3.09 | 2.28 | 0.03 | 39423.3 | 6.09 | skipped_fast |
| MNSRYUSDT | IDLE | 1.09 | 2.01 | 1.11 | 0.01 | 41583.18 | 24.21 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.15 | 0.99 | 0.01 | 52397.63 | 7.15 | skipped_fast |
| TELUSDT | IDLE | 0.71 | 1.29 | 0.93 | 0.0 | 72454.43 | 40.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.47 | 0.91 | 0.14 | 0.02 | 353.17 | 21.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
