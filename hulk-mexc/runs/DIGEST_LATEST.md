# Hulk DIGEST — 2026-09-22T03:08:37Z

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
| XRPUSDT | IDLE | 1.85 | 4.67 | 3.79 | 0.07 | 113819120.09 | 3.3 | skipped_fast |
| ETHUSDT | IDLE | 1.09 | 1.9 | 1.83 | 0.03 | 693864975.46 | 0.84 | skipped_fast |
| BTCUSDT | IDLE | 0.9 | 1.61 | 1.32 | 0.05 | 1100135795.43 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.42 | 4.43 | 2.69 | 0.05 | 672984.14 | 9.42 | skipped_fast |
| PYTHUSDT | IDLE | 1.86 | 4.02 | 2.54 | 0.03 | 769881.25 | 1.58 | skipped_fast |
| HBARUSDT | IDLE | 1.38 | 2.67 | 2.2 | 0.06 | 1123685.86 | 7.63 | skipped_fast |
| WUSDT | IDLE | 1.18 | 2.16 | 1.39 | 0.03 | 542212.89 | 8.47 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 29.52 | 21.0 | -0.33 | 56483.76 | 307.04 | skipped_fast |
| ZBCNUSDT | IDLE | 2.18 | 4.61 | 2.21 | 0.04 | 264910.84 | 43.16 | skipped_fast |
| REDUSDT | IDLE | 2.54 | 4.73 | 2.38 | 0.01 | 98093.47 | 15.63 | skipped_fast |
| CHIPUSDT | IDLE | 1.31 | 6.2 | 3.23 | 0.11 | 169105.33 | 19.23 | skipped_fast |
| BIOUSDT | IDLE | 1.44 | 2.55 | 2.18 | 0.03 | 131369.11 | 6.96 | skipped_fast |
| KITEUSDT | IDLE | 1.44 | 2.7 | 1.26 | 0.03 | 81593.04 | 10.84 | skipped_fast |
| EDELUSDT | IDLE | 0.5 | 3.29 | 0.58 | 0.07 | 235352.12 | 9.8 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.54 | 2.48 | 0.07 | 20240.29 | 5.53 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 2.73 | 1.34 | 0.03 | 114980.86 | 9.0 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 3.41 | 2.52 | 0.07 | 117074.32 | 49.29 | skipped_fast |
| MNSRYUSDT | IDLE | 0.81 | 1.48 | 0.91 | 0.02 | 41374.84 | 9.02 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.46 | 1.29 | 0.0 | 57812.01 | 36.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.33 | 1.02 | 0.08 | 12008.84 | 21.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
