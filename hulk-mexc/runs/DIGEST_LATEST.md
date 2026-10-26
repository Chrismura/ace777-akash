# Hulk DIGEST — 2026-10-26T07:17:46Z

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
| XRPUSDT | IDLE | 0.94 | 1.77 | 0.76 | -0.01 | 16896621.07 | 0.78 | skipped_fast |
| ETHUSDT | IDLE | 0.83 | 1.59 | 0.4 | -0.01 | 105081579.13 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.14 | 0.22 | -0.01 | 205958793.45 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.42 | 2.92 | 2.73 | 0.03 | 788687.56 | 4.1 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.07 | 10.26 | 1.96 | 0.03 | 101939.9 | 17.32 | skipped_fast |
| WUSDT | IDLE | 1.42 | 2.51 | 2.21 | -0.04 | 467368.75 | 14.58 | skipped_fast |
| LAUSDT | IDLE | 4.28 | 8.72 | 4.05 | -0.04 | 61657.24 | 22.67 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 3.44 | 0.26 | 0.05 | 742714.2 | 4.12 | skipped_fast |
| RWAINCUSDT | IDLE | 2.38 | 4.28 | 4.05 | -0.07 | 66549.87 | 11.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 2.92 | 2.41 | 0.01 | 180183.57 | 26.21 | skipped_fast |
| REDUSDT | IDLE | 1.98 | 3.63 | 2.24 | -0.03 | 60526.46 | 9.02 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 3.01 | 1.88 | -0.0 | 53584.29 | 14.3 | skipped_fast |
| BIOUSDT | IDLE | 1.38 | 2.52 | 1.65 | -0.02 | 61024.93 | 9.09 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.58 | 1.21 | 0.0 | 161169.35 | 6.96 | skipped_fast |
| EDELUSDT | IDLE | 0.84 | 2.1 | 0.87 | 0.06 | 143348.85 | 31.46 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.57 | 0.97 | -0.01 | 180593.72 | 6.52 | skipped_fast |
| WAXLUSDT | IDLE | 1.69 | 2.98 | 2.7 | -0.01 | 52623.31 | 52.53 | skipped_fast |
| RIZEUSDT | IDLE | 0.52 | 1.0 | 0.3 | 0.0 | 33034.99 | 55.27 | skipped_fast |
| IOTAUSDT | IDLE | 1.12 | 2.01 | 1.55 | -0.03 | 62811.71 | 23.78 | skipped_fast |
| FLUIDUSDT | IDLE | 0.28 | 1.49 | 0.0 | -0.02 | 19116.06 | 21.43 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.01 | 52696.53 | 23.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.57 | 0.34 | -0.01 | 38229.95 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
