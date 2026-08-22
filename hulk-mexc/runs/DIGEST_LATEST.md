# Hulk DIGEST — 2026-08-22T07:51:32Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.72 | 0.01 | 23835561.6 | 17.65 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 23.87 | 7.12 | 0.2 | 222769526.65 | 3.8 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.66 | 0.04 | 1352530.32 | 6.36 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.97 | -0.1 | 692929.05 | 3.34 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 17.58 | 8.17 | 0.04 | 616019.51 | 12.44 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.53 | -0.04 | 248080.59 | 6.38 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 11.09 | 0.06 | 160614.24 | 14.0 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.04 | 11.25 | 3.01 | 0.2 | 806633.35 | 5.77 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.1 | 0.03 | 538630.35 | 30.98 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.79 | 0.04 | 194784.25 | 9.28 | n/a |
| KITEUSDT | IDLE | 3.42 | 9.68 | 3.46 | 0.08 | 74125.14 | 11.74 | no_map |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.04 | 87136.08 | 33.46 | no_map |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 16.06 | tvl≈2,556,699,557 |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11302.57 | 112.81 | no_map |
| TELUSDT | IDLE | 2.1 | 5.36 | 4.29 | -0.01 | 176228.81 | 25.77 | no_map |
| QAITUSDT | IDLE | 1.68 | 3.24 | 0.86 | -0.01 | 3254.01 | 67.45 | no_map |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 0.98 | 0.01 | 52369.49 | 41.01 | no_map |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.35 | 0.04 | 58279.61 | 8.07 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
