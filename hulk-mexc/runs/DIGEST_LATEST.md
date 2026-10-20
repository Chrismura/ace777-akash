# Hulk DIGEST — 2026-10-20T19:23:32Z

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
| ETHUSDT | IDLE | 1.56 | 2.84 | 1.92 | 0.01 | 148641779.5 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.56 | 2.82 | 2.02 | 0.01 | 23787343.72 | 0.76 | skipped_fast |
| BTCUSDT | IDLE | 0.89 | 1.61 | 1.14 | 0.01 | 321421801.87 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.32 | 5.65 | 2.19 | 0.07 | 1090918.37 | 3.88 | skipped_fast |
| WUSDT | IDLE | 2.54 | 4.91 | 1.09 | 0.0 | 649192.34 | 14.94 | skipped_fast |
| QNTUSDT | IDLE | 2.93 | 5.15 | 4.68 | 0.0 | 736367.16 | 5.69 | skipped_fast |
| ZBCNUSDT | IDLE | 3.89 | 7.13 | 4.3 | 0.01 | 189572.28 | 15.61 | skipped_fast |
| EDELUSDT | IDLE | 1.56 | 14.65 | 3.37 | 0.3 | 350534.69 | 14.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 7.7 | 7.11 | 0.06 | 199551.46 | 6.82 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 2.55 | 1.95 | 0.01 | 390814.38 | 9.54 | skipped_fast |
| REDUSDT | IDLE | 2.41 | 4.44 | 2.56 | 0.02 | 59701.04 | 15.86 | skipped_fast |
| BIOUSDT | IDLE | 2.24 | 4.17 | 2.04 | 0.04 | 62996.83 | 8.19 | skipped_fast |
| HBARUSDT | IDLE | 2.08 | 3.68 | 3.17 | 0.01 | 388155.31 | 9.64 | skipped_fast |
| RWAINCUSDT | IDLE | 1.27 | 4.0 | 2.28 | -0.03 | 69659.76 | 5.31 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 2.28 | 1.99 | 0.01 | 82989.51 | 12.31 | skipped_fast |
| WAXLUSDT | IDLE | 2.71 | 4.75 | 4.53 | -0.05 | 55904.91 | 37.54 | skipped_fast |
| IOTAUSDT | IDLE | 2.34 | 4.12 | 3.95 | 0.04 | 73661.17 | 26.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.01 | 4.35 | 0.35 | 0.04 | 69765.92 | 55.35 | skipped_fast |
| LAUSDT | IDLE | 1.96 | 3.55 | 2.47 | 0.02 | 56102.39 | 22.58 | skipped_fast |
| FLUIDUSDT | IDLE | 2.13 | 4.1 | 1.02 | 0.05 | 6086.16 | 18.57 | skipped_fast |
| RWAUSDT | IDLE | 0.78 | 1.42 | 0.93 | 0.0 | 52576.84 | 7.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 1.02 | 0.38 | 0.0 | 40181.16 | 14.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
