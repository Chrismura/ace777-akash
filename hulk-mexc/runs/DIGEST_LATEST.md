# Hulk DIGEST — 2026-09-27T22:13:43Z

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
| QNTUSDT | IDLE | 1.77 | 31.91 | 3.47 | 0.84 | 8905273.8 | 19.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.94 | 4.6 | 4.24 | 0.04 | 2319399.92 | 4.82 | skipped_fast |
| WUSDT | IDLE | 1.36 | 7.72 | 5.28 | 0.2 | 4965184.6 | 11.07 | skipped_fast |
| XRPUSDT | IDLE | 1.19 | 2.09 | 1.97 | -0.01 | 40378302.38 | 0.66 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 0.98 | 0.88 | -0.0 | 201984462.0 | 0.22 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.6 | 0.53 | 0.0 | 431952238.34 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.23 | 4.12 | 2.25 | 0.0 | 628257.05 | 9.57 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 24.25 | 18.31 | -0.23 | 54057.97 | 28.4 | skipped_fast |
| ZBCNUSDT | IDLE | 2.41 | 4.23 | 3.96 | -0.02 | 218076.68 | 21.89 | skipped_fast |
| HBARUSDT | IDLE | 1.27 | 2.28 | 1.68 | 0.01 | 745928.06 | 1.07 | skipped_fast |
| EDELUSDT | IDLE | 1.98 | 7.71 | 5.49 | -0.13 | 144103.53 | 23.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.92 | 3.5 | 3.17 | -0.05 | 97943.6 | 13.01 | skipped_fast |
| RWAINCUSDT | IDLE | 2.07 | 21.47 | 2.16 | 0.24 | 29030.58 | 125.49 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 2.62 | 0.75 | 0.01 | 124139.37 | 8.51 | skipped_fast |
| REDUSDT | IDLE | 1.5 | 2.62 | 2.56 | 0.01 | 64023.64 | 8.28 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.49 | 1.47 | -0.02 | 82946.38 | 6.35 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 4.06 | 2.16 | 0.14 | 176323.01 | 37.75 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 1.47 | 1.21 | 0.03 | 2828.51 | 18.34 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.5 | 0.42 | 0.01 | 58191.18 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.41 | 0.05 | 0.01 | 40168.69 | 12.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
