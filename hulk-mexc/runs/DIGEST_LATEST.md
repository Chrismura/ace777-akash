# Hulk DIGEST — 2026-10-25T17:05:43Z

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
| ETHUSDT | IDLE | 0.73 | 1.42 | 0.24 | 0.02 | 88662986.97 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.68 | 1.32 | 0.21 | 0.02 | 14909936.88 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.38 | 0.74 | 0.07 | 0.01 | 145322274.12 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.84 | 3.61 | 0.42 | -0.01 | 631620.77 | 23.05 | skipped_fast |
| ZBCNUSDT | IDLE | 3.7 | 7.49 | 0.32 | 0.08 | 206662.49 | 38.46 | skipped_fast |
| PYTHUSDT | IDLE | 1.6 | 3.08 | 0.78 | 0.05 | 412027.53 | 2.77 | skipped_fast |
| EDELUSDT | IDLE | 1.73 | 3.31 | 1.02 | -0.0 | 408135.16 | 33.46 | skipped_fast |
| KITEUSDT | IDLE | 2.75 | 5.12 | 2.59 | 0.0 | 54122.1 | 11.51 | skipped_fast |
| CHIPUSDT | IDLE | 2.19 | 4.83 | 2.77 | 0.04 | 93346.96 | 17.97 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 3.7 | 0.28 | 0.06 | 452697.94 | 1.59 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 2.91 | 0.35 | 0.03 | 178630.75 | 6.8 | skipped_fast |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.56 | 13.42 | 0.0 | 0.03 | 18769.6 | 21.34 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.86 | 0.04 | -0.02 | 66250.3 | 15.16 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 2.12 | 0.4 | 0.0 | 60378.95 | 8.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 1.72 | 1.2 | -0.01 | 58705.03 | 5.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.27 | 2.61 | 1.26 | -0.01 | 45150.63 | 64.89 | skipped_fast |
| WAXLUSDT | IDLE | 1.87 | 3.71 | 0.22 | 0.03 | 53621.41 | 48.09 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.92 | 0.12 | 0.02 | 137490.79 | 6.42 | skipped_fast |
| LAUSDT | IDLE | 0.93 | 4.01 | 0.05 | -0.09 | 70085.69 | 24.0 | skipped_fast |
| IOTAUSDT | IDLE | 1.01 | 1.97 | 0.3 | 0.0 | 61727.96 | 25.43 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.36 | 0.48 | 0.01 | 50977.06 | 15.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.17 | 0.0 | 36654.55 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
