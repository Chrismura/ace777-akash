# Hulk DIGEST — 2026-08-22T07:16:35Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 19.14 | 9.58 | 0.04 | 21658832.92 | 3.96 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 23.87 | 6.55 | 0.21 | 218187079.93 | 3.78 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 15.8 | 9.19 | 0.05 | 1356872.68 | 5.07 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.71 | -0.1 | 704601.85 | 6.67 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.74 | 0.06 | 620716.77 | 16.54 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 11.98 | -0.03 | 247421.67 | 6.59 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.58 | 0.07 | 160616.44 | 13.04 | skipped_fast |
| CCUSDT | IDLE | 2.07 | 11.25 | 4.13 | 0.18 | 796510.38 | 9.99 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 8.47 | 5.88 | 0.05 | 542136.93 | 31.46 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.41 | 0.04 | 199603.96 | 6.15 | skipped_fast |
| KITEUSDT | IDLE | 3.39 | 9.68 | 2.82 | 0.1 | 74345.97 | 10.76 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6991.08 | 21.94 | skipped_fast |
| EDELUSDT | IDLE | 2.18 | 4.52 | 2.05 | -0.02 | 87280.53 | 66.59 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.02 | 11393.75 | 101.69 | skipped_fast |
| TELUSDT | IDLE | 2.07 | 5.36 | 3.7 | 0.06 | 196591.8 | 41.03 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3286.33 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.59 | 0.02 | 56773.64 | 27.43 | skipped_fast |
| RWAUSDT | IDLE | 1.78 | 3.29 | 1.75 | 0.04 | 58016.76 | 24.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
