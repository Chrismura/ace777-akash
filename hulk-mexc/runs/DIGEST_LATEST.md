# Hulk DIGEST — 2026-08-22T10:23:32Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 16.77 | 12.12 | -0.01 | 51624479.74 | 20.79 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.91 | 23.87 | 14.13 | 0.06 | 216187804.01 | 2.06 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 15.8 | 11.81 | 0.0 | 1250414.07 | 5.22 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.06 | 22.93 | 13.2 | -0.12 | 664694.73 | 13.75 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 16.84 | 11.13 | -0.0 | 596348.57 | 23.74 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.76 | -0.06 | 236872.42 | 13.2 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.41 | 0.11 | 816354.13 | 8.73 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 37.92 | 12.12 | 0.03 | 155524.45 | 11.83 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.88 | 8.04 | -0.03 | 428203.34 | 23.12 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 9.28 | 6.03 | 0.02 | 73136.47 | 20.5 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 9.75 | 7.58 | -0.01 | 189338.93 | 1.58 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 8.01 | 7.32 | -0.04 | 168611.19 | 21.36 | skipped_fast |
| EDELUSDT | IDLE | 2.67 | 4.76 | 3.89 | -0.03 | 78473.43 | 56.09 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5825.49 | 61.84 | skipped_fast |
| QAITUSDT | IDLE | 1.6 | 2.91 | 1.98 | -0.01 | 3205.44 | 63.29 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11368.82 | 43.43 | skipped_fast |
| RWAUSDT | IDLE | 1.83 | 3.29 | 2.47 | 0.02 | 57490.41 | 16.33 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.23 | 0.0 | 49248.55 | 46.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
