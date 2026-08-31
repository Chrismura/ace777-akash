# Hulk DIGEST — 2026-08-31T19:18:50Z

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
| XRPUSDT | IDLE | 1.4 | 2.71 | 0.54 | -0.02 | 39272976.87 | 2.16 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 2.13 | 0.2 | -0.01 | 431333939.96 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.97 | 1.91 | 0.16 | 0.0 | 610902698.06 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.84 | 5.95 | 1.07 | -0.03 | 442375.0 | 2.04 | skipped_fast |
| CCUSDT | IDLE | 2.94 | 5.81 | 0.49 | 0.04 | 279023.79 | 6.53 | skipped_fast |
| CHIPUSDT | IDLE | 1.68 | 4.47 | 3.28 | -0.03 | 476362.16 | 2.59 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 7.89 | 6.43 | -0.06 | 40309.97 | 63.73 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 2.89 | 0.15 | -0.01 | 203993.51 | 16.34 | skipped_fast |
| WUSDT | IDLE | 0.91 | 1.64 | 1.19 | -0.04 | 213202.61 | 7.69 | skipped_fast |
| EDELUSDT | IDLE | 0.94 | 5.9 | 2.47 | 0.0 | 129129.19 | 24.46 | skipped_fast |
| BIOUSDT | IDLE | 1.31 | 2.5 | 0.75 | -0.04 | 74347.38 | 3.78 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 2.08 | 0.77 | -0.06 | 98680.13 | 10.95 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.06 | 1.72 | -0.04 | 66545.35 | 10.41 | skipped_fast |
| RWAINCUSDT | IDLE | 1.41 | 2.55 | 1.86 | -0.05 | 2475.87 | 28.71 | skipped_fast |
| RWAUSDT | IDLE | 2.07 | 4.9 | 1.41 | 0.07 | 58212.14 | 22.6 | skipped_fast |
| TELUSDT | IDLE | 2.29 | 4.53 | 0.4 | -0.0 | 88656.02 | 68.69 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.44 | 0.98 | -0.03 | 266732.25 | 1.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.67 | 2.95 | 2.56 | -0.03 | 2017.15 | 22.09 | skipped_fast |
| QNTUSDT | IDLE | 0.74 | 1.4 | 0.52 | -0.0 | 52215.04 | 6.51 | skipped_fast |
| MNSRYUSDT | IDLE | 0.74 | 1.46 | 0.2 | -0.01 | 25116.51 | 32.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
