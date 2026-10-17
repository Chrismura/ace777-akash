# Hulk DIGEST — 2026-10-17T20:22:16Z

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
| ETHUSDT | IDLE | 0.62 | 1.18 | 0.38 | 0.0 | 78731231.21 | 0.17 | skipped_fast |
| XRPUSDT | IDLE | 0.61 | 1.18 | 0.22 | -0.0 | 13780476.81 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.29 | 0.57 | 0.05 | -0.0 | 168037498.3 | 0.02 | skipped_fast |
| PYTHUSDT | IDLE | 2.45 | 6.26 | 1.93 | -0.01 | 1019757.82 | 1.2 | skipped_fast |
| WUSDT | IDLE | 1.78 | 5.3 | 1.89 | -0.0 | 1082259.17 | 14.29 | skipped_fast |
| QNTUSDT | IDLE | 1.93 | 3.62 | 1.54 | -0.01 | 541379.28 | 0.5 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 2.28 | 0.53 | 0.02 | 248623.84 | 11.43 | skipped_fast |
| EDELUSDT | IDLE | 1.31 | 2.37 | 1.62 | -0.03 | 147906.3 | 7.03 | skipped_fast |
| ZBCNUSDT | IDLE | 1.24 | 2.45 | 0.14 | -0.02 | 194495.84 | 17.18 | skipped_fast |
| HBARUSDT | IDLE | 2.27 | 4.36 | 1.25 | 0.02 | 199880.58 | 8.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.47 | 2.66 | 1.83 | -0.03 | 85575.64 | 15.95 | skipped_fast |
| BIOUSDT | IDLE | 1.34 | 2.62 | 0.41 | -0.02 | 71748.85 | 4.08 | skipped_fast |
| RWAINCUSDT | IDLE | 1.2 | 4.48 | 0.21 | 0.11 | 21496.81 | 10.36 | skipped_fast |
| RIZEUSDT | IDLE | 1.5 | 2.8 | 1.37 | -0.04 | 50610.66 | 59.03 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.83 | 1.27 | -0.02 | 66008.21 | 9.38 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.78 | 0.61 | -0.01 | 59827.9 | 10.68 | skipped_fast |
| TELUSDT | IDLE | 1.66 | 3.11 | 1.42 | -0.05 | 97800.27 | 18.01 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.2 | 0.67 | 0.02 | 2258.26 | 21.39 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.96 | 0.63 | 0.0 | 50826.01 | 15.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.56 | 1.12 | 0.04 | 0.01 | 30836.18 | 9.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
