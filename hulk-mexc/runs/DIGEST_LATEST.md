# Hulk DIGEST — 2026-10-28T18:42:42Z

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
| ETHUSDT | IDLE | 0.98 | 1.91 | 0.39 | 0.0 | 178335028.37 | 0.59 | no_map |
| XRPUSDT | IDLE | 0.92 | 1.81 | 0.24 | 0.0 | 21767566.07 | 2.26 | n/a |
| BTCUSDT | IDLE | 0.57 | 1.11 | 0.22 | 0.01 | 294147827.52 | 0.47 | no_map |
| CCUSDT | IDLE | 2.86 | 6.56 | 2.39 | 0.0 | 406384.97 | 5.03 | no_map |
| CHIPUSDT | IDLE | 2.41 | 10.65 | 7.02 | -0.08 | 219517.43 | 18.25 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 8.4 | 7.37 | -0.03 | 35126.59 | 27.42 | no_map |
| WUSDT | IDLE | 1.3 | 2.52 | 0.58 | -0.0 | 426189.34 | 15.64 | tvl≈1,496,419,662 |
| PYTHUSDT | IDLE | 1.33 | 2.6 | 0.4 | -0.02 | 396865.23 | 47.13 | tvl≈158,727,627 |
| ZBCNUSDT | IDLE | 1.51 | 2.84 | 1.15 | -0.06 | 263463.0 | 10.63 | n/a |
| QNTUSDT | IDLE | 1.52 | 2.9 | 0.98 | -0.02 | 401524.71 | 11.19 | n/a |
| HBARUSDT | IDLE | 0.91 | 1.77 | 0.28 | -0.0 | 537316.12 | 6.6 | empty_tvl |
| EDELUSDT | IDLE | 1.19 | 2.24 | 0.94 | 0.0 | 182602.62 | 27.63 | no_map |
| BIOUSDT | IDLE | 1.53 | 3.02 | 0.26 | 0.01 | 84803.59 | 92.17 | n/a |
| REDUSDT | IDLE | 0.79 | 1.53 | 0.34 | -0.02 | 54723.22 | 14.5 | tvl≈3,765,901 |
| RIZEUSDT | IDLE | 1.05 | 1.91 | 1.24 | 0.02 | 23456.03 | 34.37 | no_map |
| LAUSDT | IDLE | 1.25 | 2.34 | 1.09 | -0.05 | 57814.23 | 22.44 | no_map |
| KITEUSDT | IDLE | 0.72 | 1.4 | 0.27 | -0.02 | 58230.74 | 111.15 | no_map |
| IOTAUSDT | IDLE | 1.12 | 2.24 | 0.0 | -0.01 | 75254.7 | 52.52 | no_map |
| WAXLUSDT | IDLE | 1.05 | 2.09 | 0.12 | -0.0 | 55759.74 | 45.1 | no_map |
| RWAUSDT | IDLE | 0.63 | 1.12 | 0.95 | -0.01 | 55419.69 | 48.08 | no_map |
| FLUIDUSDT | IDLE | 0.53 | 1.77 | 0.05 | -0.01 | 6836.16 | 21.68 | tvl≈2,220,865,451 |
| MNSRYUSDT | IDLE | 0.28 | 0.51 | 0.35 | 0.01 | 35574.95 | 54.03 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
