# Hulk DIGEST — 2026-08-22T09:06:34Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 19.14 | 10.75 | 0.04 | 36185660.87 | 4.01 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 23.87 | 11.19 | 0.11 | 220964566.61 | 3.32 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 15.8 | 10.74 | 0.03 | 1302165.76 | 7.73 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 23.96 | 12.77 | -0.11 | 673909.62 | 6.78 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.34 | 17.58 | 9.78 | 0.02 | 602180.41 | 13.72 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 29.98 | 11.35 | -0.04 | 242376.6 | 3.26 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 41.27 | 12.46 | 0.04 | 155082.01 | 9.78 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.19 | 11.25 | 6.18 | 0.13 | 797859.6 | 10.2 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 8.0 | 6.95 | -0.01 | 477159.31 | 8.61 | n/a |
| KITEUSDT | IDLE | 4.26 | 9.68 | 4.27 | 0.05 | 73342.61 | 14.57 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 13.91 | 9.66 | 0.01 | 192981.72 | 4.68 | n/a |
| EDELUSDT | IDLE | 2.52 | 4.52 | 3.46 | -0.05 | 86444.93 | 22.4 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 7.38 | 5.05 | 0.01 | 6940.47 | 21.49 | tvl≈2,562,763,298 |
| RWAINCUSDT | IDLE | 2.32 | 4.36 | 1.88 | 0.03 | 11599.81 | 15.99 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.69 | 6.12 | -0.03 | 170789.83 | 21.04 | no_map |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.87 | -0.03 | 50574.25 | 46.77 | no_map |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.27 | 0.03 | 57848.56 | 40.44 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
