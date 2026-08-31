# Hulk DIGEST — 2026-08-31T13:17:31Z

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
| XRPUSDT | IDLE | 1.04 | 1.91 | 1.11 | -0.02 | 39956719.44 | 2.19 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.43 | 0.92 | -0.01 | 533355634.54 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.24 | 0.39 | -0.0 | 441825981.14 | 0.37 | skipped_fast |
| CHIPUSDT | IDLE | 2.09 | 6.29 | 4.56 | -0.02 | 590903.2 | 2.5 | skipped_fast |
| PYTHUSDT | IDLE | 1.6 | 3.74 | 2.48 | -0.03 | 514875.72 | 2.14 | skipped_fast |
| WUSDT | IDLE | 1.72 | 3.14 | 2.41 | -0.03 | 236455.73 | 6.55 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.44 | 1.69 | 0.0 | 238094.41 | 9.24 | skipped_fast |
| REDUSDT | IDLE | 2.0 | 3.55 | 2.94 | -0.03 | 70660.78 | 13.96 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.49 | 2.02 | -0.05 | 84849.37 | 3.81 | skipped_fast |
| ZBCNUSDT | IDLE | 0.94 | 2.36 | 0.56 | -0.08 | 232446.14 | 24.97 | skipped_fast |
| KITEUSDT | IDLE | 0.87 | 2.23 | 1.63 | -0.06 | 98304.69 | 10.86 | skipped_fast |
| QNTUSDT | IDLE | 2.07 | 3.9 | 1.58 | -0.0 | 48758.44 | 3.25 | skipped_fast |
| EDELUSDT | IDLE | 0.39 | 2.43 | 1.63 | -0.02 | 121249.4 | 16.6 | skipped_fast |
| RIZEUSDT | IDLE | 1.26 | 2.42 | 0.64 | -0.01 | 34163.72 | 61.74 | skipped_fast |
| RWAUSDT | IDLE | 1.9 | 3.8 | 0.0 | 0.04 | 54245.71 | 31.25 | skipped_fast |
| RWAINCUSDT | IDLE | 1.35 | 2.35 | 2.29 | -0.01 | 2854.64 | 113.83 | skipped_fast |
| HBARUSDT | IDLE | 0.58 | 1.06 | 0.72 | -0.02 | 250371.38 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.16 | 2.06 | 1.78 | 0.01 | 90317.27 | 58.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.52 | 1.5 | -0.0 | 1743.97 | 0.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.54 | 0.08 | -0.01 | 27175.51 | 23.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
