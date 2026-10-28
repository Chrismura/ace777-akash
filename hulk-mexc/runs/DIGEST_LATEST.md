# Hulk DIGEST — 2026-10-28T11:32:12Z

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
| ETHUSDT | IDLE | 0.86 | 1.57 | 0.99 | 0.02 | 240228905.72 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.69 | 1.24 | 0.96 | 0.02 | 20192470.5 | 0.75 | n/a |
| BTCUSDT | IDLE | 0.61 | 1.15 | 0.48 | 0.02 | 307055435.25 | 0.0 | no_map |
| CCUSDT | IDLE | 3.24 | 6.2 | 2.98 | 0.05 | 292618.3 | 5.91 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 7.64 | 5.02 | 0.03 | 156584.91 | 16.64 | no_map |
| RWAINCUSDT | IDLE | 3.42 | 6.85 | 0.0 | 0.05 | 51801.99 | 6.41 | no_map |
| WUSDT | IDLE | 0.74 | 1.36 | 0.76 | 0.04 | 629971.3 | 17.92 | tvl≈1,524,382,795 |
| ZBCNUSDT | IDLE | 1.61 | 3.17 | 1.14 | -0.04 | 216055.53 | 11.01 | n/a |
| PYTHUSDT | IDLE | 0.71 | 1.38 | 0.32 | 0.0 | 399822.06 | 2.75 | tvl≈160,234,737 |
| QNTUSDT | IDLE | 1.49 | 2.75 | 1.52 | -0.01 | 475895.98 | 2.99 | n/a |
| EDELUSDT | IDLE | 1.23 | 2.26 | 1.3 | 0.02 | 285989.57 | 33.71 | no_map |
| HBARUSDT | IDLE | 0.73 | 1.32 | 0.87 | 0.01 | 407554.6 | 7.86 | empty_tvl |
| REDUSDT | IDLE | 0.99 | 1.77 | 1.45 | 0.04 | 54602.5 | 15.06 | tvl≈3,812,721 |
| BIOUSDT | IDLE | 0.8 | 1.5 | 0.7 | 0.03 | 83375.68 | 8.78 | n/a |
| KITEUSDT | IDLE | 0.89 | 1.6 | 1.25 | 0.02 | 60531.88 | 12.01 | no_map |
| RIZEUSDT | IDLE | 0.69 | 1.33 | 0.38 | 0.03 | 36345.22 | 63.42 | no_map |
| WAXLUSDT | IDLE | 1.15 | 2.15 | 1.03 | 0.02 | 55871.22 | 30.66 | no_map |
| LAUSDT | IDLE | 0.73 | 1.38 | 0.89 | 0.03 | 59819.21 | 25.4 | no_map |
| IOTAUSDT | IDLE | 0.71 | 1.31 | 0.77 | 0.0 | 75112.34 | 35.5 | no_map |
| RWAUSDT | IDLE | 0.7 | 1.37 | 0.24 | 0.01 | 55091.62 | 23.88 | no_map |
| FLUIDUSDT | IDLE | 0.54 | 1.76 | 0.0 | 0.01 | 6667.15 | 21.45 | tvl≈2,216,959,076 |
| MNSRYUSDT | IDLE | 0.66 | 1.25 | 0.5 | 0.0 | 36030.78 | 54.03 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
