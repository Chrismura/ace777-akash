# Hulk DIGEST — 2026-09-13T12:33:08Z

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
| ETHUSDT | IDLE | 1.19 | 2.15 | 1.56 | -0.02 | 235184467.48 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.01 | 1.82 | 1.39 | -0.02 | 14183050.61 | 1.49 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.88 | 0.48 | -0.01 | 305950623.29 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.98 | 14.26 | 10.95 | 0.08 | 203749.4 | 24.56 | skipped_fast |
| CCUSDT | IDLE | 2.29 | 4.14 | 2.99 | -0.03 | 299656.06 | 4.2 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 3.05 | 0.42 | 0.03 | 441799.53 | 3.65 | skipped_fast |
| WUSDT | IDLE | 1.58 | 2.92 | 1.54 | 0.02 | 245001.91 | 11.08 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 2.68 | 1.78 | -0.04 | 182596.65 | 17.52 | skipped_fast |
| RIZEUSDT | IDLE | 1.07 | 16.98 | 7.44 | 0.16 | 102612.51 | 98.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.18 | 2.96 | -0.06 | 79974.8 | 13.07 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.06 | 2.97 | -0.06 | 7781.82 | 5.67 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.69 | 1.73 | 0.02 | 63641.07 | 11.93 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.14 | 1.4 | -0.02 | 69687.14 | 3.94 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 1.8 | 0.61 | 0.02 | 56724.87 | 15.99 | skipped_fast |
| TELUSDT | IDLE | 1.62 | 3.07 | 1.12 | -0.05 | 86053.19 | 43.96 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.57 | 0.66 | 0.01 | 159102.22 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.67 | 1.26 | 0.59 | -0.01 | 36858.36 | 6.26 | skipped_fast |
| FLUIDUSDT | IDLE | 0.78 | 1.35 | 1.34 | -0.0 | 1225.97 | 23.76 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.96 | 0.44 | -0.01 | 54872.86 | 74.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.35 | 0.17 | 0.0 | 32694.96 | 20.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
