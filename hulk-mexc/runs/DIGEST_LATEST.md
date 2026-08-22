# Hulk DIGEST — 2026-08-22T06:19:00Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 19.14 | 8.38 | 0.07 | 19339824.96 | 13.69 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 23.87 | 9.72 | 0.16 | 209399827.43 | 1.96 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 15.8 | 9.39 | 0.05 | 1384493.14 | 3.81 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.62 | -0.09 | 694874.84 | 6.66 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.79 | 0.06 | 615364.27 | 13.46 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 13.28 | -0.04 | 245207.89 | 10.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.51 | 0.09 | 166088.93 | 17.5 | skipped_fast |
| CCUSDT | IDLE | 1.96 | 11.25 | 1.69 | 0.2 | 767516.76 | 9.75 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 8.47 | 5.67 | 0.03 | 545785.25 | 33.34 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.04 | 0.04 | 197389.34 | 1.55 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 9.68 | 5.62 | 0.08 | 74897.16 | 20.32 | skipped_fast |
| EDELUSDT | IDLE | 2.33 | 4.52 | 4.22 | -0.03 | 88100.4 | 67.19 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.35 | 0.01 | 11505.67 | 64.66 | skipped_fast |
| FLUIDUSDT | IDLE | 3.24 | 7.9 | 4.42 | 0.06 | 5356.23 | 22.03 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.52 | 4.1 | 0.06 | 197120.17 | 41.17 | skipped_fast |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.97 | 3.99 | 2.97 | 0.08 | 59415.83 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 1.84 | 3.38 | 1.99 | 0.04 | 58134.89 | 32.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
