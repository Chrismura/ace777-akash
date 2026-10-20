# Hulk DIGEST — 2026-10-20T05:58:39Z

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
| ETHUSDT | IDLE | 0.96 | 1.8 | 0.81 | -0.01 | 122527089.36 | 0.13 | skipped_fast |
| XRPUSDT | IDLE | 0.86 | 1.66 | 0.46 | -0.01 | 20176827.34 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.28 | 0.61 | -0.01 | 300350517.93 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.78 | 3.21 | 2.27 | -0.04 | 1074610.04 | 4.15 | skipped_fast |
| WUSDT | IDLE | 2.23 | 3.98 | 3.14 | -0.0 | 739478.37 | 15.51 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.8 | 15.18 | 0.0 | 0.11 | 233720.08 | 3.28 | skipped_fast |
| CCUSDT | IDLE | 2.26 | 4.01 | 3.34 | 0.02 | 475649.75 | 8.64 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 13.3 | 10.82 | -0.07 | 66937.85 | 53.87 | skipped_fast |
| QNTUSDT | IDLE | 2.22 | 3.97 | 3.07 | -0.02 | 726924.03 | 9.34 | skipped_fast |
| CHIPUSDT | IDLE | 3.29 | 7.85 | 1.19 | 0.03 | 90445.55 | 11.4 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 3.41 | 1.75 | 0.06 | 78490.46 | 10.59 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 3.03 | 1.09 | -0.01 | 67922.64 | 4.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.17 | 2.14 | 1.37 | -0.02 | 154810.65 | 17.74 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 2.62 | 1.01 | -0.01 | 369012.94 | 2.4 | skipped_fast |
| REDUSDT | IDLE | 1.5 | 2.93 | 0.53 | 0.01 | 58447.9 | 9.41 | skipped_fast |
| RWAINCUSDT | IDLE | 0.87 | 1.88 | 0.51 | 0.01 | 73760.33 | 5.16 | skipped_fast |
| FLUIDUSDT | IDLE | 2.26 | 4.4 | 0.8 | -0.01 | 7574.71 | 21.28 | skipped_fast |
| IOTAUSDT | IDLE | 1.92 | 3.71 | 0.82 | 0.02 | 89467.49 | 30.53 | skipped_fast |
| LAUSDT | IDLE | 1.75 | 3.32 | 1.2 | -0.02 | 54928.8 | 24.74 | skipped_fast |
| WAXLUSDT | IDLE | 1.56 | 3.59 | 1.94 | -0.05 | 56468.81 | 38.5 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.47 | 0.47 | 0.01 | 51833.03 | 23.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.27 | 0.06 | -0.0 | 40107.19 | 15.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
