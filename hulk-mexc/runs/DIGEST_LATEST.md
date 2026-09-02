# Hulk DIGEST — 2026-09-02T00:29:24Z

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
| XRPUSDT | IDLE | 1.09 | 1.97 | 1.36 | -0.03 | 35618263.51 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.58 | 1.08 | 0.47 | -0.02 | 346051500.6 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.9 | 0.4 | -0.02 | 527492991.37 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.81 | 7.41 | 1.06 | 0.06 | 722860.96 | 13.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 9.45 | 4.68 | 0.12 | 742343.78 | 2.28 | skipped_fast |
| WUSDT | IDLE | 2.51 | 4.39 | 4.17 | 0.02 | 419329.74 | 14.68 | skipped_fast |
| ZBCNUSDT | IDLE | 2.42 | 4.24 | 3.95 | -0.04 | 196669.19 | 2.75 | skipped_fast |
| REDUSDT | IDLE | 2.03 | 5.5 | 3.47 | 0.08 | 120250.17 | 11.39 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.82 | 1.34 | -0.07 | 333112.41 | 9.7 | skipped_fast |
| EDELUSDT | IDLE | 1.02 | 9.32 | 1.39 | -0.04 | 158014.63 | 8.81 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 4.22 | 1.93 | -0.04 | 40649.79 | 74.83 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 2.11 | 0.51 | 0.04 | 68889.87 | 11.31 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 1.82 | 0.85 | -0.04 | 69140.41 | 3.92 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 1.95 | 1.91 | -0.02 | 5487.56 | 17.68 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.43 | 1.41 | -0.01 | 250762.35 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 2.8 | 1.1 | 0.04 | 46473.95 | 6.29 | skipped_fast |
| TELUSDT | IDLE | 1.48 | 2.69 | 1.85 | -0.04 | 93799.7 | 66.73 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 1.01 | 0.15 | -0.03 | 58605.74 | 7.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.48 | 0.96 | 0.0 | -0.04 | 244.85 | 21.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.7 | 0.29 | -0.02 | 34612.82 | 53.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
