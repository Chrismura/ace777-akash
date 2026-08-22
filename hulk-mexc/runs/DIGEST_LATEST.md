# Hulk DIGEST — 2026-08-22T07:21:35Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.39 | 0.03 | 21809471.63 | 15.81 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 23.87 | 6.65 | 0.2 | 218294492.11 | 1.26 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.32 | 0.05 | 1352953.23 | 3.81 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.62 | -0.1 | 701237.68 | 9.98 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.62 | 0.06 | 618627.2 | 9.29 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 29.98 | 12.18 | -0.05 | 246358.26 | 13.15 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.39 | 0.07 | 160680.24 | 12.99 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.07 | 11.25 | 4.15 | 0.17 | 798984.08 | 7.5 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.19 | 0.04 | 542209.16 | 33.06 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.29 | 0.04 | 199674.74 | 7.69 | n/a |
| KITEUSDT | IDLE | 3.39 | 9.68 | 2.84 | 0.1 | 74325.73 | 11.66 | no_map |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.04 | 87179.67 | 44.54 | no_map |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6900.29 | 21.1 | tvl≈2,556,699,557 |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 2.04 | 0.02 | 11393.75 | 59.0 | no_map |
| TELUSDT | IDLE | 2.06 | 5.36 | 3.6 | 0.05 | 196372.31 | 40.96 | no_map |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.02 | 3232.19 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.59 | -0.0 | 55971.57 | 27.43 | no_map |
| RWAUSDT | IDLE | 1.76 | 3.29 | 1.51 | 0.04 | 58101.48 | 16.18 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
