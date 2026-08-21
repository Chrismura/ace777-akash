# Hulk DIGEST — 2026-08-21T23:58:57Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.49 | 0.1 | 6229668.98 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.96 | 8.23 | 1.25 | 0.15 | 142074863.53 | 2.75 | skipped_fast |
| HBARUSDT | IDLE | 2.62 | 6.36 | 1.13 | 0.09 | 909397.93 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.89 | 0.12 | 515107.73 | 32.93 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 7.42 | 0.73 | 0.13 | 645727.31 | 7.1 | skipped_fast |
| WUSDT | IDLE | 2.77 | 6.91 | 1.74 | 0.08 | 379007.45 | 11.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 1.0 | 0.04 | 545648.68 | 9.23 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.92 | 0.03 | 187231.52 | 6.21 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | 0.0 | 80067.19 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 9.82 | 4.18 | 0.13 | 58946.22 | 45.81 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.41 | 0.06 | 189892.38 | 10.27 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 5.03 | 0.18 | 157685.23 | 10.52 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.06 | 0.07 | 155210.86 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10291.37 | 53.56 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.83 | 0.09 | 61522.23 | 12.0 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54496.24 | 16.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 21.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
