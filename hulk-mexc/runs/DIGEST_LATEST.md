# Hulk DIGEST — 2026-09-19T00:55:45Z

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
| XRPUSDT | IDLE | 1.11 | 2.47 | 0.71 | 0.09 | 67399042.6 | 2.84 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.46 | 0.89 | 0.07 | 649002289.7 | 0.5 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.82 | 0.13 | 0.06 | 781597199.65 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 18.7 | 10.46 | -0.02 | 194436.16 | 44.9 | skipped_fast |
| WUSDT | IDLE | 0.94 | 3.32 | 1.25 | 0.1 | 923965.04 | 6.36 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 18.02 | 15.14 | 0.07 | 71966.89 | 4.17 | skipped_fast |
| PYTHUSDT | IDLE | 1.13 | 2.01 | 1.72 | 0.05 | 764970.69 | 3.34 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 2.98 | 0.48 | 0.09 | 676569.69 | 8.93 | skipped_fast |
| CHIPUSDT | IDLE | 1.73 | 8.08 | 4.56 | 0.14 | 159536.79 | 15.68 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.72 | 0.83 | 0.06 | 683577.65 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 2.33 | 1.18 | 0.04 | 231232.69 | 17.03 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 2.54 | 0.7 | 0.06 | 78572.23 | 9.82 | skipped_fast |
| TELUSDT | IDLE | 2.29 | 11.46 | 5.52 | 0.14 | 126420.57 | 80.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.27 | 2.46 | 0.57 | 0.03 | 7197.36 | 5.75 | skipped_fast |
| BIOUSDT | IDLE | 0.8 | 1.77 | 0.65 | 0.08 | 87473.38 | 10.95 | skipped_fast |
| FLUIDUSDT | IDLE | 1.03 | 4.42 | 1.08 | 0.17 | 3545.79 | 21.74 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.33 | 0.72 | 0.04 | 74084.69 | 4.72 | skipped_fast |
| RIZEUSDT | IDLE | 0.13 | 2.27 | 0.04 | -0.08 | 56531.11 | 98.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.72 | 1.41 | 0.16 | 0.07 | 43036.4 | 2.62 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.74 | 0.29 | 0.01 | 58206.37 | 22.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
