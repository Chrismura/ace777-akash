# Hulk DIGEST — 2026-10-13T02:54:08Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 8.76 | 1.18 | 0.04 | 3759217.38 | 1.19 | skipped_fast |
| WUSDT | IDLE | 0.72 | 11.65 | 9.75 | -0.36 | 13997559.55 | 12.45 | skipped_fast |
| ETHUSDT | IDLE | 2.38 | 4.55 | 1.37 | -0.02 | 279446576.12 | 0.28 | skipped_fast |
| XRPUSDT | IDLE | 2.09 | 4.31 | 0.34 | -0.03 | 36356273.41 | 1.47 | skipped_fast |
| BTCUSDT | IDLE | 1.29 | 2.54 | 0.26 | -0.01 | 346821807.31 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.2 | 6.0 | 1.74 | -0.04 | 826082.85 | 1.76 | skipped_fast |
| CCUSDT | IDLE | 2.42 | 5.58 | 1.13 | -0.04 | 417839.69 | 10.72 | skipped_fast |
| HBARUSDT | IDLE | 2.15 | 6.54 | 2.96 | -0.07 | 644959.75 | 8.03 | skipped_fast |
| BIOUSDT | IDLE | 2.43 | 8.78 | 4.2 | -0.09 | 75654.86 | 3.68 | skipped_fast |
| KITEUSDT | IDLE | 2.62 | 7.13 | 3.24 | -0.04 | 67109.32 | 11.33 | skipped_fast |
| EDELUSDT | IDLE | 1.53 | 6.64 | 4.42 | -0.13 | 296611.36 | 21.29 | skipped_fast |
| REDUSDT | IDLE | 1.25 | 8.52 | 4.8 | 0.01 | 281542.11 | 14.45 | skipped_fast |
| ZBCNUSDT | IDLE | 1.69 | 3.34 | 0.24 | -0.02 | 248434.48 | 19.76 | skipped_fast |
| CHIPUSDT | IDLE | 1.47 | 7.46 | 1.3 | -0.11 | 165989.63 | 6.78 | skipped_fast |
| FLUIDUSDT | IDLE | 2.98 | 5.78 | 1.23 | 0.02 | 14271.36 | 21.16 | skipped_fast |
| RIZEUSDT | IDLE | 1.11 | 7.24 | 2.55 | -0.05 | 74111.08 | 40.05 | skipped_fast |
| TELUSDT | IDLE | 2.23 | 4.18 | 1.92 | 0.0 | 118043.14 | 28.79 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 2.9 | 2.33 | 0.0 | 37576.31 | 39.72 | skipped_fast |
| MNSRYUSDT | IDLE | 1.52 | 2.74 | 2.03 | -0.02 | 40585.68 | 20.94 | skipped_fast |
| RWAUSDT | IDLE | 0.95 | 1.81 | 0.54 | -0.0 | 52831.41 | 7.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
