# Hulk DIGEST — 2026-10-17T08:16:06Z

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
| WUSDT | IDLE | 3.41 | 6.49 | 2.22 | -0.02 | 1268230.38 | 19.74 | skipped_fast |
| PYTHUSDT | IDLE | 0.93 | 2.74 | 1.94 | -0.1 | 1626599.95 | 2.37 | skipped_fast |
| ETHUSDT | IDLE | 0.38 | 0.74 | 0.11 | -0.01 | 180046928.61 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.35 | 0.66 | 0.3 | -0.02 | 23830755.32 | 0.76 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.4 | 0.03 | -0.01 | 299046873.07 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.33 | 5.81 | 1.75 | -0.03 | 210872.49 | 14.35 | skipped_fast |
| QNTUSDT | IDLE | 1.44 | 2.71 | 1.17 | -0.02 | 712631.04 | 1.48 | skipped_fast |
| KITEUSDT | IDLE | 2.63 | 4.81 | 3.04 | 0.0 | 57218.11 | 9.79 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 1.82 | 1.12 | -0.02 | 350666.4 | 9.64 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 2.31 | 1.82 | -0.02 | 176604.12 | 17.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.57 | 6.3 | 2.15 | -0.1 | 24039.74 | 10.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.45 | 3.14 | 2.13 | -0.04 | 50887.75 | 46.84 | skipped_fast |
| CHIPUSDT | IDLE | 0.87 | 2.43 | 1.0 | -0.06 | 108393.33 | 12.94 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 1.85 | 1.42 | -0.04 | 74415.49 | 15.44 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.49 | 1.27 | -0.04 | 65167.16 | 4.02 | skipped_fast |
| HBARUSDT | IDLE | 0.49 | 0.91 | 0.49 | -0.03 | 312849.83 | 8.33 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 1.89 | 1.79 | -0.05 | 85359.3 | 23.56 | skipped_fast |
| FLUIDUSDT | IDLE | 0.8 | 1.54 | 0.41 | 0.02 | 4136.5 | 21.46 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.88 | 0.32 | -0.01 | 51480.94 | 15.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.28 | 0.13 | -0.0 | 29449.78 | 7.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
