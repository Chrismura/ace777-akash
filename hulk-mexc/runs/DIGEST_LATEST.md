# Hulk DIGEST — 2026-09-19T11:57:47Z

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
| XRPUSDT | IDLE | 0.94 | 2.09 | 0.12 | 0.09 | 68629883.75 | 2.09 | skipped_fast |
| ETHUSDT | IDLE | 0.82 | 1.52 | 0.76 | 0.05 | 552996611.68 | 0.57 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.7 | 0.24 | 0.04 | 627524522.27 | 0.06 | skipped_fast |
| WUSDT | IDLE | 1.09 | 3.32 | 0.27 | 0.09 | 982820.67 | 6.35 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 3.28 | 0.15 | 0.04 | 705560.14 | 6.56 | skipped_fast |
| BIOUSDT | IDLE | 3.67 | 7.7 | 1.25 | 0.07 | 83191.59 | 14.05 | skipped_fast |
| EDELUSDT | IDLE | 2.23 | 12.85 | 7.22 | -0.1 | 193973.26 | 47.89 | skipped_fast |
| HBARUSDT | IDLE | 1.76 | 3.5 | 0.12 | 0.05 | 593617.35 | 1.24 | skipped_fast |
| KITEUSDT | IDLE | 2.33 | 4.34 | 2.15 | 0.04 | 70097.69 | 12.16 | skipped_fast |
| CCUSDT | IDLE | 0.81 | 1.6 | 0.1 | 0.03 | 409792.19 | 7.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.35 | 4.45 | 3.2 | 0.06 | 142153.74 | 17.89 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 5.45 | 2.83 | 0.06 | 133270.64 | 16.04 | skipped_fast |
| ZBCNUSDT | IDLE | 1.16 | 2.27 | 0.31 | 0.01 | 173073.78 | 22.88 | skipped_fast |
| QNTUSDT | IDLE | 1.78 | 3.56 | 0.05 | 0.04 | 74845.02 | 4.6 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.26 | 0.17 | 0.04 | 5122.39 | 5.66 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 3.46 | 1.96 | 0.03 | 123995.38 | 45.12 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 4.45 | 1.56 | 0.14 | 11264.54 | 19.43 | skipped_fast |
| RIZEUSDT | IDLE | 0.25 | 2.07 | 1.4 | -0.08 | 38756.86 | 94.72 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.96 | 0.66 | 0.0 | 56781.15 | 29.52 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.55 | 0.16 | 0.04 | 39098.95 | 6.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
