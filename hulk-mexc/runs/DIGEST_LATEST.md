# Hulk DIGEST — 2026-09-02T14:44:17Z

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
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.48 | 14.29 | 11.35 | -0.05 | 948499.78 | 4.83 | no_map |
| XRPUSDT | IDLE | 1.44 | 2.79 | 0.56 | -0.03 | 39395384.43 | 2.24 | n/a |
| ETHUSDT | IDLE | 1.37 | 2.63 | 0.78 | -0.02 | 407382444.1 | 1.25 | no_map |
| BTCUSDT | IDLE | 0.82 | 1.59 | 0.36 | -0.01 | 518066502.79 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.87 | 7.8 | 0.42 | 0.14 | 1085093.36 | 13.95 | tvl≈122,283,218 |
| CCUSDT | IDLE | 2.1 | 3.69 | 3.38 | -0.07 | 357532.12 | 9.99 | no_map |
| REDUSDT | IDLE | 2.78 | 5.41 | 1.0 | 0.03 | 160884.58 | 19.12 | tvl≈2,128,255 |
| WUSDT | IDLE | 1.6 | 2.91 | 1.96 | -0.03 | 397069.94 | 13.72 | tvl≈1,489,033,472 |
| RIZEUSDT | IDLE | 2.26 | 7.8 | 2.8 | -0.07 | 37042.92 | 62.66 | no_map |
| KITEUSDT | IDLE | 1.61 | 6.19 | 1.01 | 0.12 | 88403.16 | 5.07 | no_map |
| RWAINCUSDT | IDLE | 1.93 | 5.69 | 2.85 | 0.06 | 10971.61 | 27.31 | no_map |
| ZBCNUSDT | IDLE | 1.05 | 2.07 | 2.0 | -0.03 | 196969.05 | 5.57 | n/a |
| EDELUSDT | IDLE | 0.66 | 3.7 | 1.13 | 0.08 | 171444.82 | 32.73 | no_map |
| BIOUSDT | IDLE | 1.14 | 2.2 | 0.47 | -0.02 | 72785.75 | 27.54 | n/a |
| FLUIDUSDT | IDLE | 2.38 | 4.18 | 3.93 | -0.07 | 1740.39 | 46.97 | tvl≈2,596,700,031 |
| TELUSDT | IDLE | 1.78 | 3.44 | 0.76 | -0.0 | 74552.07 | 17.61 | no_map |
| HBARUSDT | IDLE | 0.95 | 1.84 | 0.43 | -0.01 | 203502.43 | 1.35 | empty_tvl |
| QNTUSDT | IDLE | 1.27 | 2.48 | 0.34 | 0.02 | 69441.46 | 6.19 | n/a |
| RWAUSDT | IDLE | 0.73 | 1.39 | 0.53 | 0.0 | 51535.11 | 7.65 | no_map |
| MNSRYUSDT | IDLE | 0.38 | 0.72 | 0.23 | -0.01 | 34766.26 | 33.03 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
