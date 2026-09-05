# Hulk DIGEST — 2026-09-05T20:29:40Z

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
| XRPUSDT | IDLE | 0.7 | 1.25 | 0.99 | 0.01 | 22462038.08 | 1.41 | n/a |
| ETHUSDT | IDLE | 0.6 | 1.16 | 0.26 | 0.01 | 159864646.27 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.37 | 0.65 | 0.58 | -0.0 | 355223547.64 | 0.0 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.64 | 23.78 | 7.93 | -0.02 | 142529.28 | 58.29 | no_map |
| CHIPUSDT | IDLE | 2.34 | 6.2 | 1.59 | 0.06 | 459430.42 | 5.06 | no_map |
| ZBCNUSDT | IDLE | 2.69 | 4.95 | 2.81 | -0.03 | 196391.36 | 2.17 | n/a |
| CCUSDT | IDLE | 1.41 | 2.5 | 2.1 | 0.03 | 300713.29 | 8.25 | no_map |
| PYTHUSDT | IDLE | 1.08 | 2.0 | 1.1 | 0.0 | 328027.34 | 1.82 | tvl≈123,719,242 |
| RWAINCUSDT | IDLE | 2.7 | 5.31 | 0.57 | 0.02 | 7749.16 | 68.58 | no_map |
| WUSDT | IDLE | 1.46 | 2.65 | 1.75 | 0.04 | 139364.0 | 11.08 | tvl≈1,654,426,116 |
| REDUSDT | IDLE | 1.09 | 2.13 | 0.31 | 0.04 | 60567.27 | 11.81 | tvl≈2,314,601 |
| BIOUSDT | IDLE | 0.87 | 1.69 | 0.32 | 0.05 | 82844.3 | 7.11 | n/a |
| EDELUSDT | IDLE | 0.16 | 2.89 | 0.75 | -0.01 | 165786.5 | 18.87 | no_map |
| KITEUSDT | IDLE | 0.7 | 1.73 | 0.55 | -0.06 | 62604.38 | 11.84 | no_map |
| HBARUSDT | IDLE | 0.63 | 1.2 | 0.44 | 0.04 | 327804.15 | 1.24 | empty_tvl |
| QNTUSDT | IDLE | 1.39 | 2.63 | 0.99 | 0.02 | 42403.51 | 4.63 | n/a |
| RWAUSDT | IDLE | 0.81 | 1.49 | 0.84 | 0.03 | 52049.49 | 7.03 | no_map |
| TELUSDT | IDLE | 0.94 | 1.82 | 0.35 | 0.01 | 66883.11 | 40.45 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 0.99 | 0.19 | 0.01 | 497.42 | 21.73 | tvl≈2,651,395,242 |
| MNSRYUSDT | IDLE | 0.15 | 0.27 | 0.25 | -0.0 | 37826.69 | 27.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
