# Hulk DIGEST — 2026-08-22T09:12:20Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.46 | 0.04 | 37731353.88 | 6.0 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 23.87 | 10.63 | 0.12 | 219864417.53 | 3.29 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 15.8 | 10.2 | 0.03 | 1303317.06 | 5.13 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 23.96 | 12.09 | -0.09 | 668386.36 | 6.72 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 17.58 | 8.88 | 0.03 | 600742.98 | 15.67 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.74 | -0.03 | 239484.36 | 12.93 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 12.14 | 0.03 | 155123.68 | 13.27 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.2 | 11.25 | 6.45 | 0.14 | 797176.2 | 11.1 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 8.0 | 6.3 | -0.01 | 468418.5 | 28.13 | n/a |
| KITEUSDT | IDLE | 4.21 | 9.68 | 3.31 | 0.07 | 73135.55 | 10.82 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.1 | 0.02 | 193032.76 | 9.31 | n/a |
| EDELUSDT | IDLE | 2.52 | 4.52 | 3.46 | -0.05 | 86164.92 | 33.65 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.38 | 5.05 | 0.01 | 6940.47 | 22.15 | tvl≈2,562,763,298 |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.69 | 6.17 | -0.03 | 171389.91 | 10.53 | no_map |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.03 | 11574.81 | 15.99 | no_map |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.79 | 3.36 | 1.7 | -0.02 | 50461.68 | 46.77 | no_map |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.51 | 0.03 | 57698.71 | 32.36 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
