# Hulk DIGEST — 2026-10-02T00:20:10Z

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
| QNTUSDT | IDLE | 1.56 | 9.18 | 7.54 | -0.16 | 6525408.11 | 9.83 | skipped_fast |
| XRPUSDT | IDLE | 0.66 | 1.24 | 0.48 | 0.01 | 38985248.3 | 2.0 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.71 | 0.05 | 0.01 | 358272073.31 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.54 | 0.03 | 0.02 | 658732195.97 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 15.76 | 11.74 | 0.11 | 156150.11 | 22.2 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.44 | 1.92 | -0.01 | 440572.37 | 8.97 | skipped_fast |
| CCUSDT | IDLE | 0.5 | 0.93 | 0.45 | -0.05 | 582313.81 | 5.81 | skipped_fast |
| PYTHUSDT | IDLE | 1.15 | 2.12 | 1.18 | -0.03 | 390258.92 | 5.38 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.97 | 0.8 | -0.01 | 667782.46 | 3.89 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 2.6 | 0.56 | -0.03 | 358289.87 | 28.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.43 | 2.68 | 1.2 | -0.0 | 85605.5 | 14.01 | skipped_fast |
| BIOUSDT | IDLE | 1.21 | 2.31 | 0.72 | -0.02 | 78335.19 | 6.6 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 2.46 | 0.32 | 0.07 | 107206.69 | 7.91 | skipped_fast |
| RIZEUSDT | IDLE | 1.25 | 4.89 | 2.56 | 0.06 | 41099.05 | 27.68 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.13 | 1.18 | -0.0 | 68452.58 | 14.16 | skipped_fast |
| TELUSDT | IDLE | 1.23 | 2.79 | 2.16 | -0.08 | 138671.99 | 18.8 | skipped_fast |
| RWAINCUSDT | IDLE | 0.4 | 1.24 | 0.0 | 0.07 | 24628.21 | 73.92 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.68 | 0.34 | -0.01 | 37229.11 | 18.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.49 | 0.99 | 0.0 | 0.02 | 3875.77 | 23.94 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.51 | 0.22 | 0.01 | 54642.99 | 43.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
