# Hulk DIGEST — 2026-10-25T07:59:24Z

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
| XRPUSDT | IDLE | 0.89 | 1.62 | 1.09 | 0.01 | 26609919.38 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.82 | 1.49 | 1.02 | -0.01 | 126513466.0 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.73 | 0.42 | -0.0 | 214500817.93 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.07 | 2.01 | 0.93 | -0.04 | 837964.56 | 11.48 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 2.41 | 1.53 | 0.0 | 496588.52 | 1.41 | skipped_fast |
| EDELUSDT | IDLE | 0.87 | 2.01 | 1.77 | -0.07 | 586667.81 | 26.75 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 2.7 | 1.74 | 0.01 | 381379.59 | 1.64 | skipped_fast |
| KITEUSDT | IDLE | 1.62 | 2.84 | 2.64 | -0.05 | 58740.49 | 14.3 | skipped_fast |
| CCUSDT | IDLE | 0.86 | 1.59 | 0.89 | -0.03 | 203325.23 | 7.94 | skipped_fast |
| RWAINCUSDT | IDLE | 1.43 | 2.59 | 1.77 | -0.02 | 57598.47 | 5.47 | skipped_fast |
| BIOUSDT | IDLE | 1.2 | 2.1 | 2.01 | -0.03 | 63929.22 | 4.46 | skipped_fast |
| ZBCNUSDT | IDLE | 0.65 | 1.52 | 0.51 | 0.02 | 234520.21 | 23.54 | skipped_fast |
| CHIPUSDT | IDLE | 1.03 | 2.95 | 2.34 | 0.06 | 89641.84 | 18.05 | skipped_fast |
| WAXLUSDT | IDLE | 2.7 | 5.02 | 4.46 | -0.01 | 55866.39 | 66.93 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 2.21 | 1.55 | -0.02 | 80965.46 | 16.33 | skipped_fast |
| LAUSDT | IDLE | 1.23 | 7.27 | 6.78 | -0.11 | 95320.51 | 22.67 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 1.98 | 1.16 | 0.01 | 217846.19 | 6.43 | skipped_fast |
| RIZEUSDT | IDLE | 0.32 | 0.91 | 0.25 | -0.04 | 41402.36 | 62.39 | skipped_fast |
| IOTAUSDT | IDLE | 0.95 | 1.69 | 1.39 | -0.01 | 65359.39 | 29.99 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 1.28 | 1.27 | -0.03 | 8292.83 | 21.38 | skipped_fast |
| RWAUSDT | IDLE | 0.78 | 1.52 | 0.31 | 0.0 | 52678.4 | 47.28 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.76 | 0.32 | -0.01 | 37439.64 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
