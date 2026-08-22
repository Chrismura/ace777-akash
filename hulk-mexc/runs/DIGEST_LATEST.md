# Hulk DIGEST — 2026-08-22T07:44:42Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.97 | 0.02 | 23024510.08 | 7.87 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 23.87 | 6.09 | 0.21 | 222600548.49 | 3.76 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.22 | 0.04 | 1349074.46 | 6.34 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.68 | -0.09 | 695016.15 | 6.66 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.17 | 0.05 | 616995.16 | 14.53 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.15 | -0.03 | 247746.74 | 12.75 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.91 | 0.07 | 160796.88 | 20.05 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 11.25 | 3.1 | 0.2 | 806617.46 | 9.89 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 8.47 | 5.56 | 0.04 | 538329.76 | 0.5 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.87 | 0.03 | 195670.0 | 13.9 | skipped_fast |
| KITEUSDT | IDLE | 3.43 | 9.68 | 3.68 | 0.09 | 74361.08 | 11.76 | skipped_fast |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.04 | 87137.41 | 11.14 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.17 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.36 | 3.9 | -0.0 | 177339.51 | 46.24 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3225.39 | 59.7 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.25 | -0.04 | 52698.42 | 41.01 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.27 | 0.04 | 58353.08 | 16.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
