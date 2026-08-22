# Hulk DIGEST — 2026-08-22T17:17:26Z

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
| PYTHUSDT | IDLE | 1.74 | 8.48 | 0.95 | 0.1 | 49168933.41 | 3.82 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.61 | 0.05 | 214083384.48 | 1.36 | n/a |
| CCUSDT | IDLE | 0.95 | 4.25 | 0.59 | 0.11 | 770596.18 | 8.36 | no_map |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.1 | -0.0 | 1103344.76 | 5.17 | empty_tvl |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.0 | -0.1 | 631047.95 | 3.36 | no_map |
| WUSDT | IDLE | 0.6 | 2.58 | 0.34 | -0.01 | 535623.8 | 12.64 | tvl≈1,556,368,553 |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.67 | -0.07 | 226285.43 | 3.34 | n/a |
| ZBCNUSDT | IDLE | 1.26 | 3.45 | 1.18 | -0.01 | 309834.11 | 25.01 | n/a |
| EDELUSDT | IDLE | 1.76 | 3.11 | 2.8 | -0.03 | 74858.97 | 22.99 | no_map |
| KITEUSDT | IDLE | 1.38 | 3.22 | 0.85 | 0.04 | 87845.11 | 13.27 | no_map |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.21 | -0.13 | 122175.33 | 11.74 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.14 | 2.63 | 1.12 | 0.04 | 46107.88 | 23.73 | no_map |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.94 | -0.01 | 181145.48 | 1.57 | n/a |
| TELUSDT | IDLE | 0.99 | 2.37 | 2.0 | -0.01 | 136297.86 | 32.15 | no_map |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 102.23 | no_map |
| RWAUSDT | IDLE | 0.58 | 1.14 | 0.16 | 0.02 | 56184.29 | 8.08 | no_map |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.6 | tvl≈2,551,700,555 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
