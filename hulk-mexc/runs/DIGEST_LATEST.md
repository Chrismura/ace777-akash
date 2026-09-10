# Hulk DIGEST — 2026-09-10T04:14:09Z

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
| XRPUSDT | IDLE | 0.75 | 1.43 | 0.42 | -0.02 | 42987571.33 | 2.88 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.17 | 0.12 | -0.01 | 387069028.95 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.78 | 0.24 | -0.01 | 538445911.2 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.78 | 2.12 | 0.8 | -0.02 | 1001716.6 | 1.92 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 2.71 | 1.61 | -0.04 | 635358.62 | 7.7 | skipped_fast |
| EDELUSDT | IDLE | 2.49 | 9.71 | 2.32 | 0.08 | 237205.99 | 35.12 | skipped_fast |
| ZBCNUSDT | IDLE | 2.62 | 5.11 | 0.87 | 0.05 | 192068.55 | 6.9 | skipped_fast |
| WUSDT | IDLE | 1.57 | 3.0 | 1.92 | -0.03 | 211946.7 | 10.14 | skipped_fast |
| REDUSDT | IDLE | 2.0 | 3.51 | 3.32 | -0.0 | 63428.09 | 10.26 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 3.62 | 2.34 | -0.06 | 102158.42 | 7.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.03 | 5.52 | 4.71 | -0.08 | 123115.55 | 14.25 | skipped_fast |
| KITEUSDT | IDLE | 1.52 | 2.74 | 2.0 | -0.01 | 57192.56 | 12.48 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.7 | 0.25 | -0.03 | 446934.81 | 1.3 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 1.71 | 1.4 | -0.01 | 5786.12 | 5.67 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 7.53 | 0.85 | 0.06 | 60453.24 | 94.79 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 2.0 | 0.57 | -0.0 | 47271.81 | 5.93 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 1.97 | 0.77 | -0.0 | 94124.61 | 38.99 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.9 | 0.37 | -0.03 | 54922.66 | 14.94 | skipped_fast |
| FLUIDUSDT | IDLE | 0.61 | 1.16 | 1.15 | -0.07 | 1437.99 | 15.11 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 1.0 | 0.18 | -0.02 | 27888.27 | 13.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
