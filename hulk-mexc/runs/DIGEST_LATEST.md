# Hulk DIGEST — 2026-10-11T12:16:04Z

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
| XRPUSDT | IDLE | 0.34 | 0.66 | 0.1 | -0.0 | 10116083.63 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.23 | 0.46 | 0.05 | 0.0 | 179138487.82 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.17 | 0.34 | 0.06 | 0.0 | 122396390.49 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.24 | 3.27 | 2.01 | -0.01 | 1160895.47 | 6.31 | skipped_fast |
| QNTUSDT | IDLE | 1.88 | 3.75 | 0.84 | -0.02 | 1096620.75 | 3.71 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 31.62 | 15.97 | 0.06 | 55912.37 | 17.05 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 2.76 | 1.9 | -0.02 | 719794.31 | 5.21 | skipped_fast |
| EDELUSDT | IDLE | 1.82 | 3.27 | 2.42 | -0.01 | 374142.94 | 12.88 | skipped_fast |
| RIZEUSDT | IDLE | 3.32 | 9.17 | 4.59 | -0.07 | 35807.03 | 59.4 | skipped_fast |
| CHIPUSDT | IDLE | 0.89 | 8.41 | 2.67 | 0.28 | 368176.92 | 10.48 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 3.09 | 1.07 | 0.01 | 255515.86 | 9.92 | skipped_fast |
| TELUSDT | IDLE | 3.24 | 5.97 | 4.96 | -0.07 | 144869.17 | 35.27 | skipped_fast |
| BIOUSDT | IDLE | 1.61 | 2.99 | 1.57 | 0.03 | 74947.41 | 3.39 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 2.2 | 1.51 | -0.02 | 58109.15 | 9.42 | skipped_fast |
| ZBCNUSDT | IDLE | 0.83 | 1.61 | 0.31 | -0.0 | 155750.89 | 22.4 | skipped_fast |
| KITEUSDT | IDLE | 0.68 | 1.24 | 0.76 | -0.0 | 73964.7 | 11.92 | skipped_fast |
| RWAINCUSDT | IDLE | 0.75 | 1.36 | 0.95 | -0.03 | 19572.87 | 5.03 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.74 | 0.64 | -0.01 | 251469.83 | 4.36 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.63 | 0.39 | -0.01 | 52800.6 | 7.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.34 | 0.11 | -0.01 | 31968.51 | 15.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
