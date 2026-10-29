# Hulk DIGEST — 2026-10-29T19:50:37Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 10.15 | 8.33 | -0.05 | 1117645.18 | 1.45 | tvl≈163,033,227 |
| XRPUSDT | IDLE | 1.72 | 3.06 | 2.48 | -0.04 | 24775286.72 | 1.56 | n/a |
| ETHUSDT | IDLE | 1.34 | 2.41 | 1.77 | -0.01 | 265592167.38 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.14 | 2.09 | 1.28 | -0.01 | 365829872.6 | 0.0 | no_map |
| WUSDT | IDLE | 2.55 | 4.6 | 3.28 | -0.05 | 398855.55 | 13.94 | tvl≈1,502,901,010 |
| QNTUSDT | IDLE | 3.18 | 5.78 | 3.8 | -0.04 | 520979.64 | 2.6 | n/a |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 8.73 | 7.93 | -0.02 | 120506.32 | 8.23 | no_map |
| CCUSDT | IDLE | 2.18 | 4.72 | 3.57 | 0.0 | 373960.39 | 5.92 | no_map |
| EDELUSDT | IDLE | 2.12 | 3.8 | 2.87 | -0.05 | 351878.39 | 22.75 | no_map |
| HBARUSDT | IDLE | 2.6 | 4.67 | 3.52 | -0.04 | 370286.51 | 2.73 | empty_tvl |
| BIOUSDT | IDLE | 2.5 | 4.82 | 2.21 | -0.0 | 74965.42 | 8.71 | n/a |
| REDUSDT | IDLE | 1.83 | 3.22 | 2.89 | -0.03 | 64159.67 | 7.41 | tvl≈3,793,287 |
| KITEUSDT | IDLE | 1.86 | 3.32 | 2.73 | -0.04 | 61370.36 | 13.31 | no_map |
| ZBCNUSDT | IDLE | 0.84 | 1.5 | 1.25 | -0.01 | 217007.54 | 34.0 | n/a |
| LAUSDT | IDLE | 2.47 | 4.49 | 2.94 | -0.02 | 61012.61 | 24.51 | no_map |
| RWAINCUSDT | IDLE | 1.32 | 2.35 | 1.88 | -0.02 | 35629.64 | 28.33 | no_map |
| IOTAUSDT | IDLE | 2.01 | 3.67 | 3.01 | -0.04 | 95907.25 | 14.9 | no_map |
| RIZEUSDT | IDLE | 0.85 | 1.55 | 0.95 | -0.0 | 51711.72 | 65.56 | no_map |
| FLUIDUSDT | IDLE | 1.56 | 4.37 | 3.72 | -0.09 | 19664.54 | 23.05 | tvl≈2,218,201,883 |
| WAXLUSDT | IDLE | 1.55 | 3.47 | 3.06 | -0.05 | 52824.19 | 57.85 | no_map |
| MNSRYUSDT | IDLE | 1.05 | 2.04 | 0.44 | 0.0 | 38423.58 | 26.33 | no_map |
| RWAUSDT | IDLE | 0.87 | 1.62 | 0.8 | -0.0 | 57004.36 | 32.1 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
