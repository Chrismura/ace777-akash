# Hulk DIGEST — 2026-09-27T11:34:48Z

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
| WUSDT | IDLE | 1.87 | 11.19 | 8.05 | 0.13 | 3172536.73 | 8.22 | tvl≈1,918,099,918 |
| PYTHUSDT | IDLE | 1.5 | 6.09 | 1.33 | 0.12 | 2090961.79 | 1.14 | tvl≈188,329,996 |
| QNTUSDT | IDLE | 0.62 | 12.22 | 9.89 | 0.58 | 5458358.43 | 8.49 | n/a |
| XRPUSDT | IDLE | 1.04 | 2.0 | 0.47 | -0.01 | 40937440.4 | 1.95 | n/a |
| ETHUSDT | IDLE | 0.46 | 0.82 | 0.71 | 0.01 | 161530974.98 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.38 | 0.71 | 0.28 | 0.01 | 432494302.74 | 0.0 | no_map |
| CCUSDT | IDLE | 1.77 | 3.39 | 1.0 | 0.02 | 624253.4 | 8.03 | no_map |
| EDELUSDT | IDLE | 2.4 | 5.84 | 3.91 | -0.05 | 148641.67 | 45.34 | no_map |
| REDUSDT | IDLE | 2.5 | 4.43 | 3.79 | 0.01 | 64413.29 | 12.84 | tvl≈3,108,999 |
| HBARUSDT | IDLE | 1.21 | 2.26 | 1.07 | 0.0 | 621218.35 | 1.05 | empty_tvl |
| KITEUSDT | IDLE | 1.4 | 5.5 | 4.69 | 0.09 | 171542.94 | 8.79 | no_map |
| ZBCNUSDT | IDLE | 1.47 | 2.73 | 1.43 | -0.01 | 227387.9 | 11.83 | n/a |
| CHIPUSDT | IDLE | 1.12 | 2.7 | 1.24 | 0.01 | 120894.58 | 16.26 | no_map |
| BIOUSDT | IDLE | 0.87 | 1.57 | 1.09 | -0.04 | 94326.98 | 9.4 | n/a |
| RWAINCUSDT | IDLE | 0.97 | 4.16 | 0.0 | 0.07 | 7173.54 | 4.59 | no_map |
| RIZEUSDT | IDLE | 0.99 | 3.84 | 1.0 | -0.03 | 46705.21 | 61.87 | no_map |
| TELUSDT | IDLE | 1.29 | 4.58 | 0.61 | 0.12 | 139847.34 | 33.48 | no_map |
| MNSRYUSDT | IDLE | 0.97 | 1.92 | 0.09 | 0.01 | 39385.23 | 7.56 | no_map |
| RWAUSDT | IDLE | 0.99 | 1.85 | 0.91 | 0.04 | 55397.15 | 28.25 | no_map |
| FLUIDUSDT | IDLE | 1.03 | 1.9 | 1.11 | 0.02 | 1017.93 | 21.63 | tvl≈2,594,725,898 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
