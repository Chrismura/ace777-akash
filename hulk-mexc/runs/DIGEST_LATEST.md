# Hulk DIGEST — 2026-09-29T08:34:11Z

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
| QNTUSDT | IDLE | 2.52 | 26.71 | 3.44 | 0.05 | 11555031.88 | 9.56 | skipped_fast |
| ETHUSDT | IDLE | 1.54 | 2.97 | 0.68 | 0.03 | 395211219.55 | 0.04 | skipped_fast |
| WUSDT | IDLE | 3.69 | 8.66 | 2.85 | 0.01 | 1147236.26 | 9.16 | skipped_fast |
| XRPUSDT | IDLE | 1.4 | 2.71 | 0.59 | 0.02 | 58714099.1 | 1.33 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 4.54 | 3.23 | 0.2 | 11889193.85 | 2.55 | skipped_fast |
| BTCUSDT | IDLE | 0.91 | 1.76 | 0.4 | 0.01 | 672393405.0 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.08 | 3.85 | 2.06 | -0.0 | 1034535.56 | 3.76 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 3.51 | 2.55 | -0.05 | 1217493.24 | 9.11 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 15.81 | 9.31 | -0.03 | 58952.36 | 130.94 | skipped_fast |
| BIOUSDT | IDLE | 3.5 | 6.79 | 1.42 | 0.03 | 90244.1 | 9.82 | skipped_fast |
| CHIPUSDT | IDLE | 2.95 | 6.66 | 1.55 | 0.01 | 74438.66 | 18.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 4.53 | 0.09 | 0.1 | 250226.36 | 12.22 | skipped_fast |
| KITEUSDT | IDLE | 2.15 | 4.05 | 1.68 | -0.01 | 76118.9 | 9.42 | skipped_fast |
| TELUSDT | IDLE | 1.17 | 12.01 | 0.73 | 0.29 | 418956.83 | 43.31 | skipped_fast |
| FLUIDUSDT | IDLE | 3.14 | 6.78 | 0.0 | 0.07 | 3805.76 | 21.61 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 2.67 | 0.12 | -0.0 | 57581.25 | 13.02 | skipped_fast |
| EDELUSDT | IDLE | 0.45 | 2.62 | 0.23 | 0.05 | 115447.62 | 19.1 | skipped_fast |
| MNSRYUSDT | IDLE | 0.98 | 1.96 | 0.05 | -0.01 | 34641.3 | 10.33 | skipped_fast |
| RWAUSDT | IDLE | 0.76 | 1.46 | 0.43 | -0.0 | 56789.3 | 7.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 2.82 | 0.41 | 0.11 | 38199.74 | 168.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
