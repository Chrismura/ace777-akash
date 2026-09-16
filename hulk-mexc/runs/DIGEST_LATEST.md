# Hulk DIGEST — 2026-09-16T17:14:13Z

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
| XRPUSDT | IDLE | 1.08 | 2.79 | 2.31 | -0.08 | 80192303.75 | 2.37 | skipped_fast |
| ETHUSDT | IDLE | 1.02 | 1.83 | 1.37 | -0.01 | 406449089.04 | 0.5 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.13 | 0.77 | -0.01 | 533514962.53 | 0.15 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.0 | 6.58 | 0.01 | 66709.49 | 23.94 | skipped_fast |
| PYTHUSDT | IDLE | 1.79 | 3.21 | 2.51 | -0.05 | 666726.62 | 1.92 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 36.05 | 20.12 | 0.33 | 60196.35 | 98.52 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 6.75 | 5.17 | -0.03 | 93984.73 | 19.36 | skipped_fast |
| CCUSDT | IDLE | 1.85 | 3.55 | 1.0 | -0.02 | 471346.14 | 9.89 | skipped_fast |
| EDELUSDT | IDLE | 1.06 | 10.01 | 8.04 | 0.24 | 398382.74 | 46.08 | skipped_fast |
| REDUSDT | IDLE | 2.46 | 4.32 | 3.96 | -0.05 | 67006.95 | 19.0 | skipped_fast |
| BIOUSDT | IDLE | 1.67 | 2.97 | 2.52 | -0.03 | 81302.4 | 4.1 | skipped_fast |
| HBARUSDT | IDLE | 1.74 | 3.45 | 1.92 | -0.06 | 351493.66 | 1.37 | skipped_fast |
| ZBCNUSDT | IDLE | 0.91 | 2.44 | 0.89 | -0.03 | 219529.93 | 6.99 | skipped_fast |
| WUSDT | IDLE | 1.09 | 2.22 | 1.82 | -0.07 | 186513.87 | 13.67 | skipped_fast |
| TELUSDT | IDLE | 1.71 | 4.81 | 3.29 | -0.08 | 121074.41 | 35.42 | skipped_fast |
| RWAINCUSDT | IDLE | 1.06 | 1.84 | 1.81 | -0.03 | 12583.39 | 59.28 | skipped_fast |
| FLUIDUSDT | IDLE | 1.65 | 3.0 | 1.97 | -0.06 | 2518.27 | 22.54 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.11 | 0.98 | -0.05 | 39457.78 | 3.36 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.61 | 0.08 | -0.0 | 52938.76 | 7.53 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.6 | 0.42 | -0.02 | 32841.05 | 29.77 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
