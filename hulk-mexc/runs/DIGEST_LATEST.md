# Hulk DIGEST — 2026-10-10T18:01:01Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 10.11 | 6.81 | 0.01 | 1226717.34 | 6.23 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.84 | 0.34 | 0.01 | 88802593.69 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.39 | 0.7 | 0.57 | 0.01 | 14929760.49 | 1.42 | skipped_fast |
| QNTUSDT | IDLE | 3.66 | 6.57 | 4.95 | -0.01 | 1209260.57 | 3.3 | skipped_fast |
| BTCUSDT | IDLE | 0.23 | 0.46 | 0.06 | 0.0 | 180122263.31 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.2 | 2.34 | 0.45 | -0.03 | 867935.23 | 1.26 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.11 | 15.68 | 1.27 | 0.18 | 120106.07 | 15.32 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.5 | 2.44 | -0.03 | 383733.73 | 9.31 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.92 | 1.46 | -0.04 | 220084.02 | 12.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.03 | 1.96 | 0.73 | 0.01 | 199271.84 | 7.84 | skipped_fast |
| RWAINCUSDT | IDLE | 2.23 | 4.24 | 1.45 | -0.03 | 9708.33 | 83.23 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 3.16 | 1.39 | 0.08 | 72551.83 | 8.46 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 2.13 | 0.89 | 0.03 | 88056.16 | 6.9 | skipped_fast |
| TELUSDT | IDLE | 2.23 | 4.03 | 2.84 | -0.04 | 125480.36 | 28.05 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.45 | 1.31 | 0.02 | 354073.79 | 3.25 | skipped_fast |
| REDUSDT | IDLE | 0.67 | 1.21 | 0.86 | 0.02 | 54336.25 | 7.31 | skipped_fast |
| RIZEUSDT | IDLE | 0.52 | 1.16 | 0.99 | -0.01 | 43595.06 | 39.85 | skipped_fast |
| FLUIDUSDT | IDLE | 0.66 | 1.94 | 1.28 | -0.01 | 15301.86 | 21.01 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.71 | 0.63 | -0.0 | 54002.44 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.11 | 0.0 | 38827.81 | 13.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
