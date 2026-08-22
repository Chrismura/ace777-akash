# Hulk DIGEST — 2026-08-22T08:04:18Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.99 | 0.01 | 24948546.57 | 5.91 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 23.87 | 8.48 | 0.18 | 224054167.0 | 3.22 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.52 | 0.04 | 1354674.15 | 2.55 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.88 | -0.09 | 683278.78 | 6.67 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 7.99 | 0.04 | 609020.79 | 16.56 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 29.98 | 9.3 | -0.04 | 247568.56 | 3.18 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 11.09 | 0.06 | 157311.67 | 16.59 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.04 | 11.25 | 2.03 | 0.2 | 813031.17 | 10.6 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.19 | 0.03 | 537242.13 | 5.01 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.22 | 0.04 | 194275.76 | 3.07 | n/a |
| KITEUSDT | IDLE | 3.81 | 9.68 | 4.01 | 0.07 | 72852.25 | 9.09 | no_map |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 20.42 | tvl≈2,556,699,557 |
| EDELUSDT | IDLE | 2.21 | 4.52 | 2.38 | -0.03 | 87091.52 | 55.52 | no_map |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11250.14 | 112.63 | no_map |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.95 | -0.01 | 173869.66 | 36.05 | no_map |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.71 | 0.0 | 52284.34 | 44.42 | no_map |
| RWAUSDT | IDLE | 1.72 | 3.29 | 0.96 | 0.05 | 58297.13 | 16.09 | no_map |
| QAITUSDT | IDLE | 0.99 | 1.92 | 0.35 | 0.01 | 3170.95 | 67.05 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
