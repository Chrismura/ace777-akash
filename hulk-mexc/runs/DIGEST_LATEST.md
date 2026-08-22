# Hulk DIGEST — 2026-08-22T08:47:22Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 9.89 | 0.04 | 32911501.83 | 1.99 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 23.87 | 11.26 | 0.1 | 224500598.73 | 2.65 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.13 | 0.02 | 1329685.29 | 2.56 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.41 | -0.1 | 688086.52 | 6.71 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 17.58 | 9.16 | 0.02 | 602210.4 | 13.63 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.79 | -0.04 | 254791.39 | 6.39 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.58 | 0.04 | 155671.05 | 14.2 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.07 | 11.25 | 3.25 | 0.17 | 802473.5 | 10.74 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 8.47 | 6.83 | -0.01 | 505821.92 | 18.65 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.32 | 0.01 | 192803.59 | 6.22 | n/a |
| KITEUSDT | IDLE | 3.79 | 9.68 | 3.68 | 0.06 | 73672.18 | 9.96 | no_map |
| EDELUSDT | IDLE | 2.32 | 4.52 | 4.0 | -0.04 | 86721.74 | 33.69 | no_map |
| FLUIDUSDT | IDLE | 3.79 | 7.38 | 4.56 | 0.03 | 6885.76 | 20.77 | tvl≈2,562,763,298 |
| RWAINCUSDT | IDLE | 2.39 | 4.48 | 1.99 | 0.02 | 11077.79 | 5.33 | no_map |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 6.41 | 5.87 | -0.02 | 174742.34 | 62.99 | no_map |
| RIZEUSDT | IDLE | 0.87 | 3.73 | 1.47 | 0.01 | 52233.92 | 27.55 | no_map |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | no_map |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.04 | 58290.18 | 24.24 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
