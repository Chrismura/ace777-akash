# Hulk DIGEST — 2026-08-22T00:02:17Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.33 | 0.1 | 6242075.06 | 2.04 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.02 | 8.23 | 1.5 | 0.14 | 142236957.35 | 2.75 | n/a |
| HBARUSDT | IDLE | 2.77 | 6.36 | 1.19 | 0.08 | 906365.53 | 1.25 | empty_tvl |
| ZBCNUSDT | IDLE | 2.88 | 11.25 | 2.61 | 0.12 | 515163.55 | 12.56 | n/a |
| CCUSDT | IDLE | 1.92 | 7.42 | 0.5 | 0.14 | 645097.89 | 4.43 | no_map |
| WUSDT | IDLE | 2.77 | 6.91 | 1.58 | 0.08 | 378961.62 | 13.35 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.16 | 0.04 | 537216.82 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.89 | 0.03 | 187148.28 | 6.21 | n/a |
| EDELUSDT | IDLE | 2.56 | 5.5 | 1.09 | -0.01 | 80025.88 | 21.98 | no_map |
| RIZEUSDT | IDLE | 2.26 | 9.82 | 4.13 | 0.13 | 58948.96 | 45.81 | no_map |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.46 | 0.06 | 189812.38 | 35.89 | no_map |
| QNTUSDT | IDLE | 2.48 | 5.42 | 0.31 | 0.07 | 166696.95 | 7.49 | n/a |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | no_map |
| REDUSDT | IDLE | 0.57 | 4.91 | 2.07 | 0.19 | 157881.17 | 19.36 | tvl≈2,226,572 |
| KITEUSDT | IDLE | 1.09 | 3.12 | 0.8 | 0.1 | 61521.16 | 9.22 | no_map |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | no_map |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54505.75 | 16.35 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.1 | 4934.79 | 50.25 | tvl≈2,594,160,978 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
