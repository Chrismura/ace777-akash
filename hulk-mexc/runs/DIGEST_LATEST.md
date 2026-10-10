# Hulk DIGEST — 2026-10-10T09:46:12Z

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
| WUSDT | IDLE | 1.79 | 3.79 | 1.08 | -0.04 | 1432471.62 | 16.97 | tvl≈1,646,028,748 |
| XRPUSDT | IDLE | 0.35 | 0.66 | 0.26 | 0.01 | 23130697.91 | 2.13 | n/a |
| BTCUSDT | IDLE | 0.22 | 0.43 | 0.06 | 0.0 | 237704269.6 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.16 | 0.31 | 0.09 | -0.0 | 114442335.1 | 0.04 | no_map |
| PYTHUSDT | IDLE | 1.16 | 2.96 | 2.74 | -0.08 | 1378515.9 | 1.28 | tvl≈177,215,533 |
| QNTUSDT | IDLE | 1.84 | 3.57 | 0.76 | 0.02 | 1229436.37 | 1.99 | n/a |
| CCUSDT | IDLE | 0.67 | 1.36 | 0.96 | 0.03 | 570024.35 | 9.92 | no_map |
| KITEUSDT | IDLE | 2.5 | 4.72 | 1.87 | 0.0 | 77641.27 | 10.4 | no_map |
| RWAINCUSDT | IDLE | 1.98 | 3.6 | 2.38 | 0.01 | 11009.85 | 14.62 | no_map |
| ZBCNUSDT | IDLE | 0.6 | 1.51 | 0.24 | -0.06 | 262398.65 | 15.26 | n/a |
| REDUSDT | IDLE | 1.43 | 2.64 | 1.52 | 0.01 | 56409.33 | 10.04 | tvl≈3,700,279 |
| CHIPUSDT | IDLE | 1.11 | 3.56 | 2.92 | 0.06 | 99711.57 | 15.23 | no_map |
| EDELUSDT | IDLE | 0.64 | 2.32 | 1.5 | 0.12 | 205107.79 | 9.99 | no_map |
| BIOUSDT | IDLE | 1.17 | 2.06 | 1.81 | 0.02 | 72532.17 | 3.48 | n/a |
| HBARUSDT | IDLE | 1.0 | 1.9 | 0.65 | 0.01 | 310920.63 | 4.31 | empty_tvl |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.61 | -0.01 | 52709.84 | 7.86 | no_map |
| TELUSDT | IDLE | 1.61 | 2.95 | 1.75 | -0.01 | 118541.24 | 43.17 | no_map |
| RIZEUSDT | IDLE | 0.39 | 2.28 | 0.78 | 0.08 | 64820.04 | 57.18 | no_map |
| MNSRYUSDT | IDLE | 0.39 | 0.77 | 0.13 | 0.01 | 41112.94 | 8.1 | no_map |
| FLUIDUSDT | IDLE | 0.25 | 1.47 | 1.05 | -0.01 | 17332.36 | 21.38 | tvl≈2,424,436,932 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
