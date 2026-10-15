# Hulk DIGEST — 2026-10-15T23:18:49Z

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
| WUSDT | IDLE | 1.37 | 3.68 | 3.39 | -0.05 | 2840045.66 | 18.6 | skipped_fast |
| PYTHUSDT | IDLE | 0.94 | 5.32 | 3.99 | 0.09 | 4488551.19 | 14.0 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.26 | 1.05 | 0.01 | 310232232.73 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.65 | 1.14 | 1.12 | -0.0 | 47626398.53 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.82 | 0.5 | 0.01 | 501950235.28 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.79 | 5.19 | 4.88 | -0.01 | 1356531.81 | 0.98 | skipped_fast |
| CCUSDT | IDLE | 1.17 | 2.48 | 2.35 | -0.08 | 470097.44 | 3.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 7.69 | 2.76 | 0.04 | 81664.94 | 4.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 3.49 | 2.61 | 0.02 | 218047.72 | 22.54 | skipped_fast |
| EDELUSDT | IDLE | 1.33 | 4.73 | 3.06 | -0.12 | 240046.97 | 23.95 | skipped_fast |
| KITEUSDT | IDLE | 1.51 | 2.71 | 2.29 | -0.02 | 68904.03 | 8.92 | skipped_fast |
| CHIPUSDT | IDLE | 0.95 | 4.64 | 1.62 | -0.08 | 152935.6 | 10.58 | skipped_fast |
| HBARUSDT | IDLE | 1.3 | 2.48 | 0.85 | 0.0 | 301509.52 | 4.72 | skipped_fast |
| REDUSDT | IDLE | 0.7 | 2.03 | 1.97 | -0.02 | 72647.07 | 9.64 | skipped_fast |
| RWAINCUSDT | IDLE | 0.86 | 1.76 | 1.38 | 0.01 | 28877.64 | 14.99 | skipped_fast |
| BIOUSDT | IDLE | 0.5 | 1.05 | 0.92 | -0.03 | 83842.76 | 3.89 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.99 | 0.39 | 0.01 | 90315.17 | 16.81 | skipped_fast |
| RWAUSDT | IDLE | 0.93 | 1.67 | 1.25 | 0.01 | 54675.4 | 23.86 | skipped_fast |
| FLUIDUSDT | IDLE | 1.0 | 2.38 | 1.2 | -0.04 | 10668.59 | 21.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.35 | 0.11 | -0.0 | 35107.47 | 4.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
