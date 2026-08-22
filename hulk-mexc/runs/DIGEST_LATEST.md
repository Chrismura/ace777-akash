# Hulk DIGEST — 2026-08-22T08:55:14Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.99 | 0.03 | 34544900.5 | 3.98 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 23.87 | 9.95 | 0.1 | 223557802.27 | 1.96 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 15.8 | 10.0 | 0.02 | 1313882.72 | 6.4 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.15 | -0.1 | 680781.23 | 6.7 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.82 | 0.02 | 602459.82 | 11.5 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.27 | -0.04 | 254468.68 | 3.18 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.28 | 0.04 | 155128.71 | 13.27 | skipped_fast |
| CCUSDT | IDLE | 2.09 | 11.25 | 3.68 | 0.15 | 799933.21 | 7.46 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.33 | 8.47 | 7.17 | -0.02 | 497415.44 | 25.29 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.04 | 0.01 | 193128.35 | 6.2 | skipped_fast |
| KITEUSDT | IDLE | 3.75 | 9.68 | 2.97 | 0.06 | 73563.82 | 10.78 | skipped_fast |
| FLUIDUSDT | IDLE | 3.79 | 7.38 | 4.56 | 0.03 | 6885.76 | 20.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 1.99 | 0.02 | 11077.79 | 5.33 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 4.52 | 3.46 | -0.04 | 86668.92 | 44.84 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.6 | 6.52 | 6.07 | -0.03 | 174018.4 | 36.79 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.87 | 3.73 | 1.59 | 0.01 | 52231.91 | 44.83 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.2 | 0.04 | 58225.28 | 24.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
