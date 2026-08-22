# Hulk DIGEST — 2026-08-22T06:22:36Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.07 | 19.14 | 6.77 | 0.09 | 19537898.5 | 24.97 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 23.87 | 9.6 | 0.17 | 209733252.72 | 2.6 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 15.8 | 9.22 | 0.05 | 1385090.13 | 5.08 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.5 | -0.09 | 691446.74 | 3.32 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.67 | 0.06 | 615852.68 | 13.42 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 29.98 | 13.31 | -0.04 | 245098.5 | 13.34 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 42.58 | 10.87 | 0.1 | 166097.6 | 27.78 | tvl≈2,081,438 |
| CCUSDT | IDLE | 1.97 | 11.25 | 2.06 | 0.2 | 770109.79 | 10.58 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 8.47 | 5.65 | 0.03 | 545831.34 | 28.86 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 13.91 | 8.83 | 0.04 | 200319.23 | 7.73 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 9.68 | 5.27 | 0.09 | 74854.74 | 11.96 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 8.47 | 5.26 | 0.05 | 6989.9 | 24.91 | tvl≈2,556,657,142 |
| RWAINCUSDT | IDLE | 2.49 | 4.48 | 3.29 | 0.01 | 11491.79 | 64.66 | no_map |
| EDELUSDT | IDLE | 2.25 | 4.52 | 3.03 | -0.04 | 88176.65 | 89.69 | no_map |
| TELUSDT | IDLE | 2.14 | 5.52 | 4.05 | 0.06 | 196823.32 | 41.17 | no_map |
| QAITUSDT | IDLE | 1.63 | 3.24 | 0.16 | -0.01 | 3303.04 | 63.67 | no_map |
| RIZEUSDT | IDLE | 0.97 | 3.99 | 2.94 | 0.08 | 59427.45 | 46.99 | no_map |
| RWAUSDT | IDLE | 1.83 | 3.38 | 1.83 | 0.05 | 58127.11 | 16.22 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
