# Hulk DIGEST — 2026-09-01T20:24:39Z

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
| XRPUSDT | IDLE | 1.77 | 3.21 | 2.2 | -0.03 | 33507509.12 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 1.6 | 2.98 | 1.43 | -0.03 | 326498561.11 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.22 | 2.29 | 1.0 | -0.02 | 535526111.37 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.08 | 3.94 | 1.44 | 0.03 | 647363.37 | 3.96 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.05 | 10.09 | 0.09 | 0.17 | 573301.22 | 6.61 | skipped_fast |
| ZBCNUSDT | IDLE | 3.44 | 6.37 | 3.41 | 0.02 | 201467.52 | 17.54 | skipped_fast |
| CCUSDT | IDLE | 1.72 | 3.62 | 3.07 | -0.09 | 351226.25 | 9.66 | skipped_fast |
| WUSDT | IDLE | 1.72 | 3.61 | 0.56 | 0.08 | 355482.42 | 23.38 | skipped_fast |
| REDUSDT | IDLE | 2.08 | 6.24 | 5.06 | 0.05 | 109469.65 | 14.25 | skipped_fast |
| RIZEUSDT | IDLE | 2.6 | 4.92 | 2.85 | -0.04 | 44412.99 | 71.98 | skipped_fast |
| BIOUSDT | IDLE | 1.81 | 3.31 | 2.13 | -0.03 | 70775.45 | 3.9 | skipped_fast |
| KITEUSDT | IDLE | 1.56 | 3.03 | 0.57 | 0.03 | 69020.72 | 12.96 | skipped_fast |
| EDELUSDT | IDLE | 0.95 | 7.1 | 5.6 | -0.05 | 171911.63 | 63.55 | skipped_fast |
| TELUSDT | IDLE | 2.85 | 5.08 | 4.19 | -0.06 | 94730.79 | 60.68 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.74 | 0.17 | -0.0 | 6678.44 | 17.39 | skipped_fast |
| FLUIDUSDT | IDLE | 2.52 | 4.41 | 4.22 | -0.03 | 129.84 | 22.57 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.74 | 0.21 | 0.01 | 249364.62 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 1.31 | 2.4 | 1.52 | 0.03 | 47860.18 | 4.73 | skipped_fast |
| MNSRYUSDT | IDLE | 0.93 | 1.71 | 1.02 | -0.02 | 34017.45 | 19.2 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 1.01 | 0.84 | -0.02 | 59529.84 | 23.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
