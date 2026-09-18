# Hulk DIGEST — 2026-09-18T10:28:13Z

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
| XRPUSDT | IDLE | 0.94 | 1.82 | 0.34 | 0.03 | 40076361.64 | 1.5 | n/a |
| ETHUSDT | IDLE | 0.9 | 1.76 | 0.29 | 0.03 | 376612407.83 | 0.24 | no_map |
| BTCUSDT | IDLE | 0.71 | 1.37 | 0.37 | 0.02 | 566034858.06 | 0.35 | no_map |
| CCUSDT | IDLE | 1.41 | 4.52 | 2.44 | 0.08 | 656603.37 | 6.37 | no_map |
| PYTHUSDT | IDLE | 0.79 | 2.46 | 1.15 | 0.12 | 655923.84 | 1.66 | tvl≈135,937,013 |
| WUSDT | IDLE | 1.18 | 3.71 | 0.37 | 0.12 | 395488.56 | 11.59 | tvl≈1,561,825,442 |
| BIOUSDT | IDLE | 2.09 | 5.73 | 0.83 | 0.1 | 84848.48 | 7.29 | n/a |
| HBARUSDT | IDLE | 1.42 | 2.84 | 0.0 | 0.05 | 474923.12 | 1.28 | empty_tvl |
| ZBCNUSDT | IDLE | 1.1 | 2.17 | 0.21 | 0.05 | 259108.54 | 16.1 | n/a |
| CHIPUSDT | IDLE | 1.23 | 5.98 | 1.46 | 0.13 | 155006.75 | 18.13 | no_map |
| REDUSDT | IDLE | 1.79 | 4.47 | 0.75 | 0.06 | 68114.26 | 18.42 | tvl≈2,500,114 |
| EDELUSDT | IDLE | 0.64 | 6.51 | 2.16 | -0.04 | 262518.53 | 34.0 | no_map |
| TELUSDT | IDLE | 2.98 | 6.08 | 0.53 | 0.04 | 86969.31 | 46.4 | no_map |
| RWAINCUSDT | IDLE | 1.7 | 3.4 | 0.06 | -0.01 | 10441.34 | 23.53 | no_map |
| KITEUSDT | IDLE | 1.16 | 2.2 | 0.79 | 0.05 | 74720.81 | 10.0 | no_map |
| FLUIDUSDT | IDLE | 2.42 | 4.83 | 0.0 | 0.07 | 133.11 | 22.42 | tvl≈2,620,474,605 |
| QNTUSDT | IDLE | 0.92 | 1.79 | 0.36 | 0.03 | 46036.2 | 3.18 | n/a |
| RIZEUSDT | IDLE | 0.2 | 2.55 | 1.09 | 0.11 | 53926.91 | 103.66 | no_map |
| MNSRYUSDT | IDLE | 0.5 | 0.98 | 0.14 | 0.03 | 42968.89 | 6.82 | no_map |
| RWAUSDT | IDLE | 0.42 | 0.82 | 0.15 | 0.01 | 57757.39 | 36.94 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
