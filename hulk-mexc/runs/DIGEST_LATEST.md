# Hulk DIGEST — 2026-08-21T21:44:03Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.47 | 0.1 | 5658254.06 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.59 | 0.1 | 129193486.45 | 3.56 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.49 | 0.05 | 522777.47 | 3.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.94 | 8.19 | 3.28 | 0.1 | 491215.49 | 26.51 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 3.75 | 0.15 | 0.1 | 651413.02 | 7.31 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.28 | 0.0 | 0.07 | 819286.12 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.92 | 3.83 | 0.12 | 0.07 | 368901.16 | 13.54 | skipped_fast |
| BIOUSDT | IDLE | 2.41 | 5.2 | 1.81 | 0.02 | 187720.23 | 3.13 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.23 | 0.17 | 154148.04 | 19.67 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 0.88 | 0.04 | 55844.0 | 36.78 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 4.12 | 0.99 | -0.04 | 83608.94 | 33.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.4 | 0.11 | 61122.56 | 13.81 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 119.76 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 4.81 | 1.41 | 0.02 | 183079.37 | 68.73 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.65 | 0.51 | 0.04 | 62623.65 | 6.18 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.41 | 0.03 | 53978.12 | 24.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
