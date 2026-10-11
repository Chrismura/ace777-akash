# Hulk DIGEST — 2026-10-11T01:03:31Z

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
| XRPUSDT | IDLE | 0.53 | 0.93 | 0.87 | -0.0 | 12773681.06 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.26 | 0.46 | 0.41 | 0.01 | 128555374.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.12 | 0.2 | 0.2 | 0.0 | 148783303.83 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.31 | 4.02 | 3.74 | -0.0 | 1254466.91 | 8.62 | skipped_fast |
| QNTUSDT | IDLE | 1.03 | 1.88 | 1.25 | -0.04 | 1273201.61 | 2.51 | skipped_fast |
| PYTHUSDT | IDLE | 1.72 | 3.03 | 2.73 | -0.04 | 751968.0 | 1.29 | skipped_fast |
| EDELUSDT | IDLE | 2.51 | 4.54 | 3.18 | -0.04 | 258417.53 | 13.04 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.63 | 7.08 | 6.61 | -0.11 | 34308.93 | 27.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.13 | 9.76 | 2.97 | 0.31 | 267978.89 | 17.59 | skipped_fast |
| BIOUSDT | IDLE | 1.67 | 2.91 | 2.82 | 0.01 | 87805.95 | 3.46 | skipped_fast |
| TELUSDT | IDLE | 2.64 | 5.07 | 4.61 | -0.07 | 144316.58 | 46.0 | skipped_fast |
| CCUSDT | IDLE | 0.56 | 1.02 | 0.69 | -0.03 | 237128.66 | 7.57 | skipped_fast |
| ZBCNUSDT | IDLE | 0.68 | 1.34 | 0.1 | 0.02 | 170765.08 | 9.94 | skipped_fast |
| KITEUSDT | IDLE | 0.74 | 1.53 | 1.49 | 0.04 | 75289.25 | 10.26 | skipped_fast |
| REDUSDT | IDLE | 0.69 | 1.21 | 1.18 | 0.0 | 56348.97 | 10.04 | skipped_fast |
| HBARUSDT | IDLE | 0.6 | 1.06 | 0.96 | -0.0 | 307872.38 | 6.53 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 1.29 | 0.54 | -0.02 | 11453.26 | 19.81 | skipped_fast |
| MNSRYUSDT | IDLE | 1.01 | 1.8 | 1.41 | -0.01 | 37006.26 | 28.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.71 | 1.36 | 0.43 | 0.02 | 7774.46 | 17.73 | skipped_fast |
| RWAUSDT | IDLE | 0.18 | 0.32 | 0.24 | 0.0 | 53887.06 | 15.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
