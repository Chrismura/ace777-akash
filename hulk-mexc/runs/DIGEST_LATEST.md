# Hulk DIGEST — 2026-10-03T00:46:04Z

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
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.13 | 13.13 | 0.1 | 0.03 | 4806513.02 | 9.84 | n/a |
| XRPUSDT | IDLE | 1.0 | 1.99 | 0.1 | -0.0 | 67433545.43 | 1.34 | n/a |
| BTCUSDT | IDLE | 0.38 | 0.76 | 0.01 | -0.0 | 903622783.29 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.37 | 0.73 | 0.07 | -0.01 | 548852402.92 | 0.04 | no_map |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.66 | 9.53 | 0.23 | 0.1 | 644236.68 | 11.02 | tvl≈173,073,077 |
| EDELUSDT | IDLE | 1.56 | 14.79 | 3.02 | 0.33 | 702579.01 | 2.41 | no_map |
| HBARUSDT | IDLE | 1.77 | 4.68 | 0.47 | 0.0 | 965649.84 | 8.78 | empty_tvl |
| WUSDT | IDLE | 1.49 | 3.98 | 0.65 | 0.0 | 507453.53 | 15.71 | tvl≈1,900,398,890 |
| CCUSDT | IDLE | 1.24 | 2.85 | 0.58 | -0.0 | 539154.25 | 9.19 | no_map |
| RWAINCUSDT | IDLE | 3.2 | 9.48 | 2.02 | 0.03 | 6653.23 | 28.23 | no_map |
| CHIPUSDT | IDLE | 2.57 | 5.0 | 1.1 | 0.03 | 90254.65 | 20.45 | no_map |
| BIOUSDT | IDLE | 2.21 | 5.7 | 0.06 | 0.03 | 100786.25 | 12.81 | n/a |
| ZBCNUSDT | IDLE | 1.42 | 4.46 | 0.41 | -0.01 | 222466.88 | 16.32 | n/a |
| KITEUSDT | IDLE | 1.89 | 3.75 | 0.21 | -0.01 | 80203.76 | 10.04 | no_map |
| REDUSDT | IDLE | 1.18 | 5.84 | 1.09 | -0.05 | 117746.4 | 6.53 | tvl≈4,069,147 |
| RIZEUSDT | IDLE | 1.58 | 7.8 | 1.72 | 0.01 | 46715.95 | 245.7 | no_map |
| TELUSDT | IDLE | 0.72 | 2.21 | 0.75 | -0.07 | 149734.93 | 50.66 | no_map |
| FLUIDUSDT | IDLE | 1.07 | 2.7 | 0.49 | 0.08 | 6528.08 | 18.09 | tvl≈2,491,821,024 |
| MNSRYUSDT | IDLE | 0.78 | 1.45 | 0.78 | 0.01 | 40823.68 | 39.97 | no_map |
| RWAUSDT | IDLE | 0.28 | 0.51 | 0.29 | -0.01 | 55500.75 | 7.31 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
