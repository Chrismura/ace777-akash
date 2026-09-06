# Hulk DIGEST — 2026-09-06T01:30:22Z

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
| XRPUSDT | IDLE | 0.73 | 1.41 | 0.36 | 0.01 | 23772342.38 | 2.82 | n/a |
| ETHUSDT | IDLE | 0.51 | 0.98 | 0.22 | 0.02 | 174470797.18 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.21 | 0.4 | 0.09 | 0.0 | 370244163.69 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.95 | 3.73 | 1.12 | 0.03 | 394906.11 | 3.58 | tvl≈123,271,808 |
| CHIPUSDT | IDLE | 1.28 | 3.41 | 0.52 | 0.06 | 420656.08 | 11.72 | no_map |
| RWAINCUSDT | IDLE | 2.97 | 5.2 | 4.95 | -0.01 | 8342.38 | 27.11 | no_map |
| RIZEUSDT | IDLE | 1.7 | 11.01 | 4.34 | -0.08 | 127037.59 | 32.27 | no_map |
| CCUSDT | IDLE | 1.32 | 2.52 | 0.85 | 0.03 | 285277.91 | 6.34 | no_map |
| ZBCNUSDT | IDLE | 1.56 | 2.87 | 1.64 | -0.01 | 223988.28 | 21.12 | n/a |
| WUSDT | IDLE | 1.67 | 3.34 | 0.03 | 0.05 | 164065.97 | 2.93 | tvl≈1,654,385,292 |
| REDUSDT | IDLE | 1.12 | 2.24 | 0.0 | 0.04 | 60014.94 | 7.76 | tvl≈2,331,573 |
| KITEUSDT | IDLE | 0.93 | 1.98 | 0.56 | -0.07 | 64603.72 | 12.55 | no_map |
| BIOUSDT | IDLE | 0.77 | 1.44 | 0.6 | 0.03 | 83783.17 | 3.57 | n/a |
| HBARUSDT | IDLE | 0.69 | 1.33 | 0.28 | 0.02 | 363876.75 | 1.24 | empty_tvl |
| EDELUSDT | IDLE | 0.24 | 3.05 | 2.68 | 0.01 | 116411.75 | 19.01 | no_map |
| RWAUSDT | IDLE | 1.81 | 3.18 | 2.94 | 0.04 | 53249.26 | 21.15 | no_map |
| TELUSDT | IDLE | 1.86 | 3.46 | 1.67 | -0.0 | 72934.84 | 52.96 | no_map |
| QNTUSDT | IDLE | 0.99 | 1.98 | 0.02 | 0.03 | 36809.37 | 6.08 | n/a |
| FLUIDUSDT | IDLE | 0.4 | 0.79 | 0.1 | 0.01 | 385.8 | 0.79 | tvl≈2,653,785,138 |
| MNSRYUSDT | IDLE | 0.15 | 0.26 | 0.25 | -0.0 | 38816.82 | 20.48 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
