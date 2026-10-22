# Hulk DIGEST — 2026-10-22T14:32:33Z

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
| WUSDT | IDLE | 0.83 | 4.01 | 3.36 | -0.12 | 2564478.81 | 14.25 | skipped_fast |
| XRPUSDT | IDLE | 0.66 | 1.18 | 0.9 | -0.03 | 31430210.51 | 1.51 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.96 | 0.54 | -0.03 | 528513695.28 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.49 | 0.91 | 0.49 | -0.03 | 210280449.93 | 0.25 | skipped_fast |
| EDELUSDT | IDLE | 2.85 | 5.91 | 4.85 | -0.06 | 540363.29 | 9.27 | skipped_fast |
| HBARUSDT | IDLE | 0.69 | 1.24 | 0.98 | -0.05 | 1326818.97 | 4.96 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.08 | 1.35 | -0.01 | 1246739.72 | 2.57 | skipped_fast |
| PYTHUSDT | IDLE | 1.07 | 2.99 | 1.45 | -0.07 | 627344.57 | 2.68 | skipped_fast |
| ZBCNUSDT | IDLE | 2.21 | 6.18 | 1.76 | -0.03 | 223910.53 | 19.95 | skipped_fast |
| RWAINCUSDT | IDLE | 2.34 | 4.49 | 1.27 | -0.0 | 63070.22 | 5.58 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 2.96 | 2.42 | -0.04 | 339700.92 | 6.83 | skipped_fast |
| CHIPUSDT | IDLE | 0.61 | 2.6 | 1.13 | -0.05 | 338459.62 | 16.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.64 | 4.32 | 0.6 | 0.06 | 43677.78 | 55.76 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.77 | 1.04 | -0.05 | 75939.6 | 12.56 | skipped_fast |
| REDUSDT | IDLE | 0.85 | 1.69 | 0.85 | -0.05 | 84892.86 | 16.88 | skipped_fast |
| KITEUSDT | IDLE | 0.86 | 1.65 | 0.43 | -0.02 | 60529.71 | 10.82 | skipped_fast |
| WAXLUSDT | IDLE | 0.92 | 3.1 | 2.58 | -0.09 | 58688.3 | 35.17 | skipped_fast |
| LAUSDT | IDLE | 0.74 | 1.91 | 1.36 | -0.06 | 57148.43 | 23.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 3.5 | 3.38 | -0.04 | 20280.5 | 21.42 | skipped_fast |
| IOTAUSDT | IDLE | 0.66 | 1.34 | 0.68 | -0.04 | 79527.89 | 28.85 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 0.95 | 0.87 | -0.01 | 52488.17 | 39.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.53 | 0.5 | -0.0 | 39891.82 | 55.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
