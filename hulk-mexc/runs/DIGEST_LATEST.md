# Hulk DIGEST — 2026-09-22T17:06:17Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 18.79 | 9.7 | 0.03 | 1550370.56 | 3.0 | tvl≈142,720,178 |
| XRPUSDT | IDLE | 2.26 | 4.27 | 1.69 | 0.05 | 116528154.93 | 1.91 | n/a |
| ETHUSDT | IDLE | 0.91 | 1.73 | 0.61 | -0.0 | 474875754.23 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.73 | 1.42 | 0.26 | 0.01 | 908841710.62 | 0.64 | no_map |
| HBARUSDT | IDLE | 2.56 | 5.76 | 2.44 | 0.05 | 1353828.77 | 1.04 | empty_tvl |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 6.91 | 5.55 | -0.03 | 483994.63 | 5.31 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.52 | 14.26 | 12.05 | -0.01 | 263760.85 | 52.07 | no_map |
| CHIPUSDT | IDLE | 2.44 | 4.48 | 2.63 | -0.01 | 142379.89 | 19.64 | no_map |
| WUSDT | IDLE | 1.45 | 2.86 | 0.21 | 0.03 | 362521.89 | 8.31 | tvl≈1,783,448,022 |
| ZBCNUSDT | IDLE | 1.92 | 3.64 | 1.29 | -0.0 | 240819.24 | 38.46 | n/a |
| RIZEUSDT | IDLE | 1.95 | 23.47 | 3.33 | -0.17 | 42836.73 | 113.61 | no_map |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.18 | 8.52 | 0.0 | 0.07 | 103588.4 | 34.25 | no_map |
| REDUSDT | IDLE | 1.78 | 3.53 | 0.25 | 0.03 | 66258.13 | 7.58 | tvl≈2,820,552 |
| KITEUSDT | IDLE | 1.33 | 6.05 | 0.26 | 0.16 | 110313.18 | 9.38 | no_map |
| BIOUSDT | IDLE | 1.62 | 3.21 | 0.14 | 0.01 | 107232.21 | 20.52 | n/a |
| QNTUSDT | IDLE | 1.9 | 6.04 | 1.85 | 0.1 | 186443.87 | 8.19 | n/a |
| RWAINCUSDT | IDLE | 0.84 | 1.61 | 0.49 | 0.04 | 24010.53 | 5.51 | no_map |
| FLUIDUSDT | IDLE | 0.67 | 1.25 | 0.63 | 0.01 | 7969.26 | 20.49 | tvl≈2,653,203,313 |
| RWAUSDT | IDLE | 0.51 | 0.95 | 0.44 | -0.0 | 54001.46 | 43.73 | no_map |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.01 | -0.0 | 40283.08 | 9.02 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
