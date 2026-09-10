# Hulk DIGEST — 2026-09-10T18:15:58Z

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
| ETHUSDT | IDLE | 1.49 | 2.87 | 0.71 | -0.01 | 451511186.73 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.08 | 1.97 | 1.3 | -0.05 | 46252136.25 | 0.74 | n/a |
| BTCUSDT | IDLE | 0.55 | 1.0 | 0.65 | -0.02 | 558199440.98 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.92 | 4.44 | 2.78 | -0.08 | 883866.15 | 1.94 | tvl≈117,068,218 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 16.37 | 11.99 | 0.06 | 261281.49 | 18.17 | no_map |
| CCUSDT | IDLE | 2.34 | 4.15 | 3.55 | -0.04 | 559612.91 | 9.15 | no_map |
| RIZEUSDT | IDLE | 0.83 | 44.57 | 20.9 | -0.52 | 121401.91 | 131.43 | no_map |
| ZBCNUSDT | IDLE | 1.76 | 3.28 | 1.57 | 0.0 | 197714.88 | 5.96 | n/a |
| WUSDT | IDLE | 1.13 | 3.07 | 1.47 | -0.07 | 220733.38 | 13.54 | tvl≈1,478,926,033 |
| KITEUSDT | IDLE | 1.83 | 3.83 | 0.92 | -0.04 | 57425.8 | 13.6 | no_map |
| BIOUSDT | IDLE | 1.53 | 3.1 | 1.95 | -0.07 | 81508.88 | 7.96 | n/a |
| REDUSDT | IDLE | 1.41 | 2.93 | 2.43 | -0.09 | 68161.41 | 19.94 | tvl≈2,207,192 |
| CHIPUSDT | IDLE | 0.97 | 4.51 | 2.95 | -0.18 | 86840.3 | 17.01 | no_map |
| RWAINCUSDT | IDLE | 1.31 | 2.38 | 1.55 | -0.02 | 5136.94 | 33.76 | no_map |
| HBARUSDT | IDLE | 0.96 | 1.76 | 1.09 | -0.04 | 285746.71 | 1.33 | empty_tvl |
| TELUSDT | IDLE | 1.44 | 2.68 | 1.39 | -0.02 | 82121.39 | 5.63 | no_map |
| QNTUSDT | IDLE | 1.35 | 2.5 | 1.29 | -0.02 | 36171.98 | 1.52 | n/a |
| MNSRYUSDT | IDLE | 0.62 | 1.17 | 0.44 | -0.03 | 29773.0 | 19.53 | no_map |
| RWAUSDT | IDLE | 0.36 | 0.69 | 0.15 | -0.05 | 52860.89 | 15.2 | no_map |
| FLUIDUSDT | IDLE | 0.47 | 0.94 | 0.0 | -0.07 | 2232.87 | 21.78 | tvl≈2,642,886,548 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
