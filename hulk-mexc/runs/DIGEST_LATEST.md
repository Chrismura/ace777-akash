# Hulk DIGEST — 2026-10-19T20:56:18Z

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
| ETHUSDT | IDLE | 0.76 | 1.39 | 0.88 | 0.02 | 141594158.09 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.69 | 1.25 | 0.82 | 0.03 | 23848054.51 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.53 | 0.96 | 0.67 | 0.01 | 349799667.0 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.53 | 4.47 | 3.95 | 0.0 | 895957.51 | 2.78 | skipped_fast |
| WUSDT | IDLE | 2.79 | 5.03 | 3.73 | 0.03 | 692563.49 | 9.23 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 3.59 | 2.75 | 0.05 | 728472.87 | 3.61 | skipped_fast |
| RIZEUSDT | IDLE | 3.04 | 10.48 | 3.95 | -0.05 | 53317.49 | 45.95 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.95 | 2.2 | 0.06 | 416026.37 | 7.72 | skipped_fast |
| EDELUSDT | IDLE | 1.51 | 2.9 | 2.27 | 0.03 | 207241.71 | 26.22 | skipped_fast |
| ZBCNUSDT | IDLE | 0.93 | 3.11 | 2.94 | 0.01 | 251887.81 | 15.47 | skipped_fast |
| REDUSDT | IDLE | 1.58 | 2.87 | 1.93 | 0.03 | 57713.56 | 0.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.42 | 3.63 | 2.06 | 0.06 | 78818.22 | 12.08 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.48 | 1.31 | -0.01 | 517637.23 | 7.33 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 3.65 | 2.02 | 0.09 | 68437.03 | 10.7 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.07 | 1.48 | 0.03 | 69310.05 | 4.29 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 2.33 | 1.72 | 0.05 | 78400.96 | 30.85 | skipped_fast |
| LAUSDT | IDLE | 1.14 | 2.07 | 1.44 | 0.03 | 56438.4 | 19.21 | skipped_fast |
| IOTAUSDT | IDLE | 0.85 | 1.63 | 0.53 | 0.04 | 90901.92 | 24.59 | skipped_fast |
| WAXLUSDT | IDLE | 1.15 | 2.74 | 1.77 | -0.01 | 64191.56 | 60.6 | skipped_fast |
| FLUIDUSDT | IDLE | 0.68 | 1.66 | 1.64 | 0.05 | 4749.48 | 21.74 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.95 | 0.08 | 0.02 | 55428.12 | 23.56 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.39 | 0.09 | 0.0 | 40053.2 | 15.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
