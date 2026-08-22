# Hulk DIGEST — 2026-08-22T08:09:17Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.08 | 0.0 | 25798545.54 | 3.94 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 23.87 | 9.4 | 0.16 | 224992031.01 | 1.3 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 15.8 | 9.85 | 0.03 | 1355564.23 | 6.39 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.03 | -0.09 | 682126.51 | 3.34 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.26 | 0.04 | 609424.31 | 14.54 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.47 | -0.04 | 247455.68 | 3.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.45 | 0.06 | 155747.57 | 11.41 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 11.25 | 2.38 | 0.2 | 815724.37 | 9.82 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 8.47 | 6.43 | 0.03 | 537173.23 | 23.08 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.7 | 0.03 | 194168.21 | 12.33 | skipped_fast |
| KITEUSDT | IDLE | 3.83 | 9.68 | 4.41 | 0.06 | 72926.75 | 10.03 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 44.49 | skipped_fast |
| EDELUSDT | IDLE | 2.21 | 4.52 | 2.49 | -0.04 | 87024.88 | 100.28 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11250.14 | 112.75 | skipped_fast |
| TELUSDT | IDLE | 1.86 | 4.7 | 4.15 | -0.01 | 173933.95 | 56.63 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.81 | 0.0 | 52276.16 | 44.42 | skipped_fast |
| RWAUSDT | IDLE | 1.72 | 3.29 | 0.96 | 0.05 | 58316.96 | 8.05 | skipped_fast |
| QAITUSDT | IDLE | 0.99 | 1.92 | 0.35 | 0.01 | 3170.95 | 67.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
