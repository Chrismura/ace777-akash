# Hulk DIGEST — 2026-08-22T08:21:50Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 9.17 | 0.03 | 27124043.73 | 5.91 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 23.87 | 9.2 | 0.14 | 223315612.91 | 2.59 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.42 | 0.03 | 1343694.53 | 11.44 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.74 | -0.1 | 684701.48 | 3.34 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.5 | 0.04 | 605358.14 | 14.42 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.47 | -0.04 | 249688.02 | 3.19 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.25 | 0.07 | 154558.76 | 11.39 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.04 | 11.25 | 2.06 | 0.2 | 823612.35 | 8.16 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.08 | 0.03 | 537568.87 | 22.0 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.35 | 0.03 | 194173.2 | 18.49 | n/a |
| KITEUSDT | IDLE | 3.8 | 9.68 | 3.78 | 0.07 | 72871.12 | 11.8 | no_map |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.71 | tvl≈2,562,763,298 |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.35 | -0.03 | 86841.61 | 89.19 | no_map |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11182.34 | 112.81 | no_map |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.95 | -0.0 | 174186.62 | 10.28 | no_map |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.02 | 3209.86 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.85 | 3.73 | 0.85 | 0.01 | 52284.26 | 46.13 | no_map |
| RWAUSDT | IDLE | 1.72 | 3.29 | 0.96 | 0.05 | 58162.18 | 16.1 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
