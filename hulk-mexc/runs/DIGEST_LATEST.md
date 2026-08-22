# Hulk DIGEST — 2026-08-22T09:50:17Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 19.14 | 11.37 | 0.01 | 46764379.8 | 2.02 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.85 | 23.87 | 11.66 | 0.08 | 218360532.4 | 4.67 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 15.8 | 10.74 | 0.02 | 1265970.96 | 3.87 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 23.96 | 12.59 | -0.1 | 665202.13 | 6.76 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 17.58 | 9.38 | 0.02 | 591757.05 | 14.74 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.48 | -0.03 | 237654.71 | 3.23 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 12.07 | 0.05 | 154255.0 | 11.55 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.25 | 11.25 | 8.33 | 0.12 | 805327.4 | 8.7 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 8.0 | 6.94 | -0.02 | 438496.03 | 17.22 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 9.68 | 5.04 | 0.04 | 73147.12 | 11.01 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.28 | 0.0 | 192872.73 | 1.55 | n/a |
| EDELUSDT | IDLE | 2.53 | 4.52 | 3.57 | -0.03 | 79232.44 | 22.4 | no_map |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 21.36 | tvl≈2,553,890,177 |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.79 | 7.03 | 6.42 | -0.02 | 170876.68 | 47.48 | no_map |
| RWAINCUSDT | IDLE | 2.42 | 4.36 | 3.14 | 0.01 | 11436.39 | 91.42 | no_map |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3199.56 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.85 | -0.01 | 49358.16 | 46.77 | no_map |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.27 | 0.03 | 57610.61 | 8.07 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
