# Hulk DIGEST — 2026-09-01T17:27:16Z

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
| XRPUSDT | IDLE | 1.03 | 1.89 | 1.17 | -0.0 | 30827620.54 | 2.19 | n/a |
| ETHUSDT | IDLE | 0.87 | 1.59 | 1.02 | -0.01 | 291691922.13 | 0.25 | no_map |
| BTCUSDT | IDLE | 0.79 | 1.41 | 1.12 | -0.01 | 519230360.77 | 0.0 | no_map |
| CHIPUSDT | IDLE | 3.45 | 14.28 | 4.95 | 0.1 | 501108.69 | 4.71 | no_map |
| ZBCNUSDT | IDLE | 3.66 | 6.8 | 3.43 | 0.03 | 217145.26 | 14.36 | n/a |
| PYTHUSDT | IDLE | 1.55 | 2.96 | 0.96 | 0.05 | 631909.84 | 1.98 | tvl≈112,789,076 |
| CCUSDT | IDLE | 2.05 | 4.86 | 3.5 | -0.03 | 417482.92 | 9.6 | no_map |
| WUSDT | IDLE | 2.24 | 4.35 | 0.82 | 0.06 | 284381.46 | 14.44 | tvl≈1,535,468,072 |
| REDUSDT | IDLE | 2.38 | 5.3 | 1.58 | 0.06 | 74920.13 | 11.61 | tvl≈2,031,843 |
| RIZEUSDT | IDLE | 2.33 | 5.19 | 4.2 | -0.06 | 43536.97 | 25.48 | no_map |
| KITEUSDT | IDLE | 2.05 | 3.97 | 0.88 | 0.05 | 70116.16 | 10.57 | no_map |
| BIOUSDT | IDLE | 1.27 | 2.26 | 1.83 | -0.02 | 69268.74 | 3.88 | n/a |
| EDELUSDT | IDLE | 0.75 | 5.12 | 3.42 | -0.06 | 172599.9 | 53.0 | no_map |
| HBARUSDT | IDLE | 1.13 | 2.05 | 1.46 | 0.02 | 230025.65 | 1.34 | empty_tvl |
| QNTUSDT | IDLE | 1.93 | 3.79 | 0.41 | 0.04 | 43217.93 | 7.83 | n/a |
| RWAINCUSDT | IDLE | 1.51 | 2.86 | 1.1 | -0.03 | 6195.38 | 116.28 | no_map |
| TELUSDT | IDLE | 1.06 | 1.89 | 1.56 | 0.01 | 97227.57 | 5.87 | no_map |
| RWAUSDT | IDLE | 0.72 | 1.62 | 1.37 | -0.02 | 60696.96 | 7.7 | no_map |
| MNSRYUSDT | IDLE | 0.63 | 1.13 | 0.91 | -0.01 | 32647.05 | 42.2 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 266.03 | 22.23 | tvl≈2,593,543,808 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
