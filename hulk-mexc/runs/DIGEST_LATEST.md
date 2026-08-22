# Hulk DIGEST — 2026-08-22T07:50:30Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.05 | 0.01 | 23762288.6 | 5.91 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 23.87 | 7.03 | 0.2 | 222730683.56 | 6.97 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.55 | 0.04 | 1348548.88 | 6.37 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.12 | -0.1 | 696050.32 | 3.35 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.37 | 0.04 | 616032.25 | 12.48 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.41 | -0.04 | 248074.86 | 3.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 11.08 | 0.06 | 160739.11 | 9.61 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 11.25 | 3.08 | 0.2 | 807223.11 | 6.59 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.07 | 0.03 | 538682.36 | 31.01 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.88 | 0.03 | 194762.0 | 58.74 | skipped_fast |
| KITEUSDT | IDLE | 3.44 | 9.68 | 3.81 | 0.08 | 74226.58 | 12.69 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.81 | -0.04 | 87086.08 | 33.35 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 23.38 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 2.09 | 5.36 | 4.2 | -0.01 | 176325.81 | 30.93 | skipped_fast |
| QAITUSDT | IDLE | 1.68 | 3.24 | 0.86 | -0.01 | 3254.01 | 31.68 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 0.98 | 0.01 | 52355.0 | 41.01 | skipped_fast |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.2 | 0.04 | 58331.66 | 8.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
