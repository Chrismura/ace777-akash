# Hulk DIGEST — 2026-09-19T08:58:00Z

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
| XRPUSDT | IDLE | 1.04 | 2.18 | 1.56 | 0.06 | 68821413.68 | 1.41 | n/a |
| ETHUSDT | IDLE | 0.94 | 1.8 | 0.51 | 0.06 | 601312443.93 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.31 | 0.6 | 0.1 | 0.04 | 651103359.68 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.63 | 4.8 | 3.13 | -0.01 | 712546.26 | 1.66 | tvl≈138,470,224 |
| WUSDT | IDLE | 1.06 | 3.23 | 0.88 | 0.06 | 985972.62 | 8.24 | tvl≈1,584,006,692 |
| CCUSDT | IDLE | 2.22 | 3.92 | 3.53 | -0.01 | 433110.1 | 1.82 | no_map |
| EDELUSDT | IDLE | 2.2 | 10.9 | 8.99 | -0.11 | 194408.89 | 53.54 | no_map |
| CHIPUSDT | IDLE | 2.2 | 7.21 | 5.61 | 0.03 | 145932.25 | 15.58 | no_map |
| RIZEUSDT | IDLE | 2.03 | 16.62 | 10.59 | -0.08 | 40384.86 | 67.45 | no_map |
| HBARUSDT | IDLE | 1.1 | 2.11 | 0.66 | 0.03 | 626641.62 | 1.26 | empty_tvl |
| KITEUSDT | IDLE | 2.06 | 4.06 | 0.43 | 0.06 | 70853.87 | 11.17 | no_map |
| ZBCNUSDT | IDLE | 1.21 | 2.36 | 0.38 | 0.02 | 190080.34 | 15.83 | n/a |
| BIOUSDT | IDLE | 1.46 | 2.73 | 1.31 | 0.01 | 82511.75 | 11.06 | n/a |
| REDUSDT | IDLE | 1.22 | 6.49 | 1.53 | 0.09 | 127498.13 | 63.9 | tvl≈2,684,962 |
| RWAINCUSDT | IDLE | 0.72 | 1.44 | 0.0 | 0.05 | 5380.05 | 39.76 | no_map |
| QNTUSDT | IDLE | 0.8 | 1.59 | 0.0 | 0.02 | 75141.47 | 3.13 | n/a |
| TELUSDT | IDLE | 0.7 | 3.03 | 1.07 | 0.1 | 136533.82 | 57.05 | no_map |
| RWAUSDT | IDLE | 0.92 | 1.71 | 0.81 | 0.0 | 56682.17 | 36.91 | no_map |
| FLUIDUSDT | IDLE | 0.6 | 2.57 | 1.5 | 0.17 | 7478.73 | 17.68 | tvl≈2,634,281,652 |
| MNSRYUSDT | IDLE | 0.3 | 0.55 | 0.33 | 0.04 | 40495.76 | 22.34 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
