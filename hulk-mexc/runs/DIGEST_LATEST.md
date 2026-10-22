# Hulk DIGEST — 2026-10-22T16:33:43Z

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
| WUSDT | IDLE | 0.95 | 3.85 | 2.66 | -0.15 | 1885994.06 | 17.32 | tvl≈1,558,727,367 |
| ETHUSDT | IDLE | 0.71 | 1.25 | 1.14 | -0.05 | 188838835.27 | 0.42 | no_map |
| XRPUSDT | IDLE | 0.72 | 1.34 | 0.66 | -0.04 | 28680020.37 | 1.51 | n/a |
| BTCUSDT | IDLE | 0.5 | 0.9 | 0.72 | -0.04 | 496859149.82 | 0.0 | no_map |
| HBARUSDT | IDLE | 1.11 | 2.06 | 1.65 | -0.07 | 1301512.44 | 6.24 | empty_tvl |
| QNTUSDT | IDLE | 1.37 | 3.91 | 2.89 | -0.03 | 1166139.19 | 1.05 | n/a |
| EDELUSDT | IDLE | 2.47 | 5.61 | 4.25 | -0.07 | 538727.58 | 24.84 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.8 | 6.62 | 5.74 | -0.08 | 226299.22 | 19.43 | n/a |
| PYTHUSDT | IDLE | 1.22 | 3.07 | 2.69 | -0.09 | 560550.12 | 1.35 | tvl≈166,516,791 |
| RWAINCUSDT | IDLE | 2.36 | 4.49 | 1.54 | -0.02 | 58996.49 | 11.2 | no_map |
| CHIPUSDT | IDLE | 0.68 | 3.0 | 0.95 | -0.08 | 321462.9 | 15.95 | no_map |
| CCUSDT | IDLE | 0.62 | 2.15 | 0.75 | -0.06 | 326902.72 | 9.71 | no_map |
| RIZEUSDT | IDLE | 1.77 | 4.32 | 2.96 | 0.06 | 38942.7 | 59.22 | no_map |
| BIOUSDT | IDLE | 1.18 | 2.68 | 2.15 | -0.07 | 77747.76 | 4.23 | n/a |
| REDUSDT | IDLE | 1.16 | 2.09 | 1.57 | -0.06 | 100559.51 | 21.21 | tvl≈3,559,551 |
| KITEUSDT | IDLE | 0.83 | 1.55 | 0.68 | -0.03 | 60611.63 | 10.84 | no_map |
| LAUSDT | IDLE | 1.17 | 3.61 | 2.87 | -0.09 | 58422.11 | 20.35 | no_map |
| IOTAUSDT | IDLE | 1.0 | 2.16 | 1.68 | -0.06 | 78662.35 | 13.46 | no_map |
| RWAUSDT | IDLE | 0.9 | 1.6 | 1.34 | -0.02 | 52254.95 | 15.97 | no_map |
| WAXLUSDT | IDLE | 0.91 | 3.22 | 2.33 | -0.11 | 58355.4 | 53.95 | no_map |
| FLUIDUSDT | IDLE | 0.3 | 1.67 | 1.53 | -0.07 | 19162.16 | 21.63 | tvl≈2,212,873,699 |
| MNSRYUSDT | IDLE | 0.29 | 0.53 | 0.31 | -0.01 | 39796.31 | 55.51 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
