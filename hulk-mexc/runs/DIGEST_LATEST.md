# Hulk DIGEST — 2026-10-19T13:59:47Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 1.07 | 1.88 | 1.76 | 0.0 | 153544852.32 | 0.25 | no_map |
| XRPUSDT | IDLE | 0.84 | 1.51 | 1.14 | 0.01 | 32326184.29 | 1.54 | n/a |
| BTCUSDT | IDLE | 0.67 | 1.17 | 1.07 | 0.01 | 332663404.37 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.39 | 4.18 | 3.98 | -0.03 | 983316.43 | 1.38 | tvl≈168,285,307 |
| QNTUSDT | IDLE | 1.62 | 4.45 | 4.18 | 0.01 | 891719.97 | 4.08 | n/a |
| WUSDT | IDLE | 1.99 | 3.86 | 0.84 | -0.01 | 541141.95 | 15.4 | tvl≈1,564,590,340 |
| CCUSDT | IDLE | 1.81 | 4.43 | 0.67 | 0.05 | 337048.17 | 9.48 | no_map |
| EDELUSDT | IDLE | 2.1 | 4.24 | 2.88 | 0.01 | 233453.21 | 22.23 | no_map |
| RWAINCUSDT | IDLE | 2.34 | 6.71 | 5.44 | -0.02 | 90324.53 | 10.56 | no_map |
| HBARUSDT | IDLE | 1.53 | 2.78 | 2.53 | -0.06 | 612047.32 | 3.62 | empty_tvl |
| KITEUSDT | IDLE | 2.14 | 4.17 | 0.73 | 0.04 | 61864.17 | 10.97 | no_map |
| CHIPUSDT | IDLE | 1.55 | 3.94 | 3.69 | 0.0 | 86119.26 | 12.07 | no_map |
| ZBCNUSDT | IDLE | 0.72 | 2.45 | 1.85 | 0.01 | 266742.23 | 33.96 | n/a |
| BIOUSDT | IDLE | 1.4 | 2.54 | 1.68 | -0.0 | 71244.74 | 4.27 | n/a |
| REDUSDT | IDLE | 1.21 | 2.28 | 0.96 | 0.0 | 76322.03 | 9.52 | tvl≈3,388,531 |
| RIZEUSDT | IDLE | 0.94 | 4.84 | 4.55 | -0.07 | 58777.92 | 57.79 | no_map |
| IOTAUSDT | IDLE | 1.72 | 3.11 | 2.14 | 0.0 | 76273.57 | 20.25 | no_map |
| LAUSDT | IDLE | 1.43 | 2.58 | 1.92 | -0.0 | 59005.0 | 24.74 | no_map |
| WAXLUSDT | IDLE | 1.1 | 4.2 | 3.2 | 0.04 | 78281.05 | 52.47 | no_map |
| RWAUSDT | IDLE | 0.72 | 1.35 | 0.63 | 0.01 | 55401.86 | 31.6 | no_map |
| FLUIDUSDT | IDLE | 0.71 | 1.74 | 1.71 | 0.02 | 6323.2 | 21.4 | tvl≈2,230,402,735 |
| MNSRYUSDT | IDLE | 0.29 | 0.53 | 0.27 | -0.0 | 40323.69 | 19.95 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
