# Hulk DIGEST — 2026-09-17T06:02:58Z

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
| XRPUSDT | IDLE | 0.83 | 1.49 | 1.08 | -0.0 | 55263371.63 | 2.31 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.33 | 0.36 | 0.01 | 386279459.3 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.89 | 0.57 | 0.0 | 510230810.28 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.38 | 4.56 | 1.4 | 0.02 | 532877.13 | 1.84 | skipped_fast |
| CCUSDT | IDLE | 1.11 | 4.07 | 1.95 | 0.07 | 577165.78 | 3.06 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 7.86 | 6.61 | -0.05 | 215014.47 | 16.12 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 4.35 | 1.59 | 0.02 | 172517.53 | 5.18 | skipped_fast |
| RIZEUSDT | IDLE | 1.72 | 16.51 | 11.5 | -0.02 | 61206.31 | 69.09 | skipped_fast |
| WUSDT | IDLE | 1.63 | 3.06 | 1.45 | 0.02 | 223054.36 | 13.02 | skipped_fast |
| CHIPUSDT | IDLE | 1.95 | 4.33 | 2.58 | -0.02 | 79708.39 | 19.09 | skipped_fast |
| REDUSDT | IDLE | 1.58 | 2.93 | 1.48 | -0.02 | 59936.79 | 16.73 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.65 | 0.48 | 0.07 | 66799.18 | 11.96 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.59 | 0.98 | 0.01 | 78158.69 | 3.96 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.38 | 1.1 | -0.01 | 318280.77 | 1.36 | skipped_fast |
| RWAINCUSDT | IDLE | 0.88 | 1.7 | 0.4 | -0.01 | 16496.74 | 28.84 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 1.42 | 0.96 | 0.01 | 37848.45 | 4.95 | skipped_fast |
| TELUSDT | IDLE | 0.75 | 1.32 | 1.17 | -0.03 | 115724.08 | 41.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.95 | 0.03 | 0.01 | 36192.05 | 9.83 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.98 | 0.15 | 0.02 | 55648.87 | 37.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1571.52 | 21.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
