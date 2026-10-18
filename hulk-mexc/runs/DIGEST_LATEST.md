# Hulk DIGEST — 2026-10-18T17:04:30Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 8.52 | 5.83 | -0.07 | 1416755.24 | 2.66 | skipped_fast |
| XRPUSDT | IDLE | 1.41 | 2.52 | 2.02 | -0.01 | 24000551.54 | 1.57 | skipped_fast |
| ETHUSDT | IDLE | 1.39 | 2.48 | 2.0 | -0.01 | 99286397.66 | 0.55 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.34 | 1.12 | -0.0 | 218531191.37 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.73 | 4.1 | 2.87 | -0.04 | 971920.81 | 16.1 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.48 | 18.85 | 14.92 | -0.0 | 59469.12 | 59.57 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 12.83 | 9.0 | -0.01 | 37176.67 | 26.55 | skipped_fast |
| HBARUSDT | IDLE | 2.66 | 5.07 | 4.03 | 0.04 | 715582.8 | 6.99 | skipped_fast |
| QNTUSDT | IDLE | 3.54 | 6.34 | 4.87 | -0.04 | 499112.38 | 3.16 | skipped_fast |
| ZBCNUSDT | IDLE | 2.58 | 4.78 | 3.94 | -0.05 | 198043.73 | 32.08 | skipped_fast |
| CHIPUSDT | IDLE | 2.39 | 5.29 | 5.0 | -0.08 | 71812.59 | 7.45 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 2.97 | 2.02 | -0.04 | 242209.18 | 11.07 | skipped_fast |
| REDUSDT | IDLE | 2.19 | 3.89 | 3.23 | -0.03 | 96479.18 | 10.4 | skipped_fast |
| EDELUSDT | IDLE | 1.6 | 3.77 | 2.93 | -0.09 | 235751.71 | 22.8 | skipped_fast |
| BIOUSDT | IDLE | 1.99 | 3.55 | 2.88 | -0.04 | 84616.6 | 4.31 | skipped_fast |
| KITEUSDT | IDLE | 1.72 | 3.07 | 2.51 | -0.04 | 69482.05 | 13.27 | skipped_fast |
| LAUSDT | IDLE | 2.44 | 5.77 | 4.83 | -0.07 | 58507.6 | 27.21 | skipped_fast |
| IOTAUSDT | IDLE | 1.82 | 3.24 | 2.67 | -0.04 | 68478.37 | 22.7 | skipped_fast |
| WAXLUSDT | IDLE | 1.67 | 7.51 | 4.52 | -0.02 | 73463.81 | 73.31 | skipped_fast |
| FLUIDUSDT | IDLE | 1.67 | 2.96 | 2.53 | -0.03 | 3613.52 | 20.65 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.53 | 0.71 | -0.01 | 49331.25 | 15.99 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.59 | 0.09 | -0.01 | 34708.78 | 36.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
