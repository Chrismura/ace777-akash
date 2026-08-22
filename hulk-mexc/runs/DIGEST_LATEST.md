# Hulk DIGEST — 2026-08-22T09:45:20Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 19.14 | 10.85 | 0.02 | 45130059.31 | 2.01 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 23.87 | 11.12 | 0.09 | 218473832.53 | 1.98 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 15.8 | 10.11 | 0.03 | 1292746.45 | 3.84 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 23.96 | 12.12 | -0.1 | 665729.68 | 6.72 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.74 | 0.03 | 590772.37 | 7.31 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.02 | -0.03 | 237648.54 | 6.41 | n/a |
| CCUSDT | IDLE | 2.23 | 11.25 | 7.66 | 0.12 | 802653.04 | 9.52 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.09 | 41.27 | 11.46 | 0.06 | 154341.38 | 21.16 | tvl≈2,081,438 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.0 | 6.52 | -0.02 | 439754.66 | 6.56 | n/a |
| KITEUSDT | IDLE | 4.3 | 9.68 | 4.77 | 0.04 | 73113.34 | 9.15 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.73 | 0.01 | 192935.22 | 3.09 | n/a |
| EDELUSDT | IDLE | 2.52 | 4.52 | 3.46 | -0.02 | 79286.07 | 44.79 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.8 | 7.03 | 6.56 | -0.02 | 170954.1 | 42.17 | no_map |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 6941.81 | 52.79 | tvl≈2,553,890,177 |
| RWAINCUSDT | IDLE | 2.42 | 4.36 | 3.14 | 0.01 | 11436.39 | 91.42 | no_map |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.87 | -0.01 | 49367.85 | 17.3 | no_map |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | no_map |
| RWAUSDT | IDLE | 1.73 | 3.29 | 1.12 | 0.03 | 57710.97 | 16.14 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
