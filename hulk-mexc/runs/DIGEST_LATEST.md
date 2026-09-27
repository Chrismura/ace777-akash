# Hulk DIGEST — 2026-09-27T23:37:23Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.92 | 105.87 | 23.41 | 0.93 | 13869113.79 | 18.93 | n/a |
| PYTHUSDT | IDLE | 2.18 | 4.8 | 4.1 | 0.03 | 2305175.42 | 3.61 | tvl≈193,194,886 |
| WUSDT | IDLE | 1.34 | 7.72 | 2.97 | 0.2 | 5102742.04 | 7.0 | tvl≈1,897,992,344 |
| XRPUSDT | IDLE | 1.4 | 2.51 | 1.87 | -0.01 | 42537243.27 | 1.98 | n/a |
| ETHUSDT | IDLE | 0.59 | 1.1 | 0.5 | -0.0 | 208575642.93 | 0.15 | no_map |
| BTCUSDT | IDLE | 0.45 | 0.83 | 0.52 | -0.0 | 422472993.35 | 0.02 | no_map |
| CCUSDT | IDLE | 1.69 | 2.98 | 2.65 | -0.0 | 619413.6 | 9.61 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 24.16 | 18.29 | -0.24 | 54987.81 | 75.95 | no_map |
| ZBCNUSDT | IDLE | 2.85 | 5.08 | 4.19 | -0.02 | 217129.92 | 24.39 | n/a |
| EDELUSDT | IDLE | 2.39 | 11.46 | 8.61 | -0.15 | 141605.92 | 31.77 | no_map |
| HBARUSDT | IDLE | 1.08 | 2.13 | 0.25 | 0.02 | 793615.76 | 1.05 | empty_tvl |
| RWAINCUSDT | IDLE | 2.02 | 20.76 | 3.65 | 0.19 | 29254.31 | 56.11 | no_map |
| CHIPUSDT | IDLE | 1.97 | 3.74 | 3.02 | -0.05 | 99318.15 | 15.14 | no_map |
| REDUSDT | IDLE | 1.61 | 2.87 | 2.36 | 0.0 | 65577.05 | 12.39 | tvl≈3,109,907 |
| KITEUSDT | IDLE | 1.04 | 2.07 | 0.51 | 0.0 | 114197.64 | 8.49 | no_map |
| BIOUSDT | IDLE | 0.99 | 1.88 | 0.63 | -0.01 | 82013.4 | 9.44 | n/a |
| TELUSDT | IDLE | 0.83 | 2.96 | 0.37 | 0.13 | 178633.74 | 32.12 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.07 | 0.36 | 0.04 | 2838.49 | 21.99 | tvl≈2,591,959,221 |
| RWAUSDT | IDLE | 0.38 | 0.71 | 0.28 | 0.01 | 59049.04 | 56.74 | no_map |
| MNSRYUSDT | IDLE | 0.22 | 0.41 | 0.15 | 0.01 | 39891.95 | 32.9 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
