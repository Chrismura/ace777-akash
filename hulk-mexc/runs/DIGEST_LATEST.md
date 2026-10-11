# Hulk DIGEST — 2026-10-11T21:28:02Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.64 | 32.38 | 10.74 | 0.16 | 4051337.85 | 11.55 | tvl≈1,703,313,486 |
| XRPUSDT | IDLE | 1.11 | 1.95 | 1.77 | -0.01 | 15788580.55 | 2.14 | n/a |
| ETHUSDT | IDLE | 0.86 | 1.54 | 1.25 | 0.01 | 214334059.19 | 0.12 | no_map |
| BTCUSDT | IDLE | 0.61 | 1.07 | 0.94 | 0.0 | 154888824.22 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.43 | 4.34 | 3.46 | -0.02 | 903534.98 | 3.88 | tvl≈174,086,355 |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 21.63 | 10.84 | 0.03 | 39914.37 | 56.7 | no_map |
| EDELUSDT | IDLE | 2.77 | 4.96 | 3.84 | -0.03 | 400788.81 | 23.82 | no_map |
| QNTUSDT | IDLE | 2.21 | 3.86 | 3.72 | -0.02 | 770160.31 | 6.34 | n/a |
| ZBCNUSDT | IDLE | 2.53 | 4.44 | 4.07 | -0.0 | 203293.85 | 10.03 | n/a |
| CCUSDT | IDLE | 1.46 | 2.78 | 2.71 | 0.04 | 344037.47 | 8.85 | no_map |
| CHIPUSDT | IDLE | 1.09 | 4.13 | 3.58 | -0.01 | 291322.56 | 14.86 | no_map |
| BIOUSDT | IDLE | 1.44 | 2.54 | 2.31 | -0.0 | 89299.29 | 3.38 | n/a |
| TELUSDT | IDLE | 2.62 | 4.8 | 2.89 | -0.05 | 179764.69 | 46.65 | no_map |
| RWAINCUSDT | IDLE | 1.42 | 3.82 | 2.72 | 0.01 | 28731.93 | 4.92 | no_map |
| REDUSDT | IDLE | 1.11 | 1.94 | 1.9 | -0.0 | 57654.53 | 8.62 | tvl≈3,802,172 |
| KITEUSDT | IDLE | 1.03 | 1.83 | 1.53 | -0.01 | 75296.64 | 8.7 | no_map |
| HBARUSDT | IDLE | 1.18 | 2.13 | 1.47 | 0.01 | 298408.81 | 6.44 | empty_tvl |
| RWAUSDT | IDLE | 1.68 | 3.05 | 2.05 | 0.02 | 52564.7 | 15.5 | no_map |
| MNSRYUSDT | IDLE | 0.97 | 1.79 | 1.03 | -0.01 | 32195.26 | 15.06 | no_map |
| FLUIDUSDT | IDLE | 0.38 | 2.63 | 2.49 | 0.04 | 61273.98 | 18.8 | tvl≈2,422,636,921 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
