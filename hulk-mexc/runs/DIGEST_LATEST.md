# Hulk DIGEST — 2026-09-28T21:30:53Z

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
| HBARUSDT | IDLE | 1.57 | 14.78 | 5.35 | 0.31 | 11611585.42 | 0.81 | empty_tvl |
| WUSDT | IDLE | 1.06 | 4.77 | 3.2 | -0.16 | 1979611.2 | 10.37 | tvl≈1,830,777,442 |
| QNTUSDT | IDLE | 0.8 | 17.44 | 5.19 | 0.03 | 21073387.78 | 8.54 | n/a |
| XRPUSDT | IDLE | 1.66 | 3.03 | 1.91 | -0.02 | 68308339.73 | 2.01 | n/a |
| ETHUSDT | IDLE | 1.13 | 2.05 | 1.43 | -0.0 | 406099041.95 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.81 | 1.47 | 1.06 | -0.01 | 843758353.74 | 0.0 | no_map |
| CCUSDT | IDLE | 1.43 | 5.38 | 2.98 | -0.06 | 1355385.72 | 8.47 | no_map |
| PYTHUSDT | IDLE | 1.57 | 3.46 | 0.47 | -0.04 | 1202303.85 | 3.72 | tvl≈177,971,605 |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.32 | 27.79 | 0.55 | 0.26 | 310680.31 | 29.99 | no_map |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.42 | 9.08 | 1.33 | -0.01 | 16190.8 | 79.52 | no_map |
| EDELUSDT | IDLE | 1.91 | 11.97 | 7.2 | 0.06 | 166219.04 | 70.33 | no_map |
| ZBCNUSDT | IDLE | 1.45 | 2.77 | 0.88 | -0.04 | 227184.34 | 4.95 | n/a |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.11 | 8.01 | 0.45 | 0.13 | 46276.87 | 56.13 | no_map |
| CHIPUSDT | IDLE | 1.68 | 3.9 | 2.74 | -0.07 | 73574.43 | 13.84 | no_map |
| KITEUSDT | IDLE | 1.32 | 4.87 | 3.2 | -0.1 | 100869.01 | 8.04 | no_map |
| REDUSDT | IDLE | 1.5 | 2.86 | 2.01 | -0.07 | 60106.02 | 14.39 | tvl≈2,939,149 |
| BIOUSDT | IDLE | 0.95 | 2.76 | 1.75 | -0.08 | 115280.91 | 6.83 | n/a |
| FLUIDUSDT | IDLE | 1.54 | 3.66 | 2.11 | -0.05 | 5151.45 | 21.47 | tvl≈2,601,244,143 |
| RWAUSDT | IDLE | 0.6 | 1.08 | 0.78 | -0.02 | 59297.44 | 14.37 | no_map |
| MNSRYUSDT | IDLE | 0.41 | 0.75 | 0.49 | -0.02 | 35147.42 | 30.97 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
