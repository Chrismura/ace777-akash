# Hulk DIGEST — 2026-10-20T17:21:58Z

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
| ETHUSDT | IDLE | 2.1 | 4.03 | 1.09 | 0.02 | 150325664.24 | 0.04 | no_map |
| XRPUSDT | IDLE | 2.06 | 3.93 | 1.31 | 0.02 | 23410399.72 | 0.75 | n/a |
| BTCUSDT | IDLE | 1.33 | 2.55 | 0.77 | 0.01 | 327078045.88 | 0.03 | no_map |
| PYTHUSDT | IDLE | 3.93 | 8.81 | 3.81 | 0.03 | 1002250.45 | 2.64 | tvl≈168,998,113 |
| WUSDT | IDLE | 3.28 | 6.16 | 2.64 | 0.02 | 721689.3 | 12.15 | tvl≈1,591,304,045 |
| QNTUSDT | IDLE | 3.28 | 6.0 | 3.7 | 0.0 | 706227.65 | 3.07 | n/a |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 16.6 | 10.4 | 0.02 | 69517.47 | 63.42 | no_map |
| ZBCNUSDT | IDLE | 3.99 | 7.65 | 2.16 | 0.03 | 192483.33 | 5.09 | n/a |
| CHIPUSDT | IDLE | 2.83 | 10.03 | 4.83 | 0.08 | 141731.05 | 2.21 | no_map |
| EDELUSDT | IDLE | 1.62 | 15.55 | 1.5 | 0.33 | 328170.34 | 11.1 | no_map |
| CCUSDT | IDLE | 1.74 | 3.41 | 0.48 | 0.03 | 411378.89 | 6.58 | no_map |
| BIOUSDT | IDLE | 3.13 | 6.17 | 0.56 | 0.06 | 63192.1 | 8.06 | n/a |
| HBARUSDT | IDLE | 2.52 | 4.66 | 2.54 | 0.01 | 420255.91 | 3.59 | empty_tvl |
| REDUSDT | IDLE | 2.92 | 5.63 | 1.36 | 0.03 | 58896.25 | 15.66 | tvl≈3,520,448 |
| KITEUSDT | IDLE | 2.2 | 4.09 | 2.04 | 0.01 | 85545.27 | 9.04 | no_map |
| IOTAUSDT | IDLE | 3.12 | 6.35 | 2.33 | 0.06 | 91868.47 | 23.48 | no_map |
| LAUSDT | IDLE | 3.07 | 6.0 | 0.97 | 0.03 | 56200.8 | 18.5 | no_map |
| RWAINCUSDT | IDLE | 1.3 | 3.88 | 3.48 | -0.05 | 73729.59 | 5.38 | no_map |
| WAXLUSDT | IDLE | 2.89 | 5.42 | 2.42 | -0.03 | 55514.37 | 75.44 | no_map |
| FLUIDUSDT | IDLE | 2.05 | 4.1 | 0.0 | 0.06 | 4841.78 | 20.94 | tvl≈2,240,817,673 |
| RWAUSDT | IDLE | 0.79 | 1.42 | 1.01 | 0.01 | 51977.96 | 15.7 | no_map |
| MNSRYUSDT | IDLE | 0.83 | 1.52 | 0.96 | -0.0 | 40075.32 | 41.33 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
