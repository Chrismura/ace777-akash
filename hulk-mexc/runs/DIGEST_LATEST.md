# Hulk DIGEST — 2026-10-20T16:18:58Z

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
| XRPUSDT | IDLE | 2.2 | 4.09 | 2.02 | 0.01 | 22970854.31 | 0.76 | n/a |
| ETHUSDT | IDLE | 2.15 | 4.03 | 1.75 | 0.01 | 146745006.86 | 0.21 | no_map |
| BTCUSDT | IDLE | 1.36 | 2.55 | 1.19 | 0.0 | 326308952.39 | 0.0 | no_map |
| PYTHUSDT | IDLE | 3.92 | 8.81 | 3.74 | 0.01 | 992104.11 | 7.94 | tvl≈162,629,459 |
| WUSDT | IDLE | 3.34 | 6.16 | 3.5 | -0.02 | 710296.0 | 14.56 | tvl≈1,596,475,438 |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.26 | 10.31 | 0.02 | 69323.24 | 58.88 | no_map |
| QNTUSDT | IDLE | 3.33 | 6.0 | 4.35 | -0.01 | 684395.62 | 6.7 | n/a |
| ZBCNUSDT | IDLE | 4.1 | 7.65 | 3.73 | 0.01 | 192086.65 | 35.26 | n/a |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 9.6 | 8.71 | -0.04 | 76570.79 | 69.06 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.84 | 10.03 | 5.02 | 0.08 | 113537.41 | 13.36 | no_map |
| EDELUSDT | IDLE | 1.59 | 15.05 | 1.54 | 0.33 | 320832.48 | 16.77 | no_map |
| CCUSDT | IDLE | 1.78 | 3.41 | 0.99 | 0.02 | 415769.87 | 9.45 | no_map |
| BIOUSDT | IDLE | 3.08 | 5.87 | 1.97 | 0.03 | 63567.15 | 8.2 | n/a |
| HBARUSDT | IDLE | 2.54 | 4.66 | 2.82 | 0.01 | 370246.91 | 6.0 | empty_tvl |
| REDUSDT | IDLE | 2.65 | 5.05 | 1.62 | 0.01 | 58747.74 | 17.24 | tvl≈3,520,448 |
| KITEUSDT | IDLE | 2.32 | 4.35 | 1.88 | -0.02 | 84895.43 | 11.48 | no_map |
| IOTAUSDT | IDLE | 3.31 | 6.63 | 3.2 | 0.04 | 91257.7 | 27.99 | no_map |
| LAUSDT | IDLE | 3.1 | 6.0 | 1.3 | 0.02 | 55899.55 | 26.0 | no_map |
| WAXLUSDT | IDLE | 2.95 | 5.42 | 3.21 | -0.05 | 55136.86 | 60.99 | no_map |
| FLUIDUSDT | IDLE | 1.38 | 2.67 | 0.66 | 0.04 | 4058.72 | 21.54 | tvl≈2,242,038,732 |
| RWAUSDT | IDLE | 0.84 | 1.5 | 1.17 | 0.0 | 51535.51 | 7.86 | no_map |
| MNSRYUSDT | IDLE | 0.8 | 1.52 | 0.59 | 0.0 | 39971.43 | 15.63 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
