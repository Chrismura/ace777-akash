# Hulk DIGEST — 2026-09-22T14:12:45Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 20.05 | 6.78 | 0.06 | 1139887.91 | 20.35 | tvl≈142,912,836 |
| XRPUSDT | IDLE | 2.54 | 4.93 | 0.96 | 0.07 | 113453229.15 | 1.9 | n/a |
| ETHUSDT | IDLE | 0.62 | 1.21 | 0.25 | 0.01 | 538792244.53 | 0.07 | no_map |
| BTCUSDT | IDLE | 0.45 | 0.89 | 0.06 | 0.01 | 955490533.24 | 0.0 | no_map |
| HBARUSDT | IDLE | 2.55 | 5.39 | 0.04 | 0.08 | 1213951.06 | 6.13 | empty_tvl |
| CCUSDT | IDLE | 1.98 | 3.68 | 1.93 | 0.03 | 541560.31 | 7.66 | no_map |
| RIZEUSDT | IDLE | 2.07 | 24.12 | 8.91 | -0.2 | 49425.49 | 87.88 | no_map |
| QNTUSDT | IDLE | 3.45 | 11.12 | 2.53 | 0.08 | 179844.3 | 12.38 | n/a |
| EDELUSDT | IDLE | 2.22 | 9.22 | 5.9 | 0.11 | 253339.76 | 81.53 | no_map |
| WUSDT | IDLE | 1.49 | 2.89 | 0.61 | 0.01 | 371876.48 | 5.86 | tvl≈1,783,810,409 |
| CHIPUSDT | IDLE | 2.41 | 4.42 | 2.67 | -0.01 | 159661.64 | 17.31 | no_map |
| KITEUSDT | IDLE | 1.79 | 6.66 | 2.14 | 0.12 | 115868.98 | 8.28 | no_map |
| ZBCNUSDT | IDLE | 1.53 | 2.87 | 1.22 | -0.0 | 266562.51 | 35.39 | n/a |
| REDUSDT | IDLE | 2.03 | 3.74 | 2.17 | 0.02 | 67174.7 | 16.08 | tvl≈2,820,552 |
| BIOUSDT | IDLE | 1.41 | 2.78 | 0.21 | 0.01 | 117095.52 | 3.43 | n/a |
| TELUSDT | IDLE | 2.12 | 4.24 | 0.0 | 0.04 | 109371.32 | 17.96 | no_map |
| RWAINCUSDT | IDLE | 1.15 | 2.18 | 0.82 | 0.04 | 27035.28 | 33.13 | no_map |
| FLUIDUSDT | IDLE | 1.04 | 2.07 | 0.13 | 0.03 | 8841.72 | 19.72 | tvl≈2,654,188,116 |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.29 | 0.0 | 55105.6 | 43.73 | no_map |
| MNSRYUSDT | IDLE | 0.2 | 0.4 | 0.04 | 0.0 | 39994.47 | 6.44 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
