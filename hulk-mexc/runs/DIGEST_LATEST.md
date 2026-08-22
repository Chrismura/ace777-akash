# Hulk DIGEST — 2026-08-22T07:43:17Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.6 | 0.02 | 22823546.34 | 19.61 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 23.87 | 6.14 | 0.21 | 222491064.17 | 8.16 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.22 | 0.05 | 1357263.01 | 5.07 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.53 | -0.09 | 695053.95 | 3.33 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.9 | 0.05 | 616735.61 | 15.52 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.76 | -0.03 | 247403.85 | 15.96 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 10.98 | 0.06 | 160767.56 | 13.08 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.04 | 11.25 | 3.04 | 0.2 | 804971.21 | 9.9 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 8.47 | 5.56 | 0.04 | 537702.96 | 0.5 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 13.91 | 9.15 | 0.03 | 195712.47 | 44.81 | n/a |
| KITEUSDT | IDLE | 3.42 | 9.68 | 3.51 | 0.09 | 74344.98 | 12.65 | no_map |
| EDELUSDT | IDLE | 2.26 | 4.52 | 3.14 | -0.03 | 87140.35 | 55.59 | no_map |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 17.52 | tvl≈2,556,699,557 |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 112.81 | no_map |
| TELUSDT | IDLE | 2.07 | 5.36 | 3.8 | -0.0 | 177578.36 | 46.24 | no_map |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.18 | -0.01 | 3225.39 | 59.7 | no_map |
| RIZEUSDT | IDLE | 0.92 | 3.99 | 1.49 | -0.04 | 52678.53 | 27.42 | no_map |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.04 | 58360.81 | 8.08 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
