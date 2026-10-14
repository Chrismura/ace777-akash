# Hulk DIGEST — 2026-10-14T18:21:48Z

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
| PYTHUSDT | IDLE | 3.73 | 8.72 | 4.29 | 0.04 | 2099290.1 | 4.89 | skipped_fast |
| WUSDT | IDLE | 1.06 | 4.62 | 2.13 | -0.06 | 2867246.95 | 9.15 | skipped_fast |
| XRPUSDT | IDLE | 1.74 | 3.06 | 2.82 | -0.03 | 42789011.13 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 1.61 | 2.86 | 2.39 | -0.03 | 192648379.35 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.08 | 1.9 | 1.78 | -0.02 | 424933426.23 | 0.14 | skipped_fast |
| QNTUSDT | IDLE | 2.12 | 4.8 | 3.16 | -0.03 | 1360223.53 | 4.88 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 22.88 | 16.66 | 0.03 | 50982.99 | 56.6 | skipped_fast |
| ZBCNUSDT | IDLE | 2.76 | 4.94 | 3.88 | -0.03 | 185561.23 | 11.85 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 7.3 | 5.52 | -0.07 | 105660.68 | 11.35 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 13.1 | 7.49 | 0.06 | 18030.42 | 21.34 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 2.19 | 1.84 | -0.08 | 424128.19 | 4.26 | skipped_fast |
| REDUSDT | IDLE | 2.59 | 4.95 | 1.53 | 0.0 | 62576.58 | 16.09 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 2.75 | 2.18 | -0.04 | 520193.42 | 3.57 | skipped_fast |
| KITEUSDT | IDLE | 1.93 | 4.93 | 4.31 | 0.01 | 86852.99 | 10.16 | skipped_fast |
| EDELUSDT | IDLE | 1.87 | 3.27 | 3.16 | -0.03 | 168962.45 | 45.31 | skipped_fast |
| BIOUSDT | IDLE | 1.65 | 2.92 | 2.47 | -0.04 | 70588.36 | 7.57 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 5.27 | 0.15 | -0.07 | 30861.81 | 15.47 | skipped_fast |
| TELUSDT | IDLE | 2.22 | 4.34 | 0.66 | 0.02 | 101339.17 | 22.3 | skipped_fast |
| RWAUSDT | IDLE | 1.23 | 2.15 | 2.02 | -0.02 | 56047.21 | 7.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.68 | 0.56 | -0.01 | 37753.55 | 52.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
