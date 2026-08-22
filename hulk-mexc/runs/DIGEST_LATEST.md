# Hulk DIGEST — 2026-08-22T06:07:08Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.94 | 0.07 | 18491717.51 | 27.55 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 23.87 | 10.48 | 0.16 | 207697593.08 | 5.92 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.5 | 0.05 | 1376967.6 | 1.27 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 24.54 | 13.09 | -0.1 | 700578.3 | 6.76 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.74 | 0.06 | 611448.73 | 21.91 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 13.37 | -0.04 | 245820.61 | 6.66 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 42.58 | 12.56 | 0.08 | 165681.12 | 12.42 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 8.47 | 6.14 | 0.04 | 547586.88 | 3.0 | skipped_fast |
| CCUSDT | IDLE | 1.86 | 9.8 | 2.44 | 0.18 | 766306.79 | 9.14 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.18 | 0.04 | 198349.69 | 1.55 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 9.68 | 5.96 | 0.07 | 74852.36 | 12.04 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 4.52 | 1.73 | -0.02 | 88067.49 | 55.22 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.01 | 11531.83 | 64.66 | skipped_fast |
| FLUIDUSDT | IDLE | 3.24 | 7.9 | 4.42 | 0.06 | 5356.23 | 21.24 | skipped_fast |
| TELUSDT | IDLE | 2.08 | 5.52 | 2.81 | 0.07 | 195493.17 | 45.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.99 | 3.99 | 3.53 | 0.07 | 59026.43 | 26.26 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.82 | 3.38 | 1.75 | 0.05 | 57911.42 | 16.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
