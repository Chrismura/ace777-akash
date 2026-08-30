# Hulk DIGEST — 2026-08-30T17:12:32Z

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
| ETHUSDT | IDLE | 1.56 | 3.05 | 0.42 | 0.03 | 204759686.99 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.25 | 2.44 | 0.38 | 0.02 | 20054149.85 | 1.41 | n/a |
| BTCUSDT | IDLE | 0.81 | 1.58 | 0.31 | 0.01 | 270896851.55 | 0.0 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 7.33 | 5.79 | -0.03 | 525157.57 | 2.5 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 9.26 | 5.84 | -0.07 | 194037.47 | 13.46 | n/a |
| PYTHUSDT | IDLE | 3.01 | 5.66 | 2.41 | 0.03 | 399441.39 | 2.04 | tvl≈107,930,951 |
| WUSDT | IDLE | 1.41 | 2.81 | 0.02 | 0.05 | 222682.68 | 14.6 | tvl≈1,543,338,227 |
| EDELUSDT | IDLE | 2.07 | 5.99 | 3.47 | 0.07 | 72587.33 | 58.46 | no_map |
| CCUSDT | IDLE | 0.89 | 1.62 | 1.05 | 0.01 | 256985.14 | 10.13 | no_map |
| REDUSDT | IDLE | 1.08 | 2.02 | 0.89 | 0.02 | 61660.8 | 11.74 | tvl≈2,031,180 |
| BIOUSDT | IDLE | 0.83 | 1.65 | 0.11 | 0.0 | 79503.65 | 3.62 | n/a |
| KITEUSDT | IDLE | 0.92 | 1.67 | 1.09 | -0.02 | 60775.86 | 10.92 | no_map |
| RWAINCUSDT | IDLE | 1.52 | 2.95 | 0.66 | 0.01 | 1919.93 | 60.42 | no_map |
| TELUSDT | IDLE | 2.21 | 4.37 | 0.29 | 0.0 | 83592.03 | 40.26 | no_map |
| RIZEUSDT | IDLE | 0.94 | 3.06 | 2.15 | -0.06 | 38346.93 | 61.18 | no_map |
| HBARUSDT | IDLE | 0.54 | 1.07 | 0.09 | 0.0 | 130973.8 | 1.32 | empty_tvl |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.56 | 0.0 | 32272.36 | 2.67 | no_map |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 21.47 | tvl≈2,625,311,109 |
| QNTUSDT | IDLE | 0.5 | 0.97 | 0.21 | 0.01 | 38421.62 | 3.22 | n/a |
| RWAUSDT | IDLE | 0.49 | 0.98 | 0.0 | 0.02 | 52691.58 | 8.09 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
