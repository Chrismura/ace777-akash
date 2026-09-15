# Hulk DIGEST — 2026-09-15T18:46:48Z

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
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 11.92 | 10.34 | -0.11 | 86700089.53 | 7.64 | n/a |
| ETHUSDT | IDLE | 2.12 | 4.66 | 4.46 | -0.06 | 538383375.65 | 4.46 | no_map |
| BTCUSDT | IDLE | 1.45 | 2.53 | 2.47 | -0.05 | 599311622.05 | 0.0 | no_map |
| EDELUSDT | IDLE | 2.13 | 34.62 | 12.69 | 0.47 | 494225.35 | 23.42 | no_map |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 5.78 | 5.21 | -0.08 | 588004.1 | 24.88 | tvl≈120,975,427 |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.09 | 7.19 | 6.58 | -0.05 | 452850.74 | 4.02 | empty_tvl |
| ZBCNUSDT | IDLE | 3.29 | 6.57 | 4.87 | -0.04 | 214101.82 | 34.61 | n/a |
| CCUSDT | IDLE | 2.04 | 3.62 | 3.39 | -0.05 | 323244.62 | 11.91 | no_map |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 5.58 | 5.29 | -0.04 | 64495.13 | 28.65 | no_map |
| WUSDT | IDLE | 2.32 | 6.18 | 5.55 | -0.09 | 193353.43 | 25.07 | tvl≈1,423,051,458 |
| CHIPUSDT | IDLE | 2.49 | 8.47 | 7.58 | -0.12 | 99202.8 | 29.77 | no_map |
| BIOUSDT | IDLE | 2.31 | 4.04 | 3.85 | -0.06 | 79070.98 | 28.47 | n/a |
| RWAINCUSDT | IDLE | 2.12 | 3.83 | 2.79 | -0.05 | 8346.68 | 5.75 | no_map |
| REDUSDT | IDLE | 1.06 | 5.41 | 4.78 | -0.06 | 100160.26 | 17.43 | tvl≈2,402,984 |
| RIZEUSDT | IDLE | 1.08 | 9.74 | 7.13 | 0.06 | 51093.85 | 103.38 | no_map |
| FLUIDUSDT | IDLE | 2.0 | 4.27 | 4.1 | -0.08 | 2290.26 | 38.09 | tvl≈2,640,532,544 |
| QNTUSDT | IDLE | 1.55 | 2.73 | 2.53 | -0.04 | 50089.3 | 19.47 | n/a |
| RWAUSDT | IDLE | 1.42 | 2.56 | 1.91 | -0.01 | 52468.16 | 59.66 | no_map |
| TELUSDT | IDLE | 1.45 | 4.78 | 3.11 | -0.07 | 101085.2 | 124.3 | no_map |
| MNSRYUSDT | IDLE | 1.08 | 1.89 | 1.86 | -0.01 | 32749.65 | 77.34 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
