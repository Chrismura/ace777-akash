# Hulk DIGEST — 2026-10-16T06:23:47Z

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
| WUSDT | IDLE | 2.54 | 6.45 | 3.18 | -0.01 | 2293686.92 | 9.98 | skipped_fast |
| PYTHUSDT | IDLE | 0.56 | 3.5 | 0.24 | 0.11 | 4036670.31 | 3.15 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.35 | 0.51 | 0.04 | 226381812.37 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.73 | 1.41 | 0.3 | 0.03 | 31755330.4 | 2.24 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.01 | 0.52 | 0.02 | 416786431.48 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 3.9 | 0.94 | 0.08 | 1178110.91 | 1.44 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 3.07 | 1.09 | -0.01 | 407836.2 | 10.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 8.26 | 3.93 | 0.12 | 188345.04 | 10.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 3.13 | 0.86 | 0.06 | 184643.05 | 13.35 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 3.44 | 2.54 | 0.02 | 68772.12 | 9.04 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 4.76 | 3.79 | -0.07 | 92566.8 | 7.43 | skipped_fast |
| EDELUSDT | IDLE | 0.79 | 2.07 | 1.49 | -0.08 | 208915.79 | 13.72 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 2.36 | 0.77 | 0.05 | 66994.61 | 3.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.75 | 0.5 | 0.02 | 27916.24 | 14.96 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 1.73 | 0.87 | 0.01 | 65074.39 | 40.78 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.26 | 0.57 | 0.06 | 154715.7 | 5.83 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 2.94 | 2.14 | 0.04 | 91502.43 | 22.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.71 | 0.38 | 0.01 | 7873.68 | 21.47 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.88 | 0.47 | 0.01 | 52668.77 | 39.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.38 | 0.32 | 0.01 | 39244.31 | 9.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
