# Hulk DIGEST — 2026-10-22T15:33:37Z

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
| WUSDT | IDLE | 1.0 | 4.99 | 4.03 | -0.17 | 2192882.02 | 15.86 | skipped_fast |
| XRPUSDT | IDLE | 0.86 | 1.53 | 1.25 | -0.04 | 29100114.52 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.7 | 1.25 | 0.97 | -0.05 | 199097169.67 | 0.63 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.02 | 0.84 | -0.04 | 500882389.35 | 0.07 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.04 | 1.89 | -0.07 | 1320587.94 | 7.51 | skipped_fast |
| QNTUSDT | IDLE | 1.19 | 3.0 | 2.81 | -0.03 | 1237136.75 | 1.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.78 | 5.7 | 5.18 | -0.06 | 548445.27 | 34.13 | skipped_fast |
| PYTHUSDT | IDLE | 1.14 | 2.9 | 2.19 | -0.09 | 591515.73 | 2.7 | skipped_fast |
| ZBCNUSDT | IDLE | 2.22 | 5.67 | 5.35 | -0.09 | 226824.46 | 10.35 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 3.38 | 2.81 | -0.06 | 330664.14 | 8.81 | skipped_fast |
| RWAINCUSDT | IDLE | 2.47 | 4.49 | 2.98 | -0.01 | 59987.63 | 56.66 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 3.0 | 2.24 | -0.09 | 337196.09 | 18.51 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.68 | 2.07 | -0.08 | 77060.08 | 8.46 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.09 | 1.53 | -0.07 | 100527.82 | 16.27 | skipped_fast |
| KITEUSDT | IDLE | 0.89 | 1.65 | 0.85 | -0.03 | 59803.94 | 10.86 | skipped_fast |
| LAUSDT | IDLE | 1.34 | 4.04 | 3.83 | -0.09 | 58027.37 | 42.6 | skipped_fast |
| IOTAUSDT | IDLE | 1.02 | 2.21 | 1.76 | -0.07 | 78970.98 | 20.15 | skipped_fast |
| WAXLUSDT | IDLE | 0.99 | 3.33 | 3.18 | -0.11 | 58985.23 | 47.85 | skipped_fast |
| FLUIDUSDT | IDLE | 0.62 | 3.48 | 3.37 | -0.06 | 18878.33 | 21.55 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.44 | 1.18 | -0.01 | 52419.99 | 31.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.75 | 4.32 | 2.67 | 0.04 | 57715.71 | 378.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.1 | -0.01 | 39399.34 | 55.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
