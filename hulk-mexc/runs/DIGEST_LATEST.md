# Hulk DIGEST — 2026-09-23T06:17:09Z

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
| XRPUSDT | IDLE | 2.32 | 5.31 | 2.3 | 0.07 | 115434669.94 | 1.85 | skipped_fast |
| PYTHUSDT | IDLE | 0.63 | 3.06 | 0.68 | 0.06 | 1766497.69 | 2.99 | skipped_fast |
| ETHUSDT | IDLE | 0.83 | 1.52 | 0.96 | 0.01 | 409524347.34 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.29 | 0.77 | 0.01 | 870894764.14 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 2.82 | 1.98 | 0.07 | 1798746.87 | 1.01 | skipped_fast |
| ZBCNUSDT | IDLE | 3.52 | 8.81 | 2.26 | 0.06 | 223269.89 | 23.76 | skipped_fast |
| CCUSDT | IDLE | 1.53 | 2.97 | 0.64 | -0.02 | 411573.44 | 8.63 | skipped_fast |
| WUSDT | IDLE | 1.9 | 3.68 | 0.81 | 0.03 | 313212.8 | 10.51 | skipped_fast |
| KITEUSDT | IDLE | 1.49 | 4.42 | 3.75 | 0.09 | 130771.63 | 8.08 | skipped_fast |
| CHIPUSDT | IDLE | 1.36 | 2.65 | 1.4 | -0.02 | 204013.17 | 8.58 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 3.38 | 0.42 | 0.06 | 112158.47 | 13.13 | skipped_fast |
| EDELUSDT | IDLE | 0.86 | 4.25 | 1.26 | -0.03 | 267197.82 | 26.18 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 14.58 | 7.5 | 0.42 | 57923.97 | 48.39 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 2.68 | 0.24 | 0.03 | 59922.62 | 20.5 | skipped_fast |
| RWAINCUSDT | IDLE | 0.72 | 1.84 | 0.8 | 0.04 | 22463.0 | 10.68 | skipped_fast |
| QNTUSDT | IDLE | 0.91 | 2.9 | 1.85 | 0.11 | 215822.48 | 9.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.3 | 2.42 | 1.17 | 0.02 | 4334.0 | 21.7 | skipped_fast |
| TELUSDT | IDLE | 0.72 | 3.08 | 1.33 | 0.15 | 109808.42 | 32.4 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.8 | 0.43 | 0.01 | 53397.87 | 21.64 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.72 | 0.04 | 0.01 | 39360.68 | 5.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
