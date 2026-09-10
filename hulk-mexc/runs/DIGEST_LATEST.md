# Hulk DIGEST — 2026-09-10T19:16:22Z

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
| XRPUSDT | IDLE | 1.07 | 1.97 | 1.12 | -0.04 | 46478975.5 | 2.95 | skipped_fast |
| ETHUSDT | IDLE | 0.97 | 1.88 | 0.38 | -0.01 | 458769332.39 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.93 | 0.46 | -0.02 | 557771512.44 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.43 | 4.44 | 2.76 | -0.07 | 873416.45 | 1.94 | skipped_fast |
| CCUSDT | IDLE | 2.32 | 4.25 | 2.61 | -0.05 | 582874.27 | 7.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 16.37 | 10.39 | 0.09 | 264801.49 | 35.71 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 44.57 | 22.28 | -0.53 | 124457.83 | 122.84 | skipped_fast |
| WUSDT | IDLE | 1.59 | 3.07 | 1.49 | -0.07 | 209559.42 | 5.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.67 | 3.06 | 1.86 | 0.01 | 198020.94 | 17.38 | skipped_fast |
| BIOUSDT | IDLE | 1.55 | 3.1 | 1.64 | -0.07 | 81149.18 | 3.97 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 3.37 | 0.91 | -0.04 | 57719.37 | 9.96 | skipped_fast |
| REDUSDT | IDLE | 1.4 | 2.93 | 2.28 | -0.07 | 67754.99 | 13.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.09 | 5.22 | 1.29 | -0.13 | 83973.17 | 12.48 | skipped_fast |
| RWAINCUSDT | IDLE | 1.29 | 2.38 | 1.39 | -0.01 | 5073.83 | 22.51 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.76 | 0.95 | -0.04 | 270444.22 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 2.06 | 1.52 | -0.02 | 36356.38 | 3.06 | skipped_fast |
| TELUSDT | IDLE | 1.12 | 2.16 | 0.56 | -0.01 | 86884.74 | 50.27 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.07 | 0.53 | -0.04 | 53127.33 | 15.19 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.62 | 0.0 | -0.02 | 30777.48 | 5.57 | skipped_fast |
| FLUIDUSDT | IDLE | 0.47 | 0.94 | 0.0 | -0.06 | 1854.16 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
