# Hulk DIGEST — 2026-10-20T11:14:35Z

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
| XRPUSDT | IDLE | 0.63 | 1.14 | 0.74 | -0.0 | 19441850.65 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 1.03 | 0.6 | -0.01 | 125956376.12 | 0.71 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.66 | 0.37 | -0.01 | 292865007.86 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.9 | 1.71 | 0.63 | -0.02 | 926078.75 | 4.13 | skipped_fast |
| WUSDT | IDLE | 1.66 | 2.99 | 2.23 | 0.02 | 711118.29 | 17.03 | skipped_fast |
| RWAINCUSDT | IDLE | 3.6 | 10.32 | 3.75 | 0.06 | 82089.03 | 4.93 | skipped_fast |
| EDELUSDT | IDLE | 1.65 | 9.33 | 0.74 | 0.19 | 301892.85 | 24.89 | skipped_fast |
| CCUSDT | IDLE | 1.1 | 2.07 | 0.82 | 0.01 | 444617.3 | 7.69 | skipped_fast |
| ZBCNUSDT | IDLE | 1.64 | 3.02 | 1.77 | -0.02 | 175209.71 | 7.71 | skipped_fast |
| KITEUSDT | IDLE | 1.94 | 3.47 | 2.74 | 0.01 | 88551.56 | 10.88 | skipped_fast |
| QNTUSDT | IDLE | 1.24 | 2.43 | 0.32 | -0.03 | 524816.53 | 1.03 | skipped_fast |
| CHIPUSDT | IDLE | 1.31 | 3.31 | 1.8 | 0.05 | 88267.11 | 13.6 | skipped_fast |
| REDUSDT | IDLE | 1.24 | 2.22 | 1.75 | 0.01 | 58655.2 | 8.08 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.19 | 1.8 | -0.0 | 351928.97 | 4.84 | skipped_fast |
| BIOUSDT | IDLE | 0.6 | 1.15 | 0.3 | 0.01 | 65801.39 | 8.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.58 | 2.22 | 1.21 | -0.07 | 64460.12 | 66.23 | skipped_fast |
| IOTAUSDT | IDLE | 1.42 | 2.56 | 1.82 | 0.03 | 84546.38 | 28.74 | skipped_fast |
| WAXLUSDT | IDLE | 1.64 | 3.63 | 2.32 | -0.06 | 57982.14 | 67.03 | skipped_fast |
| LAUSDT | IDLE | 1.2 | 2.2 | 1.33 | -0.02 | 55789.22 | 27.0 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.31 | 0.01 | 51375.8 | 7.86 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 0.99 | 0.6 | -0.0 | 4463.59 | 20.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.07 | -0.0 | 39580.75 | 9.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
