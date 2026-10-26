# Hulk DIGEST — 2026-10-26T16:24:54Z

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
| ETHUSDT | IDLE | 1.13 | 2.11 | 0.98 | -0.01 | 137002978.84 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 2.01 | 1.03 | -0.0 | 23745360.51 | 2.32 | skipped_fast |
| BTCUSDT | IDLE | 0.9 | 1.69 | 0.78 | -0.0 | 332699339.04 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.75 | 7.44 | 6.26 | 0.13 | 1474903.24 | 3.34 | skipped_fast |
| PYTHUSDT | IDLE | 1.99 | 3.76 | 1.46 | 0.06 | 936885.19 | 3.95 | skipped_fast |
| WUSDT | IDLE | 3.04 | 5.96 | 0.74 | 0.02 | 580700.53 | 30.06 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.36 | 13.6 | 1.54 | 0.17 | 225595.37 | 26.97 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.7 | 4.14 | -0.08 | 61451.97 | 6.03 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.05 | 1.4 | -0.03 | 215477.64 | 32.95 | skipped_fast |
| BIOUSDT | IDLE | 1.77 | 3.28 | 1.68 | -0.0 | 59784.18 | 8.96 | skipped_fast |
| REDUSDT | IDLE | 1.62 | 2.98 | 1.69 | 0.03 | 62861.43 | 16.35 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.74 | 1.11 | -0.02 | 188595.23 | 10.95 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 3.4 | 0.37 | 0.09 | 131408.06 | 33.61 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 2.63 | 1.48 | 0.01 | 53562.39 | 11.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 3.33 | 0.75 | 0.01 | 34461.01 | 64.04 | skipped_fast |
| LAUSDT | IDLE | 1.78 | 3.75 | 0.92 | 0.03 | 66784.04 | 18.69 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.61 | 1.46 | -0.0 | 233135.44 | 7.8 | skipped_fast |
| WAXLUSDT | IDLE | 2.05 | 4.01 | 0.57 | -0.02 | 53326.74 | 56.92 | skipped_fast |
| IOTAUSDT | IDLE | 1.33 | 2.44 | 1.41 | -0.01 | 74044.86 | 21.11 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.99 | 0.34 | -0.02 | 1706.2 | 21.25 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.44 | 0.71 | -0.0 | 54784.85 | 31.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.74 | 0.35 | -0.01 | 42681.58 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
