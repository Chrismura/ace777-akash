# Hulk DIGEST — 2026-09-11T12:20:29Z

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
| XRPUSDT | IDLE | 1.67 | 2.98 | 2.38 | -0.04 | 39790512.6 | 2.26 | skipped_fast |
| ETHUSDT | IDLE | 0.75 | 1.34 | 1.09 | -0.0 | 463652459.46 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.94 | 0.6 | -0.01 | 511683144.37 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.81 | 5.15 | 3.11 | -0.05 | 439184.28 | 6.22 | skipped_fast |
| PYTHUSDT | IDLE | 2.23 | 4.04 | 2.79 | -0.03 | 365731.31 | 3.96 | skipped_fast |
| RIZEUSDT | IDLE | 1.2 | 24.77 | 7.2 | 0.11 | 126828.28 | 88.89 | skipped_fast |
| WUSDT | IDLE | 1.87 | 3.32 | 2.76 | -0.02 | 128343.15 | 11.73 | skipped_fast |
| BIOUSDT | IDLE | 1.76 | 3.16 | 2.39 | -0.04 | 79698.6 | 4.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 2.95 | 0.92 | -0.02 | 189092.46 | 55.55 | skipped_fast |
| QNTUSDT | IDLE | 2.92 | 5.13 | 4.67 | -0.03 | 41665.56 | 7.82 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 3.09 | 1.97 | -0.03 | 59578.08 | 20.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.12 | 3.47 | 1.36 | -0.06 | 129340.91 | 13.18 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 3.14 | 1.58 | 0.02 | 4306.18 | 11.07 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 2.48 | 1.62 | -0.02 | 57830.03 | 12.09 | skipped_fast |
| EDELUSDT | IDLE | 0.64 | 2.87 | 1.95 | -0.07 | 197696.76 | 18.96 | skipped_fast |
| HBARUSDT | IDLE | 1.41 | 2.55 | 1.74 | -0.03 | 195461.38 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.21 | 2.17 | 1.66 | -0.04 | 100067.49 | 52.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.14 | 1.98 | 1.94 | -0.04 | 2304.28 | 21.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.59 | 0.45 | -0.01 | 38074.23 | 5.59 | skipped_fast |
| RWAUSDT | IDLE | 0.24 | 0.46 | 0.15 | -0.01 | 49581.06 | 15.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
