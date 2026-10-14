# Hulk DIGEST — 2026-10-14T23:23:06Z

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
| PYTHUSDT | IDLE | 2.72 | 7.97 | 2.4 | 0.09 | 2074811.51 | 1.17 | skipped_fast |
| WUSDT | IDLE | 1.3 | 4.66 | 2.79 | -0.1 | 2396788.25 | 8.48 | skipped_fast |
| ETHUSDT | IDLE | 0.73 | 1.35 | 0.79 | -0.03 | 237935871.22 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.67 | 1.28 | 0.36 | -0.03 | 46926754.1 | 2.25 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.64 | 0.52 | -0.02 | 445929033.31 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.96 | 3.6 | 2.15 | -0.04 | 1066264.28 | 0.98 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 2.15 | 1.91 | -0.08 | 399963.47 | 0.87 | skipped_fast |
| RWAINCUSDT | IDLE | 2.44 | 5.89 | 2.04 | -0.03 | 25689.76 | 5.07 | skipped_fast |
| EDELUSDT | IDLE | 1.72 | 3.21 | 1.54 | -0.03 | 174121.34 | 15.03 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 2.62 | 1.99 | -0.04 | 202243.11 | 26.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.41 | 4.82 | 4.37 | -0.11 | 101635.11 | 11.73 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.87 | 0.51 | -0.03 | 522109.36 | 4.74 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 4.58 | 3.94 | -0.02 | 100540.23 | 28.45 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 2.39 | 0.15 | 0.02 | 62847.51 | 15.17 | skipped_fast |
| KITEUSDT | IDLE | 0.74 | 2.09 | 1.89 | -0.02 | 86564.25 | 10.29 | skipped_fast |
| BIOUSDT | IDLE | 0.82 | 1.56 | 0.49 | -0.04 | 66746.48 | 7.55 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 3.64 | 2.57 | -0.01 | 50881.24 | 57.98 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 4.0 | 1.36 | 0.05 | 19165.45 | 21.64 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.88 | 0.71 | -0.03 | 56491.23 | 15.99 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.39 | -0.01 | 35249.88 | 23.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
