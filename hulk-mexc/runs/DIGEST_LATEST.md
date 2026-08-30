# Hulk DIGEST — 2026-08-30T17:08:16Z

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
| ETHUSDT | IDLE | 1.56 | 3.05 | 0.53 | 0.03 | 203888330.58 | 0.12 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 2.44 | 0.6 | 0.02 | 19888454.95 | 2.12 | skipped_fast |
| BTCUSDT | IDLE | 0.81 | 1.58 | 0.28 | 0.01 | 270170921.79 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 7.33 | 5.58 | -0.03 | 523481.1 | 2.5 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 9.26 | 6.17 | -0.07 | 193491.1 | 6.48 | skipped_fast |
| PYTHUSDT | IDLE | 3.01 | 5.66 | 2.43 | 0.03 | 399416.83 | 4.08 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 5.99 | 2.58 | 0.08 | 72503.44 | 8.29 | skipped_fast |
| WUSDT | IDLE | 1.38 | 2.69 | 0.42 | 0.04 | 222732.66 | 9.44 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 1.62 | 1.09 | 0.01 | 256989.43 | 9.29 | skipped_fast |
| REDUSDT | IDLE | 1.08 | 2.02 | 0.96 | 0.02 | 61561.04 | 13.56 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 1.65 | 0.07 | 0.0 | 79489.8 | 3.61 | skipped_fast |
| KITEUSDT | IDLE | 0.92 | 1.67 | 1.15 | -0.02 | 61077.69 | 10.92 | skipped_fast |
| TELUSDT | IDLE | 2.22 | 4.37 | 0.52 | -0.0 | 83480.43 | 34.6 | skipped_fast |
| RIZEUSDT | IDLE | 0.94 | 3.06 | 2.11 | -0.06 | 38340.36 | 61.18 | skipped_fast |
| RWAINCUSDT | IDLE | 1.52 | 2.95 | 0.66 | 0.01 | 1859.72 | 110.38 | skipped_fast |
| HBARUSDT | IDLE | 0.55 | 1.07 | 0.26 | 0.0 | 130946.46 | 1.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.56 | 0.0 | 32314.86 | 2.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 21.46 | skipped_fast |
| QNTUSDT | IDLE | 0.5 | 0.97 | 0.19 | 0.01 | 38359.24 | 4.83 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.9 | 0.08 | 0.01 | 52840.29 | 16.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
