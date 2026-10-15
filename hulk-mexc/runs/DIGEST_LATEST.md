# Hulk DIGEST — 2026-10-15T19:04:41Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.7 | 22.41 | 5.81 | 0.16 | 4415605.36 | 2.1 | tvl≈206,195,902 |
| WUSDT | IDLE | 2.28 | 7.07 | 0.53 | -0.0 | 2660721.25 | 17.99 | tvl≈1,669,796,578 |
| ETHUSDT | IDLE | 2.6 | 5.17 | 0.2 | 0.01 | 341642482.93 | 0.04 | no_map |
| XRPUSDT | IDLE | 2.37 | 4.71 | 0.21 | 0.01 | 50491371.35 | 2.23 | n/a |
| BTCUSDT | IDLE | 1.55 | 3.08 | 0.2 | 0.01 | 501096472.47 | 0.0 | no_map |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.52 | 11.34 | 1.87 | 0.04 | 1343306.83 | 5.2 | n/a |
| REDUSDT | IDLE | 4.18 | 13.25 | 3.89 | 0.02 | 72880.82 | 8.23 | tvl≈4,010,084 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.78 | 10.86 | 8.82 | -0.13 | 244579.15 | 17.23 | no_map |
| ZBCNUSDT | IDLE | 3.28 | 6.83 | 0.18 | 0.04 | 205461.62 | 0.44 | n/a |
| CCUSDT | IDLE | 1.81 | 4.84 | 1.86 | -0.07 | 439382.9 | 6.46 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 11.39 | 8.52 | -0.0 | 81118.4 | 59.57 | no_map |
| KITEUSDT | IDLE | 3.29 | 7.05 | 0.6 | -0.01 | 70399.35 | 8.75 | no_map |
| CHIPUSDT | IDLE | 2.02 | 12.28 | 2.88 | -0.11 | 150244.08 | 15.01 | no_map |
| BIOUSDT | IDLE | 2.54 | 6.26 | 0.38 | -0.01 | 85177.29 | 7.73 | n/a |
| HBARUSDT | IDLE | 2.49 | 4.98 | 0.0 | 0.01 | 307162.09 | 3.55 | empty_tvl |
| RWAINCUSDT | IDLE | 2.26 | 5.54 | 4.91 | 0.05 | 27871.53 | 24.88 | no_map |
| TELUSDT | IDLE | 3.32 | 6.57 | 0.5 | -0.01 | 92830.81 | 22.54 | no_map |
| FLUIDUSDT | IDLE | 1.48 | 3.91 | 0.0 | -0.02 | 8868.89 | 21.68 | tvl≈2,270,858,440 |
| MNSRYUSDT | IDLE | 1.45 | 2.77 | 0.82 | 0.0 | 32898.91 | 29.61 | no_map |
| RWAUSDT | IDLE | 1.05 | 2.02 | 0.55 | -0.0 | 54714.59 | 15.92 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
