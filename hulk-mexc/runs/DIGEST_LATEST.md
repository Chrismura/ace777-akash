# Hulk DIGEST — 2026-10-10T20:02:39Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 8.29 | 6.62 | 0.03 | 1263747.86 | 7.35 | tvl≈1,652,141,982 |
| ETHUSDT | IDLE | 0.3 | 0.58 | 0.2 | 0.01 | 97743918.67 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.28 | 0.51 | 0.33 | 0.01 | 13732531.04 | 2.13 | n/a |
| BTCUSDT | IDLE | 0.13 | 0.24 | 0.09 | 0.01 | 172092206.44 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.42 | 4.33 | 3.35 | -0.01 | 1224394.79 | 0.83 | n/a |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.63 | 29.57 | 0.51 | 0.33 | 182911.06 | 12.05 | no_map |
| PYTHUSDT | IDLE | 1.21 | 2.26 | 1.07 | -0.02 | 797293.83 | 1.27 | tvl≈177,352,946 |
| CCUSDT | IDLE | 1.4 | 2.54 | 1.69 | -0.03 | 321049.19 | 10.09 | no_map |
| EDELUSDT | IDLE | 1.76 | 3.92 | 0.31 | -0.02 | 225046.46 | 20.44 | no_map |
| BIOUSDT | IDLE | 1.55 | 2.92 | 1.18 | 0.05 | 88026.71 | 6.83 | n/a |
| KITEUSDT | IDLE | 1.3 | 3.16 | 2.88 | 0.08 | 71662.48 | 12.48 | no_map |
| RWAINCUSDT | IDLE | 2.23 | 4.24 | 1.5 | -0.03 | 9657.45 | 78.86 | no_map |
| ZBCNUSDT | IDLE | 0.68 | 1.21 | 0.94 | 0.01 | 201771.66 | 17.03 | n/a |
| TELUSDT | IDLE | 1.95 | 3.63 | 1.75 | -0.01 | 133568.38 | 39.05 | no_map |
| REDUSDT | IDLE | 0.63 | 1.18 | 0.57 | 0.03 | 54614.06 | 7.29 | tvl≈3,764,014 |
| HBARUSDT | IDLE | 0.65 | 1.16 | 0.91 | 0.03 | 326446.71 | 4.33 | empty_tvl |
| RIZEUSDT | IDLE | 0.62 | 1.1 | 0.93 | -0.03 | 43269.46 | 39.85 | no_map |
| FLUIDUSDT | IDLE | 1.29 | 2.45 | 0.83 | 0.01 | 9190.64 | 20.96 | tvl≈2,429,210,471 |
| RWAUSDT | IDLE | 0.44 | 0.79 | 0.63 | 0.01 | 54009.08 | 7.86 | no_map |
| MNSRYUSDT | IDLE | 0.13 | 0.24 | 0.11 | 0.0 | 37759.91 | 12.18 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
