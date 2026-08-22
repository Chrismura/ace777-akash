# Hulk DIGEST — 2026-08-22T08:54:22Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.71 | 0.03 | 34255879.53 | 7.94 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 23.87 | 9.92 | 0.1 | 223770261.67 | 2.61 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.05 | 0.01 | 1314205.42 | 1.28 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.09 | -0.1 | 680889.88 | 3.35 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.93 | 0.02 | 602197.93 | 14.64 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.41 | -0.04 | 254397.43 | 6.37 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.23 | 0.03 | 155206.86 | 11.51 | skipped_fast |
| CCUSDT | IDLE | 2.09 | 11.25 | 3.77 | 0.16 | 802343.54 | 8.29 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.33 | 8.47 | 7.18 | -0.02 | 497425.88 | 30.84 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.0 | 0.01 | 193108.93 | 4.65 | skipped_fast |
| KITEUSDT | IDLE | 3.77 | 9.68 | 3.28 | 0.06 | 73541.53 | 10.82 | skipped_fast |
| FLUIDUSDT | IDLE | 3.79 | 7.38 | 4.56 | 0.03 | 6885.76 | 21.42 | skipped_fast |
| EDELUSDT | IDLE | 2.32 | 4.52 | 4.11 | -0.05 | 86693.88 | 44.94 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 1.99 | 0.02 | 11077.79 | 5.33 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.6 | 6.52 | 6.12 | -0.03 | 174517.77 | 36.79 | skipped_fast |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.87 | 3.73 | 1.61 | 0.01 | 52228.54 | 44.83 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.2 | 0.04 | 58271.44 | 8.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
