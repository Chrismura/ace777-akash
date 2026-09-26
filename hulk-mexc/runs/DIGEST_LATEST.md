# Hulk DIGEST — 2026-09-26T14:00:18Z

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
| XRPUSDT | IDLE | 0.72 | 1.3 | 0.96 | -0.03 | 61765649.18 | 2.59 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.66 | 0.42 | -0.0 | 184875043.29 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.54 | 0.45 | 0.0 | 433002102.37 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.22 | 6.78 | 3.19 | 0.08 | 1167606.68 | 10.41 | skipped_fast |
| CCUSDT | IDLE | 1.39 | 5.28 | 1.66 | 0.12 | 991312.93 | 9.4 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.54 | 12.85 | 11.39 | -0.06 | 7443.18 | 117.65 | skipped_fast |
| QNTUSDT | IDLE | 1.76 | 6.75 | 3.48 | 0.13 | 798467.02 | 8.48 | skipped_fast |
| WUSDT | IDLE | 1.57 | 3.94 | 2.48 | 0.06 | 452071.46 | 5.53 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 4.54 | 0.45 | 0.04 | 156326.14 | 38.66 | skipped_fast |
| BIOUSDT | IDLE | 2.05 | 3.66 | 2.93 | -0.0 | 110957.33 | 6.17 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.78 | 1.38 | -0.01 | 602663.54 | 1.07 | skipped_fast |
| ZBCNUSDT | IDLE | 1.55 | 3.08 | 0.08 | 0.02 | 223232.03 | 30.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 2.54 | 1.76 | -0.01 | 129660.04 | 14.44 | skipped_fast |
| RIZEUSDT | IDLE | 1.41 | 7.38 | 3.61 | -0.11 | 47097.26 | 61.89 | skipped_fast |
| REDUSDT | IDLE | 1.22 | 2.23 | 1.36 | -0.01 | 58073.11 | 13.02 | skipped_fast |
| KITEUSDT | IDLE | 0.95 | 2.13 | 0.93 | 0.05 | 74739.98 | 7.37 | skipped_fast |
| RWAUSDT | IDLE | 2.18 | 4.23 | 0.93 | 0.02 | 56105.83 | 21.59 | skipped_fast |
| TELUSDT | IDLE | 1.56 | 2.78 | 2.28 | -0.05 | 122563.66 | 75.61 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.9 | 0.0 | 0.01 | 2939.49 | 20.01 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.05 | 0.0 | 39315.21 | 3.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
