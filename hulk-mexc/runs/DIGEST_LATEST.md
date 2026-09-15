# Hulk DIGEST — 2026-09-15T08:45:22Z

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
| XRPUSDT | IDLE | 1.51 | 2.68 | 2.21 | 0.0 | 74917535.14 | 2.16 | n/a |
| ETHUSDT | IDLE | 1.07 | 1.9 | 1.55 | -0.02 | 460034233.75 | 0.08 | no_map |
| BTCUSDT | IDLE | 0.89 | 1.57 | 1.37 | -0.01 | 544313839.63 | 0.03 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 22.32 | 15.49 | -0.0 | 147576.16 | 16.76 | tvl≈2,634,302 |
| EDELUSDT | IDLE | 1.74 | 26.01 | 8.82 | 0.32 | 450910.57 | 10.93 | no_map |
| PYTHUSDT | IDLE | 2.52 | 4.46 | 3.8 | -0.03 | 309280.2 | 1.84 | tvl≈124,869,886 |
| CCUSDT | IDLE | 1.14 | 2.12 | 1.01 | 0.0 | 356849.79 | 4.19 | no_map |
| WUSDT | IDLE | 1.77 | 3.13 | 2.75 | -0.05 | 163618.1 | 14.52 | tvl≈1,461,660,855 |
| CHIPUSDT | IDLE | 1.96 | 3.51 | 2.71 | -0.02 | 67548.38 | 17.07 | no_map |
| HBARUSDT | IDLE | 1.59 | 2.86 | 2.18 | -0.0 | 374971.64 | 1.3 | empty_tvl |
| ZBCNUSDT | IDLE | 0.92 | 1.74 | 0.64 | 0.02 | 223966.85 | 11.1 | n/a |
| BIOUSDT | IDLE | 1.07 | 1.87 | 1.75 | -0.01 | 92420.11 | 7.93 | n/a |
| KITEUSDT | IDLE | 1.12 | 2.13 | 0.78 | -0.0 | 63662.42 | 14.06 | no_map |
| FLUIDUSDT | IDLE | 2.23 | 3.9 | 3.75 | -0.04 | 2094.45 | 22.33 | tvl≈2,656,109,190 |
| RWAINCUSDT | IDLE | 0.73 | 1.28 | 1.16 | -0.02 | 6817.32 | 5.58 | no_map |
| QNTUSDT | IDLE | 1.72 | 3.02 | 2.75 | -0.01 | 44652.73 | 6.32 | n/a |
| TELUSDT | IDLE | 1.48 | 3.17 | 3.07 | -0.0 | 98872.82 | 12.67 | no_map |
| RIZEUSDT | IDLE | 0.8 | 7.78 | 1.85 | -0.15 | 48868.46 | 113.99 | no_map |
| RWAUSDT | IDLE | 0.29 | 0.52 | 0.45 | -0.01 | 54047.78 | 14.93 | no_map |
| MNSRYUSDT | IDLE | 0.52 | 0.93 | 0.72 | 0.0 | 34153.57 | 47.21 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
