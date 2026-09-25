# Hulk DIGEST — 2026-09-25T05:24:50Z

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
| XRPUSDT | IDLE | 1.37 | 2.45 | 1.88 | 0.01 | 72465057.2 | 0.65 | skipped_fast |
| ETHUSDT | IDLE | 0.58 | 1.02 | 0.9 | -0.01 | 352492773.26 | 0.6 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 0.97 | 0.9 | -0.0 | 734216475.31 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.8 | 2.72 | 1.83 | 0.04 | 1018310.78 | 7.33 | skipped_fast |
| RIZEUSDT | IDLE | 2.33 | 62.83 | 19.05 | 0.73 | 105241.58 | 285.41 | skipped_fast |
| HBARUSDT | IDLE | 1.4 | 2.48 | 2.1 | 0.01 | 914875.57 | 2.17 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 3.32 | 2.0 | 0.05 | 527027.56 | 7.83 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 5.38 | 5.1 | -0.04 | 65332.23 | 10.36 | skipped_fast |
| REDUSDT | IDLE | 2.2 | 6.53 | 3.92 | 0.06 | 110895.01 | 14.74 | skipped_fast |
| WUSDT | IDLE | 1.62 | 2.87 | 2.43 | 0.02 | 268419.19 | 10.33 | skipped_fast |
| QNTUSDT | IDLE | 1.15 | 11.09 | 2.21 | 0.33 | 360953.02 | 11.42 | skipped_fast |
| EDELUSDT | IDLE | 0.57 | 6.2 | 3.65 | 0.06 | 191279.48 | 20.25 | skipped_fast |
| ZBCNUSDT | IDLE | 0.79 | 1.55 | 0.16 | 0.01 | 231643.7 | 18.94 | skipped_fast |
| CHIPUSDT | IDLE | 0.89 | 4.62 | 3.37 | 0.09 | 107543.22 | 19.42 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 2.67 | 1.54 | 0.04 | 91887.47 | 6.54 | skipped_fast |
| TELUSDT | IDLE | 2.64 | 4.86 | 2.77 | -0.07 | 107506.1 | 61.88 | skipped_fast |
| RWAINCUSDT | IDLE | 0.63 | 3.38 | 0.27 | 0.19 | 14123.79 | 68.45 | skipped_fast |
| MNSRYUSDT | IDLE | 0.74 | 1.41 | 0.42 | 0.01 | 40153.86 | 5.16 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.59 | 0.22 | 0.01 | 58865.24 | 7.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.33 | 0.66 | 0.0 | 0.04 | 1081.64 | 21.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
