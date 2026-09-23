# Hulk DIGEST — 2026-09-23T22:25:13Z

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
| ETHUSDT | IDLE | 1.0 | 1.94 | 0.38 | -0.02 | 484033763.38 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.75 | 2.19 | 0.56 | -0.04 | 112126036.68 | 2.0 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.17 | 0.19 | -0.02 | 839145648.4 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 4.79 | 0.29 | -0.03 | 1404553.09 | 10.88 | skipped_fast |
| HBARUSDT | IDLE | 0.48 | 1.59 | 0.63 | -0.08 | 1329542.43 | 1.11 | skipped_fast |
| CCUSDT | IDLE | 1.0 | 2.39 | 0.81 | -0.05 | 526013.81 | 5.52 | skipped_fast |
| WUSDT | IDLE | 1.17 | 3.24 | 2.29 | -0.08 | 391358.06 | 6.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.45 | 4.87 | 2.96 | -0.09 | 219605.09 | 16.68 | skipped_fast |
| KITEUSDT | IDLE | 1.64 | 3.32 | 1.47 | -0.04 | 174781.79 | 8.3 | skipped_fast |
| ZBCNUSDT | IDLE | 1.2 | 3.19 | 0.55 | 0.02 | 236060.76 | 10.33 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 3.99 | 2.2 | -0.06 | 169880.25 | 32.14 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 2.7 | 1.57 | -0.04 | 59287.78 | 14.46 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 2.43 | 1.36 | -0.05 | 95982.8 | 7.09 | skipped_fast |
| TELUSDT | IDLE | 1.09 | 3.08 | 0.98 | -0.07 | 150279.26 | 23.17 | skipped_fast |
| RWAINCUSDT | IDLE | 0.71 | 1.31 | 0.7 | -0.03 | 20494.41 | 70.37 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.01 | 1.25 | -0.04 | 129862.16 | 5.63 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.11 | 0.15 | -0.02 | 56351.42 | 29.63 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 2.19 | 0.47 | -0.05 | 5069.67 | 21.46 | skipped_fast |
| RIZEUSDT | IDLE | 0.72 | 4.43 | 1.99 | 0.12 | 70088.64 | 215.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.75 | 0.18 | -0.01 | 40703.0 | 35.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
