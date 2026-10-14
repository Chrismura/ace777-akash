# Hulk DIGEST — 2026-10-14T16:22:57Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.93 | 8.7 | 7.84 | -0.0 | 2081595.52 | 3.81 | skipped_fast |
| WUSDT | IDLE | 1.94 | 8.09 | 6.68 | -0.12 | 3186863.69 | 15.25 | skipped_fast |
| XRPUSDT | IDLE | 2.48 | 4.34 | 4.11 | -0.04 | 42214275.45 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 2.38 | 4.22 | 3.63 | -0.04 | 187287044.51 | 0.45 | skipped_fast |
| BTCUSDT | IDLE | 1.61 | 2.82 | 2.72 | -0.02 | 417932258.71 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.97 | 4.8 | 2.56 | 0.0 | 1474772.05 | 6.78 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 22.88 | 17.83 | 0.02 | 62747.66 | 59.57 | skipped_fast |
| ZBCNUSDT | IDLE | 3.92 | 7.17 | 4.49 | -0.03 | 188258.83 | 15.73 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 9.7 | 7.29 | -0.07 | 109884.72 | 7.54 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 3.9 | 2.62 | -0.09 | 448630.76 | 8.45 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 7.31 | 5.7 | 0.01 | 86669.87 | 10.85 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 13.1 | 8.75 | 0.06 | 17833.62 | 21.33 | skipped_fast |
| HBARUSDT | IDLE | 2.32 | 4.11 | 3.47 | -0.04 | 464219.36 | 5.94 | skipped_fast |
| BIOUSDT | IDLE | 2.64 | 4.67 | 4.1 | -0.04 | 68549.0 | 3.78 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 3.55 | 2.32 | -0.01 | 163516.66 | 29.66 | skipped_fast |
| REDUSDT | IDLE | 2.15 | 3.88 | 2.84 | -0.01 | 61045.67 | 15.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.54 | 4.94 | 4.45 | -0.1 | 31311.15 | 16.23 | skipped_fast |
| TELUSDT | IDLE | 2.28 | 4.39 | 1.16 | 0.01 | 114492.69 | 11.2 | skipped_fast |
| RWAUSDT | IDLE | 1.31 | 2.31 | 2.1 | -0.03 | 56354.95 | 7.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.62 | 1.13 | 0.67 | -0.01 | 38875.15 | 40.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
