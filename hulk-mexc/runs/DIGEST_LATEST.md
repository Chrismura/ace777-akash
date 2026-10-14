# Hulk DIGEST — 2026-10-14T11:15:22Z

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
| WUSDT | IDLE | 1.42 | 6.53 | 4.42 | -0.17 | 3549592.17 | 7.51 | tvl≈1,647,119,647 |
| PYTHUSDT | IDLE | 2.57 | 5.23 | 2.01 | -0.01 | 1759025.46 | 7.31 | tvl≈181,249,525 |
| ETHUSDT | IDLE | 1.04 | 1.94 | 0.98 | 0.0 | 123833997.9 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.97 | 1.8 | 0.97 | 0.02 | 28010046.96 | 0.73 | n/a |
| BTCUSDT | IDLE | 0.71 | 1.31 | 0.79 | 0.0 | 321135735.28 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.02 | 4.75 | 3.73 | 0.01 | 1547761.52 | 2.4 | n/a |
| CCUSDT | IDLE | 1.7 | 3.38 | 2.91 | -0.01 | 582709.29 | 7.44 | no_map |
| CHIPUSDT | IDLE | 2.83 | 4.99 | 4.43 | -0.04 | 80703.04 | 9.01 | no_map |
| KITEUSDT | IDLE | 2.13 | 6.53 | 4.64 | 0.08 | 78332.62 | 8.85 | no_map |
| EDELUSDT | IDLE | 1.33 | 2.49 | 1.1 | 0.04 | 208777.63 | 14.59 | no_map |
| REDUSDT | IDLE | 1.8 | 3.17 | 2.89 | 0.02 | 62013.41 | 15.55 | tvl≈3,916,642 |
| BIOUSDT | IDLE | 1.39 | 2.47 | 2.05 | 0.0 | 68818.6 | 7.34 | n/a |
| RIZEUSDT | IDLE | 1.46 | 4.98 | 1.16 | 0.05 | 49959.84 | 53.53 | no_map |
| ZBCNUSDT | IDLE | 0.61 | 1.19 | 0.2 | -0.01 | 200344.97 | 13.99 | n/a |
| RWAINCUSDT | IDLE | 1.13 | 2.56 | 2.09 | -0.06 | 34776.0 | 15.61 | no_map |
| HBARUSDT | IDLE | 1.16 | 2.06 | 1.71 | 0.0 | 276043.75 | 4.64 | empty_tvl |
| FLUIDUSDT | IDLE | 2.19 | 6.63 | 3.05 | 0.07 | 18184.15 | 21.41 | tvl≈2,380,473,938 |
| TELUSDT | IDLE | 0.74 | 1.41 | 0.5 | 0.03 | 111813.62 | 16.74 | no_map |
| RWAUSDT | IDLE | 0.29 | 0.55 | 0.31 | -0.01 | 56118.7 | 23.34 | no_map |
| MNSRYUSDT | IDLE | 0.16 | 0.32 | 0.06 | -0.01 | 38605.48 | 2.79 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
