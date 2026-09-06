# Hulk DIGEST — 2026-09-06T16:32:21Z

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
| XRPUSDT | IDLE | 1.08 | 2.0 | 1.04 | -0.0 | 26571554.69 | 2.13 | n/a |
| ETHUSDT | IDLE | 0.93 | 1.72 | 0.92 | 0.01 | 258600562.73 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.54 | 1.02 | 0.39 | -0.0 | 397839719.67 | 0.0 | no_map |
| CHIPUSDT | IDLE | 3.28 | 6.75 | 4.35 | -0.03 | 474811.85 | 1.74 | no_map |
| PYTHUSDT | IDLE | 2.59 | 4.73 | 2.94 | -0.01 | 509414.34 | 1.83 | tvl≈123,271,808 |
| WUSDT | IDLE | 2.27 | 4.42 | 0.82 | 0.05 | 250468.44 | 10.57 | tvl≈1,663,589,288 |
| EDELUSDT | IDLE | 2.95 | 5.34 | 3.69 | -0.0 | 64559.09 | 38.2 | no_map |
| CCUSDT | IDLE | 1.24 | 2.2 | 1.92 | -0.02 | 324690.73 | 6.43 | no_map |
| ZBCNUSDT | IDLE | 1.76 | 3.1 | 2.8 | -0.01 | 199802.35 | 12.38 | n/a |
| REDUSDT | IDLE | 2.24 | 4.14 | 2.28 | 0.02 | 63552.28 | 8.59 | tvl≈2,331,573 |
| RIZEUSDT | IDLE | 1.74 | 12.46 | 10.03 | -0.12 | 80103.09 | 70.01 | no_map |
| BIOUSDT | IDLE | 1.99 | 3.74 | 1.57 | -0.01 | 92188.17 | 3.63 | n/a |
| RWAINCUSDT | IDLE | 2.06 | 4.61 | 1.6 | 0.07 | 6501.79 | 15.25 | no_map |
| HBARUSDT | IDLE | 1.0 | 1.83 | 1.16 | 0.0 | 423741.41 | 1.24 | empty_tvl |
| KITEUSDT | IDLE | 0.88 | 1.61 | 1.04 | 0.0 | 60992.42 | 11.05 | no_map |
| RWAUSDT | IDLE | 0.82 | 1.44 | 1.35 | -0.02 | 54914.47 | 7.2 | no_map |
| QNTUSDT | IDLE | 0.78 | 1.52 | 0.33 | 0.02 | 37214.99 | 6.08 | n/a |
| TELUSDT | IDLE | 0.83 | 1.59 | 0.46 | 0.0 | 65760.74 | 40.83 | no_map |
| MNSRYUSDT | IDLE | 0.2 | 0.36 | 0.25 | 0.02 | 41561.04 | 24.18 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.04 | 214.0 | 21.27 | tvl≈2,659,762,913 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
