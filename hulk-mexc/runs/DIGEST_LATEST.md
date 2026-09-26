# Hulk DIGEST — 2026-09-26T09:58:10Z

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
| XRPUSDT | IDLE | 0.95 | 1.69 | 1.34 | -0.01 | 107832333.36 | 1.95 | skipped_fast |
| ETHUSDT | IDLE | 0.37 | 0.66 | 0.56 | -0.01 | 261384151.48 | 0.52 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.54 | 0.39 | -0.01 | 565562191.31 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.22 | 4.76 | 1.46 | 0.07 | 1205710.61 | 1.33 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 7.25 | 3.04 | 0.15 | 1046935.25 | 5.18 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.29 | 9.16 | 0.48 | 0.11 | 752599.12 | 7.47 | skipped_fast |
| WUSDT | IDLE | 2.26 | 4.98 | 1.74 | 0.06 | 480867.45 | 7.96 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.46 | 1.01 | 0.01 | 805431.25 | 1.07 | skipped_fast |
| KITEUSDT | IDLE | 2.04 | 4.32 | 3.81 | 0.03 | 75025.66 | 9.66 | skipped_fast |
| EDELUSDT | IDLE | 1.55 | 3.07 | 0.17 | 0.02 | 175660.94 | 6.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.69 | 1.38 | 0.03 | 250325.31 | 30.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 2.89 | 2.16 | -0.01 | 145377.83 | 14.46 | skipped_fast |
| RWAINCUSDT | IDLE | 2.38 | 4.42 | 2.29 | -0.01 | 7657.58 | 79.37 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 1.78 | 1.46 | 0.01 | 59785.52 | 8.25 | skipped_fast |
| BIOUSDT | IDLE | 0.53 | 1.3 | 0.49 | 0.04 | 120651.24 | 3.07 | skipped_fast |
| RIZEUSDT | IDLE | 0.36 | 3.21 | 1.34 | -0.22 | 51681.69 | 40.94 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 1.93 | 1.83 | -0.03 | 123658.61 | 18.63 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.34 | 0.66 | -0.01 | 53056.62 | 7.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.82 | 0.0 | 0.01 | 3396.54 | 22.2 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.63 | 0.13 | 0.01 | 40402.13 | 8.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
