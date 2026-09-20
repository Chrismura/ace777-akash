# Hulk DIGEST — 2026-09-20T16:02:59Z

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
| HBARUSDT | IDLE | 3.94 | 12.31 | 4.0 | 0.07 | 1225474.18 | 3.47 | skipped_fast |
| ETHUSDT | IDLE | 0.95 | 1.85 | 0.28 | -0.01 | 250987952.83 | 0.42 | skipped_fast |
| XRPUSDT | IDLE | 0.67 | 1.3 | 0.2 | -0.03 | 42443796.31 | 0.72 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.86 | 0.14 | -0.01 | 451091867.84 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.62 | 5.35 | 0.28 | -0.0 | 647274.49 | 6.62 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 5.91 | 3.75 | 0.01 | 198130.78 | 9.37 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.38 | 11.12 | 0.93 | 0.01 | 69994.31 | 42.07 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 3.62 | 0.13 | -0.04 | 378365.07 | 8.42 | skipped_fast |
| WUSDT | IDLE | 1.25 | 2.47 | 0.17 | -0.01 | 369368.66 | 8.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.77 | 3.6 | 1.35 | -0.04 | 86777.52 | 16.87 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 3.05 | 2.24 | 0.01 | 76176.96 | 22.13 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 1.84 | 0.33 | -0.05 | 78616.39 | 11.1 | skipped_fast |
| KITEUSDT | IDLE | 0.96 | 1.84 | 0.55 | -0.02 | 67654.16 | 9.75 | skipped_fast |
| RWAINCUSDT | IDLE | 1.05 | 2.04 | 0.35 | 0.04 | 9801.18 | 23.61 | skipped_fast |
| TELUSDT | IDLE | 1.69 | 3.36 | 0.2 | -0.02 | 93715.2 | 39.95 | skipped_fast |
| RIZEUSDT | IDLE | 0.83 | 2.22 | 0.0 | -0.04 | 26928.67 | 78.54 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 1.57 | 0.0 | -0.01 | 57875.98 | 1.55 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.82 | 0.3 | -0.01 | 52809.49 | 37.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.7 | 0.09 | -0.06 | 1854.35 | 21.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.69 | 0.29 | -0.0 | 35780.89 | 69.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
