# Hulk DIGEST — 2026-08-30T17:03:09Z

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
| ETHUSDT | IDLE | 1.56 | 3.05 | 0.41 | 0.03 | 205947384.98 | 1.07 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 2.44 | 0.43 | 0.02 | 19761879.89 | 1.41 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.58 | 0.16 | 0.02 | 270238261.31 | 0.23 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.33 | 5.18 | -0.03 | 523595.18 | 2.48 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 9.26 | 6.2 | -0.07 | 193294.9 | 28.1 | skipped_fast |
| PYTHUSDT | IDLE | 3.01 | 5.66 | 2.37 | 0.02 | 399225.62 | 4.08 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 5.99 | 2.18 | 0.08 | 72217.79 | 16.52 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.69 | 0.74 | 0.04 | 220887.49 | 13.68 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.62 | 0.96 | 0.02 | 258444.26 | 6.75 | skipped_fast |
| REDUSDT | IDLE | 1.08 | 2.02 | 0.93 | 0.02 | 61530.29 | 11.76 | skipped_fast |
| KITEUSDT | IDLE | 0.92 | 1.67 | 1.1 | -0.03 | 61917.95 | 8.59 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.61 | 0.11 | 0.0 | 79471.67 | 3.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.48 | 2.95 | 0.0 | 0.02 | 1854.4 | 55.28 | skipped_fast |
| TELUSDT | IDLE | 2.21 | 4.37 | 0.4 | 0.0 | 83470.34 | 34.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 3.06 | 2.22 | -0.06 | 46400.81 | 61.18 | skipped_fast |
| HBARUSDT | IDLE | 0.55 | 1.07 | 0.2 | 0.0 | 130463.88 | 1.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.56 | 0.01 | 32477.62 | 2.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 21.45 | skipped_fast |
| QNTUSDT | IDLE | 0.5 | 0.97 | 0.19 | 0.01 | 38383.15 | 4.83 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.9 | 0.08 | 0.02 | 52867.6 | 16.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
