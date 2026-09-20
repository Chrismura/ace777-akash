# Hulk DIGEST — 2026-09-20T15:02:57Z

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
| ETHUSDT | IDLE | 0.68 | 1.36 | 0.0 | -0.02 | 243002945.1 | 1.84 | skipped_fast |
| XRPUSDT | IDLE | 0.43 | 0.86 | 0.0 | -0.04 | 42448330.24 | 0.72 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.73 | 0.01 | -0.01 | 471337074.8 | 1.39 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.79 | 11.42 | 0.19 | 0.1 | 1056041.55 | 7.86 | skipped_fast |
| PYTHUSDT | IDLE | 1.76 | 3.59 | 0.22 | -0.01 | 683789.13 | 6.74 | skipped_fast |
| EDELUSDT | IDLE | 3.2 | 9.83 | 4.73 | -0.04 | 66418.1 | 68.8 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 3.47 | 0.01 | -0.05 | 370260.85 | 9.39 | skipped_fast |
| WUSDT | IDLE | 1.2 | 2.29 | 0.69 | -0.02 | 374720.38 | 6.44 | skipped_fast |
| REDUSDT | IDLE | 2.19 | 4.0 | 2.59 | -0.0 | 74690.96 | 10.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.39 | 3.94 | 0.47 | 0.03 | 207212.16 | 24.63 | skipped_fast |
| CHIPUSDT | IDLE | 1.47 | 2.95 | 1.41 | -0.06 | 86792.12 | 16.99 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.84 | 0.79 | -0.03 | 67869.85 | 12.42 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.32 | 0.22 | -0.05 | 79054.45 | 11.15 | skipped_fast |
| RWAINCUSDT | IDLE | 1.02 | 2.04 | 0.06 | 0.05 | 9718.2 | 35.44 | skipped_fast |
| RIZEUSDT | IDLE | 0.81 | 2.44 | 0.32 | -0.06 | 34209.43 | 78.54 | skipped_fast |
| TELUSDT | IDLE | 0.86 | 1.72 | 0.0 | -0.04 | 94371.64 | 40.49 | skipped_fast |
| QNTUSDT | IDLE | 0.65 | 1.2 | 0.66 | -0.03 | 55593.4 | 9.42 | skipped_fast |
| FLUIDUSDT | IDLE | 0.55 | 0.96 | 0.95 | -0.06 | 1964.21 | 21.09 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.69 | 0.58 | -0.01 | 35560.81 | 43.95 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.82 | 0.37 | -0.02 | 52913.35 | 66.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
