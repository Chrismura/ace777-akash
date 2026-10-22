# Hulk DIGEST — 2026-10-22T23:38:27Z

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
| XRPUSDT | IDLE | 0.77 | 1.45 | 0.62 | -0.04 | 30049042.56 | 0.77 | n/a |
| ETHUSDT | IDLE | 0.62 | 1.13 | 0.79 | -0.04 | 234581522.68 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.34 | 0.63 | 0.29 | -0.04 | 462857183.04 | 0.0 | no_map |
| WUSDT | IDLE | 1.1 | 2.99 | 2.08 | -0.09 | 1238224.01 | 17.47 | tvl≈1,534,547,610 |
| HBARUSDT | IDLE | 0.8 | 1.59 | 0.04 | -0.05 | 1247584.94 | 8.78 | empty_tvl |
| PYTHUSDT | IDLE | 1.67 | 3.99 | 3.68 | -0.09 | 563994.12 | 1.39 | tvl≈164,380,455 |
| EDELUSDT | IDLE | 1.47 | 3.9 | 1.42 | -0.07 | 514767.93 | 18.71 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.78 | 7.42 | 5.64 | -0.06 | 39321.77 | 2.27 | no_map |
| QNTUSDT | IDLE | 0.9 | 2.44 | 2.29 | -0.09 | 674644.09 | 2.15 | n/a |
| CHIPUSDT | IDLE | 1.25 | 5.03 | 1.85 | -0.08 | 202191.78 | 15.86 | no_map |
| RWAINCUSDT | IDLE | 1.8 | 3.47 | 0.84 | 0.02 | 49117.42 | 5.62 | no_map |
| ZBCNUSDT | IDLE | 1.05 | 2.25 | 0.4 | -0.04 | 197760.04 | 18.23 | n/a |
| CCUSDT | IDLE | 0.62 | 1.56 | 0.55 | -0.08 | 249622.16 | 5.86 | no_map |
| REDUSDT | IDLE | 1.03 | 1.94 | 0.92 | -0.06 | 86674.5 | 9.29 | tvl≈3,506,358 |
| BIOUSDT | IDLE | 0.81 | 1.64 | 1.14 | -0.07 | 60730.64 | 4.28 | n/a |
| KITEUSDT | IDLE | 0.75 | 1.43 | 0.41 | -0.02 | 60614.79 | 9.19 | no_map |
| FLUIDUSDT | IDLE | 1.57 | 4.16 | 1.64 | -0.08 | 7934.68 | 21.12 | tvl≈2,201,643,252 |
| IOTAUSDT | IDLE | 0.91 | 1.85 | 1.32 | -0.07 | 79303.64 | 15.9 | no_map |
| LAUSDT | IDLE | 0.74 | 1.98 | 0.7 | -0.08 | 55237.39 | 25.81 | no_map |
| WAXLUSDT | IDLE | 0.72 | 2.31 | 1.34 | -0.11 | 58722.97 | 50.04 | no_map |
| MNSRYUSDT | IDLE | 0.66 | 1.16 | 1.13 | -0.01 | 37206.16 | 65.78 | no_map |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.08 | -0.02 | 51783.99 | 15.95 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
