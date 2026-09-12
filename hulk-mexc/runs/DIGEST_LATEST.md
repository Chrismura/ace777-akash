# Hulk DIGEST — 2026-09-12T16:37:41Z

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
| ETHUSDT | IDLE | 0.34 | 0.6 | 0.56 | -0.01 | 290584211.87 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.33 | 0.61 | 0.31 | -0.0 | 22345441.56 | 2.19 | skipped_fast |
| BTCUSDT | IDLE | 0.17 | 0.31 | 0.16 | -0.0 | 385330336.21 | 0.0 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 6.86 | 6.28 | -0.01 | 212407.13 | 49.86 | skipped_fast |
| CHIPUSDT | IDLE | 3.12 | 7.97 | 3.68 | 0.02 | 70582.22 | 16.27 | skipped_fast |
| PYTHUSDT | IDLE | 1.69 | 3.98 | 0.96 | 0.04 | 358936.54 | 1.83 | skipped_fast |
| RIZEUSDT | IDLE | 1.93 | 57.62 | 16.31 | 0.83 | 116356.62 | 709.75 | skipped_fast |
| RWAINCUSDT | IDLE | 2.69 | 5.11 | 3.8 | 0.0 | 11573.73 | 5.49 | skipped_fast |
| EDELUSDT | IDLE | 1.67 | 4.87 | 0.34 | 0.1 | 168681.59 | 42.32 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.84 | 0.58 | 0.01 | 121031.35 | 9.07 | skipped_fast |
| CCUSDT | IDLE | 0.71 | 1.27 | 0.97 | -0.0 | 249860.2 | 5.1 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 1.97 | 0.0 | 0.03 | 61554.7 | 16.91 | skipped_fast |
| KITEUSDT | IDLE | 0.72 | 1.26 | 1.14 | -0.02 | 59652.28 | 10.37 | skipped_fast |
| BIOUSDT | IDLE | 0.59 | 1.09 | 0.66 | 0.01 | 71856.71 | 7.78 | skipped_fast |
| HBARUSDT | IDLE | 0.44 | 0.83 | 0.33 | -0.01 | 179295.95 | 1.34 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.7 | 1.6 | 0.0 | 54101.9 | 7.4 | skipped_fast |
| TELUSDT | IDLE | 0.76 | 1.44 | 0.59 | -0.06 | 94905.5 | 35.93 | skipped_fast |
| QNTUSDT | IDLE | 0.48 | 0.84 | 0.76 | -0.01 | 40595.13 | 7.77 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.71 | 0.4 | -0.01 | 24258.02 | 31.97 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.54 | 0.0 | 0.01 | 1430.19 | 22.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
