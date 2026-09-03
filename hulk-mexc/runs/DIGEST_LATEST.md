# Hulk DIGEST — 2026-09-03T00:02:41Z

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
| XRPUSDT | IDLE | 0.63 | 1.21 | 0.31 | -0.0 | 35488598.98 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.88 | 0.27 | -0.01 | 345651005.7 | 0.29 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.65 | 0.22 | -0.0 | 496684734.93 | 0.01 | skipped_fast |
| PYTHUSDT | IDLE | 0.85 | 2.78 | 1.58 | 0.1 | 1361422.01 | 3.48 | skipped_fast |
| CHIPUSDT | IDLE | 1.07 | 4.27 | 0.56 | -0.03 | 919611.62 | 2.34 | skipped_fast |
| ZBCNUSDT | IDLE | 2.88 | 6.9 | 0.81 | -0.01 | 178932.04 | 21.13 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 2.1 | 1.39 | -0.04 | 433319.51 | 9.12 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.53 | 25.82 | 8.6 | 0.2 | 54706.95 | 175.72 | skipped_fast |
| WUSDT | IDLE | 1.75 | 3.2 | 2.01 | 0.0 | 227730.22 | 15.5 | skipped_fast |
| EDELUSDT | IDLE | 1.45 | 5.58 | 4.13 | 0.09 | 148783.49 | 17.23 | skipped_fast |
| RWAINCUSDT | IDLE | 2.17 | 6.33 | 1.37 | 0.1 | 11608.2 | 15.89 | skipped_fast |
| BIOUSDT | IDLE | 1.88 | 3.59 | 1.15 | 0.01 | 70737.72 | 7.79 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 5.59 | 1.11 | 0.15 | 141166.76 | 9.14 | skipped_fast |
| REDUSDT | IDLE | 0.89 | 1.61 | 1.13 | -0.0 | 112200.04 | 9.58 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.2 | 0.74 | 0.01 | 60634.36 | 6.2 | skipped_fast |
| HBARUSDT | IDLE | 0.55 | 1.1 | 0.03 | 0.01 | 191908.62 | 1.34 | skipped_fast |
| RWAUSDT | IDLE | 0.95 | 1.85 | 0.38 | 0.01 | 51967.44 | 22.84 | skipped_fast |
| TELUSDT | IDLE | 0.84 | 1.6 | 0.58 | 0.03 | 75071.15 | 40.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.41 | 0.81 | 0.0 | -0.02 | 2357.2 | 34.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.0 | 20778.94 | 30.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
