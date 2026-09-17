# Hulk DIGEST — 2026-09-17T00:15:15Z

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
| XRPUSDT | IDLE | 1.83 | 3.44 | 1.45 | 0.01 | 57895674.22 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 1.0 | 1.98 | 0.16 | 0.01 | 369301217.91 | 0.33 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.58 | 0.17 | 0.01 | 506509330.79 | 0.0 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.69 | 10.49 | 0.65 | 0.13 | 516299.51 | 5.87 | skipped_fast |
| RWAINCUSDT | IDLE | 4.18 | 7.81 | 3.71 | -0.03 | 20636.35 | 29.25 | skipped_fast |
| WUSDT | IDLE | 2.8 | 5.55 | 0.27 | 0.0 | 207643.3 | 10.86 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.09 | 0.41 | -0.01 | 412393.07 | 3.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 5.13 | 1.55 | -0.02 | 80595.11 | 13.76 | skipped_fast |
| KITEUSDT | IDLE | 2.02 | 7.47 | 0.67 | 0.07 | 67964.95 | 14.89 | skipped_fast |
| BIOUSDT | IDLE | 1.94 | 3.79 | 0.56 | 0.0 | 79247.67 | 15.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.16 | 2.17 | 1.0 | 0.02 | 181091.65 | 18.43 | skipped_fast |
| REDUSDT | IDLE | 1.56 | 3.24 | 0.86 | -0.02 | 65134.97 | 10.06 | skipped_fast |
| EDELUSDT | IDLE | 0.52 | 3.15 | 1.79 | 0.13 | 297160.18 | 41.61 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 2.15 | 0.57 | -0.01 | 283819.93 | 1.36 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 9.65 | 6.35 | 0.24 | 60669.07 | 112.46 | skipped_fast |
| RWAUSDT | IDLE | 1.95 | 3.87 | 0.15 | 0.01 | 55202.92 | 37.36 | skipped_fast |
| QNTUSDT | IDLE | 1.52 | 2.99 | 0.28 | -0.0 | 37154.66 | 3.27 | skipped_fast |
| TELUSDT | IDLE | 1.26 | 2.38 | 0.96 | -0.03 | 114822.84 | 48.26 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 1.07 | 0.0 | -0.02 | 1573.23 | 43.1 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.93 | 0.24 | -0.01 | 31702.35 | 67.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
