# Hulk DIGEST — 2026-10-13T16:05:09Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 17.52 | 13.78 | -0.29 | 5698399.17 | 15.91 | tvl≈1,688,982,906 |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.81 | 8.67 | 7.42 | -0.12 | 2289735.02 | 5.13 | tvl≈186,369,765 |
| XRPUSDT | IDLE | 1.22 | 2.35 | 0.54 | -0.0 | 38786604.6 | 0.73 | n/a |
| ETHUSDT | IDLE | 0.8 | 1.57 | 0.26 | -0.0 | 236565980.46 | 0.44 | no_map |
| BTCUSDT | IDLE | 0.45 | 0.85 | 0.34 | 0.01 | 381985278.86 | 0.0 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 8.77 | 6.23 | -0.1 | 1284601.04 | 5.38 | n/a |
| CCUSDT | IDLE | 2.44 | 7.7 | 2.13 | 0.05 | 594451.88 | 14.79 | no_map |
| EDELUSDT | IDLE | 3.55 | 7.44 | 3.25 | 0.03 | 324810.69 | 23.53 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 9.65 | 8.8 | -0.07 | 64021.48 | 116.41 | no_map |
| ZBCNUSDT | IDLE | 1.76 | 3.31 | 1.39 | -0.01 | 241216.09 | 22.19 | n/a |
| CHIPUSDT | IDLE | 2.01 | 4.31 | 3.37 | -0.04 | 114484.33 | 12.23 | no_map |
| HBARUSDT | IDLE | 1.98 | 3.65 | 2.07 | -0.04 | 361780.43 | 8.04 | empty_tvl |
| REDUSDT | IDLE | 1.44 | 2.91 | 1.47 | -0.03 | 171246.91 | 16.51 | tvl≈3,910,309 |
| RWAINCUSDT | IDLE | 2.03 | 3.7 | 2.46 | -0.02 | 31382.99 | 34.66 | no_map |
| BIOUSDT | IDLE | 1.39 | 3.0 | 1.55 | -0.04 | 74469.97 | 7.3 | n/a |
| KITEUSDT | IDLE | 1.07 | 2.34 | 0.3 | 0.01 | 61112.84 | 7.05 | no_map |
| FLUIDUSDT | IDLE | 1.76 | 3.47 | 3.35 | 0.01 | 20183.9 | 19.73 | tvl≈2,378,903,955 |
| TELUSDT | IDLE | 1.57 | 2.95 | 1.24 | 0.0 | 107394.42 | 34.15 | no_map |
| MNSRYUSDT | IDLE | 0.59 | 1.08 | 0.65 | -0.02 | 38074.94 | 6.97 | no_map |
| RWAUSDT | IDLE | 0.26 | 0.46 | 0.38 | -0.0 | 52250.32 | 7.72 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
