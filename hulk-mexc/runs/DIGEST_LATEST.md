# Hulk DIGEST — 2026-10-07T07:39:11Z

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
| QNTUSDT | IDLE | 3.56 | 9.26 | 3.61 | 0.0 | 2683253.71 | 6.65 | skipped_fast |
| ETHUSDT | IDLE | 1.45 | 2.68 | 1.44 | -0.03 | 469008580.12 | 0.95 | skipped_fast |
| XRPUSDT | IDLE | 1.11 | 2.17 | 0.28 | -0.02 | 40341371.54 | 2.04 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.1 | 0.28 | -0.01 | 644320042.26 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 19.72 | 15.67 | -0.18 | 455917.68 | 26.85 | skipped_fast |
| PYTHUSDT | IDLE | 1.21 | 3.95 | 1.48 | -0.07 | 1136043.73 | 2.75 | skipped_fast |
| WUSDT | IDLE | 2.6 | 4.89 | 2.13 | 0.01 | 505239.45 | 10.46 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 4.54 | 3.84 | -0.07 | 469355.98 | 7.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.69 | 6.31 | 1.16 | -0.01 | 229498.26 | 10.81 | skipped_fast |
| HBARUSDT | IDLE | 1.61 | 2.92 | 1.95 | -0.04 | 733161.22 | 5.21 | skipped_fast |
| CHIPUSDT | IDLE | 2.29 | 5.59 | 3.83 | -0.06 | 218881.7 | 11.89 | skipped_fast |
| BIOUSDT | IDLE | 2.22 | 8.8 | 3.63 | -0.07 | 86328.96 | 3.43 | skipped_fast |
| REDUSDT | IDLE | 2.36 | 6.45 | 4.34 | -0.09 | 62451.26 | 15.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.45 | 10.07 | 7.16 | 0.13 | 82728.18 | 21.52 | skipped_fast |
| RWAINCUSDT | IDLE | 2.4 | 6.9 | 1.88 | -0.03 | 44890.36 | 78.57 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 3.0 | 0.01 | 0.02 | 60224.35 | 9.28 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 5.96 | 2.67 | 0.1 | 191937.33 | 28.87 | skipped_fast |
| FLUIDUSDT | IDLE | 1.16 | 3.45 | 2.0 | -0.06 | 54085.13 | 21.38 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.57 | 1.18 | -0.02 | 51828.67 | 14.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.57 | 1.04 | 0.72 | -0.01 | 38892.58 | 18.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
