# Hulk DIGEST — 2026-09-26T17:02:45Z

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
| XRPUSDT | IDLE | 0.6 | 1.12 | 0.55 | -0.01 | 42101145.87 | 1.94 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.82 | 19.89 | 0.31 | 0.24 | 1244642.94 | 9.75 | skipped_fast |
| ETHUSDT | IDLE | 0.27 | 0.52 | 0.16 | 0.0 | 127836287.84 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.07 | 0.0 | 340036057.22 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.54 | 4.19 | 1.52 | 0.08 | 993800.0 | 5.12 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 4.54 | 1.35 | 0.11 | 949605.89 | 6.48 | skipped_fast |
| CHIPUSDT | IDLE | 3.97 | 8.54 | 3.16 | 0.04 | 115461.87 | 13.85 | skipped_fast |
| WUSDT | IDLE | 1.94 | 4.83 | 0.45 | 0.09 | 452649.94 | 9.14 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.2 | 2.01 | 0.02 | 162553.29 | 3.26 | skipped_fast |
| KITEUSDT | IDLE | 2.66 | 6.16 | 0.09 | 0.1 | 79626.02 | 11.18 | skipped_fast |
| RWAINCUSDT | IDLE | 2.95 | 9.15 | 4.83 | -0.02 | 8024.31 | 98.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.49 | 2.74 | 1.66 | -0.02 | 220660.86 | 5.58 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.42 | 0.16 | 0.02 | 529769.92 | 2.1 | skipped_fast |
| BIOUSDT | IDLE | 1.26 | 2.48 | 0.3 | -0.01 | 105616.28 | 6.08 | skipped_fast |
| REDUSDT | IDLE | 0.66 | 1.27 | 0.37 | -0.03 | 57409.89 | 8.29 | skipped_fast |
| RWAUSDT | IDLE | 1.48 | 2.86 | 0.64 | 0.02 | 55705.45 | 7.17 | skipped_fast |
| RIZEUSDT | IDLE | 0.41 | 1.75 | 1.06 | -0.08 | 41339.6 | 51.96 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.22 | 0.25 | -0.02 | 127313.95 | 55.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.52 | 0.1 | 0.0 | 39857.14 | 7.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.49 | 0.28 | 0.01 | 750.49 | 21.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
