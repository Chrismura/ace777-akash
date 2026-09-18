# Hulk DIGEST — 2026-09-18T09:14:56Z

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
| XRPUSDT | IDLE | 1.03 | 2.01 | 0.31 | 0.02 | 40357421.04 | 3.74 | n/a |
| ETHUSDT | IDLE | 0.96 | 1.89 | 0.16 | 0.03 | 353923069.4 | 0.2 | no_map |
| BTCUSDT | IDLE | 0.83 | 1.63 | 0.16 | 0.02 | 546984862.81 | 0.36 | no_map |
| CCUSDT | IDLE | 1.72 | 5.8 | 1.1 | 0.09 | 652230.4 | 2.69 | no_map |
| PYTHUSDT | IDLE | 0.78 | 2.59 | 0.3 | 0.12 | 619816.14 | 1.65 | tvl≈135,621,931 |
| WUSDT | IDLE | 1.24 | 3.66 | 0.43 | 0.1 | 378526.8 | 19.48 | tvl≈1,539,387,751 |
| CHIPUSDT | IDLE | 1.42 | 6.85 | 2.17 | 0.12 | 152461.55 | 25.16 | no_map |
| BIOUSDT | IDLE | 1.81 | 4.06 | 0.52 | 0.07 | 79162.65 | 3.7 | n/a |
| KITEUSDT | IDLE | 1.89 | 3.58 | 1.34 | 0.03 | 73710.43 | 14.62 | no_map |
| REDUSDT | IDLE | 1.71 | 3.52 | 0.3 | 0.06 | 67829.55 | 10.76 | tvl≈2,487,844 |
| HBARUSDT | IDLE | 1.12 | 2.22 | 0.18 | 0.04 | 469713.43 | 1.29 | empty_tvl |
| ZBCNUSDT | IDLE | 1.02 | 1.98 | 0.34 | 0.03 | 251043.27 | 46.12 | n/a |
| EDELUSDT | IDLE | 0.43 | 4.3 | 1.95 | -0.09 | 262062.94 | 21.67 | no_map |
| RWAINCUSDT | IDLE | 1.67 | 3.34 | 0.06 | -0.01 | 10356.07 | 23.54 | no_map |
| TELUSDT | IDLE | 1.54 | 3.01 | 0.48 | 0.01 | 75607.49 | 61.2 | no_map |
| RIZEUSDT | IDLE | 0.26 | 3.41 | 1.23 | 0.07 | 54827.7 | 106.25 | no_map |
| QNTUSDT | IDLE | 0.87 | 1.62 | 0.81 | 0.02 | 44600.85 | 6.38 | n/a |
| MNSRYUSDT | IDLE | 0.5 | 0.98 | 0.12 | 0.03 | 43159.21 | 6.82 | no_map |
| RWAUSDT | IDLE | 0.53 | 1.04 | 0.15 | 0.02 | 57105.33 | 36.94 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 148.34 | 21.76 | tvl≈2,616,975,414 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
