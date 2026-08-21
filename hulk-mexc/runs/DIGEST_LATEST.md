# Hulk DIGEST — 2026-08-21T19:58:06Z

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
| PYTHUSDT | IDLE | 1.37 | 4.99 | 4.2 | 0.07 | 5442955.56 | 8.53 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.17 | 4.21 | 3.65 | 0.12 | 128951890.79 | 2.92 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 26.97 | 13.81 | 0.16 | 153934.73 | 42.71 | tvl≈2,358,074 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 11.37 | 9.35 | 0.07 | 481646.19 | 16.07 | n/a |
| CCUSDT | IDLE | 2.04 | 5.44 | 1.86 | 0.06 | 633451.68 | 2.8 | no_map |
| HBARUSDT | IDLE | 1.62 | 3.1 | 2.99 | 0.05 | 793789.33 | 1.31 | empty_tvl |
| CHIPUSDT | IDLE | 1.24 | 4.81 | 4.09 | 0.09 | 513902.9 | 6.22 | no_map |
| WUSDT | IDLE | 2.16 | 3.92 | 2.94 | 0.05 | 363570.9 | 12.85 | tvl≈1,603,481,943 |
| BIOUSDT | IDLE | 2.65 | 5.33 | 4.51 | -0.0 | 190545.87 | 6.42 | n/a |
| RIZEUSDT | IDLE | 2.24 | 11.27 | 2.82 | 0.03 | 56432.16 | 45.77 | no_map |
| EDELUSDT | IDLE | 2.43 | 4.29 | 3.79 | -0.05 | 79684.71 | 33.8 | no_map |
| KITEUSDT | IDLE | 1.28 | 4.0 | 3.31 | 0.1 | 61332.14 | 9.39 | no_map |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 80.49 | no_map |
| TELUSDT | IDLE | 1.88 | 4.46 | 2.9 | 0.01 | 183588.12 | 37.93 | no_map |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2868.1 | 63.29 | no_map |
| QNTUSDT | IDLE | 1.65 | 3.01 | 1.89 | 0.04 | 59915.81 | 7.84 | n/a |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.99 | 0.03 | 54335.88 | 8.31 | no_map |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4276.39 | 22.41 | tvl≈2,554,565,268 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
