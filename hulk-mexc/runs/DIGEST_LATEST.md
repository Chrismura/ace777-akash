# Hulk DIGEST — 2026-08-31T17:18:06Z

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
| XRPUSDT | IDLE | 1.0 | 1.92 | 0.54 | -0.03 | 40085267.09 | 2.18 | n/a |
| ETHUSDT | IDLE | 0.87 | 1.68 | 0.35 | -0.02 | 428171929.98 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.79 | 1.54 | 0.32 | -0.01 | 592527114.8 | 0.09 | no_map |
| CHIPUSDT | IDLE | 1.62 | 4.2 | 4.01 | -0.04 | 477380.2 | 2.6 | no_map |
| PYTHUSDT | IDLE | 1.82 | 4.58 | 0.68 | -0.02 | 435072.52 | 2.08 | tvl≈107,018,076 |
| RIZEUSDT | IDLE | 3.46 | 6.17 | 4.99 | -0.04 | 40872.37 | 64.69 | no_map |
| CCUSDT | IDLE | 1.53 | 2.89 | 1.1 | 0.0 | 256956.89 | 10.12 | no_map |
| REDUSDT | IDLE | 2.07 | 3.72 | 2.74 | -0.03 | 67023.99 | 14.12 | tvl≈1,971,683 |
| WUSDT | IDLE | 1.46 | 2.61 | 2.01 | -0.05 | 209272.49 | 14.29 | tvl≈1,497,353,588 |
| ZBCNUSDT | IDLE | 1.43 | 2.86 | 0.02 | -0.02 | 205982.75 | 15.87 | n/a |
| EDELUSDT | IDLE | 0.98 | 5.81 | 4.86 | -0.0 | 128435.4 | 16.75 | no_map |
| KITEUSDT | IDLE | 1.4 | 2.86 | 2.34 | -0.08 | 98275.27 | 18.72 | no_map |
| BIOUSDT | IDLE | 1.18 | 2.23 | 0.94 | -0.04 | 77741.75 | 7.6 | n/a |
| HBARUSDT | IDLE | 1.09 | 1.97 | 1.41 | -0.03 | 291530.26 | 1.36 | empty_tvl |
| RWAINCUSDT | IDLE | 1.3 | 2.55 | 0.28 | -0.03 | 2237.8 | 57.18 | no_map |
| TELUSDT | IDLE | 1.76 | 3.16 | 2.43 | -0.03 | 87875.9 | 59.24 | no_map |
| RWAUSDT | IDLE | 2.23 | 4.42 | 0.3 | 0.06 | 57612.65 | 91.46 | no_map |
| QNTUSDT | IDLE | 0.93 | 1.71 | 1.05 | -0.01 | 51460.98 | 4.9 | n/a |
| FLUIDUSDT | IDLE | 0.94 | 1.76 | 0.81 | -0.01 | 1876.21 | 21.83 | tvl≈2,618,832,661 |
| MNSRYUSDT | IDLE | 0.32 | 0.64 | 0.03 | -0.01 | 25240.98 | 8.12 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
