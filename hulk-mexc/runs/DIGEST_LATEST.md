# Hulk DIGEST — 2026-08-22T07:56:14Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.54 | 0.01 | 24210559.1 | 1.96 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.41 | 23.87 | 7.63 | 0.2 | 223775081.42 | 1.27 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.51 | 0.04 | 1349798.7 | 5.09 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.74 | -0.09 | 689381.01 | 3.33 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.1 | 0.04 | 616047.98 | 14.52 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.56 | -0.04 | 247608.97 | 3.19 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.26 | 0.06 | 160608.02 | 20.98 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.03 | 11.25 | 2.79 | 0.2 | 811011.56 | 10.69 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 8.47 | 5.98 | 0.04 | 537634.07 | 16.48 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.42 | 0.04 | 194593.82 | 9.25 | n/a |
| KITEUSDT | IDLE | 3.43 | 9.68 | 3.68 | 0.08 | 74042.45 | 9.05 | no_map |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.04 | 87136.16 | 22.3 | no_map |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 18.23 | tvl≈2,556,699,557 |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 112.81 | no_map |
| TELUSDT | IDLE | 2.09 | 5.36 | 4.15 | -0.01 | 175303.5 | 25.75 | no_map |
| QAITUSDT | IDLE | 1.71 | 3.32 | 0.67 | 0.0 | 3207.76 | 63.29 | no_map |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 1.01 | 0.01 | 52386.1 | 41.01 | no_map |
| RWAUSDT | IDLE | 1.73 | 3.29 | 1.12 | 0.04 | 58421.86 | 16.13 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
