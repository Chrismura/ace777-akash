# Hulk DIGEST — 2026-09-14T03:34:05Z

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
| XRPUSDT | IDLE | 1.66 | 3.29 | 0.15 | 0.01 | 22430657.08 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 1.12 | 2.2 | 0.25 | -0.0 | 304309237.59 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.99 | 1.94 | 0.21 | 0.01 | 363403147.74 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 49.46 | 23.65 | 0.21 | 71541.45 | 86.65 | skipped_fast |
| REDUSDT | IDLE | 4.12 | 10.0 | 2.01 | 0.03 | 89939.63 | 9.41 | skipped_fast |
| PYTHUSDT | IDLE | 2.28 | 4.62 | 1.81 | 0.03 | 475662.23 | 1.76 | skipped_fast |
| CCUSDT | IDLE | 1.54 | 3.0 | 0.55 | -0.01 | 332061.23 | 7.25 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 7.94 | 1.86 | 0.12 | 222197.83 | 43.51 | skipped_fast |
| WUSDT | IDLE | 2.07 | 4.09 | 0.29 | 0.0 | 185692.95 | 11.89 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 3.39 | 3.06 | -0.02 | 206214.28 | 24.63 | skipped_fast |
| KITEUSDT | IDLE | 2.21 | 4.27 | 0.94 | 0.01 | 59332.71 | 11.98 | skipped_fast |
| BIOUSDT | IDLE | 2.09 | 4.12 | 0.35 | 0.0 | 68156.89 | 3.89 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 5.35 | 0.74 | -0.1 | 96624.34 | 16.35 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.31 | 0.43 | 0.02 | 265704.12 | 1.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.4 | 0.72 | 0.6 | -0.01 | 9051.47 | 22.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.75 | 0.85 | -0.02 | 1413.38 | 18.5 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 2.18 | 0.3 | -0.01 | 35540.24 | 11.01 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 1.86 | 0.19 | -0.03 | 82572.8 | 37.95 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.6 | 0.22 | 0.0 | 53047.75 | 14.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.19 | -0.0 | 30220.74 | 6.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
