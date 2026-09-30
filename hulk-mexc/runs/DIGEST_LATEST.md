# Hulk DIGEST — 2026-09-30T19:49:55Z

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
| QNTUSDT | IDLE | 1.72 | 11.41 | 8.32 | 0.07 | 10848735.95 | 7.86 | n/a |
| XRPUSDT | IDLE | 1.36 | 2.44 | 1.89 | -0.0 | 55071255.97 | 2.68 | n/a |
| ETHUSDT | IDLE | 0.93 | 1.65 | 1.46 | -0.01 | 391729380.35 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.83 | 1.49 | 1.11 | 0.0 | 594303376.91 | 0.0 | no_map |
| HBARUSDT | IDLE | 1.47 | 3.17 | 0.38 | 0.04 | 1538511.84 | 10.12 | empty_tvl |
| CCUSDT | IDLE | 2.61 | 4.8 | 2.81 | -0.0 | 880461.88 | 6.36 | no_map |
| WUSDT | IDLE | 2.47 | 4.62 | 2.07 | -0.04 | 872234.49 | 8.29 | tvl≈1,814,579,024 |
| PYTHUSDT | IDLE | 2.02 | 3.69 | 2.31 | -0.03 | 680559.85 | 3.9 | tvl≈173,282,320 |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 7.52 | 6.61 | -0.02 | 70452.74 | 18.44 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 8.95 | 6.17 | -0.01 | 10827.75 | 4.27 | no_map |
| ZBCNUSDT | IDLE | 1.24 | 6.0 | 3.77 | 0.06 | 452806.66 | 0.39 | n/a |
| BIOUSDT | IDLE | 2.62 | 4.68 | 3.72 | -0.0 | 90103.61 | 6.5 | n/a |
| REDUSDT | IDLE | 1.86 | 7.46 | 6.01 | 0.09 | 73867.78 | 13.62 | tvl≈4,485,204 |
| KITEUSDT | IDLE | 1.73 | 4.18 | 2.09 | 0.06 | 77151.62 | 7.08 | no_map |
| TELUSDT | IDLE | 2.11 | 6.12 | 1.94 | 0.05 | 251833.26 | 37.81 | no_map |
| RIZEUSDT | IDLE | 1.78 | 4.13 | 1.83 | 0.06 | 42831.45 | 78.61 | no_map |
| EDELUSDT | IDLE | 0.81 | 8.65 | 0.86 | 0.14 | 190022.06 | 93.66 | no_map |
| FLUIDUSDT | IDLE | 0.88 | 1.64 | 0.83 | 0.01 | 1465.79 | 21.7 | tvl≈2,582,757,473 |
| RWAUSDT | IDLE | 0.56 | 1.03 | 0.58 | 0.0 | 54695.88 | 29.37 | no_map |
| MNSRYUSDT | IDLE | 0.54 | 0.95 | 0.89 | -0.0 | 38612.18 | 58.17 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
