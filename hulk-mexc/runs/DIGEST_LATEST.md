# Hulk DIGEST — 2026-10-14T15:19:05Z

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
| PYTHUSDT | IDLE | 2.36 | 5.34 | 3.92 | 0.01 | 2116446.71 | 1.22 | skipped_fast |
| WUSDT | IDLE | 1.93 | 7.54 | 5.92 | -0.15 | 3348310.33 | 1.96 | skipped_fast |
| XRPUSDT | IDLE | 2.37 | 4.24 | 3.3 | -0.02 | 40252190.38 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 2.34 | 4.22 | 3.07 | -0.03 | 183314046.09 | 0.25 | skipped_fast |
| BTCUSDT | IDLE | 1.52 | 2.71 | 2.21 | -0.02 | 407560296.76 | 0.33 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 4.8 | 2.16 | 0.01 | 1525718.7 | 7.24 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 22.88 | 17.52 | -0.04 | 63978.37 | 55.0 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 7.17 | 5.9 | -0.05 | 188063.5 | 21.88 | skipped_fast |
| CCUSDT | IDLE | 1.53 | 3.9 | 3.18 | -0.09 | 468697.19 | 3.4 | skipped_fast |
| CHIPUSDT | IDLE | 2.86 | 5.67 | 4.33 | -0.05 | 80880.77 | 14.61 | skipped_fast |
| HBARUSDT | IDLE | 2.28 | 4.11 | 3.02 | -0.03 | 461381.17 | 5.92 | skipped_fast |
| BIOUSDT | IDLE | 2.61 | 4.67 | 3.63 | -0.03 | 68594.29 | 11.29 | skipped_fast |
| KITEUSDT | IDLE | 2.28 | 6.33 | 5.19 | 0.03 | 85839.75 | 12.28 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.57 | 3.04 | -0.01 | 150492.05 | 17.92 | skipped_fast |
| REDUSDT | IDLE | 2.11 | 3.88 | 2.21 | 0.01 | 59864.73 | 6.54 | skipped_fast |
| RWAINCUSDT | IDLE | 1.61 | 5.32 | 3.51 | -0.08 | 32440.6 | 16.06 | skipped_fast |
| TELUSDT | IDLE | 2.43 | 4.39 | 3.16 | -0.01 | 111927.14 | 28.6 | skipped_fast |
| FLUIDUSDT | IDLE | 2.49 | 7.33 | 4.76 | 0.03 | 16104.98 | 21.72 | skipped_fast |
| RWAUSDT | IDLE | 1.3 | 2.31 | 1.94 | -0.03 | 56531.73 | 7.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.65 | 1.13 | 1.07 | -0.01 | 39337.4 | 54.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
