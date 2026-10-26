# Hulk DIGEST — 2026-10-26T00:11:26Z

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
| ETHUSDT | IDLE | 1.03 | 1.92 | 0.87 | -0.01 | 87483228.31 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.68 | 1.32 | 0.21 | -0.0 | 14388085.26 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.09 | 0.67 | -0.01 | 154662349.68 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.97 | 3.7 | 1.58 | -0.03 | 606668.05 | 17.59 | skipped_fast |
| PYTHUSDT | IDLE | 1.41 | 3.14 | 1.09 | 0.05 | 662033.27 | 3.99 | skipped_fast |
| QNTUSDT | IDLE | 1.4 | 3.89 | 2.6 | 0.07 | 661523.41 | 2.09 | skipped_fast |
| RIZEUSDT | IDLE | 3.29 | 6.05 | 3.57 | -0.0 | 33211.95 | 60.07 | skipped_fast |
| CHIPUSDT | IDLE | 2.32 | 4.26 | 2.57 | -0.04 | 87829.5 | 18.03 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.01 | 2.97 | -0.04 | 62085.42 | 11.35 | skipped_fast |
| EDELUSDT | IDLE | 1.18 | 2.95 | 1.24 | 0.05 | 301383.93 | 25.22 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 2.49 | 1.23 | 0.0 | 192977.07 | 0.99 | skipped_fast |
| ZBCNUSDT | IDLE | 1.56 | 2.86 | 2.05 | 0.03 | 188563.36 | 28.68 | skipped_fast |
| REDUSDT | IDLE | 1.24 | 2.25 | 1.52 | -0.04 | 59595.46 | 16.62 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 2.18 | 0.53 | -0.03 | 59750.14 | 8.94 | skipped_fast |
| KITEUSDT | IDLE | 0.87 | 1.74 | 0.0 | -0.02 | 53259.43 | 14.05 | skipped_fast |
| LAUSDT | IDLE | 1.67 | 3.74 | 2.4 | -0.12 | 67402.22 | 26.29 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.73 | 0.46 | -0.0 | 155753.29 | 6.43 | skipped_fast |
| IOTAUSDT | IDLE | 1.09 | 2.12 | 0.42 | -0.02 | 60391.94 | 25.51 | skipped_fast |
| WAXLUSDT | IDLE | 1.08 | 2.04 | 0.83 | -0.03 | 53628.61 | 44.93 | skipped_fast |
| FLUIDUSDT | IDLE | 0.86 | 3.96 | 3.81 | -0.02 | 18990.61 | 46.11 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.56 | 0.16 | -0.0 | 51958.5 | 7.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.59 | 0.18 | -0.01 | 38460.14 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
