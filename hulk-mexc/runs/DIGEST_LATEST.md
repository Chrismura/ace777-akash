# Hulk DIGEST — 2026-09-26T00:49:53Z

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
| XRPUSDT | IDLE | 0.91 | 1.7 | 0.84 | 0.01 | 112325140.16 | 1.92 | skipped_fast |
| ETHUSDT | IDLE | 0.38 | 0.71 | 0.38 | -0.0 | 319807530.21 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.34 | -0.01 | 685076896.74 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.97 | 5.19 | 2.39 | 0.07 | 1251957.99 | 4.08 | skipped_fast |
| CCUSDT | IDLE | 1.24 | 4.89 | 1.34 | 0.14 | 894230.16 | 11.46 | skipped_fast |
| HBARUSDT | IDLE | 1.35 | 2.48 | 1.43 | 0.02 | 903060.92 | 1.05 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.86 | 1.35 | 0.05 | 452704.24 | 10.54 | skipped_fast |
| ZBCNUSDT | IDLE | 1.99 | 4.37 | 3.99 | 0.05 | 237971.11 | 18.2 | skipped_fast |
| EDELUSDT | IDLE | 1.79 | 3.25 | 2.22 | -0.01 | 179896.72 | 6.78 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 4.72 | 2.4 | 0.03 | 157083.51 | 18.15 | skipped_fast |
| QNTUSDT | IDLE | 0.77 | 3.26 | 1.33 | 0.08 | 565430.96 | 9.16 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 11.71 | 7.89 | -0.0 | 108352.65 | 28.67 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 3.35 | 1.59 | 0.07 | 116401.09 | 3.05 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 1.86 | 1.45 | 0.08 | 112488.69 | 13.86 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 1.86 | 0.07 | 0.04 | 79040.81 | 11.21 | skipped_fast |
| RWAINCUSDT | IDLE | 0.68 | 2.15 | 0.75 | -0.09 | 13425.63 | 76.05 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.15 | 1.38 | 0.02 | 113170.82 | 60.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.5 | 0.88 | 0.75 | 0.02 | 41386.61 | 5.09 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.26 | 0.59 | -0.01 | 54310.55 | 59.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.23 | 0.4 | 0.4 | 0.03 | 3306.61 | 24.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
