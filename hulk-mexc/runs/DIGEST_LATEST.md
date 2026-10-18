# Hulk DIGEST — 2026-10-18T12:01:28Z

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
| XRPUSDT | IDLE | 0.63 | 1.2 | 0.46 | -0.01 | 20131662.73 | 0.77 | n/a |
| ETHUSDT | IDLE | 0.5 | 0.93 | 0.5 | -0.01 | 89940658.11 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.43 | 0.81 | 0.28 | 0.01 | 192746587.68 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.42 | 3.87 | 1.08 | -0.07 | 1393993.6 | 2.53 | tvl≈178,156,305 |
| WUSDT | IDLE | 1.37 | 3.28 | 1.63 | -0.08 | 1073670.46 | 16.45 | tvl≈1,581,660,490 |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 4.02 | 14.22 | 11.74 | -0.01 | 71081.95 | 56.78 | no_map |
| QNTUSDT | IDLE | 1.75 | 3.42 | 0.57 | -0.03 | 558238.08 | 2.02 | n/a |
| HBARUSDT | IDLE | 1.73 | 3.84 | 1.23 | 0.07 | 482873.19 | 11.28 | empty_tvl |
| CHIPUSDT | IDLE | 1.87 | 3.51 | 2.85 | -0.08 | 70304.66 | 14.33 | no_map |
| CCUSDT | IDLE | 0.98 | 1.78 | 1.18 | -0.03 | 251884.23 | 8.91 | no_map |
| EDELUSDT | IDLE | 1.22 | 3.25 | 1.45 | -0.08 | 226979.57 | 33.8 | no_map |
| REDUSDT | IDLE | 1.54 | 2.75 | 2.19 | -0.03 | 76407.0 | 9.46 | tvl≈3,455,600 |
| ZBCNUSDT | IDLE | 0.82 | 1.61 | 0.26 | -0.02 | 159446.43 | 13.76 | n/a |
| RIZEUSDT | IDLE | 1.63 | 3.11 | 0.97 | 0.01 | 46552.34 | 60.6 | no_map |
| KITEUSDT | IDLE | 1.08 | 2.05 | 0.72 | -0.05 | 67036.78 | 13.04 | no_map |
| BIOUSDT | IDLE | 0.91 | 1.65 | 1.12 | -0.04 | 81541.19 | 4.2 | n/a |
| RWAINCUSDT | IDLE | 0.64 | 1.16 | 0.83 | 0.01 | 14712.45 | 5.25 | no_map |
| IOTAUSDT | IDLE | 1.19 | 2.11 | 1.77 | -0.05 | 68448.43 | 28.85 | no_map |
| LAUSDT | IDLE | 0.98 | 1.79 | 1.14 | -0.06 | 54654.89 | 25.99 | no_map |
| FLUIDUSDT | IDLE | 0.98 | 1.71 | 1.68 | -0.04 | 2785.76 | 19.18 | tvl≈2,239,432,455 |
| MNSRYUSDT | IDLE | 0.35 | 0.69 | 0.03 | -0.0 | 33415.62 | 12.78 | no_map |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | 0.0 | 50128.2 | 7.96 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
