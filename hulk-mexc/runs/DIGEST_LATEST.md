# Hulk DIGEST — 2026-08-22T17:06:24Z

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
| PYTHUSDT | IDLE | 1.7 | 8.33 | 0.47 | 0.09 | 49190795.0 | 3.81 | tvl≈115,177,281 |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.46 | 0.06 | 214469875.3 | 2.03 | n/a |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.88 | -0.0 | 1123717.3 | 3.87 | empty_tvl |
| CCUSDT | IDLE | 0.9 | 4.14 | 0.07 | 0.1 | 769926.63 | 10.03 | no_map |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.06 | -0.09 | 631184.77 | 6.71 | no_map |
| WUSDT | IDLE | 0.61 | 2.58 | 0.55 | -0.01 | 543320.99 | 12.69 | tvl≈1,556,368,553 |
| BIOUSDT | IDLE | 1.04 | 6.91 | 5.8 | -0.08 | 226270.52 | 6.69 | n/a |
| ZBCNUSDT | IDLE | 1.26 | 3.45 | 1.15 | -0.02 | 312697.35 | 22.99 | n/a |
| EDELUSDT | IDLE | 1.66 | 3.0 | 2.13 | -0.01 | 74826.77 | 22.83 | no_map |
| KITEUSDT | IDLE | 1.39 | 3.22 | 0.97 | 0.03 | 87598.37 | 13.27 | no_map |
| REDUSDT | IDLE | 0.56 | 5.67 | 3.97 | -0.15 | 123766.38 | 10.03 | tvl≈2,005,037 |
| RIZEUSDT | IDLE | 1.1 | 2.63 | 0.5 | 0.05 | 46188.35 | 45.5 | no_map |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | no_map |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.0 | -0.01 | 181194.36 | 3.15 | n/a |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.73 | 0.0 | 136255.58 | 16.06 | no_map |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 91.62 | no_map |
| RWAUSDT | IDLE | 0.59 | 1.14 | 0.24 | 0.02 | 56289.96 | 8.09 | no_map |
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
