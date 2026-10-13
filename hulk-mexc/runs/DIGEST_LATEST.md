# Hulk DIGEST — 2026-10-13T12:00:26Z

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
| PYTHUSDT | IDLE | 1.71 | 6.04 | 5.08 | -0.08 | 2917534.06 | 4.85 | tvl≈189,488,088 |
| WUSDT | IDLE | 0.76 | 7.64 | 6.57 | -0.27 | 6781938.86 | 12.19 | tvl≈1,706,554,219 |
| XRPUSDT | IDLE | 1.35 | 2.44 | 1.77 | -0.03 | 39130564.75 | 1.47 | n/a |
| ETHUSDT | IDLE | 1.09 | 1.97 | 1.44 | -0.02 | 243741848.25 | 0.56 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 14.24 | 10.32 | -0.11 | 1089279.07 | 6.32 | n/a |
| BTCUSDT | IDLE | 0.8 | 1.46 | 0.93 | -0.0 | 393491110.88 | 0.0 | no_map |
| CCUSDT | IDLE | 1.85 | 3.75 | 0.71 | -0.01 | 425010.28 | 10.47 | no_map |
| EDELUSDT | IDLE | 1.97 | 6.69 | 1.61 | -0.08 | 309980.85 | 17.56 | no_map |
| RWAINCUSDT | IDLE | 3.04 | 5.4 | 4.55 | -0.03 | 31873.57 | 24.84 | no_map |
| REDUSDT | IDLE | 1.77 | 6.14 | 4.96 | -0.07 | 215618.33 | 7.25 | tvl≈3,910,309 |
| CHIPUSDT | IDLE | 2.22 | 5.98 | 5.35 | -0.1 | 138618.79 | 15.6 | no_map |
| ZBCNUSDT | IDLE | 1.95 | 3.45 | 3.06 | -0.06 | 224327.89 | 28.54 | n/a |
| HBARUSDT | IDLE | 1.5 | 3.54 | 2.93 | -0.07 | 547601.85 | 1.16 | empty_tvl |
| KITEUSDT | IDLE | 1.88 | 3.67 | 3.37 | -0.04 | 65808.55 | 11.17 | no_map |
| BIOUSDT | IDLE | 1.61 | 4.62 | 4.2 | -0.07 | 74096.33 | 3.69 | n/a |
| RIZEUSDT | IDLE | 1.23 | 7.45 | 4.61 | -0.11 | 64766.88 | 89.99 | no_map |
| FLUIDUSDT | IDLE | 2.03 | 4.01 | 3.86 | 0.05 | 14671.87 | 21.44 | tvl≈2,398,751,358 |
| TELUSDT | IDLE | 1.67 | 2.95 | 2.59 | -0.02 | 104329.92 | 23.07 | no_map |
| MNSRYUSDT | IDLE | 0.43 | 0.79 | 0.52 | -0.01 | 38471.25 | 4.16 | no_map |
| RWAUSDT | IDLE | 0.17 | 0.31 | 0.15 | 0.0 | 53305.34 | 15.42 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
