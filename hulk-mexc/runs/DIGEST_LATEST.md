# Hulk DIGEST — 2026-09-22T00:08:13Z

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
| XRPUSDT | IDLE | 1.81 | 5.16 | 2.25 | 0.08 | 111452726.72 | 1.95 | n/a |
| ETHUSDT | IDLE | 1.06 | 1.92 | 1.28 | 0.04 | 733877175.04 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.91 | 1.66 | 1.14 | 0.06 | 1070568208.91 | 0.05 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 18.24 | 13.22 | 0.07 | 254253.38 | 29.75 | no_map |
| HBARUSDT | IDLE | 1.49 | 3.8 | 0.43 | 0.07 | 1131648.86 | 8.56 | empty_tvl |
| PYTHUSDT | IDLE | 1.53 | 3.83 | 0.96 | 0.03 | 732490.82 | 1.57 | tvl≈142,822,800 |
| CCUSDT | IDLE | 1.88 | 3.69 | 0.41 | 0.08 | 616503.66 | 7.6 | no_map |
| WUSDT | IDLE | 1.13 | 2.72 | 0.12 | 0.03 | 555590.45 | 5.04 | tvl≈1,796,047,632 |
| ZBCNUSDT | IDLE | 2.19 | 5.38 | 3.52 | 0.07 | 261737.79 | 11.2 | n/a |
| RWAINCUSDT | IDLE | 2.79 | 7.23 | 1.19 | 0.09 | 19766.36 | 43.74 | no_map |
| RIZEUSDT | IDLE | 1.87 | 12.26 | 9.22 | -0.2 | 49398.28 | 135.46 | no_map |
| CHIPUSDT | IDLE | 1.04 | 4.98 | 2.61 | 0.08 | 147196.44 | 17.3 | no_map |
| BIOUSDT | IDLE | 1.03 | 2.06 | 0.03 | 0.05 | 102107.41 | 10.28 | n/a |
| KITEUSDT | IDLE | 0.95 | 1.78 | 0.77 | 0.02 | 81108.09 | 10.95 | no_map |
| REDUSDT | IDLE | 0.89 | 1.76 | 0.12 | 0.0 | 103725.86 | 15.73 | tvl≈2,738,435 |
| QNTUSDT | IDLE | 1.49 | 2.72 | 1.76 | 0.04 | 112775.53 | 13.5 | n/a |
| TELUSDT | IDLE | 1.2 | 3.43 | 2.55 | 0.09 | 116349.04 | 42.51 | no_map |
| FLUIDUSDT | IDLE | 1.05 | 2.43 | 1.36 | 0.08 | 11967.61 | 19.97 | tvl≈2,676,193,889 |
| MNSRYUSDT | IDLE | 0.77 | 1.5 | 0.22 | 0.04 | 42326.92 | 10.24 | no_map |
| RWAUSDT | IDLE | 0.56 | 1.02 | 0.65 | 0.01 | 58063.13 | 7.23 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
