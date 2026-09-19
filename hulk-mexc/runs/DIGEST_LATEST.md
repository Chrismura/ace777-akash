# Hulk DIGEST — 2026-09-19T19:59:34Z

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
| XRPUSDT | IDLE | 1.27 | 2.27 | 1.83 | 0.02 | 59008726.01 | 2.1 | n/a |
| ETHUSDT | IDLE | 0.81 | 1.42 | 1.32 | -0.0 | 284783191.38 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.43 | 0.75 | 0.74 | 0.0 | 458517629.84 | 0.05 | no_map |
| WUSDT | IDLE | 2.11 | 3.78 | 2.91 | -0.01 | 581985.4 | 10.88 | tvl≈1,611,302,671 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 12.53 | 5.14 | 0.09 | 225212.12 | 29.13 | n/a |
| PYTHUSDT | IDLE | 1.34 | 2.61 | 0.51 | 0.01 | 678871.17 | 3.28 | tvl≈136,715,653 |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.37 | 8.33 | 0.0 | 0.01 | 5423.68 | 51.8 | no_map |
| CCUSDT | IDLE | 1.52 | 2.69 | 2.34 | 0.01 | 331020.59 | 6.3 | no_map |
| HBARUSDT | IDLE | 1.13 | 2.22 | 0.27 | 0.04 | 603128.15 | 1.22 | empty_tvl |
| EDELUSDT | IDLE | 1.67 | 7.26 | 3.34 | -0.1 | 155352.81 | 57.69 | no_map |
| BIOUSDT | IDLE | 1.83 | 3.35 | 2.02 | 0.02 | 83075.27 | 7.1 | n/a |
| CHIPUSDT | IDLE | 1.33 | 3.04 | 2.86 | -0.0 | 131712.38 | 16.22 | no_map |
| KITEUSDT | IDLE | 1.16 | 2.05 | 1.82 | 0.04 | 73673.89 | 11.31 | no_map |
| RIZEUSDT | IDLE | 2.22 | 9.31 | 8.52 | 0.02 | 37758.29 | 202.51 | no_map |
| REDUSDT | IDLE | 0.57 | 2.49 | 1.35 | 0.02 | 136081.73 | 8.1 | tvl≈2,677,500 |
| TELUSDT | IDLE | 1.24 | 3.66 | 3.02 | -0.02 | 126497.08 | 26.49 | no_map |
| QNTUSDT | IDLE | 0.8 | 1.46 | 0.94 | 0.03 | 57105.78 | 4.59 | n/a |
| FLUIDUSDT | IDLE | 1.05 | 2.02 | 1.9 | 0.07 | 9472.77 | 21.74 | tvl≈2,642,558,159 |
| RWAUSDT | IDLE | 0.56 | 1.03 | 0.66 | 0.01 | 53979.92 | 29.33 | no_map |
| MNSRYUSDT | IDLE | 0.38 | 0.72 | 0.22 | -0.01 | 35791.51 | 62.32 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
