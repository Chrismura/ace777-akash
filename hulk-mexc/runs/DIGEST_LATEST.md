# Hulk DIGEST — 2026-09-10T23:16:05Z

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
| XRPUSDT | IDLE | 1.3 | 2.27 | 2.16 | -0.04 | 41948697.53 | 2.25 | n/a |
| ETHUSDT | IDLE | 0.89 | 1.55 | 1.53 | -0.01 | 419232607.42 | 0.62 | no_map |
| BTCUSDT | IDLE | 0.56 | 0.98 | 0.95 | -0.02 | 537645008.97 | 0.0 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 10.01 | 6.67 | -0.08 | 83223.83 | 23.44 | no_map |
| ZBCNUSDT | IDLE | 2.86 | 5.0 | 4.76 | -0.03 | 203984.03 | 3.94 | n/a |
| RIZEUSDT | IDLE | 0.74 | 41.48 | 6.15 | -0.45 | 132800.34 | 53.76 | no_map |
| CCUSDT | IDLE | 1.3 | 2.28 | 2.16 | -0.06 | 488207.76 | 9.2 | no_map |
| PYTHUSDT | IDLE | 1.37 | 2.46 | 1.83 | -0.01 | 439925.97 | 1.94 | tvl≈115,944,061 |
| WUSDT | IDLE | 1.6 | 2.8 | 2.65 | -0.05 | 171014.42 | 11.61 | tvl≈1,495,678,662 |
| KITEUSDT | IDLE | 1.93 | 3.38 | 3.25 | -0.05 | 56477.17 | 13.91 | no_map |
| EDELUSDT | IDLE | 1.09 | 3.88 | 3.73 | 0.0 | 239257.54 | 27.61 | no_map |
| BIOUSDT | IDLE | 1.7 | 2.97 | 2.8 | -0.05 | 78478.52 | 4.05 | n/a |
| REDUSDT | IDLE | 0.71 | 1.5 | 0.73 | -0.07 | 66535.0 | 12.37 | tvl≈2,183,923 |
| RWAINCUSDT | IDLE | 1.01 | 1.92 | 0.72 | 0.01 | 4551.29 | 27.94 | no_map |
| HBARUSDT | IDLE | 0.96 | 1.67 | 1.62 | -0.02 | 212768.03 | 2.68 | empty_tvl |
| FLUIDUSDT | IDLE | 1.87 | 3.26 | 3.16 | -0.06 | 1786.66 | 21.67 | tvl≈2,648,694,175 |
| QNTUSDT | IDLE | 1.27 | 2.23 | 2.09 | -0.03 | 35726.86 | 7.73 | n/a |
| TELUSDT | IDLE | 1.19 | 2.09 | 1.94 | -0.01 | 85818.47 | 33.92 | no_map |
| RWAUSDT | IDLE | 0.75 | 1.3 | 1.28 | -0.03 | 50908.8 | 22.94 | no_map |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.0 | -0.01 | 34065.25 | 27.89 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
