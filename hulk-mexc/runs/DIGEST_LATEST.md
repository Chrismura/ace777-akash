# Hulk DIGEST — 2026-10-29T11:22:37Z

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
| XRPUSDT | IDLE | 0.57 | 1.03 | 0.7 | -0.03 | 23738554.33 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 1.08 | 0.23 | -0.02 | 236145626.48 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.65 | 0.14 | -0.01 | 345388954.12 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.5 | 2.87 | 0.85 | -0.03 | 491762.38 | 16.12 | skipped_fast |
| PYTHUSDT | IDLE | 1.43 | 2.65 | 1.35 | -0.03 | 451811.01 | 4.27 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.86 | 0.09 | -0.03 | 402241.17 | 9.14 | skipped_fast |
| EDELUSDT | IDLE | 1.58 | 2.86 | 2.02 | -0.05 | 212290.12 | 3.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.14 | 3.78 | 0.02 | -0.13 | 203036.09 | 12.35 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 2.59 | 1.18 | -0.03 | 433686.94 | 4.14 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.35 | 0.67 | -0.03 | 560838.91 | 4.07 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 2.9 | 0.18 | -0.02 | 66834.56 | 8.96 | skipped_fast |
| LAUSDT | IDLE | 2.92 | 5.29 | 3.66 | -0.03 | 57550.79 | 36.78 | skipped_fast |
| ZBCNUSDT | IDLE | 0.49 | 0.97 | 0.08 | -0.01 | 253780.15 | 5.83 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 4.82 | 1.67 | -0.09 | 32132.22 | 14.17 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.11 | 1.11 | -0.04 | 64301.98 | 14.93 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 2.15 | 0.24 | -0.02 | 59991.29 | 9.68 | skipped_fast |
| FLUIDUSDT | IDLE | 2.26 | 4.39 | 2.55 | -0.06 | 6332.23 | 21.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.81 | 1.52 | 0.7 | -0.03 | 39757.51 | 51.66 | skipped_fast |
| IOTAUSDT | IDLE | 1.03 | 2.04 | 0.49 | -0.04 | 95769.6 | 14.86 | skipped_fast |
| WAXLUSDT | IDLE | 1.51 | 3.75 | 0.6 | -0.05 | 54215.93 | 58.08 | skipped_fast |
| RWAUSDT | IDLE | 1.14 | 2.01 | 1.74 | -0.01 | 56250.59 | 24.13 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.71 | 0.04 | -0.01 | 36832.75 | 14.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
