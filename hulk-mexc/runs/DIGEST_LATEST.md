# Hulk DIGEST — 2026-09-09T18:13:44Z

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
| XRPUSDT | IDLE | 1.29 | 2.36 | 1.42 | -0.01 | 41863328.98 | 2.11 | n/a |
| BTCUSDT | IDLE | 1.12 | 2.04 | 1.28 | -0.0 | 525101150.26 | 0.0 | no_map |
| ETHUSDT | IDLE | 1.09 | 2.0 | 1.22 | -0.0 | 337544028.79 | 0.04 | no_map |
| PYTHUSDT | IDLE | 2.4 | 4.47 | 2.26 | 0.03 | 581097.77 | 1.79 | tvl≈123,057,268 |
| CCUSDT | IDLE | 1.72 | 3.01 | 2.91 | -0.04 | 539440.33 | 6.79 | no_map |
| EDELUSDT | IDLE | 3.22 | 5.88 | 3.79 | -0.02 | 182891.87 | 57.8 | no_map |
| RIZEUSDT | IDLE | 2.14 | 22.82 | 18.1 | -0.02 | 70825.09 | 115.12 | no_map |
| WUSDT | IDLE | 2.63 | 5.15 | 0.71 | 0.01 | 178727.5 | 3.86 | tvl≈1,560,397,324 |
| ZBCNUSDT | IDLE | 2.58 | 4.92 | 1.88 | 0.03 | 197280.97 | 17.37 | n/a |
| BIOUSDT | IDLE | 1.71 | 3.2 | 1.42 | -0.03 | 96944.6 | 7.41 | n/a |
| CHIPUSDT | IDLE | 1.36 | 5.22 | 2.69 | 0.07 | 109705.44 | 14.01 | no_map |
| REDUSDT | IDLE | 1.78 | 3.39 | 1.11 | 0.02 | 60574.44 | 18.13 | tvl≈2,417,204 |
| KITEUSDT | IDLE | 1.42 | 2.7 | 0.95 | 0.01 | 64491.96 | 11.31 | no_map |
| HBARUSDT | IDLE | 1.11 | 2.03 | 1.33 | -0.02 | 405515.24 | 1.28 | empty_tvl |
| TELUSDT | IDLE | 2.38 | 4.29 | 3.1 | 0.03 | 102113.77 | 27.6 | no_map |
| RWAINCUSDT | IDLE | 1.33 | 2.4 | 1.69 | -0.0 | 7439.4 | 11.08 | no_map |
| FLUIDUSDT | IDLE | 2.03 | 3.56 | 3.29 | -0.04 | 414.4 | 13.0 | tvl≈2,662,429,977 |
| RWAUSDT | IDLE | 1.41 | 2.56 | 1.71 | -0.0 | 54479.08 | 14.51 | no_map |
| QNTUSDT | IDLE | 1.23 | 2.26 | 1.37 | -0.02 | 45652.98 | 5.97 | n/a |
| MNSRYUSDT | IDLE | 0.3 | 0.57 | 0.23 | 0.01 | 23095.93 | 43.5 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
