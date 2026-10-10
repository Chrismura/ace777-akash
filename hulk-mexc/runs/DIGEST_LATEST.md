# Hulk DIGEST — 2026-10-10T11:54:58Z

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
| XRPUSDT | IDLE | 0.4 | 0.73 | 0.51 | 0.0 | 20193218.99 | 1.42 | n/a |
| BTCUSDT | IDLE | 0.19 | 0.37 | 0.07 | -0.0 | 223518575.02 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.14 | 0.27 | 0.03 | -0.0 | 93312405.06 | 0.04 | no_map |
| WUSDT | IDLE | 2.49 | 4.95 | 0.51 | -0.03 | 1108338.8 | 13.83 | tvl≈1,640,097,182 |
| PYTHUSDT | IDLE | 1.03 | 2.92 | 1.77 | -0.07 | 1315010.05 | 3.81 | tvl≈177,215,533 |
| QNTUSDT | IDLE | 1.92 | 3.57 | 1.75 | 0.0 | 1190688.49 | 0.4 | n/a |
| EDELUSDT | IDLE | 2.87 | 7.46 | 1.53 | 0.07 | 227883.98 | 10.04 | no_map |
| CCUSDT | IDLE | 1.03 | 1.86 | 1.3 | -0.05 | 422974.92 | 7.48 | no_map |
| KITEUSDT | IDLE | 2.31 | 4.52 | 0.61 | 0.02 | 76910.96 | 10.27 | no_map |
| RWAINCUSDT | IDLE | 2.03 | 3.65 | 2.72 | -0.01 | 9035.7 | 29.28 | no_map |
| CHIPUSDT | IDLE | 1.29 | 4.08 | 3.59 | 0.04 | 98007.83 | 13.42 | no_map |
| ZBCNUSDT | IDLE | 0.79 | 1.51 | 0.44 | -0.05 | 241173.22 | 15.75 | n/a |
| REDUSDT | IDLE | 1.43 | 2.64 | 1.41 | 0.02 | 55296.77 | 7.35 | tvl≈3,700,279 |
| BIOUSDT | IDLE | 1.24 | 2.32 | 1.13 | 0.02 | 76942.11 | 3.48 | n/a |
| HBARUSDT | IDLE | 0.8 | 1.47 | 0.89 | 0.0 | 329465.97 | 3.24 | empty_tvl |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.61 | -0.01 | 53140.76 | 7.87 | no_map |
| TELUSDT | IDLE | 1.62 | 2.95 | 1.91 | -0.01 | 112359.82 | 48.66 | no_map |
| RIZEUSDT | IDLE | 0.36 | 1.56 | 1.08 | 0.09 | 52652.15 | 57.67 | no_map |
| MNSRYUSDT | IDLE | 0.43 | 0.8 | 0.4 | 0.0 | 40591.37 | 21.65 | no_map |
| FLUIDUSDT | IDLE | 0.48 | 1.42 | 0.91 | -0.01 | 10666.19 | 21.27 | tvl≈2,425,124,559 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
