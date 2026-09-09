# Hulk DIGEST — 2026-09-09T23:13:59Z

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
| XRPUSDT | IDLE | 1.8 | 3.25 | 2.4 | -0.02 | 42738217.92 | 0.72 | n/a |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 10.09 | 7.59 | -0.03 | 1022388.8 | 1.92 | tvl≈126,603,020 |
| ETHUSDT | IDLE | 1.17 | 2.12 | 1.44 | -0.01 | 379293636.03 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.71 | 1.3 | 0.83 | -0.0 | 533240554.61 | 0.04 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 8.4 | 5.14 | -0.02 | 207419.96 | 8.02 | tvl≈1,551,206,777 |
| EDELUSDT | IDLE | 4.19 | 12.28 | 3.91 | 0.04 | 201590.83 | 18.48 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 17.94 | 11.23 | -0.05 | 122790.9 | 15.67 | no_map |
| REDUSDT | IDLE | 3.73 | 7.07 | 2.57 | 0.02 | 62717.92 | 10.02 | tvl≈2,456,013 |
| CCUSDT | IDLE | 1.31 | 2.42 | 1.34 | -0.04 | 616995.27 | 6.74 | no_map |
| BIOUSDT | IDLE | 2.97 | 8.64 | 4.94 | -0.07 | 102760.29 | 3.88 | n/a |
| HBARUSDT | IDLE | 1.83 | 3.28 | 2.48 | -0.04 | 465273.07 | 1.31 | empty_tvl |
| KITEUSDT | IDLE | 2.18 | 4.1 | 1.7 | -0.01 | 58425.24 | 11.43 | no_map |
| RWAINCUSDT | IDLE | 2.23 | 3.99 | 3.13 | -0.02 | 6349.31 | 28.26 | no_map |
| ZBCNUSDT | IDLE | 1.16 | 2.22 | 0.72 | 0.02 | 188533.86 | 21.29 | n/a |
| FLUIDUSDT | IDLE | 2.2 | 3.92 | 3.77 | -0.08 | 951.16 | 21.24 | tvl≈2,651,131,327 |
| RIZEUSDT | IDLE | 0.65 | 7.91 | 0.64 | 0.05 | 72834.18 | 74.46 | no_map |
| RWAUSDT | IDLE | 1.77 | 3.14 | 2.68 | -0.03 | 54965.93 | 22.36 | no_map |
| QNTUSDT | IDLE | 1.17 | 2.16 | 1.15 | -0.0 | 44854.77 | 2.99 | n/a |
| MNSRYUSDT | IDLE | 1.09 | 1.91 | 1.78 | -0.01 | 25470.75 | 16.57 | no_map |
| TELUSDT | IDLE | 1.04 | 1.84 | 1.65 | 0.02 | 101218.7 | 50.18 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
