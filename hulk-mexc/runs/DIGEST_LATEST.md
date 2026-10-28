# Hulk DIGEST — 2026-10-28T19:42:31Z

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
| ETHUSDT | IDLE | 0.91 | 1.77 | 0.32 | 0.01 | 185841128.04 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.92 | 1.81 | 0.24 | 0.0 | 22354160.5 | 2.26 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.15 | 0.11 | 0.01 | 309485312.89 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.53 | 6.04 | 0.53 | 0.03 | 415820.52 | 5.93 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 7.59 | 7.05 | -0.05 | 34853.5 | 27.55 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 7.68 | 4.4 | -0.1 | 226990.49 | 6.08 | skipped_fast |
| PYTHUSDT | IDLE | 1.35 | 2.65 | 0.35 | -0.01 | 403945.47 | 2.77 | skipped_fast |
| WUSDT | IDLE | 1.43 | 2.77 | 0.56 | -0.0 | 406574.73 | 15.6 | skipped_fast |
| ZBCNUSDT | IDLE | 1.49 | 2.84 | 0.96 | -0.04 | 272505.37 | 34.74 | skipped_fast |
| QNTUSDT | IDLE | 1.96 | 3.79 | 0.88 | -0.01 | 399390.54 | 6.05 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.77 | 0.79 | -0.01 | 564056.29 | 10.61 | skipped_fast |
| EDELUSDT | IDLE | 1.23 | 2.18 | 1.83 | -0.01 | 180378.57 | 21.69 | skipped_fast |
| BIOUSDT | IDLE | 1.55 | 3.06 | 0.31 | 0.01 | 85165.04 | 8.76 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 3.51 | 2.89 | -0.0 | 39286.86 | 63.0 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.82 | 0.75 | -0.01 | 58785.07 | 12.03 | skipped_fast |
| REDUSDT | IDLE | 0.8 | 1.53 | 0.43 | -0.02 | 53914.33 | 7.25 | skipped_fast |
| IOTAUSDT | IDLE | 1.33 | 2.61 | 0.36 | -0.01 | 72420.46 | 26.24 | skipped_fast |
| LAUSDT | IDLE | 1.22 | 2.32 | 0.75 | -0.04 | 57380.96 | 22.35 | skipped_fast |
| WAXLUSDT | IDLE | 1.17 | 2.28 | 0.37 | -0.0 | 55259.4 | 69.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.53 | 1.77 | 0.05 | -0.0 | 6326.24 | 19.46 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.56 | 0.16 | -0.0 | 54672.31 | 48.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.51 | 0.31 | 0.01 | 35825.96 | 54.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
