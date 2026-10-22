# Hulk DIGEST — 2026-10-22T22:15:31Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.94 | 1.77 | 0.67 | -0.05 | 31254934.77 | 0.76 | n/a |
| ETHUSDT | IDLE | 0.6 | 1.13 | 0.44 | -0.04 | 238104061.64 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.32 | 0.63 | 0.09 | -0.04 | 464877160.12 | 0.0 | no_map |
| WUSDT | IDLE | 1.04 | 2.99 | 0.91 | -0.09 | 1293071.4 | 16.52 | tvl≈1,534,070,737 |
| HBARUSDT | IDLE | 0.8 | 1.59 | 0.1 | -0.06 | 1268650.93 | 7.53 | empty_tvl |
| PYTHUSDT | IDLE | 1.43 | 3.15 | 2.84 | -0.09 | 568440.76 | 1.38 | tvl≈164,380,455 |
| EDELUSDT | IDLE | 1.39 | 3.64 | 1.63 | -0.08 | 519717.18 | 31.36 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 7.42 | 5.04 | -0.04 | 40433.8 | 44.91 | no_map |
| QNTUSDT | IDLE | 0.77 | 2.13 | 0.9 | -0.1 | 697869.34 | 1.06 | n/a |
| CHIPUSDT | IDLE | 1.2 | 5.03 | 0.31 | -0.08 | 247354.76 | 15.65 | no_map |
| RWAINCUSDT | IDLE | 1.81 | 3.47 | 1.06 | 0.0 | 50178.09 | 5.65 | no_map |
| ZBCNUSDT | IDLE | 1.09 | 2.3 | 0.68 | -0.04 | 198527.62 | 29.23 | n/a |
| CCUSDT | IDLE | 0.56 | 1.6 | 0.41 | -0.11 | 260174.17 | 6.83 | no_map |
| REDUSDT | IDLE | 1.23 | 2.28 | 1.33 | -0.06 | 95679.53 | 11.44 | tvl≈3,506,358 |
| BIOUSDT | IDLE | 0.82 | 1.72 | 0.8 | -0.07 | 62397.94 | 4.27 | n/a |
| KITEUSDT | IDLE | 0.77 | 1.49 | 0.35 | -0.02 | 60066.46 | 9.16 | no_map |
| FLUIDUSDT | IDLE | 1.42 | 4.16 | 0.26 | -0.07 | 22573.59 | 21.47 | tvl≈2,201,423,923 |
| IOTAUSDT | IDLE | 0.89 | 1.94 | 0.76 | -0.08 | 78932.34 | 33.89 | no_map |
| LAUSDT | IDLE | 0.71 | 1.98 | 0.7 | -0.09 | 55452.33 | 25.81 | no_map |
| WAXLUSDT | IDLE | 0.69 | 2.42 | 0.8 | -0.12 | 58103.88 | 64.06 | no_map |
| RWAUSDT | IDLE | 0.21 | 0.4 | 0.16 | -0.02 | 52381.18 | 7.97 | no_map |
| MNSRYUSDT | IDLE | 0.62 | 1.16 | 0.55 | -0.01 | 38098.18 | 65.78 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
