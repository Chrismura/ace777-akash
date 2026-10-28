# Hulk DIGEST — 2026-10-28T14:38:53Z

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
| ETHUSDT | IDLE | 1.25 | 2.21 | 2.0 | -0.0 | 236452504.31 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.05 | 1.83 | 1.78 | -0.01 | 19977718.77 | 2.29 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.46 | 1.38 | 0.0 | 311444080.71 | 0.0 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 9.68 | 6.83 | -0.02 | 371093.18 | 10.23 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.53 | 13.04 | 11.53 | -0.04 | 184189.89 | 17.78 | skipped_fast |
| RWAINCUSDT | IDLE | 4.23 | 10.56 | 3.97 | 0.05 | 44171.32 | 19.34 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 5.54 | 5.11 | -0.04 | 463470.23 | 2.07 | skipped_fast |
| WUSDT | IDLE | 1.53 | 2.74 | 2.16 | -0.04 | 541258.96 | 15.06 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 2.78 | 2.26 | -0.02 | 437730.51 | 4.21 | skipped_fast |
| ZBCNUSDT | IDLE | 2.1 | 3.94 | 2.8 | -0.05 | 231960.57 | 13.63 | skipped_fast |
| EDELUSDT | IDLE | 1.59 | 2.83 | 2.27 | -0.01 | 239354.22 | 21.7 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.32 | 2.03 | -0.01 | 516164.18 | 6.65 | skipped_fast |
| BIOUSDT | IDLE | 1.85 | 3.29 | 2.7 | 0.0 | 88241.38 | 8.96 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 2.24 | 2.12 | -0.05 | 58009.62 | 14.0 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 2.15 | 1.85 | -0.02 | 53081.98 | 9.98 | skipped_fast |
| IOTAUSDT | IDLE | 1.96 | 3.45 | 3.15 | -0.02 | 75595.22 | 21.82 | skipped_fast |
| LAUSDT | IDLE | 1.81 | 3.17 | 3.04 | -0.03 | 59972.51 | 22.51 | skipped_fast |
| RIZEUSDT | IDLE | 1.0 | 1.79 | 1.35 | 0.03 | 36442.91 | 64.06 | skipped_fast |
| WAXLUSDT | IDLE | 1.86 | 3.26 | 3.04 | -0.02 | 55997.0 | 70.82 | skipped_fast |
| FLUIDUSDT | IDLE | 1.16 | 3.48 | 2.83 | -0.0 | 6553.18 | 21.2 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.12 | 0.87 | 0.01 | 54830.86 | 32.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.51 | 0.2 | 0.01 | 36354.21 | 48.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
