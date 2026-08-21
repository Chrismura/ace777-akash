# Hulk DIGEST — 2026-08-21T08:26:21Z

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
| PYTHUSDT | IDLE | 2.88 | 12.1 | 3.7 | 0.13 | 2895510.94 | 2.05 | tvl≈108,595,989 |
| XRPUSDT | IDLE | 1.27 | 5.69 | 1.29 | 0.19 | 126930286.21 | 2.24 | n/a |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.72 | 18.43 | 6.33 | 0.01 | 40701.73 | 46.34 | no_map |
| CHIPUSDT | IDLE | 1.09 | 6.22 | 4.41 | 0.13 | 490315.62 | 3.02 | no_map |
| CCUSDT | IDLE | 1.36 | 2.73 | 0.0 | -0.0 | 492059.16 | 8.75 | no_map |
| ZBCNUSDT | IDLE | 1.88 | 7.31 | 0.42 | 0.08 | 306038.08 | 22.48 | n/a |
| WUSDT | IDLE | 2.09 | 4.09 | 0.54 | 0.06 | 292289.85 | 13.97 | tvl≈1,552,902,640 |
| BIOUSDT | IDLE | 2.22 | 6.52 | 0.76 | 0.03 | 197097.28 | 6.13 | n/a |
| REDUSDT | IDLE | 2.06 | 6.07 | 3.04 | -0.05 | 120748.59 | 14.17 | tvl≈1,952,575 |
| HBARUSDT | IDLE | 1.32 | 2.59 | 0.38 | 0.05 | 539668.36 | 2.63 | empty_tvl |
| EDELUSDT | IDLE | 2.02 | 3.61 | 2.85 | 0.02 | 75437.72 | 21.72 | no_map |
| KITEUSDT | IDLE | 2.16 | 4.34 | 0.0 | 0.07 | 62363.19 | 23.13 | no_map |
| TELUSDT | IDLE | 1.74 | 8.98 | 1.67 | 0.19 | 220394.53 | 30.88 | no_map |
| QAITUSDT | IDLE | 1.26 | 2.95 | 2.29 | -0.05 | 5525.9 | 67.45 | no_map |
| RWAINCUSDT | IDLE | 0.92 | 1.6 | 1.57 | 0.02 | 8565.73 | 65.47 | no_map |
| QNTUSDT | IDLE | 1.13 | 2.24 | 0.16 | 0.04 | 74036.43 | 9.54 | n/a |
| RWAUSDT | IDLE | 0.9 | 1.79 | 0.08 | 0.03 | 54768.9 | 25.22 | no_map |
| FLUIDUSDT | IDLE | 0.99 | 1.98 | 0.0 | 0.05 | 2623.31 | 21.99 | tvl≈2,538,303,860 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
