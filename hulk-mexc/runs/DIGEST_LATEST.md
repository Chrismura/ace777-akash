# Hulk DIGEST — 2026-10-22T21:37:51Z

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
| XRPUSDT | IDLE | 1.31 | 2.39 | 1.56 | -0.06 | 31303829.35 | 1.53 | n/a |
| ETHUSDT | IDLE | 0.91 | 1.76 | 0.45 | -0.04 | 235694550.76 | 0.08 | no_map |
| BTCUSDT | IDLE | 0.52 | 0.99 | 0.37 | -0.04 | 471345735.93 | 0.0 | no_map |
| WUSDT | IDLE | 1.11 | 3.14 | 2.57 | -0.12 | 1304289.23 | 19.82 | tvl≈1,534,070,737 |
| HBARUSDT | IDLE | 1.14 | 2.25 | 1.0 | -0.07 | 1290361.43 | 6.29 | empty_tvl |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.67 | 9.85 | 6.98 | -0.04 | 40533.81 | 15.72 | no_map |
| PYTHUSDT | IDLE | 1.36 | 3.04 | 2.94 | -0.09 | 553521.54 | 2.76 | tvl≈164,380,455 |
| EDELUSDT | IDLE | 1.59 | 4.12 | 2.18 | -0.08 | 517585.3 | 15.71 | no_map |
| QNTUSDT | IDLE | 0.82 | 2.56 | 1.31 | -0.1 | 711102.7 | 1.59 | n/a |
| CHIPUSDT | IDLE | 1.28 | 5.03 | 2.58 | -0.11 | 247617.64 | 15.97 | no_map |
| RWAINCUSDT | IDLE | 2.05 | 3.88 | 1.45 | -0.03 | 52112.71 | 11.3 | no_map |
| ZBCNUSDT | IDLE | 1.58 | 3.25 | 1.54 | -0.05 | 198232.86 | 49.84 | n/a |
| CCUSDT | IDLE | 0.55 | 1.76 | 1.2 | -0.12 | 260681.91 | 7.85 | no_map |
| REDUSDT | IDLE | 1.36 | 2.5 | 1.5 | -0.06 | 101106.15 | 17.14 | tvl≈3,506,358 |
| BIOUSDT | IDLE | 1.02 | 2.24 | 1.43 | -0.08 | 62778.76 | 8.53 | n/a |
| KITEUSDT | IDLE | 0.81 | 1.53 | 0.58 | -0.03 | 60270.66 | 12.52 | no_map |
| IOTAUSDT | IDLE | 0.94 | 2.21 | 1.5 | -0.09 | 77437.24 | 27.18 | no_map |
| LAUSDT | IDLE | 0.76 | 2.06 | 1.03 | -0.1 | 55231.48 | 18.5 | no_map |
| WAXLUSDT | IDLE | 0.64 | 2.42 | 1.09 | -0.13 | 58003.79 | 49.78 | no_map |
| FLUIDUSDT | IDLE | 0.69 | 5.28 | 1.37 | -0.07 | 22548.78 | 69.97 | tvl≈2,201,423,923 |
| RWAUSDT | IDLE | 0.29 | 0.56 | 0.16 | -0.02 | 52574.3 | 7.97 | no_map |
| MNSRYUSDT | IDLE | 0.64 | 1.16 | 0.78 | -0.01 | 38633.6 | 65.78 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
