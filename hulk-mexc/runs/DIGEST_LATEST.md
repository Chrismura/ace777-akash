# Hulk DIGEST — 2026-09-02T13:43:11Z

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
| ETHUSDT | IDLE | 1.44 | 2.69 | 1.25 | -0.02 | 401570331.25 | 0.13 | no_map |
| XRPUSDT | IDLE | 1.47 | 2.78 | 1.05 | -0.02 | 38896872.98 | 3.0 | n/a |
| BTCUSDT | IDLE | 0.89 | 1.66 | 0.78 | -0.01 | 523310399.68 | 0.62 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 10.87 | 9.51 | 0.04 | 926414.9 | 16.59 | no_map |
| PYTHUSDT | IDLE | 0.98 | 3.44 | 0.29 | 0.11 | 883976.46 | 12.69 | tvl≈122,283,218 |
| WUSDT | IDLE | 1.88 | 3.33 | 2.82 | -0.01 | 412127.94 | 13.78 | tvl≈1,503,187,058 |
| CCUSDT | IDLE | 1.81 | 3.19 | 2.89 | -0.05 | 351802.58 | 7.22 | no_map |
| REDUSDT | IDLE | 2.46 | 5.14 | 0.01 | 0.06 | 151835.54 | 21.55 | tvl≈2,063,162 |
| KITEUSDT | IDLE | 1.58 | 6.19 | 1.25 | 0.15 | 87627.76 | 10.88 | no_map |
| EDELUSDT | IDLE | 1.0 | 5.46 | 2.95 | 0.06 | 172492.54 | 16.43 | no_map |
| ZBCNUSDT | IDLE | 0.94 | 1.99 | 0.95 | -0.01 | 207489.04 | 15.41 | n/a |
| BIOUSDT | IDLE | 1.31 | 2.4 | 1.45 | -0.03 | 72339.6 | 11.86 | n/a |
| RIZEUSDT | IDLE | 1.69 | 6.78 | 2.78 | -0.08 | 39811.77 | 74.39 | no_map |
| QNTUSDT | IDLE | 2.06 | 3.77 | 2.38 | 0.02 | 70067.37 | 6.24 | n/a |
| RWAINCUSDT | IDLE | 1.35 | 3.84 | 2.85 | 0.06 | 11101.7 | 87.58 | no_map |
| HBARUSDT | IDLE | 0.95 | 1.79 | 0.7 | -0.01 | 219042.35 | 1.36 | empty_tvl |
| FLUIDUSDT | IDLE | 1.44 | 2.52 | 2.4 | -0.05 | 427.28 | 21.26 | tvl≈2,599,335,286 |
| TELUSDT | IDLE | 1.47 | 2.9 | 0.29 | -0.01 | 84609.33 | 58.79 | no_map |
| RWAUSDT | IDLE | 0.43 | 0.77 | 0.61 | -0.0 | 51057.97 | 7.7 | no_map |
| MNSRYUSDT | IDLE | 0.4 | 0.73 | 0.49 | -0.01 | 35378.28 | 34.45 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
