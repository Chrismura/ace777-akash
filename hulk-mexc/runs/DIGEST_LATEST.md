# Hulk DIGEST — 2026-09-14T15:34:57Z

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
| XRPUSDT | IDLE | 0.95 | 1.87 | 0.21 | 0.04 | 41621950.86 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.5 | 0.7 | 0.01 | 350142272.78 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.55 | 0.19 | 0.02 | 451364867.37 | 0.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.96 | 10.34 | 6.41 | 0.06 | 176590.59 | 17.36 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 3.12 | 1.39 | 0.01 | 485222.0 | 1.81 | skipped_fast |
| WUSDT | IDLE | 2.36 | 4.27 | 3.01 | -0.01 | 220079.45 | 13.11 | skipped_fast |
| CHIPUSDT | IDLE | 2.47 | 4.89 | 2.52 | -0.04 | 87861.87 | 19.13 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 5.75 | 3.29 | 0.14 | 253099.54 | 20.8 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 2.8 | 0.4 | 0.01 | 206742.7 | 11.11 | skipped_fast |
| RIZEUSDT | IDLE | 1.36 | 15.14 | 11.42 | 0.07 | 67419.67 | 103.38 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.49 | 1.06 | 0.01 | 273054.74 | 6.26 | skipped_fast |
| BIOUSDT | IDLE | 1.28 | 2.42 | 0.93 | 0.01 | 83641.84 | 3.91 | skipped_fast |
| KITEUSDT | IDLE | 1.02 | 1.8 | 1.6 | -0.02 | 62044.5 | 15.23 | skipped_fast |
| RWAINCUSDT | IDLE | 1.11 | 2.22 | 0.0 | 0.03 | 8757.56 | 5.43 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 1.61 | 1.01 | 0.01 | 288585.19 | 1.3 | skipped_fast |
| TELUSDT | IDLE | 1.26 | 2.33 | 1.23 | 0.01 | 89357.44 | 49.97 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 1.9 | 1.86 | 0.0 | 623.71 | 21.96 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.38 | 0.03 | 0.01 | 41254.46 | 6.19 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.3 | 0.01 | 54922.28 | 29.63 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.38 | 0.18 | -0.0 | 28627.99 | 18.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
