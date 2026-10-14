# Hulk DIGEST — 2026-10-14T01:11:35Z

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
| WUSDT | IDLE | 0.97 | 6.17 | 4.61 | -0.12 | 4209740.96 | 6.51 | skipped_fast |
| PYTHUSDT | IDLE | 1.14 | 3.72 | 1.6 | -0.0 | 2005457.62 | 2.52 | skipped_fast |
| QNTUSDT | IDLE | 1.71 | 5.77 | 4.82 | -0.06 | 1700351.3 | 0.95 | skipped_fast |
| XRPUSDT | IDLE | 0.6 | 1.08 | 0.78 | 0.03 | 30898020.18 | 2.19 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.9 | 0.66 | 0.03 | 178464228.94 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.67 | 0.49 | 0.02 | 357218348.68 | 0.09 | skipped_fast |
| CCUSDT | IDLE | 1.71 | 3.41 | 2.75 | 0.06 | 593963.64 | 6.4 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 6.07 | 5.24 | -0.02 | 32587.49 | 20.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.79 | 3.19 | 2.58 | -0.0 | 97423.62 | 10.52 | skipped_fast |
| EDELUSDT | IDLE | 1.16 | 2.05 | 1.78 | 0.04 | 217868.17 | 11.71 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 2.59 | 1.87 | 0.04 | 124109.04 | 15.43 | skipped_fast |
| ZBCNUSDT | IDLE | 0.99 | 1.88 | 0.64 | 0.01 | 216426.94 | 23.31 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.89 | 0.67 | 0.08 | 57345.89 | 9.94 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.63 | 1.21 | 0.04 | 71556.25 | 7.23 | skipped_fast |
| FLUIDUSDT | IDLE | 2.45 | 4.9 | 0.0 | 0.09 | 19930.11 | 21.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.03 | 3.25 | 2.65 | -0.01 | 50429.12 | 59.57 | skipped_fast |
| TELUSDT | IDLE | 1.95 | 3.88 | 0.11 | 0.06 | 118151.94 | 38.47 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.43 | 0.75 | 0.02 | 249396.19 | 2.29 | skipped_fast |
| MNSRYUSDT | IDLE | 0.22 | 0.42 | 0.13 | 0.0 | 37371.28 | 6.98 | skipped_fast |
| RWAUSDT | IDLE | 0.16 | 0.31 | 0.08 | 0.01 | 51978.45 | 15.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
