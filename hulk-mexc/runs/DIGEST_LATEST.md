# Hulk DIGEST — 2026-09-15T04:44:55Z

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
| XRPUSDT | IDLE | 1.09 | 2.09 | 1.61 | 0.03 | 75437310.93 | 0.71 | n/a |
| ETHUSDT | IDLE | 1.0 | 1.77 | 1.57 | -0.01 | 458201031.03 | 0.04 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 49.04 | 21.56 | 0.26 | 435003.87 | 62.34 | no_map |
| BTCUSDT | IDLE | 0.74 | 1.31 | 1.19 | 0.0 | 523301329.95 | 0.0 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.97 | 40.02 | 21.97 | -0.1 | 58672.85 | 99.77 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 16.47 | 13.46 | 0.08 | 164176.14 | 100.14 | tvl≈2,634,302 |
| PYTHUSDT | IDLE | 2.04 | 3.64 | 2.96 | -0.03 | 342399.41 | 1.8 | tvl≈126,453,821 |
| ZBCNUSDT | IDLE | 2.2 | 3.98 | 2.76 | 0.02 | 195035.51 | 18.29 | n/a |
| CCUSDT | IDLE | 1.4 | 2.53 | 1.8 | -0.0 | 313672.07 | 9.37 | no_map |
| WUSDT | IDLE | 1.61 | 2.86 | 2.41 | -0.03 | 203796.49 | 12.18 | tvl≈1,461,065,554 |
| CHIPUSDT | IDLE | 1.62 | 2.85 | 2.63 | -0.05 | 67483.94 | 19.33 | no_map |
| KITEUSDT | IDLE | 1.37 | 2.46 | 1.89 | -0.02 | 64618.38 | 10.41 | no_map |
| HBARUSDT | IDLE | 1.1 | 1.97 | 1.59 | 0.01 | 378280.83 | 1.29 | empty_tvl |
| BIOUSDT | IDLE | 1.03 | 1.85 | 1.43 | -0.0 | 97475.19 | 11.73 | n/a |
| RWAINCUSDT | IDLE | 0.76 | 1.39 | 0.82 | -0.0 | 5108.88 | 33.13 | no_map |
| TELUSDT | IDLE | 1.46 | 3.29 | 2.94 | 0.02 | 103325.94 | 37.13 | no_map |
| FLUIDUSDT | IDLE | 1.12 | 2.06 | 1.21 | 0.01 | 1752.6 | 20.79 | tvl≈2,666,600,862 |
| QNTUSDT | IDLE | 0.64 | 1.21 | 0.51 | 0.01 | 45962.78 | 7.73 | n/a |
| RWAUSDT | IDLE | 0.45 | 0.82 | 0.52 | -0.01 | 54258.99 | 14.88 | no_map |
| MNSRYUSDT | IDLE | 0.49 | 0.89 | 0.63 | 0.01 | 34305.14 | 31.81 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
