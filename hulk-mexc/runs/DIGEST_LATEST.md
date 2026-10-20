# Hulk DIGEST — 2026-10-20T01:07:32Z

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
| XRPUSDT | IDLE | 0.71 | 1.25 | 1.2 | -0.01 | 20206687.07 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.06 | 0.9 | -0.01 | 122909287.34 | 0.5 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.01 | 0.8 | -0.01 | 314926325.91 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.64 | 4.62 | 4.36 | -0.01 | 706246.34 | 17.03 | skipped_fast |
| PYTHUSDT | IDLE | 2.0 | 3.51 | 3.21 | -0.04 | 832750.45 | 2.78 | skipped_fast |
| QNTUSDT | IDLE | 1.29 | 2.25 | 2.2 | 0.01 | 693954.02 | 2.59 | skipped_fast |
| CCUSDT | IDLE | 1.19 | 2.26 | 0.84 | 0.02 | 380595.14 | 5.73 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 3.61 | 1.21 | 0.01 | 187020.15 | 11.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 2.93 | 2.02 | 0.0 | 76598.34 | 14.4 | skipped_fast |
| KITEUSDT | IDLE | 1.56 | 3.0 | 2.19 | 0.05 | 76832.07 | 10.7 | skipped_fast |
| ZBCNUSDT | IDLE | 0.96 | 2.56 | 1.1 | 0.0 | 208014.91 | 15.8 | skipped_fast |
| REDUSDT | IDLE | 1.48 | 2.63 | 2.22 | -0.02 | 57915.67 | 16.93 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.79 | 0.7 | -0.02 | 435792.81 | 7.26 | skipped_fast |
| RWAINCUSDT | IDLE | 1.03 | 2.03 | 1.99 | 0.02 | 68031.5 | 10.38 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.63 | 1.52 | -0.01 | 69276.2 | 8.56 | skipped_fast |
| WAXLUSDT | IDLE | 2.1 | 4.44 | 4.25 | -0.07 | 62903.29 | 46.4 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 2.25 | 0.71 | -0.05 | 52580.34 | 41.49 | skipped_fast |
| LAUSDT | IDLE | 1.22 | 2.18 | 1.7 | -0.02 | 55790.39 | 44.24 | skipped_fast |
| IOTAUSDT | IDLE | 0.93 | 1.75 | 0.75 | -0.0 | 90267.87 | 31.08 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.71 | 0.31 | 0.01 | 53935.55 | 23.5 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.09 | 0.01 | 41616.59 | 8.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 4709.59 | 21.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
