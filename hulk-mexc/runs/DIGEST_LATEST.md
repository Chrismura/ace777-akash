# Hulk DIGEST — 2026-10-24T13:27:39Z

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
| XRPUSDT | IDLE | 0.61 | 1.17 | 0.31 | -0.03 | 28668911.11 | 1.56 | skipped_fast |
| ETHUSDT | IDLE | 0.42 | 0.79 | 0.29 | -0.02 | 111525252.17 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.46 | 0.08 | -0.01 | 269026648.91 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 3.22 | 5.72 | 4.85 | -0.03 | 664567.51 | 12.93 | skipped_fast |
| WUSDT | IDLE | 1.38 | 2.99 | 2.9 | -0.08 | 1009629.62 | 41.18 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 2.27 | 2.11 | -0.03 | 620204.72 | 1.45 | skipped_fast |
| LAUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 21.16 | 12.24 | 0.14 | 104852.8 | 34.23 | skipped_fast |
| REDUSDT | IDLE | 2.08 | 7.14 | 6.67 | 0.05 | 90920.3 | 15.63 | skipped_fast |
| RWAINCUSDT | IDLE | 2.59 | 5.11 | 0.48 | 0.04 | 45736.44 | 5.34 | skipped_fast |
| CCUSDT | IDLE | 1.57 | 2.76 | 2.47 | -0.03 | 229623.14 | 9.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 3.95 | 3.61 | -0.09 | 199582.11 | 37.22 | skipped_fast |
| QNTUSDT | IDLE | 1.22 | 2.29 | 1.0 | -0.01 | 441534.24 | 0.56 | skipped_fast |
| CHIPUSDT | IDLE | 1.37 | 2.94 | 1.39 | -0.04 | 73738.4 | 16.48 | skipped_fast |
| WAXLUSDT | IDLE | 2.41 | 7.23 | 4.61 | 0.03 | 61884.82 | 38.57 | skipped_fast |
| KITEUSDT | IDLE | 0.84 | 1.47 | 1.34 | -0.03 | 57881.42 | 9.41 | skipped_fast |
| BIOUSDT | IDLE | 0.71 | 1.26 | 1.12 | -0.03 | 78915.53 | 4.34 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 1.78 | 1.0 | 0.01 | 62536.01 | 13.4 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.41 | 0.54 | -0.04 | 190462.96 | 11.73 | skipped_fast |
| FLUIDUSDT | IDLE | 1.23 | 2.19 | 2.15 | -0.02 | 11099.8 | 40.75 | skipped_fast |
| IOTAUSDT | IDLE | 0.75 | 1.4 | 0.63 | -0.02 | 75097.79 | 27.32 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.79 | 0.47 | -0.01 | 52630.36 | 15.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.93 | 0.4 | -0.01 | 38897.32 | 69.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
