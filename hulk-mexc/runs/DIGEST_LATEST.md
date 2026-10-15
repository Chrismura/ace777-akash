# Hulk DIGEST — 2026-10-15T16:14:03Z

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
| PYTHUSDT | IDLE | 3.94 | 25.14 | 3.64 | 0.22 | 4033513.81 | 10.28 | skipped_fast |
| WUSDT | IDLE | 2.51 | 7.78 | 0.58 | 0.0 | 2681785.29 | 19.36 | skipped_fast |
| ETHUSDT | IDLE | 2.66 | 5.29 | 0.19 | 0.01 | 342423728.87 | 0.7 | skipped_fast |
| XRPUSDT | IDLE | 2.41 | 4.76 | 0.4 | 0.01 | 54019216.71 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 1.75 | 3.48 | 0.13 | 0.01 | 497332911.99 | 0.0 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.58 | 9.55 | 0.85 | 0.0 | 1183181.78 | 6.2 | skipped_fast |
| REDUSDT | IDLE | 4.12 | 13.25 | 2.55 | 0.06 | 73829.42 | 10.58 | skipped_fast |
| ZBCNUSDT | IDLE | 3.32 | 6.62 | 0.17 | 0.01 | 196558.48 | 20.49 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 4.95 | 0.51 | -0.07 | 451524.97 | 5.46 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 12.89 | 1.27 | -0.1 | 145057.74 | 4.22 | skipped_fast |
| EDELUSDT | IDLE | 1.91 | 6.7 | 1.01 | -0.06 | 221541.02 | 15.85 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 6.87 | 0.31 | -0.02 | 88008.55 | 7.72 | skipped_fast |
| KITEUSDT | IDLE | 2.4 | 7.56 | 1.26 | -0.03 | 68527.63 | 18.43 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 8.24 | 1.04 | 0.13 | 27243.72 | 28.61 | skipped_fast |
| HBARUSDT | IDLE | 2.14 | 4.27 | 0.1 | -0.0 | 370906.97 | 4.78 | skipped_fast |
| TELUSDT | IDLE | 2.72 | 6.61 | 0.68 | -0.01 | 96433.61 | 22.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.42 | 5.51 | 2.17 | 0.02 | 64359.25 | 33.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.95 | 5.11 | 0.4 | -0.01 | 16632.23 | 19.28 | skipped_fast |
| MNSRYUSDT | IDLE | 1.46 | 2.77 | 1.05 | -0.01 | 31591.1 | 43.7 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.86 | 0.48 | -0.0 | 55375.35 | 15.95 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
