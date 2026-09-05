# Hulk DIGEST — 2026-09-05T14:26:41Z

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
| XRPUSDT | IDLE | 0.61 | 1.17 | 0.3 | 0.01 | 25317876.25 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.26 | 0.48 | 0.27 | 0.0 | 198823722.92 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.26 | 0.1 | 0.0 | 394589244.48 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.91 | 3.6 | 1.51 | 0.03 | 358252.28 | 1.83 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 5.15 | 0.29 | 0.1 | 444005.88 | 3.45 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.71 | 6.21 | 5.44 | -0.06 | 65381.82 | 10.36 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.73 | 0.66 | 0.01 | 300053.58 | 1.83 | skipped_fast |
| REDUSDT | IDLE | 1.92 | 3.4 | 2.89 | 0.01 | 64823.22 | 10.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 2.66 | 0.6 | -0.01 | 188861.84 | 10.48 | skipped_fast |
| RIZEUSDT | IDLE | 1.22 | 11.89 | 3.38 | -0.01 | 155509.51 | 65.87 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 2.86 | 0.46 | 0.03 | 81847.86 | 10.74 | skipped_fast |
| WUSDT | IDLE | 0.56 | 1.03 | 0.63 | 0.05 | 162406.72 | 12.08 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 1.94 | 1.19 | 0.04 | 318921.75 | 1.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.22 | 2.01 | -0.01 | 7385.39 | 32.41 | skipped_fast |
| EDELUSDT | IDLE | 0.13 | 2.29 | 1.4 | -0.03 | 193973.37 | 47.19 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.14 | 0.81 | -0.01 | 74546.97 | 29.28 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.94 | 0.56 | 0.02 | 52544.49 | 14.18 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.15 | 0.78 | -0.02 | 39653.98 | 6.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.3 | 0.01 | -0.0 | 39086.86 | 2.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 820.75 | 21.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
