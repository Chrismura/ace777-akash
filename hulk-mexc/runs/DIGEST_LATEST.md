# Hulk DIGEST — 2026-08-22T11:02:33Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.89 | -0.0 | 51655653.87 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.57 | 0.07 | 218182610.4 | 7.4 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 10.24 | 7.5 | 0.12 | 817494.25 | 6.93 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.66 | 0.0 | 1247732.28 | 5.19 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.87 | 0.01 | 595472.5 | 4.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.99 | 5.08 | 4.13 | -0.03 | 424219.74 | 16.97 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.31 | -0.11 | 649478.69 | 3.38 | skipped_fast |
| EDELUSDT | IDLE | 2.74 | 4.93 | 3.71 | -0.04 | 78940.55 | 45.35 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.84 | -0.06 | 240790.25 | 3.27 | skipped_fast |
| KITEUSDT | IDLE | 1.92 | 4.3 | 2.25 | 0.03 | 73351.99 | 10.07 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.64 | 6.75 | 5.41 | -0.04 | 169088.84 | 53.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.76 | 0.04 | 153981.03 | 14.3 | skipped_fast |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.01 | 2418.23 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | 0.0 | 11326.93 | 59.83 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 3.47 | 2.27 | -0.01 | 189159.38 | 6.27 | skipped_fast |
| RIZEUSDT | IDLE | 0.68 | 2.89 | 1.33 | -0.0 | 49225.08 | 46.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.38 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.8 | 1.69 | 0.01 | 57413.38 | 24.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
