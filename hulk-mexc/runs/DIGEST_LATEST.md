# Hulk DIGEST — 2026-09-10T18:14:52Z

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
| ETHUSDT | IDLE | 1.49 | 2.87 | 0.72 | -0.01 | 451406832.19 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 1.97 | 1.3 | -0.05 | 46256472.55 | 2.22 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 1.0 | 0.65 | -0.02 | 558318389.32 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.92 | 4.44 | 2.72 | -0.08 | 884568.35 | 1.94 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.92 | 16.37 | 11.91 | 0.06 | 261281.53 | 27.24 | skipped_fast |
| CCUSDT | IDLE | 2.34 | 4.15 | 3.59 | -0.05 | 560358.68 | 6.1 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 44.57 | 21.42 | -0.52 | 121380.27 | 132.3 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 3.28 | 1.58 | 0.0 | 197658.48 | 5.96 | skipped_fast |
| WUSDT | IDLE | 1.13 | 3.07 | 1.49 | -0.07 | 220668.38 | 14.56 | skipped_fast |
| KITEUSDT | IDLE | 1.83 | 3.83 | 0.93 | -0.04 | 57398.23 | 8.15 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 3.1 | 1.87 | -0.07 | 81534.88 | 3.98 | skipped_fast |
| REDUSDT | IDLE | 1.41 | 2.93 | 2.42 | -0.09 | 68137.71 | 18.26 | skipped_fast |
| CHIPUSDT | IDLE | 0.97 | 4.51 | 2.99 | -0.18 | 86896.12 | 17.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.38 | 1.55 | -0.02 | 5136.94 | 33.76 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 1.76 | 1.12 | -0.04 | 285755.16 | 1.33 | skipped_fast |
| TELUSDT | IDLE | 1.44 | 2.68 | 1.39 | -0.02 | 82119.4 | 11.25 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.5 | 1.35 | -0.02 | 36174.18 | 4.58 | skipped_fast |
| MNSRYUSDT | IDLE | 0.62 | 1.17 | 0.53 | -0.03 | 29713.38 | 19.53 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.69 | 0.15 | -0.04 | 52853.41 | 15.2 | skipped_fast |
| FLUIDUSDT | IDLE | 0.47 | 0.94 | 0.0 | -0.07 | 2232.87 | 21.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
