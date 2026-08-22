# Hulk DIGEST — 2026-08-22T08:51:25Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 19.14 | 9.35 | 0.04 | 33845413.7 | 3.95 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 23.87 | 10.1 | 0.11 | 223761508.6 | 4.58 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 15.8 | 9.91 | 0.02 | 1314714.28 | 6.39 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 12.06 | -0.1 | 680554.47 | 3.35 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 17.58 | 8.69 | 0.02 | 602349.84 | 13.58 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.21 | -0.04 | 254390.31 | 3.18 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.09 | 0.04 | 155551.3 | 9.71 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.08 | 11.25 | 3.36 | 0.16 | 801635.81 | 5.79 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 8.47 | 6.88 | -0.01 | 501368.63 | 23.21 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.04 | 0.01 | 192813.62 | 7.75 | n/a |
| KITEUSDT | IDLE | 3.75 | 9.68 | 2.97 | 0.06 | 73710.45 | 11.72 | no_map |
| EDELUSDT | IDLE | 2.32 | 4.52 | 4.11 | -0.05 | 86700.89 | 33.73 | no_map |
| FLUIDUSDT | IDLE | 3.79 | 7.38 | 4.56 | 0.03 | 6885.76 | 22.16 | tvl≈2,562,763,298 |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 1.99 | 0.02 | 11077.79 | 5.33 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 6.46 | 5.97 | -0.02 | 174522.36 | 36.76 | no_map |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.87 | 3.73 | 1.58 | 0.01 | 52238.61 | 44.83 | no_map |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.04 | 58276.67 | 8.07 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
