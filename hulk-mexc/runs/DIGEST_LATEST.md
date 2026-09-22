# Hulk DIGEST — 2026-09-22T02:04:26Z

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
| XRPUSDT | IDLE | 1.85 | 4.67 | 3.81 | 0.07 | 112025855.94 | 0.66 | n/a |
| BTCUSDT | IDLE | 1.05 | 1.86 | 1.59 | 0.05 | 1079605051.34 | 0.0 | no_map |
| ETHUSDT | IDLE | 1.02 | 1.84 | 1.38 | 0.03 | 693153724.7 | 0.04 | no_map |
| PYTHUSDT | IDLE | 2.24 | 5.01 | 2.06 | 0.05 | 751435.84 | 12.58 | tvl≈142,076,380 |
| CCUSDT | IDLE | 2.33 | 4.43 | 1.6 | 0.06 | 668032.7 | 10.16 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 17.48 | 13.94 | 0.06 | 238097.24 | 16.63 | no_map |
| HBARUSDT | IDLE | 1.19 | 2.49 | 1.69 | 0.08 | 1104685.71 | 3.25 | empty_tvl |
| WUSDT | IDLE | 1.23 | 2.45 | 0.51 | 0.05 | 541057.65 | 5.04 | tvl≈1,811,717,707 |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 19.17 | 13.22 | -0.21 | 54689.44 | 114.29 | no_map |
| ZBCNUSDT | IDLE | 2.08 | 4.61 | 3.31 | 0.04 | 265241.36 | 29.76 | n/a |
| REDUSDT | IDLE | 2.39 | 4.77 | 0.01 | 0.04 | 99176.07 | 0.64 | tvl≈2,738,435 |
| CHIPUSDT | IDLE | 1.14 | 5.8 | 0.0 | 0.12 | 164200.95 | 18.84 | no_map |
| BIOUSDT | IDLE | 1.42 | 2.73 | 0.75 | 0.06 | 110426.12 | 10.29 | n/a |
| KITEUSDT | IDLE | 1.51 | 2.87 | 0.99 | 0.05 | 80884.18 | 12.47 | no_map |
| QNTUSDT | IDLE | 1.75 | 3.17 | 2.21 | 0.03 | 114969.88 | 4.51 | n/a |
| RWAINCUSDT | IDLE | 0.82 | 1.92 | 1.73 | 0.08 | 19870.69 | 5.48 | no_map |
| TELUSDT | IDLE | 1.17 | 3.35 | 2.34 | 0.07 | 115749.08 | 67.71 | no_map |
| RWAUSDT | IDLE | 0.75 | 1.31 | 1.22 | 0.0 | 57822.6 | 36.3 | no_map |
| MNSRYUSDT | IDLE | 0.79 | 1.5 | 0.52 | 0.03 | 41529.19 | 39.85 | no_map |
| FLUIDUSDT | IDLE | 0.64 | 1.33 | 1.02 | 0.09 | 12018.84 | 22.01 | tvl≈2,671,271,951 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
