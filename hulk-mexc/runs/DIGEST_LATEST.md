# Hulk DIGEST — 2026-08-22T08:59:18Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.87 | 0.02 | 35117530.23 | 3.97 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 23.87 | 9.91 | 0.1 | 223441596.24 | 1.96 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.1 | 0.01 | 1313626.4 | 6.4 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.09 | -0.11 | 678741.2 | 10.06 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.85 | 0.02 | 601652.18 | 14.62 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.47 | -0.05 | 254257.9 | 3.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 12.04 | 0.04 | 155215.19 | 19.42 | skipped_fast |
| CCUSDT | IDLE | 2.09 | 11.25 | 3.83 | 0.15 | 798566.77 | 7.47 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 8.47 | 7.14 | -0.02 | 497414.19 | 15.16 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.87 | 0.01 | 193102.77 | 3.1 | skipped_fast |
| KITEUSDT | IDLE | 3.76 | 9.68 | 3.19 | 0.06 | 73503.09 | 13.56 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 7.38 | 5.12 | 0.02 | 7020.8 | 17.72 | skipped_fast |
| EDELUSDT | IDLE | 2.29 | 4.52 | 3.57 | -0.05 | 86487.42 | 33.61 | skipped_fast |
| RWAINCUSDT | IDLE | 2.38 | 4.48 | 1.88 | 0.02 | 11627.69 | 15.99 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.59 | 6.52 | 5.87 | -0.04 | 173688.82 | 52.52 | skipped_fast |
| RIZEUSDT | IDLE | 0.9 | 3.73 | 2.42 | -0.01 | 51700.28 | 46.77 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.27 | 0.04 | 57910.67 | 16.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
