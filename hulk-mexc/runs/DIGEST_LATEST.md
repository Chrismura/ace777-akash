# Hulk DIGEST — 2026-09-23T06:17:52Z

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
| XRPUSDT | IDLE | 2.32 | 5.31 | 2.33 | 0.07 | 115423296.84 | 1.85 | skipped_fast |
| PYTHUSDT | IDLE | 0.63 | 3.06 | 0.56 | 0.06 | 1768130.41 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.83 | 1.52 | 0.95 | 0.01 | 409426313.23 | 0.11 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.29 | 0.77 | 0.02 | 870560285.27 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 2.82 | 1.98 | 0.07 | 1798441.51 | 1.01 | skipped_fast |
| ZBCNUSDT | IDLE | 3.51 | 8.81 | 2.18 | 0.06 | 223249.19 | 22.83 | skipped_fast |
| WUSDT | IDLE | 1.91 | 3.68 | 0.87 | 0.03 | 318776.94 | 5.67 | skipped_fast |
| CCUSDT | IDLE | 1.53 | 2.97 | 0.64 | -0.02 | 411584.59 | 9.5 | skipped_fast |
| KITEUSDT | IDLE | 1.49 | 4.42 | 3.76 | 0.09 | 130796.13 | 8.08 | skipped_fast |
| CHIPUSDT | IDLE | 1.36 | 2.65 | 1.42 | -0.02 | 204030.25 | 8.58 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 3.38 | 0.46 | 0.06 | 112140.16 | 9.84 | skipped_fast |
| EDELUSDT | IDLE | 0.86 | 4.25 | 1.2 | -0.03 | 267197.77 | 19.63 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 2.68 | 0.11 | 0.03 | 59909.87 | 13.66 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 14.58 | 7.62 | 0.42 | 57921.21 | 93.12 | skipped_fast |
| QNTUSDT | IDLE | 0.9 | 2.9 | 1.81 | 0.11 | 215826.83 | 5.34 | skipped_fast |
| RWAINCUSDT | IDLE | 0.72 | 1.84 | 0.85 | 0.04 | 22674.42 | 69.76 | skipped_fast |
| FLUIDUSDT | IDLE | 1.3 | 2.42 | 1.17 | 0.02 | 4334.0 | 21.69 | skipped_fast |
| TELUSDT | IDLE | 0.72 | 3.08 | 1.28 | 0.15 | 109798.57 | 48.53 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.8 | 0.43 | 0.01 | 53374.73 | 21.64 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.72 | 0.04 | 0.01 | 39347.72 | 6.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
