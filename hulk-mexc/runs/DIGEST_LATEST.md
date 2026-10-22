# Hulk DIGEST — 2026-10-22T16:13:54Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 0.93 | 3.85 | 2.07 | -0.15 | 1975114.38 | 15.71 | skipped_fast |
| XRPUSDT | IDLE | 0.73 | 1.34 | 0.75 | -0.04 | 28918502.4 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.25 | 0.89 | -0.05 | 189755659.0 | 0.58 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.9 | 0.63 | -0.04 | 498404462.95 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 3.91 | 2.9 | -0.04 | 1200758.09 | 1.57 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.06 | 1.62 | -0.07 | 1295916.33 | 9.99 | skipped_fast |
| EDELUSDT | IDLE | 2.48 | 5.61 | 4.45 | -0.07 | 539763.56 | 21.75 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.82 | 6.62 | 5.99 | -0.08 | 225603.54 | 20.84 | skipped_fast |
| PYTHUSDT | IDLE | 1.17 | 2.9 | 2.68 | -0.1 | 564642.51 | 5.42 | skipped_fast |
| RWAINCUSDT | IDLE | 2.36 | 4.49 | 1.49 | -0.01 | 59733.96 | 5.6 | skipped_fast |
| CHIPUSDT | IDLE | 0.68 | 3.0 | 1.11 | -0.07 | 329448.76 | 13.72 | skipped_fast |
| CCUSDT | IDLE | 0.65 | 2.15 | 1.38 | -0.06 | 328451.64 | 10.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.74 | 4.32 | 2.36 | 0.05 | 54317.11 | 56.59 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.68 | 2.03 | -0.07 | 78393.16 | 8.46 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.09 | 1.55 | -0.06 | 100562.56 | 15.55 | skipped_fast |
| KITEUSDT | IDLE | 0.8 | 1.55 | 0.34 | -0.03 | 60440.86 | 12.47 | skipped_fast |
| LAUSDT | IDLE | 1.16 | 3.61 | 2.55 | -0.08 | 58522.29 | 25.8 | skipped_fast |
| IOTAUSDT | IDLE | 0.98 | 2.16 | 1.41 | -0.07 | 78758.24 | 13.41 | skipped_fast |
| WAXLUSDT | IDLE | 0.91 | 3.11 | 2.77 | -0.11 | 58536.88 | 62.46 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.36 | 1.18 | -0.02 | 52140.75 | 39.89 | skipped_fast |
| FLUIDUSDT | IDLE | 0.29 | 1.67 | 1.34 | -0.06 | 19114.15 | 10.81 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.53 | 0.23 | -0.01 | 39702.71 | 55.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
