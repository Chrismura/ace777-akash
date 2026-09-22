# Hulk DIGEST — 2026-09-22T09:09:17Z

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
| XRPUSDT | IDLE | 2.14 | 4.09 | 1.33 | 0.04 | 115056549.79 | 3.26 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.47 | 0.57 | 0.02 | 1148927518.35 | 0.21 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.44 | 0.64 | 0.01 | 674686830.39 | 0.22 | skipped_fast |
| HBARUSDT | IDLE | 2.66 | 6.9 | 1.08 | 0.1 | 1380318.66 | 2.07 | skipped_fast |
| PYTHUSDT | IDLE | 2.01 | 3.6 | 2.81 | -0.02 | 822348.94 | 4.79 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 2.65 | 1.85 | 0.03 | 661907.66 | 5.95 | skipped_fast |
| WUSDT | IDLE | 1.58 | 2.97 | 1.26 | -0.01 | 421586.76 | 8.47 | skipped_fast |
| KITEUSDT | IDLE | 2.83 | 7.18 | 1.24 | 0.08 | 101258.44 | 8.59 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.15 | 3.13 | 0.03 | 180454.87 | 14.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.69 | 3.17 | 1.39 | 0.01 | 275629.66 | 48.68 | skipped_fast |
| REDUSDT | IDLE | 2.09 | 4.04 | 0.91 | 0.03 | 95176.76 | 22.16 | skipped_fast |
| EDELUSDT | IDLE | 1.16 | 6.51 | 1.25 | 0.14 | 230838.72 | 21.66 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.56 | 1.61 | 0.0 | 129534.1 | 10.44 | skipped_fast |
| RIZEUSDT | IDLE | 1.24 | 12.71 | 0.9 | -0.15 | 49938.16 | 124.22 | skipped_fast |
| RWAINCUSDT | IDLE | 0.72 | 1.51 | 1.43 | 0.06 | 25510.47 | 22.38 | skipped_fast |
| TELUSDT | IDLE | 1.73 | 3.15 | 2.02 | 0.02 | 114677.21 | 49.72 | skipped_fast |
| QNTUSDT | IDLE | 1.32 | 2.46 | 1.16 | 0.01 | 121000.58 | 5.96 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.88 | 0.65 | 0.01 | 56130.12 | 14.59 | skipped_fast |
| FLUIDUSDT | IDLE | 0.66 | 1.31 | 0.0 | 0.05 | 12485.67 | 21.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.36 | 0.13 | 0.01 | 40483.44 | 11.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
