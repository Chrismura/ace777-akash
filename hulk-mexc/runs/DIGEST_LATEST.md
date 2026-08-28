# Hulk DIGEST — 2026-08-28T23:07:06Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.97 | 1.88 | 0.4 | -0.05 | 52249958.23 | 1.45 | n/a |
| CHIPUSDT | IDLE | 1.21 | 7.37 | 5.45 | 0.04 | 1101275.93 | 12.2 | no_map |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 33.82 | 24.02 | -0.16 | 83216.99 | 71.72 | no_map |
| PYTHUSDT | IDLE | 1.25 | 2.84 | 0.02 | -0.03 | 686299.01 | 2.11 | tvl≈105,141,896 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.28 | 13.86 | 11.48 | -0.14 | 91618.81 | 136.85 | no_map |
| ZBCNUSDT | IDLE | 2.21 | 5.63 | 4.34 | -0.08 | 174852.65 | 21.44 | n/a |
| CCUSDT | IDLE | 1.11 | 2.23 | 0.0 | -0.0 | 338510.67 | 8.08 | no_map |
| REDUSDT | IDLE | 2.06 | 5.16 | 1.11 | -0.01 | 63824.32 | 12.09 | tvl≈1,963,374 |
| KITEUSDT | IDLE | 1.94 | 3.61 | 1.74 | -0.02 | 78411.11 | 12.67 | no_map |
| RWAINCUSDT | IDLE | 2.36 | 4.28 | 2.93 | -0.02 | 3438.2 | 49.25 | no_map |
| RIZEUSDT | IDLE | 1.84 | 4.97 | 2.96 | -0.0 | 35783.3 | 35.98 | no_map |
| HBARUSDT | IDLE | 1.01 | 1.82 | 1.28 | -0.04 | 469355.78 | 1.32 | empty_tvl |
| WUSDT | IDLE | 0.62 | 1.47 | 0.14 | -0.05 | 207754.13 | 5.47 | tvl≈1,524,659,841 |
| BIOUSDT | IDLE | 0.85 | 2.01 | 0.43 | -0.06 | 89157.61 | 3.59 | n/a |
| TELUSDT | IDLE | 1.21 | 2.82 | 2.3 | -0.08 | 96891.68 | 28.68 | no_map |
| QNTUSDT | IDLE | 0.69 | 1.36 | 0.16 | -0.04 | 43054.85 | 3.27 | n/a |
| RWAUSDT | IDLE | 0.31 | 0.58 | 0.25 | 0.0 | 54495.23 | 33.2 | no_map |
| FLUIDUSDT | IDLE | 0.2 | 0.41 | 0.0 | -0.05 | 4563.02 | 22.17 | tvl≈2,598,079,405 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
