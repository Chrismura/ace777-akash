# Hulk DIGEST — 2026-10-21T03:31:49Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.55 | 0.97 | 0.87 | 0.02 | 24165668.91 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.51 | 0.91 | 0.68 | 0.02 | 170947966.61 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.59 | 0.5 | 0.01 | 323734306.25 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.03 | 3.02 | 2.89 | 0.08 | 949934.23 | 1.26 | skipped_fast |
| WUSDT | IDLE | 1.37 | 2.58 | 1.06 | 0.02 | 643036.24 | 17.82 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.14 | 11.09 | 1.38 | 0.1 | 205331.63 | 47.51 | skipped_fast |
| QNTUSDT | IDLE | 1.29 | 2.46 | 0.81 | 0.0 | 813588.66 | 0.51 | skipped_fast |
| CHIPUSDT | IDLE | 1.43 | 3.53 | 2.88 | 0.03 | 446578.59 | 6.84 | skipped_fast |
| RWAINCUSDT | IDLE | 2.34 | 10.7 | 8.58 | -0.09 | 79192.56 | 39.6 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 12.41 | 10.79 | 0.04 | 17676.55 | 21.49 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.76 | 0.9 | -0.02 | 333565.96 | 10.43 | skipped_fast |
| EDELUSDT | IDLE | 0.53 | 3.4 | 2.68 | 0.26 | 333409.61 | 31.06 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 2.71 | 0.12 | 0.05 | 57394.47 | 17.38 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.64 | 1.36 | 0.01 | 344765.72 | 4.8 | skipped_fast |
| BIOUSDT | IDLE | 0.71 | 1.31 | 0.73 | 0.04 | 61291.95 | 4.06 | skipped_fast |
| KITEUSDT | IDLE | 0.59 | 1.07 | 0.76 | -0.01 | 73564.27 | 10.7 | skipped_fast |
| LAUSDT | IDLE | 1.97 | 4.98 | 0.76 | 0.07 | 55242.72 | 23.08 | skipped_fast |
| RIZEUSDT | IDLE | 0.77 | 3.01 | 2.29 | 0.05 | 61117.52 | 62.42 | skipped_fast |
| WAXLUSDT | IDLE | 1.73 | 3.28 | 1.14 | -0.02 | 57430.41 | 63.55 | skipped_fast |
| IOTAUSDT | IDLE | 0.76 | 1.36 | 1.05 | 0.02 | 75157.49 | 28.0 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.63 | 0.39 | 0.0 | 53277.89 | 15.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.37 | 0.06 | -0.0 | 40132.11 | 7.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
