# Hulk DIGEST — 2026-10-12T21:48:21Z

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
| WUSDT | IDLE | 1.85 | 26.81 | 21.07 | -0.08 | 15506766.3 | 18.15 | tvl≈1,678,403,409 |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.68 | 10.47 | 8.15 | 0.06 | 3372528.62 | 17.0 | tvl≈187,390,750 |
| XRPUSDT | IDLE | 1.69 | 2.97 | 2.73 | -0.04 | 29155555.2 | 2.23 | n/a |
| ETHUSDT | IDLE | 1.16 | 2.03 | 1.89 | -0.01 | 215576626.5 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.56 | 0.99 | 0.81 | -0.01 | 289758965.62 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.83 | 3.36 | 3.06 | -0.06 | 833445.13 | 6.21 | n/a |
| HBARUSDT | IDLE | 1.96 | 3.64 | 3.26 | -0.06 | 591775.78 | 9.09 | empty_tvl |
| RIZEUSDT | IDLE | 2.21 | 14.0 | 8.06 | -0.06 | 70955.17 | 58.95 | no_map |
| CCUSDT | IDLE | 1.02 | 1.83 | 1.44 | -0.02 | 398906.96 | 9.07 | no_map |
| EDELUSDT | IDLE | 1.56 | 6.93 | 2.52 | -0.11 | 282601.73 | 56.25 | no_map |
| KITEUSDT | IDLE | 2.25 | 4.06 | 2.91 | -0.01 | 66385.65 | 11.17 | no_map |
| BIOUSDT | IDLE | 1.91 | 3.69 | 3.52 | -0.07 | 81395.64 | 3.61 | n/a |
| ZBCNUSDT | IDLE | 1.12 | 1.98 | 1.74 | 0.01 | 273784.59 | 9.55 | n/a |
| REDUSDT | IDLE | 0.7 | 4.24 | 4.07 | 0.01 | 265722.19 | 11.76 | tvl≈3,906,190 |
| CHIPUSDT | IDLE | 0.79 | 3.58 | 3.2 | -0.15 | 161203.13 | 15.51 | no_map |
| RWAINCUSDT | IDLE | 1.11 | 2.9 | 1.94 | -0.01 | 31400.35 | 24.75 | no_map |
| TELUSDT | IDLE | 2.07 | 3.89 | 1.62 | 0.03 | 118221.89 | 28.42 | no_map |
| FLUIDUSDT | IDLE | 2.06 | 3.8 | 2.13 | 0.0 | 15823.14 | 42.35 | tvl≈2,393,380,015 |
| RWAUSDT | IDLE | 0.33 | 0.62 | 0.31 | 0.0 | 52550.04 | 23.17 | no_map |
| MNSRYUSDT | IDLE | 0.51 | 0.98 | 0.33 | -0.0 | 41485.86 | 56.37 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
