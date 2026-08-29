# Hulk DIGEST — 2026-08-29T01:10:26Z

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
| XRPUSDT | IDLE | 0.77 | 1.42 | 0.77 | -0.05 | 50543486.23 | 2.18 | n/a |
| CHIPUSDT | IDLE | 0.99 | 6.52 | 0.93 | 0.07 | 1176412.57 | 2.36 | no_map |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 33.82 | 23.55 | -0.09 | 83033.22 | 61.51 | no_map |
| PYTHUSDT | IDLE | 1.59 | 3.06 | 0.84 | -0.04 | 669946.17 | 2.1 | tvl≈105,141,896 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 13.66 | 10.28 | -0.14 | 91978.25 | 58.08 | no_map |
| CCUSDT | IDLE | 1.22 | 2.25 | 1.2 | -0.02 | 301743.2 | 8.12 | no_map |
| ZBCNUSDT | IDLE | 1.34 | 3.36 | 2.75 | -0.09 | 171859.06 | 25.14 | n/a |
| RIZEUSDT | IDLE | 1.94 | 4.74 | 3.7 | -0.05 | 33828.42 | 55.56 | no_map |
| HBARUSDT | IDLE | 0.96 | 1.68 | 1.63 | -0.05 | 473674.15 | 1.32 | empty_tvl |
| WUSDT | IDLE | 0.82 | 1.54 | 0.82 | -0.06 | 221264.16 | 13.17 | tvl≈1,532,455,349 |
| KITEUSDT | IDLE | 1.37 | 2.67 | 0.52 | -0.01 | 79099.04 | 10.11 | no_map |
| REDUSDT | IDLE | 1.28 | 3.12 | 1.17 | -0.02 | 63074.43 | 14.89 | tvl≈1,963,374 |
| RWAINCUSDT | IDLE | 2.28 | 4.28 | 1.92 | -0.02 | 3438.94 | 98.25 | no_map |
| BIOUSDT | IDLE | 0.74 | 1.38 | 0.68 | -0.06 | 85528.17 | 3.6 | n/a |
| TELUSDT | IDLE | 0.79 | 1.97 | 0.34 | -0.08 | 98893.57 | 22.75 | no_map |
| QNTUSDT | IDLE | 0.46 | 0.86 | 0.42 | -0.03 | 42213.96 | 3.28 | n/a |
| RWAUSDT | IDLE | 0.43 | 0.83 | 0.17 | 0.0 | 54519.76 | 16.53 | no_map |
| FLUIDUSDT | IDLE | 0.34 | 0.69 | 0.0 | -0.05 | 3932.96 | 21.41 | tvl≈2,602,707,191 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
