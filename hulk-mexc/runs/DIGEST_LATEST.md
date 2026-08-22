# Hulk DIGEST — 2026-08-22T07:47:00Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.79 | 0.01 | 23272855.93 | 13.75 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 23.87 | 6.34 | 0.21 | 222556255.47 | 0.63 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.3 | 0.04 | 1349100.32 | 2.54 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.91 | -0.1 | 694480.86 | 3.34 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 7.93 | 0.05 | 616399.07 | 14.5 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.64 | -0.04 | 247788.48 | 6.39 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.8 | 0.07 | 160786.81 | 18.27 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.04 | 11.25 | 2.94 | 0.2 | 806148.69 | 5.76 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 8.47 | 6.0 | 0.04 | 538526.19 | 30.51 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.74 | 0.03 | 195650.87 | 3.09 | n/a |
| KITEUSDT | IDLE | 3.43 | 9.68 | 3.58 | 0.08 | 74337.2 | 13.56 | no_map |
| EDELUSDT | IDLE | 2.26 | 4.52 | 3.14 | -0.04 | 87113.43 | 55.59 | no_map |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.9 | tvl≈2,556,699,557 |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 112.81 | no_map |
| TELUSDT | IDLE | 2.08 | 5.36 | 3.95 | -0.01 | 177263.0 | 30.82 | no_map |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.05 | -0.02 | 52561.71 | 41.01 | no_map |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.27 | 0.04 | 58346.17 | 16.16 | no_map |
| QAITUSDT | IDLE | 1.68 | 3.24 | 0.86 | -0.01 | 3244.0 | 133.91 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
