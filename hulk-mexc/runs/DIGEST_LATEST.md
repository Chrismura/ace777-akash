# Hulk DIGEST — 2026-10-19T07:56:08Z

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
| ETHUSDT | IDLE | 0.64 | 1.18 | 0.61 | 0.01 | 138080790.19 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.63 | 1.16 | 0.61 | 0.02 | 31451338.26 | 1.52 | n/a |
| BTCUSDT | IDLE | 0.52 | 0.96 | 0.52 | 0.01 | 313345600.47 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.08 | 3.02 | 1.52 | -0.03 | 1016375.4 | 1.33 | tvl≈166,335,157 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 11.35 | 5.41 | 0.02 | 312944.14 | 25.79 | n/a |
| WUSDT | IDLE | 1.58 | 2.85 | 2.66 | -0.04 | 523155.95 | 14.0 | tvl≈1,572,270,312 |
| QNTUSDT | IDLE | 2.0 | 5.46 | 0.89 | 0.03 | 673942.02 | 2.0 | n/a |
| EDELUSDT | IDLE | 2.49 | 5.3 | 1.51 | 0.03 | 236359.53 | 10.95 | no_map |
| HBARUSDT | IDLE | 0.72 | 1.69 | 0.96 | -0.03 | 833743.38 | 8.29 | empty_tvl |
| CCUSDT | IDLE | 0.82 | 1.61 | 0.21 | 0.01 | 300305.03 | 6.79 | no_map |
| RWAINCUSDT | IDLE | 1.71 | 5.06 | 2.8 | -0.02 | 77113.94 | 26.63 | no_map |
| REDUSDT | IDLE | 1.07 | 1.93 | 1.39 | -0.0 | 94132.89 | 9.48 | tvl≈3,448,494 |
| CHIPUSDT | IDLE | 1.1 | 3.04 | 0.99 | 0.01 | 78503.99 | 13.97 | no_map |
| BIOUSDT | IDLE | 1.03 | 1.92 | 0.88 | -0.0 | 85407.54 | 12.65 | n/a |
| KITEUSDT | IDLE | 1.03 | 1.83 | 1.52 | 0.01 | 65523.33 | 11.33 | no_map |
| FLUIDUSDT | IDLE | 2.24 | 6.06 | 1.9 | 0.01 | 7630.81 | 21.67 | tvl≈2,231,487,153 |
| RIZEUSDT | IDLE | 0.33 | 1.74 | 0.67 | -0.03 | 58642.17 | 58.89 | no_map |
| RWAUSDT | IDLE | 1.07 | 1.91 | 1.48 | 0.01 | 54292.48 | 15.89 | no_map |
| IOTAUSDT | IDLE | 0.97 | 1.84 | 0.68 | -0.01 | 65247.71 | 31.07 | no_map |
| LAUSDT | IDLE | 0.92 | 1.79 | 0.37 | -0.02 | 57703.4 | 20.66 | no_map |
| WAXLUSDT | IDLE | 0.66 | 3.02 | 1.53 | -0.02 | 85711.81 | 67.28 | no_map |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.11 | -0.0 | 38835.94 | 15.66 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
