# Hulk DIGEST — 2026-08-22T06:30:59Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.88 | 0.07 | 19904426.77 | 47.22 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 23.87 | 8.06 | 0.2 | 211076077.48 | 6.41 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 15.8 | 8.98 | 0.05 | 1387521.29 | 6.33 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.32 | -0.1 | 689320.53 | 6.72 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.68 | 0.07 | 614612.25 | 10.33 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 29.98 | 13.51 | -0.05 | 245702.64 | 3.33 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 42.58 | 11.23 | 0.09 | 166329.4 | 14.8 | tvl≈2,081,438 |
| CCUSDT | IDLE | 1.99 | 11.25 | 3.17 | 0.19 | 775748.33 | 9.9 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 8.47 | 5.86 | 0.03 | 545742.93 | 16.46 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.83 | 0.04 | 200276.34 | 7.73 | n/a |
| KITEUSDT | IDLE | 2.84 | 9.68 | 4.71 | 0.09 | 74843.69 | 9.15 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 23.45 | tvl≈2,556,657,142 |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.03 | 88112.74 | 55.96 | no_map |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.01 | 11437.27 | 64.66 | no_map |
| TELUSDT | IDLE | 2.14 | 5.52 | 3.95 | 0.06 | 196550.26 | 35.98 | no_map |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.93 | 3.99 | 1.59 | 0.09 | 59533.74 | 46.34 | no_map |
| RWAUSDT | IDLE | 1.84 | 3.38 | 1.99 | 0.04 | 58158.75 | 24.36 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
