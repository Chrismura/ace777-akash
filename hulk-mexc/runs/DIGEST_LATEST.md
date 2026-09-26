# Hulk DIGEST — 2026-09-26T10:59:05Z

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
| XRPUSDT | IDLE | 0.72 | 1.37 | 0.4 | -0.0 | 106577862.75 | 1.93 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.66 | 0.38 | -0.01 | 254855752.29 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.51 | 0.18 | -0.01 | 551827231.59 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.93 | 4.43 | 0.14 | 0.07 | 1181511.77 | 2.62 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 6.64 | 2.68 | 0.13 | 1022037.27 | 9.58 | skipped_fast |
| QNTUSDT | IDLE | 2.54 | 11.38 | 2.94 | 0.09 | 771251.3 | 9.38 | skipped_fast |
| WUSDT | IDLE | 2.32 | 5.86 | 0.34 | 0.07 | 489076.09 | 10.11 | skipped_fast |
| RWAINCUSDT | IDLE | 3.5 | 7.06 | 2.42 | 0.04 | 6354.03 | 72.87 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.5 | 0.18 | 0.01 | 791445.71 | 1.06 | skipped_fast |
| EDELUSDT | IDLE | 1.55 | 3.11 | 0.0 | 0.02 | 177552.59 | 23.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 2.89 | 1.49 | -0.01 | 143944.79 | 16.39 | skipped_fast |
| ZBCNUSDT | IDLE | 1.11 | 2.17 | 0.39 | -0.01 | 228402.89 | 16.93 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 3.31 | 0.96 | 0.05 | 121509.44 | 6.04 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 2.89 | 1.81 | 0.04 | 76979.08 | 11.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.05 | 9.26 | 4.37 | -0.2 | 52757.04 | 62.46 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 1.78 | 1.51 | 0.01 | 59443.82 | 6.48 | skipped_fast |
| RWAUSDT | IDLE | 2.4 | 4.31 | 3.28 | -0.01 | 55741.39 | 51.53 | skipped_fast |
| TELUSDT | IDLE | 1.06 | 1.87 | 1.71 | -0.04 | 121530.83 | 49.72 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.82 | 0.0 | 0.01 | 3396.54 | 22.11 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.37 | 0.01 | 0.01 | 40280.18 | 8.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
