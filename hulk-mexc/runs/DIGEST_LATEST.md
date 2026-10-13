# Hulk DIGEST — 2026-10-13T17:15:34Z

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
| WUSDT | IDLE | 2.12 | 16.19 | 13.18 | -0.23 | 5164846.76 | 7.93 | tvl≈1,688,982,906 |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 8.61 | 5.19 | -0.08 | 2123403.97 | 5.01 | tvl≈186,369,765 |
| XRPUSDT | IDLE | 1.06 | 1.96 | 1.01 | 0.0 | 37181439.16 | 0.73 | n/a |
| ETHUSDT | IDLE | 0.74 | 1.36 | 0.85 | -0.0 | 237319363.24 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.48 | 0.85 | 0.77 | 0.01 | 386547805.59 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.2 | 4.18 | 3.1 | -0.1 | 1302871.87 | 9.78 | n/a |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.46 | 14.13 | 10.74 | -0.09 | 76948.99 | 39.05 | no_map |
| CCUSDT | IDLE | 2.3 | 7.41 | 0.97 | 0.07 | 588317.81 | 8.45 | no_map |
| EDELUSDT | IDLE | 2.46 | 5.03 | 2.99 | 0.04 | 304541.98 | 20.58 | no_map |
| ZBCNUSDT | IDLE | 1.74 | 3.31 | 1.19 | -0.01 | 236397.41 | 15.2 | n/a |
| CHIPUSDT | IDLE | 2.02 | 4.31 | 3.57 | -0.04 | 108672.58 | 10.49 | no_map |
| RWAINCUSDT | IDLE | 2.23 | 4.45 | 0.0 | 0.03 | 30136.24 | 4.79 | no_map |
| REDUSDT | IDLE | 1.53 | 3.24 | 0.62 | -0.02 | 147241.34 | 16.3 | tvl≈3,910,309 |
| HBARUSDT | IDLE | 1.81 | 3.37 | 1.6 | -0.02 | 344040.69 | 4.57 | empty_tvl |
| BIOUSDT | IDLE | 1.36 | 3.0 | 1.08 | -0.03 | 71946.61 | 3.63 | n/a |
| KITEUSDT | IDLE | 1.1 | 2.33 | 0.81 | 0.01 | 60423.28 | 11.81 | no_map |
| TELUSDT | IDLE | 1.56 | 2.89 | 1.52 | -0.01 | 106700.09 | 34.25 | no_map |
| FLUIDUSDT | IDLE | 1.38 | 2.93 | 1.19 | 0.04 | 26423.78 | 15.53 | tvl≈2,378,903,955 |
| MNSRYUSDT | IDLE | 0.57 | 1.04 | 0.71 | -0.02 | 38373.02 | 18.13 | no_map |
| RWAUSDT | IDLE | 0.26 | 0.46 | 0.38 | 0.0 | 52451.71 | 7.72 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
