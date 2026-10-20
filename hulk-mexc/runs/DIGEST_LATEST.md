# Hulk DIGEST — 2026-10-20T20:25:22Z

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
| XRPUSDT | IDLE | 1.4 | 2.63 | 1.18 | 0.02 | 23850057.22 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 1.94 | 1.46 | 0.01 | 148690808.7 | 0.74 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.32 | 0.85 | 0.01 | 318990344.38 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.41 | 6.77 | 1.0 | 0.09 | 1128208.47 | 2.52 | skipped_fast |
| WUSDT | IDLE | 2.32 | 4.43 | 1.43 | 0.01 | 664683.02 | 15.83 | skipped_fast |
| QNTUSDT | IDLE | 2.69 | 4.78 | 4.06 | -0.01 | 781449.2 | 1.55 | skipped_fast |
| EDELUSDT | IDLE | 1.1 | 10.16 | 3.47 | 0.31 | 362570.96 | 22.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 5.69 | 3.9 | 0.06 | 284324.73 | 15.7 | skipped_fast |
| ZBCNUSDT | IDLE | 2.24 | 4.0 | 3.14 | 0.02 | 189876.19 | 18.45 | skipped_fast |
| CCUSDT | IDLE | 1.17 | 2.1 | 1.59 | 0.01 | 382363.98 | 8.57 | skipped_fast |
| HBARUSDT | IDLE | 1.98 | 3.58 | 2.53 | 0.01 | 370411.45 | 2.4 | skipped_fast |
| REDUSDT | IDLE | 1.79 | 3.3 | 1.93 | 0.02 | 59697.32 | 17.19 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 2.97 | 1.56 | 0.05 | 63002.46 | 4.07 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 2.23 | 2.03 | 0.0 | 82593.78 | 10.68 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 3.73 | 1.09 | -0.02 | 67457.34 | 5.26 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 4.88 | 0.15 | 0.04 | 69215.33 | 26.37 | skipped_fast |
| IOTAUSDT | IDLE | 2.28 | 4.14 | 2.83 | 0.04 | 72506.75 | 30.01 | skipped_fast |
| WAXLUSDT | IDLE | 2.2 | 3.85 | 3.65 | -0.05 | 56087.38 | 26.29 | skipped_fast |
| LAUSDT | IDLE | 1.38 | 2.57 | 1.23 | 0.03 | 56259.58 | 18.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.25 | 2.5 | 0.0 | 0.07 | 6257.9 | 21.98 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.79 | 0.23 | 0.0 | 52335.28 | 7.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.48 | 0.0 | 40129.96 | 22.8 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
