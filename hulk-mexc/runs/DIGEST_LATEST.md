# Hulk DIGEST — 2026-10-26T13:20:34Z

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
| XRPUSDT | IDLE | 1.08 | 2.08 | 0.48 | -0.0 | 20342242.0 | 1.55 | n/a |
| QNTUSDT | IDLE | 2.95 | 15.77 | 2.95 | 0.18 | 1377031.17 | 5.53 | n/a |
| ETHUSDT | IDLE | 0.79 | 1.45 | 0.85 | -0.01 | 112655353.52 | 0.17 | no_map |
| BTCUSDT | IDLE | 0.59 | 1.11 | 0.51 | -0.0 | 254720249.88 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.76 | 5.13 | 2.58 | 0.05 | 876264.79 | 5.37 | tvl≈162,205,079 |
| WUSDT | IDLE | 1.64 | 3.18 | 0.61 | 0.0 | 479641.67 | 10.91 | tvl≈1,520,686,619 |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.69 | 11.18 | 1.36 | 0.11 | 131404.41 | 8.13 | no_map |
| ZBCNUSDT | IDLE | 2.16 | 5.03 | 3.54 | -0.02 | 222375.98 | 37.26 | n/a |
| REDUSDT | IDLE | 2.35 | 4.57 | 0.87 | 0.03 | 62577.68 | 16.28 | tvl≈3,648,113 |
| CCUSDT | IDLE | 1.05 | 1.85 | 1.72 | -0.01 | 180480.57 | 6.98 | no_map |
| BIOUSDT | IDLE | 1.27 | 2.42 | 0.85 | -0.0 | 59209.73 | 9.01 | n/a |
| RWAINCUSDT | IDLE | 1.14 | 2.24 | 0.23 | -0.05 | 68645.87 | 11.56 | no_map |
| EDELUSDT | IDLE | 0.98 | 2.4 | 0.99 | 0.08 | 130797.48 | 37.35 | no_map |
| KITEUSDT | IDLE | 1.09 | 2.12 | 0.38 | 0.01 | 53467.14 | 11.51 | no_map |
| RIZEUSDT | IDLE | 1.13 | 2.16 | 0.7 | 0.01 | 33463.4 | 59.48 | no_map |
| MNSRYUSDT | IDLE | 2.42 | 4.38 | 3.07 | -0.02 | 42260.68 | 72.06 | no_map |
| LAUSDT | IDLE | 1.89 | 3.88 | 1.62 | 0.04 | 64364.55 | 18.82 | no_map |
| HBARUSDT | IDLE | 1.16 | 2.21 | 0.69 | 0.01 | 174299.17 | 5.16 | empty_tvl |
| IOTAUSDT | IDLE | 1.31 | 2.51 | 0.75 | -0.01 | 64983.02 | 30.55 | no_map |
| WAXLUSDT | IDLE | 1.32 | 2.58 | 0.4 | -0.02 | 52715.21 | 56.41 | no_map |
| FLUIDUSDT | IDLE | 0.35 | 1.39 | 0.42 | -0.01 | 8917.15 | 21.18 | tvl≈2,181,296,590 |
| RWAUSDT | IDLE | 0.17 | 0.32 | 0.16 | -0.0 | 53774.0 | 15.92 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
