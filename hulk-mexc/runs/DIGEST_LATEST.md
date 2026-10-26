# Hulk DIGEST — 2026-10-26T12:20:17Z

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
| XRPUSDT | IDLE | 0.93 | 1.84 | 0.13 | -0.0 | 20169557.98 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.45 | 0.33 | -0.0 | 110884088.06 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.11 | 0.32 | -0.0 | 239567052.76 | 0.0 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.79 | 15.06 | 1.57 | 0.2 | 1302390.34 | 7.79 | skipped_fast |
| PYTHUSDT | IDLE | 2.66 | 5.19 | 1.09 | 0.07 | 852710.94 | 3.97 | skipped_fast |
| WUSDT | IDLE | 1.54 | 3.06 | 0.13 | 0.01 | 481356.29 | 16.72 | skipped_fast |
| ZBCNUSDT | IDLE | 2.17 | 5.03 | 3.73 | -0.02 | 226453.31 | 45.86 | skipped_fast |
| CHIPUSDT | IDLE | 2.2 | 6.74 | 0.0 | 0.06 | 106117.73 | 20.95 | skipped_fast |
| REDUSDT | IDLE | 2.31 | 4.57 | 0.29 | 0.04 | 61584.8 | 20.86 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 1.77 | 1.35 | 0.0 | 177888.75 | 3.97 | skipped_fast |
| EDELUSDT | IDLE | 1.0 | 2.34 | 1.27 | 0.08 | 134136.75 | 24.94 | skipped_fast |
| BIOUSDT | IDLE | 1.1 | 2.15 | 0.36 | -0.0 | 59468.59 | 4.49 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.83 | 0.0 | -0.05 | 68825.34 | 5.77 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.92 | 0.27 | 0.01 | 53570.42 | 9.75 | skipped_fast |
| LAUSDT | IDLE | 2.1 | 4.34 | 1.55 | 0.04 | 65093.03 | 24.0 | skipped_fast |
| MNSRYUSDT | IDLE | 2.38 | 4.38 | 2.5 | -0.01 | 41455.02 | 76.46 | skipped_fast |
| RIZEUSDT | IDLE | 0.82 | 1.62 | 0.16 | 0.02 | 33120.56 | 63.84 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.78 | 0.13 | 0.01 | 175413.56 | 9.02 | skipped_fast |
| IOTAUSDT | IDLE | 1.14 | 2.25 | 0.26 | -0.0 | 64842.93 | 32.82 | skipped_fast |
| WAXLUSDT | IDLE | 1.3 | 2.56 | 0.25 | -0.02 | 52625.55 | 50.11 | skipped_fast |
| RWAUSDT | IDLE | 0.17 | 0.32 | 0.16 | -0.0 | 53365.69 | 7.96 | skipped_fast |
| FLUIDUSDT | IDLE | 0.25 | 1.05 | 0.0 | -0.02 | 8967.46 | 21.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
