# Hulk DIGEST — 2026-09-05T21:29:33Z

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
| XRPUSDT | IDLE | 0.62 | 1.17 | 0.48 | 0.02 | 22472055.85 | 2.11 | skipped_fast |
| ETHUSDT | IDLE | 0.53 | 1.04 | 0.13 | 0.01 | 158912020.36 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.65 | 0.44 | 0.0 | 368513560.62 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.45 | 6.2 | 3.58 | 0.06 | 452123.13 | 5.16 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 17.65 | 14.79 | -0.08 | 139258.51 | 62.72 | skipped_fast |
| ZBCNUSDT | IDLE | 2.66 | 4.95 | 2.43 | -0.03 | 198229.08 | 24.24 | skipped_fast |
| RWAINCUSDT | IDLE | 2.82 | 5.31 | 2.24 | 0.02 | 7801.52 | 15.97 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.5 | 2.1 | 0.03 | 299397.26 | 6.41 | skipped_fast |
| PYTHUSDT | IDLE | 0.93 | 1.76 | 0.65 | 0.01 | 331006.28 | 1.82 | skipped_fast |
| REDUSDT | IDLE | 1.11 | 2.11 | 0.72 | 0.04 | 60423.59 | 17.39 | skipped_fast |
| WUSDT | IDLE | 0.73 | 1.44 | 0.18 | 0.04 | 139429.25 | 18.07 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.69 | 0.39 | 0.05 | 82731.1 | 7.12 | skipped_fast |
| KITEUSDT | IDLE | 0.62 | 1.52 | 0.61 | -0.06 | 63267.38 | 12.67 | skipped_fast |
| EDELUSDT | IDLE | 0.12 | 2.2 | 0.56 | -0.02 | 165355.36 | 18.87 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.2 | 0.33 | 0.04 | 332483.59 | 1.23 | skipped_fast |
| QNTUSDT | IDLE | 1.3 | 2.46 | 0.98 | 0.02 | 42406.99 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.73 | 1.41 | 0.28 | 0.03 | 52005.86 | 13.99 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 1.76 | 0.63 | 0.01 | 67421.81 | 52.1 | skipped_fast |
| FLUIDUSDT | IDLE | 0.8 | 1.59 | 0.0 | 0.02 | 516.89 | 20.68 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.15 | 0.0 | 37968.2 | 13.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
