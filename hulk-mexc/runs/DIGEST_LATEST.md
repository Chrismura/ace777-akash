# Hulk DIGEST — 2026-10-10T16:40:49Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.79 | 12.38 | 5.58 | 0.02 | 1240462.32 | 13.42 | tvl≈1,647,106,296 |
| ETHUSDT | IDLE | 0.47 | 0.89 | 0.36 | 0.01 | 86659067.92 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.38 | 0.7 | 0.38 | 0.02 | 15634048.16 | 2.13 | n/a |
| BTCUSDT | IDLE | 0.18 | 0.36 | 0.03 | 0.0 | 184146177.44 | 0.0 | no_map |
| QNTUSDT | IDLE | 3.65 | 6.57 | 4.83 | -0.01 | 1170323.77 | 2.48 | n/a |
| PYTHUSDT | IDLE | 0.95 | 1.87 | 0.16 | -0.06 | 967455.99 | 1.27 | tvl≈175,240,177 |
| EDELUSDT | IDLE | 2.82 | 5.64 | 4.71 | -0.04 | 219119.64 | 31.45 | no_map |
| CHIPUSDT | IDLE | 2.58 | 8.93 | 2.69 | 0.11 | 98474.38 | 7.34 | no_map |
| KITEUSDT | IDLE | 2.16 | 5.87 | 2.29 | 0.07 | 72306.89 | 10.07 | no_map |
| CCUSDT | IDLE | 0.96 | 1.69 | 1.52 | -0.02 | 361713.64 | 5.03 | no_map |
| TELUSDT | IDLE | 2.9 | 5.22 | 3.83 | -0.04 | 122673.43 | 44.89 | no_map |
| ZBCNUSDT | IDLE | 1.06 | 1.96 | 1.09 | -0.01 | 202623.07 | 17.05 | n/a |
| BIOUSDT | IDLE | 1.22 | 2.38 | 0.38 | 0.04 | 85656.21 | 6.87 | n/a |
| REDUSDT | IDLE | 0.99 | 1.87 | 0.72 | 0.03 | 54751.64 | 9.96 | tvl≈3,785,310 |
| HBARUSDT | IDLE | 0.9 | 1.69 | 0.67 | 0.02 | 354235.5 | 4.31 | empty_tvl |
| RWAINCUSDT | IDLE | 0.89 | 1.73 | 0.29 | -0.0 | 9624.54 | 38.99 | no_map |
| RIZEUSDT | IDLE | 0.54 | 1.26 | 0.65 | 0.0 | 43437.5 | 57.67 | no_map |
| FLUIDUSDT | IDLE | 0.66 | 1.94 | 1.28 | 0.0 | 15311.85 | 22.17 | tvl≈2,429,079,103 |
| RWAUSDT | IDLE | 0.4 | 0.71 | 0.55 | -0.01 | 54399.7 | 15.74 | no_map |
| MNSRYUSDT | IDLE | 0.24 | 0.43 | 0.3 | 0.0 | 38846.14 | 12.18 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
