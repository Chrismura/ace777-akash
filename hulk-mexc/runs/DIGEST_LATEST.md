# Hulk DIGEST — 2026-10-26T11:20:16Z

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
| XRPUSDT | IDLE | 0.83 | 1.59 | 0.5 | -0.01 | 19967994.4 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.45 | 0.56 | -0.0 | 111169883.18 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.11 | 0.36 | -0.0 | 230702481.04 | 0.0 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.55 | 11.64 | 0.0 | 0.18 | 1133501.34 | 14.89 | skipped_fast |
| PYTHUSDT | IDLE | 1.98 | 3.92 | 0.24 | 0.06 | 831927.26 | 3.98 | skipped_fast |
| WUSDT | IDLE | 1.69 | 3.06 | 2.16 | -0.02 | 495511.62 | 18.77 | skipped_fast |
| ZBCNUSDT | IDLE | 2.44 | 5.29 | 4.47 | -0.01 | 220399.08 | 4.26 | skipped_fast |
| CHIPUSDT | IDLE | 2.23 | 6.29 | 1.74 | 0.04 | 112886.24 | 12.82 | skipped_fast |
| REDUSDT | IDLE | 2.04 | 4.01 | 0.52 | 0.03 | 60558.79 | 23.77 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.77 | 0.98 | 0.01 | 165227.19 | 8.89 | skipped_fast |
| EDELUSDT | IDLE | 1.08 | 2.57 | 1.42 | 0.09 | 132932.23 | 25.01 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 2.29 | 1.07 | -0.0 | 59728.37 | 9.04 | skipped_fast |
| LAUSDT | IDLE | 2.19 | 4.34 | 2.83 | 0.01 | 65814.99 | 1.73 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 2.0 | 0.82 | 0.01 | 54175.59 | 11.57 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.65 | 1.28 | -0.07 | 67638.71 | 23.47 | skipped_fast |
| MNSRYUSDT | IDLE | 2.39 | 4.38 | 2.73 | -0.01 | 41397.59 | 76.46 | skipped_fast |
| WAXLUSDT | IDLE | 2.01 | 3.74 | 1.91 | -0.01 | 51838.49 | 44.1 | skipped_fast |
| RIZEUSDT | IDLE | 0.57 | 1.09 | 0.3 | 0.01 | 33236.98 | 27.5 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.78 | 0.42 | 0.01 | 174865.25 | 1.29 | skipped_fast |
| IOTAUSDT | IDLE | 1.12 | 2.1 | 0.94 | -0.01 | 64396.2 | 30.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.24 | 0.86 | 0.86 | -0.03 | 19098.64 | 21.33 | skipped_fast |
| RWAUSDT | IDLE | 0.12 | 0.24 | 0.0 | -0.0 | 53611.92 | 23.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
