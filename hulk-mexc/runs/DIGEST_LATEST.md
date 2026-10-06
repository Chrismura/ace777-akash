# Hulk DIGEST — 2026-10-06T07:40:52Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 6.28 | 5.65 | -0.01 | 2771730.64 | 0.79 | skipped_fast |
| XRPUSDT | IDLE | 0.68 | 1.25 | 0.74 | -0.02 | 28228565.5 | 1.33 | skipped_fast |
| ETHUSDT | IDLE | 0.38 | 0.73 | 0.25 | -0.01 | 313031273.36 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.7 | 0.3 | -0.01 | 552058925.02 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.71 | 6.07 | 3.27 | 0.02 | 353637.03 | 17.96 | skipped_fast |
| PYTHUSDT | IDLE | 1.11 | 2.14 | 0.56 | -0.02 | 571924.43 | 1.29 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 1.84 | 0.21 | 0.01 | 470014.67 | 4.68 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 2.8 | 2.33 | -0.02 | 296733.37 | 10.27 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.73 | 15.45 | 11.48 | 0.1 | 96690.5 | 20.23 | skipped_fast |
| WUSDT | IDLE | 1.22 | 2.36 | 0.51 | -0.03 | 368981.87 | 20.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 5.12 | 2.89 | 0.08 | 132380.35 | 9.29 | skipped_fast |
| RIZEUSDT | IDLE | 1.35 | 16.75 | 6.84 | 0.2 | 104561.52 | 114.89 | skipped_fast |
| BIOUSDT | IDLE | 1.11 | 2.53 | 0.98 | 0.0 | 108737.77 | 6.39 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 2.08 | 1.92 | -0.05 | 67152.93 | 2.91 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.13 | 1.6 | -0.04 | 63376.52 | 6.62 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.23 | 1.12 | -0.04 | 410541.13 | 4.99 | skipped_fast |
| RWAINCUSDT | IDLE | 1.52 | 4.49 | 1.54 | -0.06 | 18112.09 | 72.29 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 3.62 | 1.62 | -0.04 | 134247.53 | 37.07 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.25 | 0.15 | 0.0 | 51694.79 | 21.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.62 | 0.15 | 0.0 | 45462.49 | 5.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
