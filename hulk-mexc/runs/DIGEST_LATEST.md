# Hulk DIGEST — 2026-09-07T20:37:19Z

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
| XRPUSDT | IDLE | 0.91 | 1.79 | 0.23 | -0.01 | 36401249.86 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.31 | 0.3 | -0.0 | 344395044.49 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.91 | 0.23 | -0.01 | 458473195.12 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.49 | 9.56 | 3.68 | -0.03 | 214964.25 | 11.68 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 3.02 | 1.87 | -0.0 | 565442.76 | 3.66 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 3.5 | 3.1 | -0.05 | 470613.29 | 5.76 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 10.08 | 9.16 | -0.02 | 4825.28 | 5.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.97 | 8.01 | 1.63 | -0.07 | 234851.82 | 11.07 | skipped_fast |
| HBARUSDT | IDLE | 1.59 | 3.14 | 0.31 | 0.02 | 589375.19 | 1.21 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.6 | 0.52 | 0.0 | 263084.02 | 12.63 | skipped_fast |
| RIZEUSDT | IDLE | 2.12 | 6.16 | 4.41 | -0.11 | 60039.15 | 67.48 | skipped_fast |
| EDELUSDT | IDLE | 1.47 | 5.62 | 0.99 | -0.04 | 99401.41 | 39.76 | skipped_fast |
| REDUSDT | IDLE | 1.42 | 2.64 | 1.3 | 0.03 | 58873.99 | 8.36 | skipped_fast |
| KITEUSDT | IDLE | 1.41 | 2.53 | 2.0 | -0.05 | 60701.26 | 13.44 | skipped_fast |
| BIOUSDT | IDLE | 1.2 | 2.35 | 0.33 | -0.01 | 68504.98 | 10.96 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.89 | 1.04 | -0.02 | 112543.34 | 29.33 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 2.11 | 0.13 | 0.0 | 48140.1 | 4.49 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.79 | -0.01 | 53901.04 | 7.28 | skipped_fast |
| FLUIDUSDT | IDLE | 0.79 | 1.49 | 0.62 | -0.0 | 1593.73 | 22.53 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.7 | 0.39 | -0.01 | 37310.85 | 38.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
