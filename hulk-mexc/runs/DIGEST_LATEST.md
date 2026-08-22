# Hulk DIGEST — 2026-08-22T07:34:00Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.1 | 19.14 | 7.86 | 0.04 | 22216092.72 | 3.89 | skipped_fast |
| XRPUSDT | IDLE | 3.35 | 23.87 | 4.58 | 0.24 | 221112986.62 | 3.09 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 8.55 | 0.06 | 1353741.18 | 6.29 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.06 | -0.09 | 696653.57 | 3.3 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 17.58 | 7.18 | 0.07 | 618360.65 | 11.29 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.18 | -0.02 | 248361.57 | 6.35 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 42.01 | 9.99 | 0.08 | 160663.62 | 10.34 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 11.25 | 3.45 | 0.19 | 802787.0 | 9.93 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 8.47 | 5.44 | 0.05 | 541398.93 | 34.23 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 13.91 | 8.07 | 0.04 | 198515.22 | 3.06 | skipped_fast |
| KITEUSDT | IDLE | 3.41 | 9.68 | 3.18 | 0.09 | 74157.47 | 11.7 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.81 | -0.04 | 87163.11 | 55.83 | skipped_fast |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6890.3 | 20.36 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.02 | 11300.37 | 53.65 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 5.36 | 3.5 | 0.04 | 189873.03 | 30.69 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3225.39 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.45 | -0.05 | 52771.54 | 32.59 | skipped_fast |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.51 | 0.04 | 58215.43 | 16.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
