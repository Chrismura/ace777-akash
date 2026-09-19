# Hulk DIGEST — 2026-09-19T15:59:00Z

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
| XRPUSDT | IDLE | 1.59 | 2.96 | 1.52 | 0.03 | 61419010.99 | 1.4 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.9 | 0.41 | 0.02 | 407249913.38 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.91 | 0.37 | 0.01 | 524444676.49 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.65 | 4.86 | 2.96 | 0.04 | 1013553.51 | 6.32 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.47 | 9.89 | 7.7 | -0.04 | 5224.69 | 61.27 | skipped_fast |
| PYTHUSDT | IDLE | 1.13 | 2.14 | 0.79 | 0.01 | 682621.68 | 6.6 | skipped_fast |
| BIOUSDT | IDLE | 3.1 | 5.92 | 1.91 | 0.04 | 84268.95 | 14.14 | skipped_fast |
| CHIPUSDT | IDLE | 2.35 | 5.58 | 5.15 | -0.01 | 138536.73 | 16.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.36 | 4.71 | 0.07 | 0.05 | 209279.66 | 28.93 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 2.82 | 0.76 | 0.03 | 499521.22 | 1.23 | skipped_fast |
| CCUSDT | IDLE | 0.74 | 1.48 | 0.05 | 0.02 | 350949.22 | 8.95 | skipped_fast |
| EDELUSDT | IDLE | 1.13 | 6.78 | 2.04 | -0.12 | 178084.73 | 42.42 | skipped_fast |
| RIZEUSDT | IDLE | 1.4 | 6.46 | 4.52 | 0.06 | 37453.61 | 33.77 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.57 | 1.79 | 0.04 | 71175.74 | 11.25 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 2.17 | 2.08 | 0.02 | 133429.52 | 14.92 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 4.52 | 1.78 | 0.0 | 127075.68 | 45.38 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.6 | 0.83 | 0.02 | 46198.3 | 4.58 | skipped_fast |
| FLUIDUSDT | IDLE | 1.1 | 3.38 | 0.0 | 0.07 | 10662.63 | 21.35 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.55 | 0.58 | 0.0 | 54592.65 | 7.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.85 | 1.52 | 1.17 | 0.01 | 36685.96 | 62.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
