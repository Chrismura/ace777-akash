# Hulk DIGEST — 2026-08-22T10:25:03Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.77 | 16.77 | 12.5 | -0.01 | 51632422.69 | 14.62 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.93 | 23.87 | 15.02 | 0.05 | 216168081.57 | 4.85 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 15.8 | 11.95 | -0.0 | 1251084.6 | 16.99 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.05 | 22.93 | 13.08 | -0.12 | 664925.96 | 10.29 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 16.84 | 11.06 | -0.01 | 597460.15 | 17.25 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 29.98 | 12.41 | -0.06 | 236850.04 | 13.22 | n/a |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.26 | 0.11 | 816335.74 | 8.71 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 37.92 | 11.98 | 0.03 | 155481.82 | 14.57 | tvl≈2,031,082 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.52 | 8.88 | 8.1 | -0.03 | 428226.5 | 20.02 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 9.28 | 6.18 | 0.02 | 73152.38 | 19.57 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 9.75 | 7.54 | -0.01 | 189345.66 | 12.66 | n/a |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 8.07 | 7.47 | -0.04 | 168592.57 | 42.9 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.38 | 5.83 | -0.01 | 5825.49 | 21.85 | tvl≈2,553,890,177 |
| EDELUSDT | IDLE | 2.68 | 4.76 | 4.0 | -0.03 | 78538.29 | 67.42 | no_map |
| QAITUSDT | IDLE | 1.6 | 2.91 | 1.98 | -0.01 | 3205.44 | 63.29 | no_map |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.01 | 11368.82 | 43.43 | no_map |
| RIZEUSDT | IDLE | 0.75 | 3.18 | 1.52 | -0.0 | 49236.79 | 46.66 | no_map |
| RWAUSDT | IDLE | 1.82 | 3.29 | 2.39 | 0.01 | 57552.14 | 16.31 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
