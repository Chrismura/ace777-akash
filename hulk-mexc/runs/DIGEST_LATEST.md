# Hulk DIGEST — 2026-09-22T19:15:11Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.65 | 16.78 | 9.95 | 0.05 | 1636951.4 | 1.51 | skipped_fast |
| XRPUSDT | IDLE | 2.02 | 3.98 | 0.39 | 0.06 | 117532037.18 | 1.89 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.57 | 0.07 | -0.0 | 454103281.33 | 0.4 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.42 | 0.24 | 0.01 | 940013964.63 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 4.46 | 0.17 | 0.09 | 1510304.33 | 9.11 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 15.46 | 9.44 | -0.01 | 298261.2 | 29.31 | skipped_fast |
| CCUSDT | IDLE | 2.81 | 5.07 | 3.72 | -0.01 | 491599.71 | 10.59 | skipped_fast |
| RIZEUSDT | IDLE | 2.3 | 26.82 | 8.66 | -0.16 | 44007.95 | 57.12 | skipped_fast |
| WUSDT | IDLE | 2.05 | 3.87 | 1.58 | 0.02 | 357624.37 | 4.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.54 | 4.6 | 3.17 | -0.02 | 223274.8 | 33.29 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 4.57 | 1.14 | 0.02 | 137616.02 | 6.8 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 3.44 | 2.98 | -0.01 | 140552.99 | 15.49 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 6.79 | 0.87 | 0.17 | 116134.81 | 9.37 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 3.67 | 0.5 | 0.05 | 64892.13 | 15.17 | skipped_fast |
| TELUSDT | IDLE | 2.34 | 6.81 | 0.23 | 0.07 | 104523.2 | 11.3 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 3.39 | 2.04 | 0.08 | 187773.63 | 1.39 | skipped_fast |
| RWAINCUSDT | IDLE | 0.36 | 0.72 | 0.0 | 0.05 | 19957.17 | 5.51 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.24 | 0.22 | 0.0 | 54203.37 | 7.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.33 | 0.47 | 0.02 | 7769.26 | 21.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.05 | -0.0 | 40185.68 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
