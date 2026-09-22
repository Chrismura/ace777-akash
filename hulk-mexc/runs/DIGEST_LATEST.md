# Hulk DIGEST — 2026-09-22T13:10:59Z

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
| XRPUSDT | IDLE | 1.4 | 2.67 | 0.84 | 0.04 | 109966265.35 | 0.65 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.52 | 0.21 | 0.01 | 553511958.95 | 0.11 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.23 | 0.3 | 0.01 | 981975791.14 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.49 | 5.11 | 2.22 | 0.04 | 1143429.13 | 1.05 | skipped_fast |
| PYTHUSDT | IDLE | 1.84 | 3.73 | 0.42 | -0.02 | 751543.2 | 3.15 | skipped_fast |
| CHIPUSDT | IDLE | 3.67 | 6.86 | 3.19 | -0.01 | 165668.05 | 17.08 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.56 | 1.94 | 0.02 | 567244.01 | 11.06 | skipped_fast |
| EDELUSDT | IDLE | 1.82 | 8.39 | 2.91 | 0.14 | 244644.74 | 5.98 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.89 | 0.49 | -0.01 | 373345.29 | 7.52 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.11 | 8.12 | 0.74 | 0.11 | 116564.98 | 17.75 | skipped_fast |
| REDUSDT | IDLE | 2.36 | 4.35 | 2.46 | 0.02 | 67201.57 | 15.39 | skipped_fast |
| ZBCNUSDT | IDLE | 1.56 | 2.87 | 1.73 | -0.03 | 265480.97 | 30.14 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.45 | 10.74 | 0.35 | 0.09 | 171335.7 | 83.76 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.78 | 0.17 | -0.0 | 124684.04 | 3.43 | skipped_fast |
| TELUSDT | IDLE | 2.34 | 4.65 | 0.24 | 0.02 | 107650.5 | 6.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 2.18 | 1.04 | 0.06 | 27309.74 | 33.24 | skipped_fast |
| RIZEUSDT | IDLE | 0.35 | 3.26 | 1.56 | -0.14 | 46106.77 | 71.86 | skipped_fast |
| FLUIDUSDT | IDLE | 1.11 | 2.07 | 1.04 | 0.02 | 8571.82 | 21.88 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.95 | 0.44 | -0.0 | 55238.34 | 21.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.4 | 0.05 | 0.01 | 40333.79 | 7.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
