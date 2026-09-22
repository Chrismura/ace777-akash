# Hulk DIGEST — 2026-09-22T11:06:09Z

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
| XRPUSDT | IDLE | 1.58 | 2.93 | 1.55 | 0.02 | 110285348.91 | 2.61 | n/a |
| BTCUSDT | IDLE | 0.75 | 1.42 | 0.48 | 0.02 | 1042229641.57 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.63 | 1.19 | 0.41 | 0.01 | 589850170.44 | 0.11 | no_map |
| HBARUSDT | IDLE | 2.85 | 5.69 | 4.41 | 0.04 | 1298937.73 | 1.07 | empty_tvl |
| PYTHUSDT | IDLE | 2.39 | 4.19 | 3.96 | -0.04 | 779751.65 | 3.24 | tvl≈142,912,836 |
| CCUSDT | IDLE | 1.47 | 2.65 | 1.9 | 0.01 | 614602.67 | 6.8 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 5.79 | 5.19 | -0.08 | 167473.56 | 17.36 | no_map |
| KITEUSDT | IDLE | 2.86 | 9.99 | 2.97 | 0.09 | 113537.83 | 9.94 | no_map |
| WUSDT | IDLE | 1.17 | 2.09 | 1.64 | -0.02 | 389702.09 | 5.95 | tvl≈1,783,557,558 |
| REDUSDT | IDLE | 2.24 | 3.98 | 3.36 | 0.01 | 91889.45 | 14.9 | tvl≈2,876,389 |
| ZBCNUSDT | IDLE | 1.66 | 3.01 | 2.01 | 0.0 | 273169.38 | 40.62 | n/a |
| EDELUSDT | IDLE | 1.15 | 5.39 | 1.28 | 0.12 | 232536.51 | 24.65 | no_map |
| BIOUSDT | IDLE | 1.29 | 2.29 | 1.89 | -0.02 | 129128.22 | 7.01 | n/a |
| RWAINCUSDT | IDLE | 0.96 | 2.02 | 0.77 | 0.07 | 26534.2 | 33.15 | no_map |
| QNTUSDT | IDLE | 1.64 | 3.27 | 0.0 | 0.03 | 123240.68 | 17.35 | n/a |
| TELUSDT | IDLE | 1.65 | 3.15 | 0.98 | 0.0 | 110027.47 | 37.04 | no_map |
| RIZEUSDT | IDLE | 0.45 | 4.48 | 1.23 | -0.17 | 50007.15 | 128.97 | no_map |
| RWAUSDT | IDLE | 0.44 | 0.81 | 0.51 | 0.01 | 55348.83 | 21.86 | no_map |
| FLUIDUSDT | IDLE | 0.64 | 1.27 | 0.0 | 0.05 | 8085.72 | 22.13 | tvl≈2,658,122,550 |
| MNSRYUSDT | IDLE | 0.18 | 0.36 | 0.03 | 0.01 | 40343.55 | 12.89 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
