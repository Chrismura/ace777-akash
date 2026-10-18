# Hulk DIGEST — 2026-10-18T11:01:30Z

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
| XRPUSDT | IDLE | 0.63 | 1.2 | 0.45 | -0.01 | 19841279.3 | 0.77 | n/a |
| ETHUSDT | IDLE | 0.49 | 0.93 | 0.4 | -0.01 | 91896456.96 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.42 | 0.81 | 0.22 | 0.01 | 192598338.23 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.51 | 4.09 | 1.31 | -0.07 | 1397952.52 | 1.27 | tvl≈178,156,305 |
| WUSDT | IDLE | 1.28 | 2.73 | 2.64 | -0.09 | 1068807.14 | 13.59 | tvl≈1,571,703,791 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 7.24 | 5.75 | -0.09 | 220865.03 | 15.13 | no_map |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.97 | 14.04 | 11.79 | -0.0 | 70369.81 | 69.24 | no_map |
| QNTUSDT | IDLE | 1.77 | 3.42 | 0.75 | -0.03 | 603041.33 | 0.5 | n/a |
| HBARUSDT | IDLE | 1.92 | 3.98 | 0.34 | 0.06 | 420996.68 | 10.14 | empty_tvl |
| CCUSDT | IDLE | 1.15 | 2.12 | 1.15 | -0.02 | 246744.15 | 4.93 | no_map |
| REDUSDT | IDLE | 1.82 | 3.36 | 1.92 | -0.03 | 77720.72 | 10.16 | tvl≈3,395,274 |
| CHIPUSDT | IDLE | 1.61 | 3.34 | 3.11 | -0.08 | 69345.1 | 9.52 | no_map |
| ZBCNUSDT | IDLE | 0.8 | 1.57 | 0.16 | -0.03 | 159047.69 | 14.28 | n/a |
| BIOUSDT | IDLE | 0.89 | 1.65 | 0.87 | -0.04 | 74643.75 | 8.4 | n/a |
| KITEUSDT | IDLE | 1.1 | 2.05 | 0.99 | -0.06 | 71365.79 | 83.7 | no_map |
| RIZEUSDT | IDLE | 0.94 | 1.84 | 0.23 | 0.0 | 45543.46 | 56.76 | no_map |
| RWAINCUSDT | IDLE | 0.39 | 1.21 | 0.31 | 0.03 | 13992.54 | 20.89 | no_map |
| LAUSDT | IDLE | 0.92 | 1.6 | 1.58 | -0.07 | 53989.53 | 18.64 | no_map |
| IOTAUSDT | IDLE | 0.85 | 1.48 | 1.46 | -0.04 | 68628.94 | 24.31 | no_map |
| FLUIDUSDT | IDLE | 0.76 | 1.52 | 0.0 | -0.02 | 2872.36 | 21.58 | tvl≈2,239,432,455 |
| MNSRYUSDT | IDLE | 0.37 | 0.73 | 0.07 | -0.0 | 32364.13 | 12.78 | no_map |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.0 | 50624.54 | 7.96 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
