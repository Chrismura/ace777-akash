# Hulk DIGEST — 2026-10-12T23:10:48Z

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
| WUSDT | IDLE | 1.04 | 15.87 | 13.19 | -0.13 | 15266325.45 | 14.27 | skipped_fast |
| PYTHUSDT | IDLE | 1.41 | 5.36 | 4.26 | 0.04 | 3426000.33 | 3.67 | skipped_fast |
| ETHUSDT | IDLE | 1.74 | 3.11 | 2.45 | -0.03 | 232970296.21 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.24 | 2.23 | 1.64 | -0.04 | 30452317.41 | 0.74 | skipped_fast |
| BTCUSDT | IDLE | 0.89 | 1.6 | 1.2 | -0.02 | 306191668.94 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.78 | 3.36 | 2.36 | -0.04 | 815534.73 | 6.63 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.43 | 2.16 | -0.04 | 401219.75 | 10.03 | skipped_fast |
| HBARUSDT | IDLE | 1.7 | 3.63 | 2.63 | -0.07 | 606306.23 | 10.28 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 14.0 | 8.0 | -0.05 | 73115.71 | 75.97 | skipped_fast |
| KITEUSDT | IDLE | 2.5 | 4.5 | 3.38 | -0.03 | 65405.25 | 9.63 | skipped_fast |
| BIOUSDT | IDLE | 1.87 | 4.32 | 3.16 | -0.08 | 75366.51 | 7.25 | skipped_fast |
| EDELUSDT | IDLE | 0.86 | 3.69 | 2.43 | -0.1 | 290102.72 | 23.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.18 | 2.19 | 1.14 | 0.01 | 267452.94 | 30.77 | skipped_fast |
| REDUSDT | IDLE | 0.67 | 4.24 | 2.91 | 0.02 | 267238.81 | 14.87 | skipped_fast |
| CHIPUSDT | IDLE | 0.84 | 3.88 | 3.36 | -0.14 | 160391.76 | 13.81 | skipped_fast |
| FLUIDUSDT | IDLE | 2.17 | 3.83 | 3.46 | -0.02 | 15612.97 | 19.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.72 | 2.05 | 0.2 | 0.01 | 32446.75 | 4.91 | skipped_fast |
| TELUSDT | IDLE | 1.58 | 2.79 | 2.43 | 0.01 | 120281.7 | 40.59 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.78 | 0.46 | -0.0 | 52403.34 | 15.49 | skipped_fast |
| MNSRYUSDT | IDLE | 0.6 | 1.06 | 0.99 | -0.01 | 41219.48 | 51.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
